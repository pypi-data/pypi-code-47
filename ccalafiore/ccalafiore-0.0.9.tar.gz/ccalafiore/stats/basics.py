import numpy as np
from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing
from scipy.stats import t
# from scipy.stats.stats import _ttest_finish
from ccalafiore.combinations import n_conditions_to_combinations


def scores_to_diff_of_scores(scores, axis_comparisons=0, keepdims=False):

    shape_scores = np.asarray(scores.shape)
    n_axes_scores = len(shape_scores)
    axis_comparisons %= n_axes_scores
    axes_scores = np.arange(n_axes_scores)
    axis_non_comparisons = axes_scores[np.logical_not(samples_in_arr1_are_in_arr2(axes_scores, axis_comparisons))]

    index_0 = np.empty(n_axes_scores, dtype=object)
    for a in axis_non_comparisons:
        index_0[a] = np.arange(shape_scores[a])
    index_1 = np.copy(index_0)

    index_0[axis_comparisons] = 0
    index_1[axis_comparisons] = 1

    diff_of_scores = scores[advanced_indexing(index_0)] - scores[advanced_indexing(index_1)]
    if not keepdims:
        diff_of_scores = np.squeeze(diff_of_scores, axis=axis_comparisons)

    return diff_of_scores




def scores_to_means(scores, axis_samples=-1, keepdims=False):

    shape_scores = np.asarray(scores.shape)
    n_axes_scores = len(shape_scores)
    axis_samples %= n_axes_scores

    n_samples = np.sum(np.logical_not(np.isnan(scores)), axis=axis_samples, keepdims=keepdims)
    # if keepdims:
    #     n_samples = np.expand_dims(n_samples, axis=axis_samples)
    # n_samples = np.nansum(scores, axis=axis_samples, keepdims=keepdims)
    means_of_scores = np.nansum(scores, axis=axis_samples, keepdims=keepdims) / n_samples
    return means_of_scores


def scores_to_variances(scores, axis_samples=-1, keepdims=False):


    shape_scores = scores.shape
    n_axes_scores = len(shape_scores)
    axis_samples %= n_axes_scores

    # n_samples = np.nansum(scores, axis=axis_samples, keepdims=keepdims)
    n_samples = np.sum(np.logical_not(np.isnan(scores)), axis=axis_samples, keepdims=keepdims)
    df = n_samples - 1
    means = scores_to_means(scores, axis_samples=axis_samples, keepdims=True)
    variances = np.nansum((scores - means) ** 2, axis=axis_samples, keepdims=keepdims) / df

    return variances


def scores_to_standard_error(scores, axis_samples=-1, keepdims=False):

    shape_scores = scores.shape
    n_axes = len(shape_scores)
    axis_samples %= n_axes

    n_samples = np.sum(np.logical_not(np.isnan(scores)), axis=axis_samples, keepdims=keepdims)
    variances = scores_to_variances(scores, axis_samples=axis_samples, keepdims= keepdims)
    std_error = np.sqrt(variances / n_samples)

    return std_error


def scores_to_confidence_interval(
        scores, axis_samples=-1, alpha=0.05, tails='2', keepdims=False):

    confidence = 1 - alpha
    shape_scores = scores.shape
    n_axes = len(shape_scores)
    axis_samples %= n_axes

    n_samples = np.sum(np.logical_not(np.isnan(scores)), axis=axis_samples, keepdims=keepdims)
    std_err_of_diff = scores_to_standard_error(scores, axis_samples=axis_samples, keepdims=keepdims)

    df = n_samples - 1
    shape_df = df.shape
    n_df = df.size

    t_critical = np.empty(shape_df, dtype=float)
    indexs_df = n_conditions_to_combinations(shape_df)
    for i in range(n_df):

        if tails == '2':
            t_critical[tuple(indexs_df[i])] = t.ppf((1 + confidence) / 2., df[tuple(indexs_df[i])])

        elif tails == '1l':
            t_critical[tuple(indexs_df[i])] = -t.ppf(confidence, df[tuple(indexs_df[i])])
        elif tails == '1r':
            t_critical[tuple(indexs_df[i])] = t.ppf(confidence, df[tuple(indexs_df[i])])

    h = std_err_of_diff * t_critical

    return h
