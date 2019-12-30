from abc import abstractmethod

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
from sklearn.preprocessing import KBinsDiscretizer

from azureml.studio.common.utils.datetimeutils import convert_to_ns
from azureml.studio.core.data_frame_schema import ColumnTypeName, ElementTypeName
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.utils.missing_value_utils import is_na

NUMERIC_COMPUTATION_SET = {ColumnTypeName.NUMERIC, ColumnTypeName.DATETIME,
                           ColumnTypeName.TIMESPAN, ColumnTypeName.BINARY}
TIME_SET = {ColumnTypeName.DATETIME, ColumnTypeName.TIMESPAN}


class FeatureScoringMethod:
    """Base class for all feature scoring method."""

    def __init__(self, target_col_series, target_col_type):
        self.target_col_series = self.pre_process_series(target_col_series, target_col_type)
        self.target_col_type = target_col_type

    @abstractmethod
    def score(self, scoring_col_series, scoring_col_type):
        """Get score between feature and target column.

        :param scoring_col_series: pd.Series
        :param scoring_col_type: str
        :return:
        """
        return

    @staticmethod
    def pre_process_series(series, col_type):
        # If column type is DATETIME or TIMESPAN, then nanoseconds are extracted.
        return convert_to_ns(series) if col_type in TIME_SET else series


class PearsonCorrelation(FeatureScoringMethod):
    def __init__(self, target_col_series, target_col_type):
        super().__init__(target_col_series, target_col_type)
        # Convert to categorical type if target column is not numeric computed
        # and not categorical based on V1
        if target_col_type not in NUMERIC_COMPUTATION_SET \
                and target_col_type != ColumnTypeName.CATEGORICAL:
            self.target_col_series = self.target_col_series.astype(ElementTypeName.CATEGORY)
            self.target_col_type = ColumnTypeName.CATEGORICAL

    def score(self, scoring_col_series, scoring_col_type):
        scoring_col_series = self.pre_process_series(scoring_col_series, scoring_col_type)
        # Deal with categorical series
        _is_cat_target = self.target_col_type == ColumnTypeName.CATEGORICAL
        _is_cat_score = scoring_col_type == ColumnTypeName.CATEGORICAL
        # Based on V1, will return 0 for such two cases:
        # 1. scoring column is not numeric computation type and not categorical,
        # because str but not categorical feature is not allowed in pearson correlation.
        # 2. both target and scoring series categorical,
        # because 'convert_to_numeric_using_condition_mean' op requires at least one side is numerical.
        if (scoring_col_type not in NUMERIC_COMPUTATION_SET and not _is_cat_score) \
                or (_is_cat_target and _is_cat_score):
            return 0

        scoring_col_arr = scoring_col_series.values
        target_col_arr = self.target_col_series.values
        if _is_cat_target:
            # In this case target col is categorical array and scoring is numeric array.
            target_col_arr = self.convert_to_numeric_using_condition_mean(
                target_col_arr, scoring_col_arr)
        elif _is_cat_score:
            # In this case score col is categorical array and target is numeric array
            scoring_col_arr = self.convert_to_numeric_using_condition_mean(
                scoring_col_arr, target_col_arr)
        # With above checking, both scoring_col_arr and target_col_arr are expected to be numerical,
        # proper for 'pearsonr' op.
        co_eff, _ = pearsonr(scoring_col_arr, target_col_arr)
        # Explanation for why use absolute value of pearson coefficient for rank:
        # 1. Almost no relation if coefficient is 0
        # 2. Positive correlation if coefficient is positive, stronger correlation if bigger coefficient
        # 3. Negative correlation if coefficient is negative, stronger correlation if smaller coefficient
        logger.info(f"Pearson correlation for '{scoring_col_series.name}': "
                    f"{'Negative' if co_eff < 0 else ('Positive' if co_eff > 0 else 'Unrelated')}.")
        co_eff = np.abs(co_eff)
        return 0 if is_na(co_eff) else co_eff

    @staticmethod
    def convert_to_numeric_using_condition_mean(cat_arr, num_arr):
        """Replaces every value with class mean value based on V1.

        :param cat_arr:
        :param num_arr:
        :return:
        """
        val_cnt_dict = {}
        for value in cat_arr:
            val_cnt_dict.setdefault(value, 0)
            val_cnt_dict[value] += 1

        # For each level in the categorical column, compute the conditional mean of numeric column.
        converted_val_dict = {}
        for i, target_val in enumerate(num_arr):
            cat_val = cat_arr[i]
            converted_val_dict.setdefault(cat_val, 0)
            converted_val_dict[cat_val] += 1.0 * num_arr[i] / val_cnt_dict[cat_val]

        converted_cat_arr = [converted_val_dict[value] for value in cat_arr]
        return converted_cat_arr


class ChiSquared(FeatureScoringMethod):
    def score(self, scoring_col_series, scoring_col_type):
        scoring_col_series = self.pre_process_series(scoring_col_series, scoring_col_type)
        # Scrub missing values by dropping rows if NaN in either column
        scrub_series = pd.concat([scoring_col_series, self.target_col_series], axis=1).dropna(how='any')
        # Score will be 0 if scrub series is empty
        if scrub_series.size == 0:
            return 0

        # Set up maximum category num for numeric computed input via binned series for reasonable feature rank
        scoring_col_series = self.setup_binned_series(scrub_series[scoring_col_series.name], scoring_col_type)
        target_col_series = self.setup_binned_series(scrub_series[self.target_col_series.name], self.target_col_type)
        logger.info("Constructing contingency table.")
        contingency_table = pd.crosstab(scoring_col_series, target_col_series, margins=False)
        logger.info("Calculating chi squared.")
        chi2, p, dof, expected = chi2_contingency(contingency_table.values, correction=False)
        return chi2

    @staticmethod
    def setup_binned_series(input_series, input_col_type):
        """Setup binned array for limited group (10) to avoid potential memory usage jump
        and avoid wrong rank caused by simply treating numeric feature as str.
        See 'test_success_diff_between_numeric_and_str' in 'test_chisquare' as for effects of KBinsDiscretizer.

        :param input_series: np.array
        :param input_col_type: str
        :return: pd.Series
        """
        # 10 may be an empirical value in V1 for n_bins by setting a maximum category count to prevent top
        # rank caused by too diverse categories in numerical feature.
        n_bins = 10
        input_arr = input_series.values
        # Simply treat continuous feature as str feature if distinct category num is not greater than bin num.
        if input_col_type in NUMERIC_COMPUTATION_SET and input_series.unique().size > n_bins:
            # Strengths for 'kmeans' strategy compared to 'quantile':
            # 1. Valid for imbalanced/sparse data. It is impossible to set up equal-height bins
            # with 'quantile' strategy, which leads to chi2 0 finally.
            # 2. Clustering to discretize makes more sense than simply equal height quantizer.
            est = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy='kmeans')
            binned_arr = est.fit_transform(input_arr.reshape(-1, 1)).flatten()
            logger.info(f"Set up binned array with edge {est.bin_edges_[0]}")
        else:
            binned_arr = input_arr
        return pd.Series(binned_arr)
