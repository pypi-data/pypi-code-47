import numpy as np
from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing
from scipy.stats import t
# from scipy.stats.stats import _ttest_finish
from ccalafiore.combinations import n_conditions_to_combinations


def scores_to_diff_of_scores(scores, axis=0, delta=1, stride=1, keepdims=False):

    shape_scores = np.asarray(scores.shape)
    n_axes_scores = shape_scores.size
    if axis < 0:
        axis += n_axes_scores

    n_conditions = shape_scores[axis]
    index_0 = np.empty(n_axes_scores, dtype=object)
    index_0[:] = slice(None)
    index_1 = np.copy(index_0)

    index_diff = np.copy(index_0)
    index_diff[axis] = 0

    n_differences = int((n_conditions - delta) // stride)
    shape_diff_of_scores = shape_scores
    shape_diff_of_scores[axis] = n_differences
    diff_of_scores = np.empty(shape_diff_of_scores, dtype=scores.dtype)

    for i in range(0, n_conditions - delta, stride):
        index_0[axis] = i
        index_1[axis] = i + delta
        diff_of_scores[tuple(index_diff)] = scores[tuple(index_0)] - scores[tuple(index_1)]
        index_diff[axis] += 1

    if not keepdims and (diff_of_scores.shape[axis] == 1):
        diff_of_scores = np.squeeze(diff_of_scores, axis=axis)

    return diff_of_scores




def scores_to_means(scores, axis_samples=-1, keepdims=False):

    if scores.dtype == object:
        print('object')
        shape_object_scores = np.asarray(scores.shape)
        n_axes_object_scores = shape_object_scores.size
        indexes_object = np.empty(n_axes_object_scores,dtype=object)
        indexes_object[:] = 0
        shape_scores = np.asarray(scores[tuple(indexes_object)].shape)
        n_axes_scores = shape_scores.size
        if axis_samples < 0:
            axis_samples += n_axes_scores

        if keepdims:
            shape_scores_tmp = shape_scores
            shape_scores_tmp[axis_samples] = 1
        else:
            shape_scores_tmp = shape_scores[np.arange(n_axes_scores) != axis_samples]

        shape_means_of_scores = np.append(shape_object_scores, shape_scores_tmp)
        n_samples = np.empty(shape_means_of_scores, dtype=int)
        means_of_scores = np.empty(shape_means_of_scores, dtype=float)
        n_axes_means_of_scores = shape_means_of_scores.size
        indexes_means = np.empty(n_axes_means_of_scores,dtype=object)
        indexes_means[:] = slice(None)
        axes_object_scores = np.arange(n_axes_scores)


        indexes_object = n_conditions_to_combinations(shape_object_scores)
        n_indexes_object = np.prod(shape_object_scores)
        for i in indexes_object:

            indexes_means[axes_object_scores] = i
            indexes_means_tuple = tuple(indexes_means)

            i_tuple = tuple(i)
            print(i)

            n_samples[indexes_means_tuple] = np.sum(
                np.logical_not(np.isnan(scores[i_tuple])), axis=axis_samples, keepdims=keepdims)
            means_of_scores[indexes_means_tuple] = np.nansum(
                scores[i_tuple], axis=axis_samples, keepdims=keepdims) / n_samples[indexes_means_tuple]

    else:
        print('not object')

        shape_scores = np.asarray(scores.shape)
        n_axes_scores = shape_scores.size
        if axis_samples < 0:
            axis_samples += n_axes_scores

        n_samples = np.sum(np.logical_not(np.isnan(scores)), axis=axis_samples, keepdims=keepdims)
        means_of_scores = np.nansum(scores, axis=axis_samples, keepdims=keepdims) / n_samples

    return means_of_scores


def scores_to_variances(scores, axis_samples=-1, keepdims=False):


    shape_scores = scores.shape
    n_axes_scores = len(shape_scores)
    axis_samples %= n_axes_scores

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
