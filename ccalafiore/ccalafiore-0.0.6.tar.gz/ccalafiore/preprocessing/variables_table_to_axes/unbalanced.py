# import numpy as np
from ccalafiore.array import samples_in_arr1_are_in_arr2  # , advanced_indexing
# from ccalafiore.combinations import \
#     trials_to_conditions, conditions_to_n_conditions, n_conditions_to_combinations, conditions_to_combinations
from ccalafiore.combinations import *
from ccalafiore.preprocessing.variables_table_to_axes import balanced.from_1_array

def from_1_array(
        array_input,
        axes_inserting=0,
        axis_samples=-2,
        axis_variables_table=-1,
        variables_table_adding_axes=0,
        variables_table_staying=None):  # ,
    # dtype=None):

    # Notes:
    # 1) it is safe;
    # 2) it does not assumes that the numbers of samples (or trials) in the axis_samples for all
    #    combinations of variables_table_adding_axes are equal;
    # 3) it does not assumes that the order of samples (or trials) in the axis_samples are is the same
    #    in each combination of variables' axes. The order is based on the order of the combinations
    #    of variables' conditions in axis_variables_table_input. In other words, the samples can be in random order
    #    (or in different order) in each combinations of variables axes/conditions.

    # Input requirements:
    # 1) axes_inserting cannot contain same values;
    # 2) variables_table_adding_axes cannot contain same values;
    # 3) shapes of axes_inserting and variables_table_adding_axes must be equal;
    # 4) axis_samples != axis_variables_table_input;
    # 5) the numbers of samples (or trials) in the axis_samples for all combinations
    #    of variables_table_adding_axes do not need to be equal.

    # Import requirements:
    # 1) import numpy as np
    # 2) from ccalafiore.combinations import n_conditions_to_combinations
    # 3) from ccalafiore.combinations import trials_to_conditions
    # 4) from ccalafiore.combinations import conditions_to_n_conditions
    # 5) from ccalafiore.combinations import conditions_to_combinations
    # 6) from ccalafiore.array import samples_in_arr1_are_in_arr2
    # 7) from ccalafiore.array import advanced_indexing

    # from ccalafiore.combinations import \
    #     trials_to_conditions, conditions_to_n_conditions, n_conditions_to_combinations, \
    #     conditions_to_combinations
    # from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing

    # format axes_inserting
    try:
        n_axes_inserting = len(axes_inserting)
        axes_inserting = np.asarray(axes_inserting, dtype=int)
    except TypeError:
        axes_inserting = np.asarray([axes_inserting], dtype=int)
        n_axes_inserting = axes_inserting.size

    # format variables_table_adding_axes
    try:
        n_variables_table_adding_axes = len(variables_table_adding_axes)
        variables_table_adding_axes = \
            np.asarray(variables_table_adding_axes, dtype=int)
    except TypeError:
        variables_table_adding_axes = \
            np.asarray([variables_table_adding_axes], dtype=int)
        n_variables_table_adding_axes = variables_table_adding_axes.size

    axis_variables_table_input = axis_variables_table
    axis_samples_input = axis_samples

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = shape_array_input.size
    n_variables_table_input = shape_array_input[axis_variables_table_input]

    axis_variables_table_input %= n_axes_array_input
    axis_samples_input %= n_axes_array_input
    variables_table_adding_axes %= n_variables_table_input

    n_axes_array_output = n_axes_array_input + n_axes_inserting - 2
    # 2 axes, i.e. the axis_variables_table_input and the axis_samples_input will be put inside each element
    # of the object array "array_output".
    axes_inserting %= n_axes_array_output

    # check point 1
    if np.sum(axes_inserting[0] == axes_inserting) > 1:
        raise Exception('axes_inserting cannot contain repeated values')
    # check point 2
    if np.sum(
            variables_table_adding_axes[
                0] == variables_table_adding_axes) > 1:
        raise Exception('variables_table_adding_axes cannot contain repeated values')
    # check point 3
    if n_variables_table_adding_axes != n_axes_inserting:
        raise Exception(
            'Shapes of axes_inserting and variables_table_adding_axes must be equal')

    # check point 4
    if np.sum(axis_samples_input == axis_variables_table_input) > 0:
        raise Exception('axis_samples_input and axis_variables_table_input must be different')

    axes_array_input = np.arange(n_axes_array_input)
    axes_non_axis_variables_table_input = axes_array_input[axes_array_input != axis_variables_table_input]
    axes_other_array_input = axes_non_axis_variables_table_input[
        axes_non_axis_variables_table_input != axis_samples_input]
    axes_other_array_input_inverted = axes_other_array_input[::-1]
    n_axes_other_array_input = axes_other_array_input.size

    variables_table_input = np.arange(n_variables_table_input)
    if variables_table_staying is None:
        variables_table_staying = variables_table_input[np.logical_not(
            samples_in_arr1_are_in_arr2(variables_table_input, variables_table_adding_axes))]
    # n_variables_table_staying = variables_table_staying.size

    indexes_array_input_c = np.full(n_axes_array_input, 0, dtype=object)
    indexes_array_input_c[axis_variables_table_input] = variables_table_adding_axes
    indexes_array_input_c[axis_samples_input] = np.arange(shape_array_input[axis_samples_input])
    indexes_input = advanced_indexing(indexes_array_input_c)
    array_variables_adding_axes_1_case = array_input[indexes_input]
    # indexes_array_input_i = np.full(n_axes_array_input, 0, dtype=object)
    # indexes_array_input_i[axis_samples_input] = slice(None)
    # indexes_array_input_i[axis_variables_table_input] = slice(None)
    # indexes_array_input_tuple_i = tuple(indexes_array_input_i)
    for a in axes_other_array_input_inverted:
        array_variables_adding_axes_1_case = np.squeeze(array_variables_adding_axes_1_case, axis=a)

    axis_variables_in_combinations = int(axis_variables_table_input > axis_samples_input)
    axis_combinations_in_combinations = int(not (bool(axis_variables_in_combinations)))
    conditions_variables_table_adding_axes = trials_to_conditions(
        array_variables_adding_axes_1_case, axis_combinations=axis_combinations_in_combinations)
    n_conditions_variables_table_adding_axes = conditions_to_n_conditions(
        conditions_variables_table_adding_axes)
    n_combinations_variables_table_adding_axes = int(np.prod(
        n_conditions_variables_table_adding_axes))

    # axes_inserting_sorted = np.sort(axes_inserting) # ?????????         ???

    combinations_variables_table_adding_axes = conditions_to_combinations(
        conditions_variables_table_adding_axes, axis_combinations=axis_combinations_in_combinations)
    # n_combinations_variables_table_adding_axes = combinations_variables_table_adding_axes.shape[
    #     axis_combinations_in_combinations]
    indexes_combinations = np.empty(2, dtype=object)
    indexes_combinations[axis_variables_in_combinations] = np.arange(
        n_variables_table_adding_axes)
    # indexes_combinations_to_remove_axis_combinations = np.full(2, 0, dtype=object)
    # indexes_combinations_to_remove_axis_combinations[axis_variables_in_combinations] = slice(None)
    # indexes_combinations_to_remove_axis_combinations = tuple(
    #     indexes_combinations_to_remove_axis_combinations)

    combinations_axes_inserting = n_conditions_to_combinations(
        n_conditions_variables_table_adding_axes, axis_combinations=axis_combinations_in_combinations)

    # n_variables_table_output = \
    #     n_variables_table_input - n_variables_table_adding_axes

    # if axis_variables_table_input > axis_samples_input:
    #     axis_variables_table_output = 1
    #     axis_samples_output = 0
    # elif axis_variables_table_input < axis_samples_input:
    #     axis_variables_table_output = 0
    #     axis_samples_output = 1

    axes_array_output = np.arange(n_axes_array_output)
    shape_array_output = np.empty(n_axes_array_output, dtype=int)
    shape_array_output[axes_inserting] = n_conditions_variables_table_adding_axes
    axes_other_output = axes_array_output[np.logical_not(
        samples_in_arr1_are_in_arr2(axes_array_output, axes_inserting))]
    shape_array_output[axes_other_output] = shape_array_input[axes_other_array_input]
    array_output = np.empty(shape_array_output, dtype=object)

    indexes_output = np.empty(n_axes_array_output, dtype=object)
    indexes_input = np.empty(n_axes_array_input, dtype=object)
    for a in range(n_axes_array_input):
        indexes_input[a] = np.arange(shape_array_input[a])
    indexes_input[axis_variables_table_input] = variables_table_staying

    if n_axes_other_array_input == 0:

        for c in range(n_combinations_variables_table_adding_axes):

            indexes_combinations[axis_combinations_in_combinations] = c

            indexes_input[axis_samples_input] = np.all(
                array_variables_adding_axes_1_case ==
                combinations_variables_table_adding_axes[advanced_indexing(indexes_combinations)],
                axis=axis_variables_in_combinations)

            array_variables_staying_input_c = array_input[advanced_indexing(indexes_input)]
            for a in axes_other_array_input_inverted:
                array_variables_staying_input_c = np.squeeze(array_variables_staying_input_c, axis=a)

            combinations_axes_inserting_c = combinations_axes_inserting[advanced_indexing(
                indexes_combinations)]
            combinations_axes_inserting_c = np.squeeze(
                combinations_axes_inserting_c, axis=axis_combinations_in_combinations)

            indexes_output[axes_inserting] = combinations_axes_inserting_c
            array_output[tuple(indexes_output)] = array_variables_staying_input_c
    else:

        indexes_input_conditions = np.copy(indexes_input)
        indexes_input_conditions[axis_variables_table_input] = variables_table_adding_axes

        combinations_axes_other_input = n_conditions_to_combinations(shape_array_input[axes_other_array_input])
        n_combinations_axes_other_input = combinations_axes_other_input.shape[0]
        for i in range(n_combinations_axes_other_input):

            indexes_input_conditions[axes_other_array_input] = combinations_axes_other_input[i]
            # indexes_input_conditions = advanced_indexing(indexes_input_conditions)
            array_variables_adding_axes_i = array_input[advanced_indexing(indexes_input_conditions)]
            for a in axes_other_array_input_inverted:
                array_variables_adding_axes_i = np.squeeze(array_variables_adding_axes_i, axis=a)

            indexes_input[axes_other_array_input] = combinations_axes_other_input[i]
            indexes_output[axes_other_output] = combinations_axes_other_input[i]

            for c in range(n_combinations_variables_table_adding_axes):

                indexes_combinations[axis_combinations_in_combinations] = c

                indexes_input[axis_samples_input] = np.all(
                    array_variables_adding_axes_i ==
                    combinations_variables_table_adding_axes[advanced_indexing(indexes_combinations)],
                    axis=axis_variables_in_combinations)

                array_variables_staying_input_i_c = array_input[advanced_indexing(indexes_input)]
                for a in axes_other_array_input_inverted:
                    array_variables_staying_input_i_c = np.squeeze(array_variables_staying_input_i_c, axis=a)

                combinations_axes_inserting_i_c = combinations_axes_inserting[advanced_indexing(
                    indexes_combinations)]
                combinations_axes_inserting_i_c = np.squeeze(
                    combinations_axes_inserting_i_c, axis=axis_combinations_in_combinations)
                indexes_output[axes_inserting] = combinations_axes_inserting_i_c

                array_output[tuple(indexes_output)] = array_variables_staying_input_i_c

    return array_output
