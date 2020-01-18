import numpy as np
from ccalafiore.array import pad_arr_1_from_arr_2
from scipy.stats import t, sem
from scipy.stats.stats import _ttest_finish
from ccalafiore.combinations import n_conditions_to_combinations

def reshape_to_test_all_pairs_of_conditions_for_each_variable(scores, n_variables_other=0):

    shape_scores = np.asarray(scores.shape)

    n_axis = len(shape_scores)

    variables_other = np.arange(n_variables_other)
    n_conditions_other = shape_scores[variables_other]

    axis_samples_per_combination = n_axis - 1
    n_samples_per_combination = shape_scores[axis_samples_per_combination]

    variables_to_test = np.arange(n_variables_other, axis_samples_per_combination)
    n_conditions_to_test = shape_scores[variables_to_test]
    n_variables_to_test = len(variables_to_test)

    scores_reshaped = np.empty(n_variables_to_test, dtype=object)

    n_samples_per_condition = np.empty(n_variables_to_test, dtype=int)

    index_scores = np.full(n_axis, slice(None))

    index_scores_reshaped = np.full(n_variables_other + 2, slice(None))

    shape_scores_reshaped_per_condition = np.empty(n_variables_other + 1, dtype=int)
    shape_scores_reshaped_per_condition[variables_other] = shape_scores[variables_other]

    for i_variable_to_test in range(n_variables_to_test):

        n_samples_per_condition[i_variable_to_test] = n_samples_per_combination * np.prod(
            n_conditions_to_test[variables_to_test != variables_to_test[i_variable_to_test]])

        scores_reshaped[i_variable_to_test] = np.full([
            *n_conditions_other,
            n_conditions_to_test[i_variable_to_test],
            n_samples_per_condition[i_variable_to_test]], np.nan)

        index_scores[variables_to_test] = slice(None)

        shape_scores_reshaped_per_condition[-1] = n_samples_per_condition[i_variable_to_test]

        for i_condition_to_test in range(n_conditions_to_test[i_variable_to_test]):

            index_scores[variables_to_test[i_variable_to_test]] = i_condition_to_test

            index_scores_reshaped[-2] = i_condition_to_test

            scores_reshaped[i_variable_to_test][tuple(index_scores_reshaped)] = \
                scores[tuple(index_scores)].reshape(shape_scores_reshaped_per_condition)

    return scores_reshaped


def diff_of_conditions(scores):

    n_variables_to_test = len(scores)

    diff_of_scores = np.empty(n_variables_to_test, dtype=object)

    n_conditions_to_test = np.empty(n_variables_to_test, dtype=int)
    # axis_mean = len(scores[0].shape) - 1

    for i_variable_to_test in range(n_variables_to_test):

        shape_scores = np.asarray(scores[i_variable_to_test].shape)

        n_axes_scores = len(shape_scores)

        axis_conditions_scores = n_axes_scores - 2

        n_conditions_to_test[i_variable_to_test] = shape_scores[axis_conditions_scores]

        index_1 = np.full(n_axes_scores, slice(None))

        index_2 = np.full(n_axes_scores, slice(None))


        n_axes_diff_of_scores = n_axes_scores + 1

        index_diff = np.full(n_axes_diff_of_scores, slice(None))

        shape_diff = np.insert(shape_scores, axis_conditions_scores, n_conditions_to_test[i_variable_to_test])

        diff_of_scores[i_variable_to_test] = np.full(shape_diff, np.nan)

        for i_condition_1 in range(n_conditions_to_test[i_variable_to_test]):

            index_1[axis_conditions_scores] = i_condition_1

            index_diff[-3] = i_condition_1

            for i_condition_2 in range(n_conditions_to_test[i_variable_to_test]):

                index_2[axis_conditions_scores] = i_condition_2

                index_diff[-2] = i_condition_2

                diff_of_scores[i_variable_to_test][tuple(index_diff)] = \
                    scores[i_variable_to_test][tuple(index_1)] - scores[i_variable_to_test][tuple(index_2)]

    return diff_of_scores


def means_of_conditions(scores):
    n_variables_to_test = len(scores)
    means_of_scores = np.empty(n_variables_to_test, dtype=object)

    for i_variable_to_test in range(n_variables_to_test):
        shape_scores = scores[i_variable_to_test].shape

        n_axes = len(shape_scores)

        axis_samples = n_axes - 1

        n_samples = np.sum(scores[i_variable_to_test] != np.nan, axis_samples)

        means_of_scores[i_variable_to_test] = np.nansum(scores[i_variable_to_test], axis=axis_samples) / n_samples

    return means_of_scores


def variances_of_conditions(scores):
    means_of_scores = means_of_conditions(scores)

    n_variables_experimental = len(scores)

    variances = np.empty(n_variables_experimental, dtype=object)

    for i_variable_to_test in range(n_variables_experimental):
        shape_scores = scores[i_variable_to_test].shape

        n_axes = len(shape_scores)

        axis_samples = n_axes - 1

        n_samples = np.sum(scores[i_variable_to_test] != np.nan, axis_samples)

        means = pad_arr_1_from_arr_2(means_of_scores[i_variable_to_test], scores[i_variable_to_test], axis=axis_samples)

        df = n_samples - 1

        variances[i_variable_to_test] = np.nansum((scores[i_variable_to_test] - means) ** 2, axis=axis_samples) / df

    return variances


def standard_error(scores):
    variances = variances_of_conditions(scores)

    n_variables_experimental = len(scores)
    std_error = np.empty(n_variables_experimental, dtype=object)

    for i_variable_to_test in range(n_variables_experimental):
        shape_scores = scores[i_variable_to_test].shape

        n_axes = len(shape_scores)

        axis_samples = n_axes - 1

        # n_samples = shape_scores[axis_samples]
        n_samples = np.sum(scores[i_variable_to_test] != np.nan, axis_samples)

        std_error[i_variable_to_test] = np.sqrt(variances[i_variable_to_test] / n_samples)

    return std_error


def paired_t_test(scores, scores_input=True, alpha=0.05):

    np.seterr(divide='ignore', invalid='ignore')

    confidence = 1 - alpha

    if scores_input:
        diff = diff_of_conditions(scores)
    else:
        diff = scores

    means_of_diff = means_of_conditions(diff)

    std_err_of_diff = standard_error(diff)

    n_variables_experimental = len(scores)


    t_values = np.empty(n_variables_experimental, dtype=object)
    df = np.empty(n_variables_experimental, dtype=object)
    t_critical = np.empty(n_variables_experimental, dtype=object)
    p_values = np.empty(n_variables_experimental, dtype=object)

    h = np.empty(n_variables_experimental, dtype=object)

    for i_variable_to_test in range(n_variables_experimental):

        t_values[i_variable_to_test] = means_of_diff[i_variable_to_test] / std_err_of_diff[i_variable_to_test]
        np.nan_to_num(t_values[i_variable_to_test], copy=False, nan=0.0)

        shape_diff = diff[i_variable_to_test].shape

        n_axes = len(shape_diff)

        axis_samples = n_axes - 1

        n_samples = np.sum(diff[i_variable_to_test] != np.nan, axis_samples)

        df[i_variable_to_test] = n_samples - 1

        shape_df = df[i_variable_to_test].shape

        n_df = df[i_variable_to_test].size

        t_critical[i_variable_to_test] = np.empty(shape_df, dtype=float)
        p_values[i_variable_to_test] = np.empty(shape_df, dtype=float)

        h[i_variable_to_test] = np.empty(shape_df, dtype=float)

        indexs_df = n_conditions_to_combinations(shape_df)
        for i in range(n_df):

            t_critical[i_variable_to_test][tuple(indexs_df[i])] = t.ppf(
                (1 + confidence) / 2.,
                df[i_variable_to_test][tuple(indexs_df[i])])

            # calculate the p-value
            # p_values[i_variable_to_test][tuple(indexs_df[i])] = (1.0 - t.cdf(abs(t_values[i_variable_to_test][tuple(indexs_df[i])]),df[i_variable_to_test][tuple(indexs_df[i])])) * 2.0
            p_values[i_variable_to_test][tuple(indexs_df[i])] = (1.0 - t.cdf(
                t_values[i_variable_to_test][tuple(indexs_df[i])],
                df[i_variable_to_test][tuple(indexs_df[i])])) * 2
            # other, p_values[i_variable_to_test][tuple(indexs_df[i])] = _ttest_finish(
            #    df[i_variable_to_test][tuple(indexs_df[i])],
            #    t_values[i_variable_to_test][tuple(indexs_df[i])])

            # se[i_variable_to_test][tuple(indexs_df[i])] = sem(diff[i_variable_to_test][tuple(indexs_df[i])])



            # h2[i_variable_to_test][tuple(indexs_df[i])]
            # g = t.interval(
            #     confidence,
            #     df[i_variable_to_test][tuple(indexs_df[i])],
            #     loc=means_of_diff[i_variable_to_test][tuple(indexs_df[i])],
            #     scale=std_err_of_diff[i_variable_to_test][tuple(indexs_df[i])])
        h[i_variable_to_test] = std_err_of_diff[i_variable_to_test] * t_critical[i_variable_to_test]

    # return everything
    # return t_stat, df, cv, p
    return t_values, df, t_critical, p_values, h
    # return t_values, df, p_values


# def height_of_t_confidence_interval(data, confidence=0.95):
#     a = 1.0 * np.array(data)
#     n = len(a)
#     m, se = np.mean(a), stats.sem(a)
#     h = se * stats.t.ppf((1 + confidence) / 2., n-1)
#     return h
