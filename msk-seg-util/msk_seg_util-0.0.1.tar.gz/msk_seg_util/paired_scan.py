# Here we are creating a different dataframe where each key is representative of different locations + sequence 

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from pystats import stats as pyss
from msk_seg_util.util.stats_util import concordance_correlation_coefficient, calc_cv

from typing import Sequence

__all__ = ['PairedScanAnalysis']

STR_KEYS = ['Knee', 'Location', 'Subject']


class PairedScanAnalysis(object):
    """Analyze paired scan knee data.

    Analyzing paired scan data is useful for evaluating results computed with new algorithms.
    For example, one use case would be comparing the average T2 values in femoral cartilage regions, which are segmented
    manually vs automatically.

    Scans are paired per subject. Bilateral scan analysis is supported.

    Args:
        scan1_files (:obj:`Sequence[str]`): Excel files for first element in the pair to load data from. Data is loaded
            into a pandas ``DataFrame``.
        scan2_files (:obj:`Sequence[str]`): Excel files for second element in the pair to load data from. Data is loaded
            into a pandas ``DataFrame``. File order should correspond with the file order in ``scan1_files``.
        single_knee (:obj:`bool`, optional): Not bilateral. Defaults to ``False``.
        sheet_name (:obj:`str`, optional): Sheet to load from all excel files. Defaults to first sheet in each file.
    """

    def __init__(self, scan1_files, scan2_files, single_knee: bool = False, sheet_name: str = None):
        self.scan1_files = scan1_files
        self.scan2_files = scan2_files

        self.single_knee = single_knee

        self.scan1_data = self._load_data(scan1_files, single_knee=single_knee, sheet_name=sheet_name)
        self.scan2_data = self._load_data(scan2_files, single_knee=single_knee, sheet_name=sheet_name)

        self.scan1_region_data = self.reorg_data_by_region(self.scan1_data)
        self.scan2_region_data = self.reorg_data_by_region(self.scan2_data)

        scan1_region_data = self.scan1_region_data
        scan2_region_data = self.scan2_region_data

        vals_diff = scan1_region_data.drop(STR_KEYS, axis=1) - scan2_region_data.drop(STR_KEYS, axis=1)
        vals_diff[STR_KEYS] = scan1_region_data[STR_KEYS]

        vals_mean = (scan1_region_data.drop(STR_KEYS, axis=1) + scan2_region_data.drop(STR_KEYS, axis=1)) / 2
        vals_mean[STR_KEYS] = scan1_region_data[STR_KEYS]

        self.vals_diff = vals_diff
        self.vals_mean = vals_mean

    def _load_data(self, xl_files: Sequence[str], single_knee: bool = False, sheet_name: str = None):
        """Loads excel files formatted by DOSMA for femoral cartilage.

        Args:
            xl_files (Sequence[str]): Excel files to load data from. Each file corresponds to data about a different
                subject. All files should have the following column names:

                    - 'Subject': Subject id. If both knees are analyzed, this column should be of the form
                    ``<subject_id>-<R/L>``. For example,
                    - 'Side': medial/lateral compartment
                    - 'Location': deep/superficial/total
                    - 'Region': posterior/central/anterior

            single_knee (:obj:`bool`, optional): Analyze single knee.
            sheet_name (:obj:`str`, optional): Sheet to load from all excel files. Defaults to first sheet in each file.

        Returns:
            :obj:`pd.DataFrame`:
        """
        # Load excel files one by one and then cat them
        for num, fname in enumerate(xl_files):
            xls = pd.ExcelFile(fname)
            sheet_name = xls.sheet_names[0] if sheet_name is None else sheet_name
            tmp = xls.parse(sheet_name)

            if num == 0:
                data = tmp
            else:
                data = pd.concat([data, tmp])

        if data.columns.contains('Subject') is True:
            # info = data['Subject'].astype(str).str.split('-').str
            if single_knee:
                data['Knee'] = 'N/A'
            else:
                data['Subject'], data['Knee'] = data.Subject.str.split('-').str
        data.Side = data.Side.str.capitalize()
        data.Location = data.Location.str.capitalize()
        data.Region = data.Region.str.capitalize()

        return data

    def reorg_data_by_region(self, data):
        seqs = pd.DataFrame()

        # Create key per region and side
        uniq_reg = list(data.Region.unique())
        uniq_sid = list(data.Side.unique())

        for reg in uniq_reg:
            for sid in uniq_sid:
                #         Name of key and associated values
                df_name = '%s-%s' % (sid, reg)
                seqs[df_name] = data[(data.Side == sid) & (data.Region == reg)].Mean.values

        # Adding a couple of rows to keep track of subjects 
        seqs['Knee'] = data[(data.Side == sid) & (data.Region == reg)].Knee.values
        seqs['Location'] = data[(data.Side == sid) & (data.Region == reg)].Location.values
        seqs['Subject'] = data[(data.Side == sid) & (data.Region == reg)].Subject.values

        return seqs

    def _ba_plot_args(self):
        return {'ylim': (-15, 15)}

    def plot_ba_separate_knee(self, fname=None, **kwargs):
        default_args = self._ba_plot_args()
        for k in default_args.keys():
            if k in kwargs:
                default_args[k] = kwargs.get(k)

        scan1_region_data = self.scan1_region_data
        scan2_region_data = self.scan2_region_data
        vals_diff = self.vals_diff
        vals_mean = self.vals_mean

        uniq_knee = list(scan1_region_data.Knee.unique())
        uniq_loc = list(scan1_region_data.Location.unique())
        fig_cap = ['A', 'B', 'C', 'D', 'E', 'F']

        plt.close('all')
        _, axs = plt.subplots(2, 3, figsize=(35, 20))
        splot_num = 0

        column_names = list(vals_diff.columns.values)
        num_columns = 6
        cpal = sns.color_palette("bright", num_columns)

        for knee_num, knee_name in enumerate(uniq_knee):
            for cart_num, cart_reg in enumerate(uniq_loc):

                #         Isolate the values for specific cartilage region and sequence type
                diff_arr = vals_diff[(vals_diff.Location == cart_reg) & (vals_diff.Knee == knee_name)]
                diff_arr = diff_arr.drop(STR_KEYS, axis=1).values

                mean_arr = vals_mean[(vals_mean.Location == cart_reg) & (vals_mean.Knee == knee_name)]
                mean_arr = mean_arr.drop(STR_KEYS, axis=1).values

                #         Calculate the mean and std of ALL values over all regions for the BA analysis
                ba_mean = np.mean(diff_arr)
                ba_std = np.std(diff_arr)

                splot_num += 1

                for num in range(num_columns):
                    #             Plot the 6 sub-regions for each cartilage layer as well as two sequences
                    plt.subplot(2, 3, splot_num)
                    plt.plot(mean_arr[:, num], diff_arr[:, num], label=column_names[num], color=cpal[num], LineStyle="",
                             Marker="o", MarkerSize=15)

                    plt.axhline(ba_mean, color='gray', linestyle=':', Linewidth=4)
                    plt.axhline(ba_mean + 1.96 * ba_std, color='gray', LineStyle='--', LineWidth=4)
                    plt.axhline(ba_mean - 1.96 * ba_std, color='gray', LineStyle='--', LineWidth=4)

                    plt.ylabel('T2 Difference (ms)')
                    plt.ylim(default_args['ylim'])
                    plt.xlabel('T2 Mean (ms)')
                    plt.title('{}: {} T2 {} Res'.format(fig_cap[splot_num - 1], cart_reg, knee_name), fontweight='bold')
                    plt.grid(which="Major")

        plt.legend(loc=8, bbox_to_anchor=(-0.9, -0.3), fancybox=True, ncol=6)
        plt.subplots_adjust(hspace=0.3, wspace=0.3)
        if fname is not None:
            plt.savefig(fname, bbox_inches='tight')

        return axs

    def plot_ba_both_knee(self, fname=None, **kwargs):
        default_args = self._ba_plot_args()
        for k in default_args.keys():
            if k in kwargs:
                default_args[k] = kwargs.get(k)

        scan1_region_data = self.scan1_region_data
        scan2_region_data = self.scan2_region_data
        vals_diff = self.vals_diff
        vals_mean = self.vals_mean

        uniq_knee = list(scan1_region_data.Knee.unique())
        uniq_loc = list(scan1_region_data.Location.unique())
        fig_cap = ['A', 'B', 'C']

        plt.close('all')
        plt.subplots(1, 3, figsize=(35, 10))
        splot_num = 0

        column_names = list(vals_diff.columns.values)
        num_columns = 6
        cpal = sns.color_palette("bright", num_columns)

        for cart_num, cart_reg in enumerate(uniq_loc):

            #         Isolate the values for specific cartilage region and sequence type
            diff_arr = vals_diff[(vals_diff.Location == cart_reg)]
            diff_arr = diff_arr.drop(STR_KEYS, axis=1).values

            mean_arr = vals_mean[(vals_mean.Location == cart_reg)]
            mean_arr = mean_arr.drop(STR_KEYS, axis=1).values

            #         Calculate the mean and std of ALL values over all regions for the BA analysis
            ba_mean = np.mean(diff_arr)
            ba_std = np.std(diff_arr)

            splot_num += 1

            for num in range(num_columns):
                #             Plot the 6 sub-regions for each cartilage layer as well as two sequences
                plt.subplot(1, 3, splot_num)
                plt.plot(mean_arr[:, num], diff_arr[:, num], label=column_names[num], color=cpal[num], LineStyle="",
                         Marker="o", MarkerSize=15)

                plt.axhline(ba_mean, color='gray', linestyle=':', Linewidth=4)
                plt.axhline(ba_mean + 1.96 * ba_std, color='gray', LineStyle='--', LineWidth=4)
                plt.axhline(ba_mean - 1.96 * ba_std, color='gray', LineStyle='--', LineWidth=4)

                plt.ylabel('T2 Difference (ms)')
                plt.ylim(default_args['ylim'])
                plt.xlabel('T2 Mean (ms)')
                plt.title('{}: {} T2'.format(fig_cap[splot_num - 1], cart_reg), fontweight='bold')
                plt.grid(which="Major")

        plt.legend(loc=8, bbox_to_anchor=(-0.9, -0.3), fancybox=True, ncol=6)
        plt.subplots_adjust(hspace=0.3, wspace=0.3)
        if fname is not None:
            plt.savefig(fname, bbox_inches='tight')

    def print_metrics(self, skey='Location'):
        """
        Print metrics grouped by search key (skey)
        """
        s1 = self.scan1_region_data
        s2 = self.scan2_region_data

        unique_keys = list(s1[skey].unique())
        for ukey in sorted(unique_keys):
            temp1 = s1[s1[skey] == ukey].drop(STR_KEYS, axis=1).values
            temp2 = s2[s2[skey] == ukey].drop(STR_KEYS, axis=1).values

            # calculate RMS-CV
            cvs = calc_cv(temp1.flatten(), temp2.flatten())
            rms_cv = np.sqrt(np.mean((cvs) ** 2)) * 100

            # calculate concordance correlation
            cc = concordance_correlation_coefficient(temp1.flatten(), temp2.flatten())

            print('%s: %-10s \t RMS-CV: %0.2f%% \t Lin\'s Concordance: %0.3f' % (skey, ukey, rms_cv, cc))

    def kw_dunn(self, skey='Location', alpha=0.05):
        """Run Kruskal-Wallis + Dunn posthoc analysis for different regions.

        Args:
            skey (optional): Column to compare between scans. Unique values in the column will be compared across
                scan cohorts. Defaults to ``Location``.
            alpha (:obj:`float`, optional): Alpha level. Defaults to ``0.05``.
        """
        s1 = self.scan1_region_data
        s2 = self.scan2_region_data

        unique_keys = list(s1[skey].unique())
        unique_regions = s1.columns.tolist()[:6]
        print_st = ''
        print_gt = ''
        for ukey in unique_keys:
            temp1 = s1[s1[skey] == ukey].drop(STR_KEYS, axis=1).values
            temp2 = s2[s2[skey] == ukey].drop(STR_KEYS, axis=1).values
            for ureg in unique_regions:
                temp1 = s1[s1[skey] == ukey][ureg].values
                temp2 = s2[s2[skey] == ukey][ureg].values
                temp_df = pd.DataFrame([temp1, temp2])
                results = pyss.kruskal_wallis(temp_df, posthoc_test='dunn')
                results = results['dunn']
                p = np.asarray(results)[0, 1]
                res = np.absolute(np.asarray(results.values))
                if (res <= alpha).any():
                    print_st += '%s %s (p=%0.3f):\t\t1: %0.3f +/- %0.3f\t\t2: %0.3f +/- %0.3f\n' % (ukey, ureg, p,
                                                                                                    np.mean(temp1),
                                                                                                    np.std(temp1),
                                                                                                    np.mean(temp2),
                                                                                                    np.std(temp2))
                else:
                    print_gt += '%s %s (p=%0.3f)\n' % (ukey, ureg, p)
        print(print_st)
        print(print_gt)
