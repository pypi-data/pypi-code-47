# The MIT License (MIT)
#
# Copyright (c) 2013 Weizmann Institute of Science
# Copyright (c) 2018-2020 Institute for Molecular Systems Biology,
# ETH Zurich
# Copyright (c) 2018-2020 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import logging
from collections import defaultdict
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sbtab
from equilibrator_api import Q_, ccache
from sbtab import SBtab

from .colors import ColorMap
from .cost_function import EnzymeCostFunction
from .errors import ThermodynamicallyInfeasibleError
from .html_writer import BaseHtmlWriter
from .pathway import Pathway
from .util import ECF_DEFAULTS, RT, PlotCorrelation, QuantitiesToColumnVector


class ECMmodel(object):

    DATAFRAME_NAMES = {
        "Compound",
        "Reaction",
        "ConcentrationConstraint",
        "Parameter",
        "RelativeFlux",
    }

    def __init__(
        self,
        pathway: Pathway,
        kinetic_param_df: pd.DataFrame,
        ecf_params: dict = None,
    ):
        self.ecf_params = dict(ECF_DEFAULTS)
        if ecf_params is not None:
            self.ecf_params.update(ecf_params)

        stdev_factor = self.ecf_params.get("stdev_factor", 1.0)

        (
            rid2crc_gmean,
            rid2crc_fwd,
            rid2crc_rev,
            rid_cid2KMM,
            rid2dg0,
            rid2mw,
            cid2mw,
        ) = ECMmodel.ReadParameters(kinetic_param_df)

        self.reaction_ids = list(pathway.reaction_ids)
        self.compound_ids = list(pathway.compound_names)

        if not set(self.reaction_ids).issubset(rid2dg0.keys()):
            # if at least one of the standard Gibbs energies is missing,
            # use Component Contribution to calculate all of the values.
            rid2dg0 = dict(
                zip(self.reaction_ids, pathway.standard_dg_primes.flat)
            )

        dG0 = QuantitiesToColumnVector(
            map(rid2dg0.get, self.reaction_ids), "kJ/mol"
        )

        KMM = ECMmodel._GenerateKMM(
            self.compound_ids, self.reaction_ids, rid_cid2KMM
        )

        # we need all fluxes to be positive, so for every negative flux,
        # we multiply it and the corresponding column in S by (-1)
        dir_mat = np.diag(np.sign(pathway.fluxes + 1e-10).flat)
        flux = dir_mat @ pathway.fluxes
        S = pathway.S.values @ dir_mat
        dG0 = dir_mat @ dG0

        # we only need to define get kcat in the direction of the flux
        # if we use the 'gmean' option, that means we assume we only know
        # the geometric mean of the kcat, and we distribute it between
        # kcat_fwd and kcat_bwd according to the Haldane relationship
        # if we use the 'fwd' option, we just take the kcat in the
        # direction of flux (as is) and that would mean that our
        # thermodynamic rate law would be equivalent to calculating the
        # reverse kcat using the Haldane relationship
        if self.ecf_params["kcat_source"] == "gmean":
            kcat = QuantitiesToColumnVector(
                map(rid2crc_gmean.get, self.reaction_ids), "1/s"
            )
        elif self.ecf_params["kcat_source"] == "fwd":
            # get the relevant kcat (fwd/rev) depending on the directions
            kcat = []
            for rid, d in zip(pathway.reaction_ids, np.diag(dir_mat).flat):
                if d > 0:
                    kcat.append(rid2crc_fwd[rid])
                else:
                    kcat.append(rid2crc_rev[rid])
            kcat = QuantitiesToColumnVector(kcat, "1/s")
        else:
            raise ValueError(
                "unrecognized kcat source: " + self.ecf_params["kcat_source"]
            )

        # TODO: turn this into a warning, if the MW data is missing, try to
        # assign a default value
        mw_enz = []
        for rid in self.reaction_ids:
            if rid not in rid2mw:
                raise KeyError(f"This reaction is missing an enzyme MW: {rid}")
            mw_enz.append(rid2mw[rid])
        mw_enz = QuantitiesToColumnVector(mw_enz, "Da")

        # TODO: fill gaps in MW data by using the equilibrator-cache
        mw_met = []
        for cid in self.compound_ids:
            if cid not in cid2mw:
                raise KeyError(f"This compound is missing a MW: {cid}")
            mw_met.append(cid2mw[rid])
        mw_met = QuantitiesToColumnVector(
            map(cid2mw.get, self.compound_ids), "Da"
        )

        # we must remove H2O from the model, since it should not be considered
        # as a "normal" metabolite in terms of the enzyme and metabolite costs
        idx_water = pathway.S.index.tolist().index(ccache.water)
        self.compound_ids.pop(idx_water)
        S = np.delete(S, idx_water, axis=0)
        KMM = np.delete(KMM, idx_water, axis=0)
        ln_conc_lb = np.delete(pathway.ln_conc_lb, idx_water, axis=0)
        ln_conc_ub = np.delete(pathway.ln_conc_ub, idx_water, axis=0)
        mw_met = np.delete(mw_met, idx_water, axis=0)

        self.ecf = EnzymeCostFunction(
            S,
            flux=flux,
            kcat=kcat,
            dG0=dG0,
            KMM=KMM,
            ln_conc_lb=ln_conc_lb,
            ln_conc_ub=ln_conc_ub,
            mw_enz=mw_enz,
            mw_met=mw_met,
            params=self.ecf_params,
        )

        self._val_df_dict = None

    @staticmethod
    def from_sbtab(
        sbtabdoc: sbtab.SBtab.SBtabDocument, ecf_params: dict = None
    ):
        if ecf_params is None:
            ecf_params = dict()

        pathway = Pathway.from_sbtab(sbtabdoc)
        param_sbtab = sbtabdoc.get_sbtab_by_id("Parameter")
        assert param_sbtab, "Missing table 'Parameter' in the SBtab document"
        kinetic_param_df = param_sbtab.to_data_frame()

        return ECMmodel(pathway, kinetic_param_df, ecf_params=ecf_params)

    def AddValidationData(
        self, validate_sbtabdoc: sbtab.SBtab.SBtabDocument
    ) -> None:
        conc_sbtab = validate_sbtabdoc.get_sbtab_by_id("Concentration")
        self._met_conc_unit = Q_(conc_sbtab.get_attribute("Unit"))
        assert self._met_conc_unit.check("[concentration]"), (
            f"Metabolite concentration unit is not a [concentration] quantity",
            self._met_conc_unit,
        )

        enzyme_sbtab = validate_sbtabdoc.get_sbtab_by_id("EnzymeConcentration")
        self._enz_conc_unit = Q_(enzyme_sbtab.get_attribute("Unit"))
        assert self._enz_conc_unit.check("[concentration]"), (
            f"Enzyme concentration unit is not a [concentration] quantity",
            self._enz_conc_unit,
        )

        self._val_df_dict = {
            sbtab.table_id: sbtab.to_data_frame()
            for sbtab in validate_sbtabdoc.sbtabs
        }

    @staticmethod
    def ReadParameters(parameter_df: pd.DataFrame) -> Tuple[dict, ...]:
        cols = ["QuantityType", "Value", "Compound", "Reaction", "Unit"]

        rid2mw = defaultdict(float)
        cid2mw = defaultdict(float)
        rid2dg0 = {}
        rid2crc_gmean = {}  # catalytic rate constant geomertic mean
        rid2crc_fwd = {}  # catalytic rate constant forward
        rid2crc_rev = {}  # catalytic rate constant reverse
        crctype2dict = {
            "catalytic rate constant geometric mean": rid2crc_gmean,
            "substrate catalytic rate constant": rid2crc_fwd,
            "product catalytic rate constant": rid2crc_rev,
        }

        rid_cid2KMM = {}  # Michaelis-Menten constants

        for i, row in parameter_df.iterrows():
            try:
                typ, val, cid, rid, unit = [row[c] for c in cols]
                val = Q_(float(val), unit)

                if typ in crctype2dict:
                    assert val.check("1/[time]")
                    val.ito("1/s")
                    crctype2dict[typ][rid] = val
                elif typ == "Michaelis constant":
                    assert val.check("[concentration]")
                    val.ito("molar")
                    rid_cid2KMM[rid, cid] = val
                elif typ == "equilibrium constant":
                    assert val.check("")
                    rid2dg0[rid] = -np.log(val.magnitude) * RT
                elif typ == "reaction gibbs energy":
                    assert val.check("[energy]/[substance]")
                    val.ito("kJ/mol")
                    rid2dg0[rid] = val
                elif typ == "protein molecular mass":
                    assert val.check("[mass]")
                    val.ito("Da")
                    rid2mw[rid] = val
                elif typ == "molecular mass":
                    assert val.check("[mass]")
                    val.ito("Da")
                    cid2mw[cid] = val
                else:
                    raise AssertionError(
                        "unrecognized Rate Constant Type: " + typ
                    )
            except AssertionError:
                raise ValueError(
                    "Syntax error in Parameter table, row %d - %s" % (i, row)
                )
        # make sure not to count water as contributing to the volume or
        # cost of a reaction
        return (
            rid2crc_gmean,
            rid2crc_fwd,
            rid2crc_rev,
            rid_cid2KMM,
            rid2dg0,
            rid2mw,
            cid2mw,
        )

    @staticmethod
    def _GenerateKMM(
        cids: List[str], rids: List[str], rid_cid2KMM: dict
    ) -> np.array:
        KMM = np.ones((len(cids), len(rids)))
        for i, cid in enumerate(cids):
            for j, rid in enumerate(rids):
                kmm = rid_cid2KMM.get((rid, cid), Q_("M"))
                KMM[i, j] = kmm.to("M").magnitude
        return KMM

    def MDF(self):
        mdf, lnC0 = self.ecf.MDF()

        if np.isnan(mdf) or mdf < 0.0:
            logging.error(
                "Negative MDF value: %.1f RT (= %s)" % (mdf, mdf * RT)
            )
            raise ThermodynamicallyInfeasibleError()
        return lnC0

    def ECM(self, lnC0=None, n_iter=10):
        if lnC0 is None:
            lnC0 = self.MDF()
            logging.info("initializing ECM using MDF result")

        return self.ecf.ECM(lnC0, n_iter=n_iter)

    def ECF(self, lnC):
        return self.ecf.ECF(lnC)

    @staticmethod
    def _nanfloat(x):
        if type(x) == float:
            return x
        if type(x) == int:
            return float(x)
        if type(x) == str:
            if x.lower() in ["", "nan"]:
                return np.nan
            else:
                return float(x)
        else:
            raise ValueError("unrecognized type for value: " + str(type(x)))

    @staticmethod
    def _MappingToCanonicalEnergyUnits(unit):
        """
            Assuming the canonical units for concentration are Molar

            Returns:
                A function that converts a single number or string to the
                canonical units
        """
        if unit == "kJ/mol":
            return lambda x: ECMmodel._nanfloat(x)
        if unit == "kcal/mol":
            return lambda x: ECMmodel._nanfloat(x) * 4.184

        raise ValueError("Cannot convert these units to kJ/mol: " + unit)

    def _GetMeasuredMetaboliteConcentrations(self):
        if self._val_df_dict is None:
            raise Exception(
                "cannot validate results because no validation data"
                " was given"
            )

        # assume concentrations are in mM
        met_conc_df = self._val_df_dict["Concentration"].set_index(
            "Compound:Identifiers:kegg.compound"
        )
        kegg2conc = met_conc_df["Value"].apply(
            lambda x: Q_(float(x if x else 0), self._met_conc_unit)
        )
        return QuantitiesToColumnVector(kegg2conc[self.compound_ids], "M")

    def _GetMeasuredEnzymeConcentrations(self):
        if self._val_df_dict is None:
            raise Exception(
                "cannot validate results because no validation data"
                " was given"
            )

        enz_conc_df = self._val_df_dict["EnzymeConcentration"].set_index(
            "Reaction"
        )
        rxn2conc = enz_conc_df["Value"].apply(
            lambda x: Q_(float(x if x else 0), self._enz_conc_unit)
        )
        return QuantitiesToColumnVector(rxn2conc[self.reaction_ids], "M")

    def _GetVolumeDataForPlotting(self, lnC):
        enz_vols, met_vols = self.ecf.GetVolumes(lnC)

        enz_labels = list(map(self.kegg2rxn.get, self.reaction_ids))
        enz_data = sorted(zip(enz_vols.flat, enz_labels), reverse=True)
        enz_vols, enz_labels = zip(*enz_data)
        enz_colors = [(0.5, 0.8, 0.3)] * len(enz_vols)

        met_labels = list(map(self.kegg2met.get, self.compound_ids))
        met_data = zip(met_vols.flat, met_labels)
        # remove H2O from the list and sort by descending volume
        met_data = sorted(filter(lambda x: x[1] != "h2o", met_data))
        met_vols, met_labels = zip(*met_data)
        met_colors = [(0.3, 0.5, 0.8)] * len(met_vols)

        return (
            enz_vols + met_vols,
            enz_labels + met_labels,
            enz_colors + met_colors,
        )

    def PlotVolumes(self, lnC: np.array, ax: plt.axes) -> None:
        width = 0.8
        vols, labels, colors = self._GetVolumeDataForPlotting(lnC)

        ax.bar(np.arange(len(vols)), vols, width, color=colors)
        ax.set_xticklabels(labels, size="medium", rotation=90)
        ax.set_ylabel("total weight [g/L]")

    def PlotVolumesPie(self, lnC: np.array, ax: plt.axes) -> None:
        vols, labels, colors = self._GetVolumeDataForPlotting(lnC)
        ax.pie(vols, labels=labels, colors=colors)
        ax.set_title("total weight [g/L]")

    def PlotThermodynamicProfile(self, lnC: np.array, ax: plt.axes) -> None:
        """
            Plot a cumulative line plot of the dG' values given the solution
            for the metabolite levels. This was originally designed for showing
            MDF results, but is also a useful tool for ECM.
        """
        driving_forces = self.ecf._DrivingForce(lnC)

        dgs = [0] + list((-driving_forces).flat)
        cumulative_dgs = np.cumsum(dgs)

        xticks = np.arange(0, len(cumulative_dgs)) - 0.5
        xticklabels = [""] + list(map(self.kegg2rxn.get, self.reaction_ids))
        ax.plot(cumulative_dgs)
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels, rotation=45, ha="right")
        ax.set_xlim(0, len(cumulative_dgs) - 1)
        ax.set_xlabel("")
        ax.set_ylabel(r"Cumulative $\Delta_r G'$ (kJ/mol)", family="sans-serif")

    def PlotEnzymeDemandBreakdown(
        self,
        lnC: np.array,
        ax: plt.Axes,
        top_level: int = 3,
        plot_measured: bool = False,
    ) -> None:
        """
            A bar plot in log-scale showing the partitioning of cost between
            the levels of kinetic costs:
            1 - capacity
            2 - thermodynamics
            3 - saturation
            4 - allosteric
        """
        assert top_level in range(1, 5)

        costs = np.array(self.ecf.GetEnzymeCostPartitions(lnC))

        # give all reactions with zero cost a base value, which we will
        # also set as the bottom ylim, which will simulate a "minus infinity"
        # when we plot it in log-scale
        base = min(filter(None, costs[:, 0])) / 2.0
        idx_zero = costs[:, 0] == 0
        costs[idx_zero, 0] = base
        costs[idx_zero, 1:] = 1.0

        bottoms = np.hstack(
            [np.ones((costs.shape[0], 1)) * base, np.cumprod(costs, 1)]
        )
        steps = np.diff(bottoms)

        labels = EnzymeCostFunction.ECF_LEVEL_NAMES[0:top_level]

        ind = range(costs.shape[0])  # the x locations for the groups
        width = 0.8
        ax.set_yscale("log")

        if plot_measured:
            all_labels = ["measured"] + labels
            meas_conc = self._GetMeasuredEnzymeConcentrations()
            cmap = ColorMap(
                all_labels,
                saturation=0.7,
                value=1.0,
                hues=[30.0 / 255, 170.0 / 255, 200.0 / 255, 5.0 / 255],
            )
            ax.plot(
                ind,
                meas_conc,
                color=cmap["measured"],
                marker="o",
                markersize=5,
                linewidth=0,
                markeredgewidth=0.3,
                markeredgecolor=(0.3, 0.3, 0.3),
            )
        else:
            all_labels = labels
            cmap = ColorMap(
                labels,
                saturation=0.7,
                value=0.8,
                hues=[170.0 / 255, 200.0 / 255, 5.0 / 255],
            )

        for i, label in enumerate(labels):
            ax.bar(
                ind,
                steps[:, i].flat,
                width,
                bottom=bottoms[:, i].flat,
                color=cmap[label],
            )

        ax.set_xticks(ind)
        xticks = list(map(self.kegg2rxn.get, self.reaction_ids))
        ax.set_xticklabels(xticks, size="medium", rotation=90)
        ax.legend(all_labels, loc="best", framealpha=0.2)
        ax.set_ylabel("enzyme demand [M]")
        ax.set_ylim(bottom=base)

    def ValidateMetaboliteConcentrations(
        self, lnC: np.array, ax: plt.Axes, scale: str = "log"
    ) -> None:
        pred_conc = np.exp(lnC)

        meas_conc = self._GetMeasuredMetaboliteConcentrations()

        # remove NaNs and zeros
        mask = np.nan_to_num(meas_conc) > 0
        mask &= np.nan_to_num(pred_conc) > 0

        # remove compounds with fixed concentrations
        mask &= np.diff(self.ecf.lnC_bounds) > 1e-9

        labels = list(map(self.kegg2met.get, self.compound_ids))
        PlotCorrelation(ax, meas_conc, pred_conc, labels, mask, scale=scale)
        ax.set_xlabel("measured [M]")
        ax.set_ylabel("predicted [M]")

    def ValidateEnzymeConcentrations(
        self, lnC: np.array, ax: plt.Axes, scale: str = "log"
    ) -> None:
        pred_conc = self.ecf.ECF(lnC)
        meas_conc = self._GetMeasuredEnzymeConcentrations()

        labels = list(map(self.kegg2rxn.get, self.reaction_ids))
        PlotCorrelation(ax, meas_conc, pred_conc, labels, scale=scale)

        ax.set_xlabel("measured [M]")
        ax.set_ylabel("predicted [M]")

    def ToSBtab(self, lnC: np.array) -> sbtab.SBtab.SBtabDocument:
        met_data = []
        for i, cid in enumerate(self.compound_ids):
            met_name = self.kegg2met[cid]
            met_data.append(("concentration", met_name, cid, np.exp(lnC[i, 0])))
        met_df = pd.DataFrame(
            columns=[
                "QuantityType",
                "Compound",
                "Compound:Identifiers:kegg.compound",
                "ecm",
            ],
            data=met_data,
        )

        enz_conc = self.ecf.ECF(lnC)
        enz_data = []
        for i, rid in enumerate(self.reaction_ids):
            rxn_name = self.kegg2rxn[rid]
            enz_data.append(
                ("concentration of enzyme", rxn_name, rid, enz_conc[i, 0])
            )
        enz_df = pd.DataFrame(
            columns=[
                "QuantityType",
                "Reaction",
                "Reaction:Identifiers:kegg.reaction",
                "ecm",
            ],
            data=enz_data,
        )

        sbtabdoc = SBtab.SBtabDocument("report")
        met_sbtab = SBtab.SBtabTable.from_data_frame(
            met_df,
            table_id="Predicted concentrations",
            table_type="Quantity",
            unit="M",
        )

        enz_sbtab = SBtab.SBtabTable.from_data_frame(
            enz_df,
            table_id="Predicted enzyme levels",
            table_type="Quantity",
            unit="M",
        )

        sbtabdoc.add_sbtab(met_sbtab)
        sbtabdoc.add_sbtab(enz_sbtab)
        return sbtabdoc

    def WriteHtmlTables(self, lnC: np.array, html: BaseHtmlWriter) -> None:
        meas_enz2conc = self._GetMeasuredEnzymeConcentrations()
        meas_conc = np.array(
            list(
                map(lambda r: meas_enz2conc.get(r, np.nan), self.reaction_ids)
            ),
            ndmin=2,
        ).T
        data_mat = np.hstack(
            [
                self.ecf.flux,
                meas_conc,
                self.ecf.ECF(lnC),
                self.ecf._DrivingForce(lnC),
                self.ecf.GetEnzymeCostPartitions(lnC),
            ]
        )

        data_mat[:, 0] *= 1e3  # convert flux from M/s to mM/s
        data_mat[:, 1] *= 1e6  # convert measured enzyme conc. from M to uM
        data_mat[:, 2] *= 1e6  # convert predicted enzyme conc. from M to uM
        data_mat[:, 4] *= 1e6  # convert capacity term from M to uM

        headers = [
            "reaction",
            "KEGG ID",
            "flux [mM/s]",
            "measured enz. conc. [uM]",
            "predicted enz. conc. [uM]",
            "driving force [kJ/mol]",
            "capacity [uM]",
        ] + EnzymeCostFunction.ECF_LEVEL_NAMES[1:]
        values = zip(
            map(self.kegg2rxn.get, self.reaction_ids),
            self.reaction_ids,
            *data_mat.T.tolist(),
        )
        values.append(
            [
                "total",
                "",
                "",
                data_mat[:, 1].sum(),
                data_mat[:, 2].sum(),
                "",
                "",
                "",
                "",
                "",
            ]
        )

        rowdicst = [dict(zip(headers, v)) for v in values]
        html.write_table(rowdicst, headers=headers, decimal=3)

        meas_met2conc = self._GetMeasuredMetaboliteConcentrations()
        meas_conc = np.array(
            list(
                map(lambda r: meas_met2conc.get(r, np.nan), self.compound_ids)
            ),
            ndmin=2,
        ).T
        data_mat = np.hstack(
            [meas_conc, np.exp(lnC), np.exp(self.ecf.lnC_bounds)]
        )

        data_mat *= 1e3  # convert all concentrations from M to mM

        headers = [
            "compound",
            "KEGG ID",
            "measured conc. [mM]",
            "predicted conc. [mM]",
            "lower bound [mM]",
            "upper bound [mM]",
        ]
        values = zip(
            map(self.kegg2met.get, self.compound_ids),
            self.compound_ids,
            *data_mat.T.tolist(),
        )
        rowdicst = [dict(zip(headers, v)) for v in values]
        headers = [
            "compound",
            "KEGG ID",
            "measured conc. [mM]",
            "lower bound [mM]",
            "predicted conc. [mM]",
            "upper bound [mM]",
        ]
        html.write_table(rowdicst, headers=headers)
