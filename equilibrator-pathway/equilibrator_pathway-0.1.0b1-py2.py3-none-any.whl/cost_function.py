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

import json
import logging
from typing import Tuple

import numpy as np
from equilibrator_api import Q_, Bounds
from optlang.glpk_interface import Constraint, Model, Objective, Variable
from scipy.optimize import minimize

from .util import ECF_DEFAULTS, RT, CastToColumnVector


QUAD_REGULARIZATION_COEFF = 0.2
METABOLITE_WEIGHT_CORRECTION_FACTOR = 1


class EnzymeCostFunction(object):

    ECF_LEVEL_NAMES = [
        "capacity [M]",
        "thermodynamic",
        "saturation",
        "allosteric",
    ]

    def __init__(
        self,
        S: np.ndarray,
        flux: np.ndarray,
        kcat: np.ndarray,
        dG0: np.ndarray,
        KMM: np.ndarray,
        ln_conc_lb: np.ndarray,
        ln_conc_ub: np.ndarray,
        mw_enz=None,
        mw_met=None,
        A_act=None,
        A_inh=None,
        K_act=None,
        K_inh=None,
        params=None,
    ):
        """
            Construct a toy model with N intermediate metabolites (and N+1 reactions)

            Arguments:
                S        - stoichiometric matrix [unitless]
                v        - steady-state fluxes [M/s]
                kcat     - turnover numbers [1/s]
                kcat_source - either 'gmean' or 'fwd'
                dG0      - standard Gibbs free energies of reaction [kJ/mol]
                KMM      - Michaelis-Menten coefficients [M]
                ln_conc_lb - lower bounds on metabolite concentrations [ln M]
                ln_conc_ub - upper bounds on metabolite concentrations [ln M]
                mw_enz   - enzyme molecular weight [Da]
                mw_met   - metabolite molecular weight [Da]
                A_act    - Hill coefficient matrix of allosteric activators [unitless]
                A_inh    - Hill coefficient matrix of allosteric inhibitors [unitless]
                K_act    - affinity coefficient matrix of allosteric activators [M]
                K_inh    - affinity coefficient matrix of allosteric inhibitors [M]
                params   - dictionary of extra parameters
        """
        self.params = dict(ECF_DEFAULTS)
        if params is not None:
            self.params.update(params)
        self.S = S
        self.flux = flux.flatten()
        self.kcat = kcat.flatten()
        self.dG0 = dG0.flatten()
        self.KMM = KMM
        self.ln_conc_lb = ln_conc_lb.flatten()
        self.ln_conc_ub = ln_conc_ub.flatten()

        self.Nc, self.Nr = S.shape
        assert self.flux.shape == (self.Nr,)
        assert self.kcat.shape == (self.Nr,)
        assert self.dG0.shape == (self.Nr,)
        assert self.KMM.shape == (self.Nc, self.Nr)
        assert self.ln_conc_lb.shape == (self.Nc,)
        assert self.ln_conc_ub.shape == (self.Nc,)

        self.cids = ["C%04d" % i for i in range(self.Nc)]

        ln_kmm = np.log(self.KMM)

        self.S_subs = abs(self.S)
        self.S_prod = abs(self.S)
        self.S_subs[self.S > 0] = 0
        self.S_prod[self.S < 0] = 0

        # if the kcat source is 'gmean' we need to recalculate the
        # kcat_fwd using the formula:
        # kcat_fwd = kcat_gmean * sqrt(kEQ * prod_S(KMM) / prod_P(KMM))
        if self.params["kcat_source"] == "gmean":
            ln_KMM_prod = np.array(np.diag(self.S.T @ ln_kmm))
            ln_ratio = -ln_KMM_prod - (self.dG0 / RT).magnitude
            factor = np.sqrt(np.exp(ln_ratio))
            self.kcat *= factor

        # molecular weights of enzymes and metabolites
        if mw_enz is None:
            self.mw_enz = np.ones((self.Nr, 1))
        else:
            assert mw_enz.shape == ((self.Nr, 1))
            self.mw_enz = mw_enz

        if mw_met is None:
            self.mw_met = np.ones((self.Nc, 1))
        else:
            assert mw_met.shape == (self.Nc, 1)
            self.mw_met = mw_met

        # allosteric regulation term

        if A_act is None or K_act is None:
            self.A_act = np.zeros(S.shape)
            self.K_act = np.ones(S.shape)
        else:
            assert S.shape == A_act.shape
            assert S.shape == K_act.shape
            self.A_act = A_act
            self.K_act = K_act

        if A_inh is None or K_inh is None:
            self.A_inh = np.zeros(S.shape)
            self.K_inh = np.ones(S.shape)
        else:
            assert S.shape == A_inh.shape
            assert S.shape == K_inh.shape
            self.A_inh = A_inh
            self.K_inh = K_inh

        # preprocessing: these auxiliary matrices help calculate the ECF3 and
        # ECF4 faster
        ln_k_act = np.log(self.K_act)
        ln_k_inh = np.log(self.K_inh)

        self.D_S_coeff = np.diag(self.S_subs.T @ ln_kmm)
        self.D_P_coeff = np.diag(self.S_prod.T @ ln_kmm)
        self.act_denom = np.diag(self.A_act.T @ ln_k_act)
        self.inh_denom = np.diag(self.A_inh.T @ ln_k_inh)

        try:
            self.ECF = eval("self._ECF%d" % self.params["version"])
        except AttributeError:
            raise ValueError(
                "The enzyme cost function %d is unknown"
                % self.params["version"]
            )

        try:
            self.D = eval("self._D_%s" % self.params["denominator"])
        except AttributeError:
            raise ValueError(
                "The denominator function %s is unknown"
                % self.params["denominator"]
            )

        self.regularization = self.params["regularization"]

    def _DrivingForce(self, lnC):
        """
            calculate the driving force for every reaction in every condition
        """
        assert lnC.shape[0] == self.Nc

        dg0_over_rt = self.dG0 / RT.to("kJ/mol").magnitude
        if len(lnC.shape) == 1:
            return -dg0_over_rt - self.S.T @ lnC
        else:
            return -np.tile(dg0_over_rt, (lnC.shape[1], 1)).T - self.S.T @ lnC

    def _EtaThermodynamic(self, lnC):
        assert lnC.shape[0] == self.Nc
        df = self._DrivingForce(lnC)

        # replace infeasbile reactions with a positive driving force to avoid
        # negative cost in ECF2
        eta_thermo = 1.0 - np.exp(-df)

        # set the value of eta to a negative number when the reaction is
        # infeasible so it will be easy to find them, and also calculating
        # 1/x will not return an error
        eta_thermo[df <= 0] = -1.0
        return eta_thermo

    def _D_S(self, lnC):
        """
            return a matrix containing the values of D_S
            i.e. prod(s_i / K_i)^n_i

            each row corresponds to a reaction in the model
            each column corresponds to another set of concentrations (assuming
            lnC is a matrix)
        """
        assert lnC.shape[0] == self.Nc
        return np.exp(
            self.S_subs.T @ lnC - np.tile(self.D_S_coeff, (lnC.shape[1], 1)).T
        )

    def _D_SP(self, lnC):
        """
            return a matrix containing the values of D_SP
            i.e. prod(s_i / K_i)^n_i + prod(p_j / K_j)^n_j

            each row corresponds to a reaction in the model
            each column corresponds to another set of concentrations (assuming
            lnC is a matrix)
        """
        assert lnC.shape[0] == self.Nc
        return np.exp(
            self.S_subs.T @ lnC - np.tile(self.D_S_coeff, (lnC.shape[1], 1)).T
        ) + np.exp(
            self.S_prod.T @ lnC - np.tile(self.D_P_coeff, (lnC.shape[1]), 1).T
        )

    def _D_1S(self, lnC):
        """
            return a matrix containing the values of D_1S
            i.e. 1 + prod(s_i / K_i)^n_i

            each row corresponds to a reaction in the model
            each column corresponds to another set of concentrations (assuming
            lnC is a matrix)
        """
        return 1.0 + self._D_S(lnC)

    def _D_1SP(self, lnC):
        """
            return a matrix containing the values of D_1SP
            i.e. 1 + prod(s_i / K_i)^n_i + prod(p_j / K_j)^n_j

            each row corresponds to a reaction in the model
            each column corresponds to another set of concentrations (assuming
            lnC is a matrix)
        """
        return 1.0 + self._D_SP(lnC)

    def _D_CM(self, lnC):
        """
            return a matrix containing the values of D_CM
            i.e. prod(1 + s_i / K_i)^n_i + prod(1 + p_j / K_j)^n_j - 1

            each row corresponds to a reaction in the model
            each column corresponds to another set of concentrations (assuming
            lnC is a matrix)
        """
        assert lnC.shape[0] == self.Nc
        D = np.zeros((self.Nr, lnC.shape[1]))
        for k in range(lnC.shape[1]):
            X_k = np.log(
                np.exp(np.tile(lnC[:, k], (self.Nr, 1)).T) / self.KMM + 1.0
            )
            ln_1_plus_S = np.diag(self.S_subs.T @ X_k)
            ln_1_plus_P = np.diag(self.S_prod.T @ X_k)
            D[:, k] = np.exp(ln_1_plus_S) + np.exp(ln_1_plus_P) - 1.0
        return D

    def _EtaKinetic(self, lnC):
        """
            the kinetic part of ECF3 and ECF4
        """
        return self._D_S(lnC) / self.D(lnC)

    def _EtaAllosteric(self, lnC):
        assert lnC.shape[0] == self.Nc
        kin_act = np.exp(
            -self.A_act.T @ lnC + np.tile(self.act_denom, (lnC.shape[1], 1)).T
        )
        kin_inh = np.exp(
            self.A_inh.T @ lnC - np.tile(self.inh_denom, (lnC.shape[1], 1)).T
        )
        eta_kin = 1.0 / (1.0 + kin_act) / (1.0 + kin_inh)
        return eta_kin

    def IsFeasible(self, lnC):
        assert lnC.shape == (self.Nc, 1)
        df = self._DrivingForce(lnC)
        return (df > 0).all()

    def GetVmax(self, E):
        """
            calculate the maximal rate of each reaction, kcat is in
            umol/min/mg and E is in gr, so we multiply by 1000

            Returns:
                Vmax  - in units of [umol/min]
        """
        assert E.shape == (self.Nr,)
        return self.kcat * E  # in M/s

    def _ECF1(self, lnC):
        """
            Arguments:
                A single metabolite ln-concentration vector

            Returns:
                The most basic Enzyme Cost Function (only dependent on flux
                and kcat). Gives the predicted enzyme concentrations in [M]
        """
        # lnC is not used for ECF1, except to determine the size of the result
        # matrix.
        assert lnC.shape[0] == self.Nc

        ecf1 = np.tile(self.flux / self.kcat, (lnC.shape[1], 1)).T

        return ecf1

    def _ECF2(self, lnC):
        """
            Arguments:
                A single metabolite ln-concentration vector

            Returns:
                The thermodynamic-only Enzyme Cost Function.
                Gives the predicted enzyme concentrations in [M].
        """
        assert lnC.shape[0] == self.Nc
        ecf2 = self._ECF1(lnC) / self._EtaThermodynamic(lnC)

        # fix the "fake" values that were given in ECF2 to infeasible reactions
        ecf2[ecf2 < 0] = np.nan

        return ecf2

    def _ECF3(self, lnC):
        """
            Arguments:
                A single metabolite ln-concentration vector

            Returns:
                An Enzyme Cost Function that integrates kinetic and
                thermodynamic data, but no allosteric regulation.
                Gives the predicted enzyme concentrations in [M].
        """
        # calculate the product of all substrates and products for the kinetic
        # term
        assert lnC.shape[0] == self.Nc

        ecf3 = self._ECF2(lnC) / self._EtaKinetic(lnC)

        return ecf3

    def _ECF4(self, lnC):
        """
            Arguments:
                A single metabolite ln-concentration vector

            Returns:
                The full Enzyme Cost Function, i.e. with kinetic, thermodynamic
                and allosteric data.
                Gives the predicted enzyme concentrations in [M].
        """
        assert lnC.shape[0] == self.Nc

        ecf4 = self._ECF3(lnC) / self._EtaAllosteric(lnC)

        return ecf4

    def GetEnzymeCostPartitions(self, lnC):
        """
            Arguments:
                A single metabolite ln-concentration vector

            Returns:
                A matrix contining the enzyme costs separated to the 4 ECF
                factors (as columns).
                The first column is the ECF1 predicted concentrations in [M].
                The other columns are unitless (added cost, always > 1)
        """
        assert lnC.shape[0] == self.Nc
        cap = self._ECF1(lnC)  # capacity
        trm = 1.0 / self._EtaThermodynamic(lnC)  # thermodynamics
        kin = 1.0 / self._EtaKinetic(lnC)  # kinetics
        alo = 1.0 / self._EtaAllosteric(lnC)  # allostery
        return np.hstack([cap, trm, kin, alo])

    def GetVolumes(self, lnC: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
            Arguments:
                A single metabolite ln-concentration vector

            Returns:
                Two arrays containing the enzyme volumes and
                metabolite volumes (at the provided point)
        """
        assert lnC.shape[0] == self.Nc
        enz_conc = self.ECF(lnC)
        met_conc = np.exp(lnC)
        enz_vol = enz_conc * self.mw_enz
        met_vol = met_conc * self.mw_met
        return enz_vol, met_vol

    def GetFluxes(self, lnC: np.ndarray, E: np.ndarray) -> np.ndarray:
        assert lnC.shape[0] == self.Nc
        assert E.shape == (self.Nr,)

        v = np.tile(self.GetVmax(E), (lnC.shape[1], 1)).T
        v *= self._EtaThermodynamic(lnC)
        v *= self._EtaKinetic(lnC)
        v *= self._EtaAllosteric(lnC)
        return v

    def ECM(self, lnC0: np.ndarray = None, n_iter: int = 10) -> np.ndarray:
        """
            Use convex optimization to find the y with the minimal total
            enzyme cost per flux, i.e. sum(ECF(lnC))
        """

        def optfun(lnC, regularization=1e-2):
            """
                regularization function:
                    d      = x - 0.5 * (x_min + x_max)
                    lambda = median(enzyme cost weights)
                    reg    = 0.01 * lambda * 0.5 * (d.T * d)
            """
            lnC = np.array(lnC.flatten(), ndmin=2).T

            # if some reaction is not feasible, give a large penalty
            # proportional to the negative driving force.
            minimal_df = self._DrivingForce(lnC).min()
            if minimal_df <= 0:
                return 1e20 * abs(minimal_df)

            enz_conc = self.ECF(lnC)
            met_conc = np.exp(lnC)

            e = float(enz_conc.T @ self.mw_enz)
            m = float(met_conc.T @ self.mw_met)
            if np.isnan(e) or e <= 0:
                raise Exception(
                    "ECF returns NaN although all reactions are feasible"
                )

            if (
                self.regularization is None
                or self.regularization.lower() == "none"
            ):
                return e
            elif self.regularization.lower() == "volume":
                return e + METABOLITE_WEIGHT_CORRECTION_FACTOR * m
            elif self.regularization.lower() == "quadratic":
                d = lnC - 0.5 * (lnC.min() + lnC.max())
                return e + QUAD_REGULARIZATION_COEFF * 0.5 * float(d.T * d)
            else:
                raise Exception(
                    "Unknown regularization: " + self.regularization
                )

        if lnC0 is None:
            mdf, lnC0 = self.MDF()
            if np.isnan(mdf) or mdf < 0.0:
                raise ValueError(
                    "It seems that the problem is thermodynamically"
                    " infeasible, therefore ECM is not applicable."
                )
        assert lnC0.shape == (self.Nc, 1)

        bounds = list(zip(self.ln_conc_lb.tolist(), self.ln_conc_ub.tolist()))

        min_res = np.inf
        lnC_min = lnC0
        for i in range(n_iter):
            lnC0_rand = lnC0 * (1.0 + 0.1 * np.random.rand(lnC0.shape[0], 1))
            r = minimize(optfun, x0=lnC0_rand, bounds=bounds, method="SLSQP")

            if not r.success:
                logging.info(
                    f"iteration #{i}: optimization unsuccessful "
                    f"because of {r.message}, "
                    "trying again"
                )
                continue

            res = optfun(r.x)
            if res < min_res:
                if min_res == np.inf:
                    logging.info("iteration #%d: cost = %.5f" % (i, res))
                else:
                    logging.info(
                        "iteration #%d: cost = %.5f, decrease factor = %.3e"
                        % (i, res, 1.0 - res / min_res)
                    )
                min_res = res
                lnC_min = np.array(r.x, ndmin=2).T
            else:
                logging.info(
                    "iteration #%d: cost = %.5f, no improvement" % (i, res)
                )

        return lnC_min

    def MDF(self) -> Tuple[Q_, np.ndarray]:
        """
            Find an initial point (x0) for the optimization using MDF.
        """
        Nc, Nr = self.S.shape

        # ln-concentration variables
        ln_conc = [Variable("l%d" % i) for i in range(self.Nc)]
        B = Variable("mdf")

        lp = Model(name="MDF_PRIMAL")

        dg0_over_rt = list((-self.dG0 / RT).magnitude.flat)
        constraints = []
        for j in range(Nr):
            driving_force = [self.S[i, j] * ln_conc[i] for i in range(Nc)]
            cnstr = Constraint(
                sum(driving_force) + B,
                ub=dg0_over_rt[j],
                name=f"driving_force_{j:02d}",
            )
            constraints.append(cnstr)

        for i in range(Nc):
            cnstr = Constraint(
                ln_conc[i],
                lb=self.ln_conc_lb[i],
                ub=self.ln_conc_ub[i],
                name=f"ln_conc_{i:02d}",
            )
            constraints.append(cnstr)

        lp.add(constraints)

        lp.objective = Objective(B, direction="max")

        if lp.optimize() != "optimal":
            logging.warning("LP status %s", lp.status)
            raise Exception("Cannot solve MDF primal optimization problem")

        mdf = B.primal
        lnC0 = np.array([_m.primal for _m in ln_conc], ndmin=2).T
        return mdf * RT, lnC0
