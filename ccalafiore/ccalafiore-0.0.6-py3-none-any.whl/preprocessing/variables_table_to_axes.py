import numpy as np
from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing
# from ccalafiore.combinations import \
#     trials_to_conditions, conditions_to_n_conditions, n_conditions_to_combinations, conditions_to_combinations
from ccalafiore.combinations import *


def faster_balanced(
        array_input,
        axes_inserting_output=0,
        axis_samples_input=-2,
        axis_variables_table_input=-1,
        variables_removing_table_input=0,
        variables_staying_table_input=None,
        dtype=None):

    # Notes:
    # 1) it is faster than the safer version;
    # 2) it assumes that the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal;
    # 3) it does assumes that the order of samples (or trials) in the axis_samples_input are is the same
    #    in each combination of variables' axes. The order is based on the order of the combinations
    #    of variables' conditions in axis_variables_table_input. In other words, the samples cannot be in random order
    #    (or in different order) in each combinations of variables axes/conditions.

    # Input requirements:
    # 1) axes_inserting_output cannot contain same values;
    # 2) variables_removing_table_input cannot contain same values;
    # 3) shapes of axes_inserting_output and variables_removing_in_axis_variables_table_input must be equal;
    # 4) axis_samples_input != axis_variables_table_input;
    # 5) the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal;
    # 6) the order of samples (or trials) in the axis_samples_input is the same
    #    in each combination of variables' axes.

    # Import requirements:
    # 1) import numpy as np
    # 2) from ccalafiore.combinations import n_conditions_to_combinations
    # 3) from ccalafiore.combinations import trials_to_conditions
    # 4) from ccalafiore.combinations import conditions_to_n_conditions
    # 5) from ccalafiore.combinations import conditions_to_combinations
    # 6) from ccalafiore.array import samples_in_arr1_are_in_arr2
    # 7) from ccalafiore.array import advanced_indexing

    # from ccalafiore.combinations import \
    #     trials_to_conditions, conditions_to_n_conditions, n_conditions_to_combinations, conditions_to_combinations
    # from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing

    # format axes_inserting_input
    try:
        n_axes_inserting_output = len(axes_inserting_output)
        axes_inserting_output = np.asarray(axes_inserting_output, dtype=int)
    except TypeError:
        axes_inserting_output = np.asarray([axes_inserting_output], dtype=int)
        n_axes_inserting_output = len(axes_inserting_output)

    # format variables_removing_in_axes_variables_output
    try:
        n_variables_removing_table_input = len(variables_removing_table_input)
        variables_removing_table_input = \
            np.asarray(variables_removing_table_input, dtype=int)
    except TypeError:
        variables_removing_table_input = \
            np.asarray([variables_removing_table_input], dtype=int)
        n_variables_removing_table_input = len(variables_removing_table_input)

    if dtype is None:
        dtype = array_input.dtype

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)
    n_variables_table_input = shape_array_input[axis_variables_table_input]

    if axis_variables_table_input < 0:
        axis_variables_table_input += n_axes_array_input
    if axis_samples_input < 0:
        axis_samples_input += n_axes_array_input

    variables_removing_table_input[variables_removing_table_input < 0] += n_variables_table_input

    n_axes_array_output = n_axes_array_input + n_axes_inserting_output
    axes_inserting_output[axes_inserting_output < 0] += n_axes_array_output

    # check point 1
    if np.sum(axes_inserting_output[0] == axes_inserting_output) > 1:
        raise Exception('axes_inserting_output cannot contain repeated values')
    # check point 2
    if np.sum(
            variables_removing_table_input[0] == variables_removing_table_input) > 1:
        raise Exception('variables_removing_table_input cannot contain repeated values')
    # check point 3
    if n_variables_removing_table_input != n_axes_inserting_output:
        raise Exception(
            'Shapes of axes_inserting_output and variables_removing_table_input must be equal')

    # check point 4
    if np.sum(axis_samples_input == axis_variables_table_input) > 0:
        raise Exception('axis_samples_input and axis_variables_table_input must be different')

    axes_array_input = np.arange(n_axes_array_input)
    axes_non_axis_variables_table_input = axes_array_input[axes_array_input != axis_variables_table_input]
    axes_other_array_input = axes_non_axis_variables_table_input[
        axes_non_axis_variables_table_input != axis_samples_input]
    axes_other_array_input_inverted = axes_other_array_input[::-1]
    # n_axes_other_array_input = len(axes_other_array_input)

    variables_table_input = np.arange(n_variables_table_input)

    if variables_staying_table_input is None:
        variables_staying_table_input = variables_table_input[np.logical_not(
            samples_in_arr1_are_in_arr2(variables_table_input, variables_removing_table_input))]
    # n_variables_staying_table_input = len(variables_staying_table_input)

    indexes_array_input_c = np.full(n_axes_array_input, 0, dtype=object)
    indexes_array_input_c[axis_variables_table_input] = variables_removing_table_input
    indexes_array_input_c[axis_samples_input] = np.arange(shape_array_input[axis_samples_input])
    array_variables_removing_input_1_case = array_input[advanced_indexing(indexes_array_input_c)]
    for a in axes_other_array_input_inverted:
        array_variables_removing_input_1_case = np.squeeze(array_variables_removing_input_1_case, axis=a)

    axis_variables_in_combinations_removing = int(axis_variables_table_input > axis_samples_input)
    axis_combinations_in_combinations_removing = int(not (bool(axis_variables_in_combinations_removing)))
    conditions_variables_removing_table_input = trials_to_conditions(
        array_variables_removing_input_1_case, axis_combinations=axis_combinations_in_combinations_removing)
    n_conditions_variables_removing_table_input = conditions_to_n_conditions(
        conditions_variables_removing_table_input)
    n_combinations_variables_removing_table_input = int(np.prod(
        n_conditions_variables_removing_table_input))

    # axes_inserting_output_sorted = np.sort(axes_inserting_output) # ?????????         ???

    combinations_variables_removing_table_input = conditions_to_combinations(
        conditions_variables_removing_table_input,
        axis_combinations=axis_combinations_in_combinations_removing)
    # n_combinations_removing = combinations_variables_removing_table_input.shape[
    #     axis_combinations_in_combinations_removing]
    indexes_combinations_removing = np.empty(2, dtype=object)
    indexes_combinations_removing[axis_variables_in_combinations_removing] = np.arange(
        n_variables_removing_table_input)

    combinations_axes_inserting_output = n_conditions_to_combinations(
        n_conditions_variables_removing_table_input,
        axis_combinations=axis_combinations_in_combinations_removing)

    # n_variables_table_output = \
    #     n_variables_table_input - n_variables_removing_table_input

    axis_variables_table_output = axis_variables_table_input + np.sum(axes_inserting_output <= axis_variables_table_input)
    axis_samples_output = axis_samples_input + np.sum(axes_inserting_output <= axis_samples_input)
    while axis_variables_table_output in axes_inserting_output:
        axis_variables_table_output += 1
    while axis_samples_output in axes_inserting_output:
        axis_samples_output += 1

    if axis_variables_table_output == axis_samples_output:
        if axis_variables_table_input > axis_samples_input:
            axis_variables_table_output += 1
        elif axis_variables_table_input < axis_samples_input:
            axis_samples_output += 1

    axes_array_output = np.arange(n_axes_array_output)
    axes_non_axis_variables_table_output = axes_array_output[axes_array_output != axis_variables_table_output]
    axes_other_output = axes_non_axis_variables_table_output[
        axes_non_axis_variables_table_output != axis_samples_output]
    axes_other_output = axes_other_output[np.logical_not(
        samples_in_arr1_are_in_arr2(axes_other_output, axes_inserting_output))]

    shape_array_output = np.empty(n_axes_array_output, dtype=int)
    shape_array_output[axes_inserting_output] = n_conditions_variables_removing_table_input
    shape_array_output[axis_variables_table_output] = \
        shape_array_input[axis_variables_table_input] - n_variables_removing_table_input
    shape_array_output[axis_samples_output] = \
        shape_array_input[axis_samples_input] / n_combinations_variables_removing_table_input
    shape_array_output[axes_other_output] = shape_array_input[axes_other_array_input]
    array_output = np.empty(shape_array_output, dtype=dtype)

    indexes_output = np.empty(n_axes_array_output, dtype=object)
    for a in range(n_axes_array_output):
        indexes_output[a] = np.arange(shape_array_output[a])

    indexes_input = np.empty(n_axes_array_input, dtype=object)
    for a in range(n_axes_array_input):
        indexes_input[a] = np.arange(shape_array_input[a])
    indexes_input[axis_variables_table_input] = variables_staying_table_input

    axes_inserting_output_sorted = np.sort(axes_inserting_output)

    for c in range(n_combinations_variables_removing_table_input):

        indexes_combinations_removing[axis_combinations_in_combinations_removing] = c

        indexes_input[axis_samples_input] = np.all(
            array_variables_removing_input_1_case ==
            combinations_variables_removing_table_input[advanced_indexing(indexes_combinations_removing)],
            axis=axis_variables_in_combinations_removing)

        array_variables_staying_input_c = array_input[advanced_indexing(indexes_input)]
        for a in axes_inserting_output_sorted:
            array_variables_staying_input_c = np.expand_dims(array_variables_staying_input_c, axis=a)

        combinations_axes_inserting_output_c = combinations_axes_inserting_output[advanced_indexing(
            indexes_combinations_removing)]
        combinations_axes_inserting_output_c = np.squeeze(
            combinations_axes_inserting_output_c, axis=axis_combinations_in_combinations_removing)
        indexes_output[axes_inserting_output] = combinations_axes_inserting_output_c

        array_output[advanced_indexing(indexes_output)] = array_variables_staying_input_c

    return array_output


def safer_fast_balanced(
        array_input,
        axes_inserting_output=0,
        axis_samples_input=-2,
        axis_variables_table_input=-1,
        variables_removing_table_input=0,
        variables_staying_table_input=None,
        dtype=None):

    # Notes:
    # 1) it is safer than the faster version;
    # 2) it assumes that the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal;
    # 3) it does not assumes that the order of samples (or trials) in the axis_samples_input are is the same
    #    in each combination of variables' axes. The order is based on the order of the combinations
    #    of variables' conditions in axis_variables_table_input. In other words, the samples can be in random order
    #    (or in different order) in each combinations of variables axes/conditions.

    # Input requirements:
    # 1) axes_inserting_output cannot contain same values;
    # 2) variables_removing_table_input cannot contain same values;
    # 3) shapes of axes_inserting_output and variables_removing_table_input must be equal
    # 4) axis_samples_input != axis_variables_table_input
    # 5) the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal

    # Import requirements:
    # 1) import numpy as np
    # 2) from ccalafiore.combinations import n_conditions_to_combinations
    # 3) from ccalafiore.combinations import trials_to_conditions
    # 4) from ccalafiore.combinations import conditions_to_n_conditions
    # 5) from ccalafiore.combinations import conditions_to_combinations
    # 6) from ccalafiore.array import samples_in_arr1_are_in_arr2
    # 7) from ccalafiore.array import advanced_indexing

    # from ccalafiore.combinations import \
    #     trials_to_conditions, conditions_to_n_conditions, n_conditions_to_combinations, conditions_to_combinations
    # from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing

    # format axes_inserting_input
    try:
        n_axes_inserting_output = len(axes_inserting_output)
        axes_inserting_output = np.asarray(axes_inserting_output, dtype=int)
    except TypeError:
        axes_inserting_output = np.asarray([axes_inserting_output], dtype=int)
        n_axes_inserting_output = len(axes_inserting_output)

    # format variables_removing_in_axes_variables_output
    try:
        n_variables_removing_table_input = len(variables_removing_table_input)
        variables_removing_table_input = \
            np.asarray(variables_removing_table_input, dtype=int)
    except TypeError:
        variables_removing_table_input = \
            np.asarray([variables_removing_table_input], dtype=int)
        n_variables_removing_table_input = len(variables_removing_table_input)

    if dtype is None:
        dtype = array_input.dtype

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)
    n_variables_table_input = shape_array_input[axis_variables_table_input]

    if axis_variables_table_input < 0:
        axis_variables_table_input += n_axes_array_input
    if axis_samples_input < 0:
        axis_samples_input += n_axes_array_input

    variables_removing_table_input[variables_removing_table_input < 0] += n_variables_table_input

    n_axes_array_output = n_axes_array_input + n_axes_inserting_output
    axes_inserting_output[axes_inserting_output < 0] += n_axes_array_output

    # check point 1
    if np.sum(axes_inserting_output[0] == axes_inserting_output) > 1:
        raise Exception('axes_inserting_output cannot contain repeated values')
    # check point 2
    if np.sum(
            variables_removing_table_input[
                0] == variables_removing_table_input) > 1:
        raise Exception('variables_removing_table_input cannot contain repeated values')
    # check point 3
    if n_variables_removing_table_input != n_axes_inserting_output:
        raise Exception(
            'Shapes of axes_inserting_output and variables_removing_table_input must be equal')

    # check point 4
    if np.sum(axis_samples_input == axis_variables_table_input) > 0:
        raise Exception('axis_samples_input and axis_variables_table_input must be different')

    axes_array_input = np.arange(n_axes_array_input)
    axes_non_axis_variables_table_input = axes_array_input[axes_array_input != axis_variables_table_input]
    axes_other_array_input = axes_non_axis_variables_table_input[
        axes_non_axis_variables_table_input != axis_samples_input]
    axes_other_array_input_inverted = axes_other_array_input[::-1]
    n_axes_other_array_input = len(axes_other_array_input)

    variables_table_input = np.arange(n_variables_table_input)
    if variables_staying_table_input is None:
        variables_staying_table_input = variables_table_input[np.logical_not(
            samples_in_arr1_are_in_arr2(variables_table_input, variables_removing_table_input))]
    n_variables_staying_table_input = len(variables_staying_table_input)

    indexes_array_input_c = np.full(n_axes_array_input, 0, dtype=object)
    indexes_array_input_c[axis_variables_table_input] = variables_removing_table_input
    indexes_array_input_c[axis_samples_input] = np.arange(shape_array_input[axis_samples_input])
    indexes_input = advanced_indexing(indexes_array_input_c)
    array_variables_removing_input_1_case = array_input[indexes_input]
    for a in axes_other_array_input_inverted:
        array_variables_removing_input_1_case = np.squeeze(array_variables_removing_input_1_case, axis=a)

    axis_variables_in_combinations_removing = int(axis_variables_table_input > axis_samples_input)
    axis_combinations_in_combinations_removing = int(not (bool(axis_variables_in_combinations_removing)))
    conditions_variables_removing_table_input = trials_to_conditions(
        array_variables_removing_input_1_case, axis_combinations=axis_combinations_in_combinations_removing)
    n_conditions_variables_removing_table_input = conditions_to_n_conditions(
        conditions_variables_removing_table_input)
    n_combinations_variables_removing_table_input = int(np.prod(
        n_conditions_variables_removing_table_input))

    combinations_variables_removing_table_input = conditions_to_combinations(
        conditions_variables_removing_table_input,
        axis_combinations=axis_combinations_in_combinations_removing)
    # n_combinations_removing = combinations_variables_removing_table_input.shape[
    #     axis_combinations_in_combinations_removing]
    indexes_combinations_removing = np.empty(2, dtype=object)
    indexes_combinations_removing[axis_variables_in_combinations_removing] = np.arange(
        n_variables_removing_table_input)

    combinations_axes_inserting_output = n_conditions_to_combinations(
        n_conditions_variables_removing_table_input)

    # n_variables_table_output = \
    #     n_variables_table_input - n_variables_removing_table_input

    axis_variables_table_output = axis_variables_table_input + np.sum(axes_inserting_output <= axis_variables_table_input)
    axis_samples_output = axis_samples_input + np.sum(axes_inserting_output <= axis_samples_input)
    while axis_variables_table_output in axes_inserting_output:
        axis_variables_table_output += 1
    while axis_samples_output in axes_inserting_output:
        axis_samples_output += 1

    if axis_variables_table_output == axis_samples_output:
        if axis_variables_table_input > axis_samples_input:
            axis_variables_table_output += 1
        elif axis_variables_table_input < axis_samples_input:
            axis_samples_output += 1

    axes_array_output = np.arange(n_axes_array_output)
    axes_non_axis_variables_table_output = axes_array_output[axes_array_output != axis_variables_table_output]
    axes_other_output = axes_non_axis_variables_table_output[
        axes_non_axis_variables_table_output != axis_samples_output]
    axes_other_output = axes_other_output[np.logical_not(
        samples_in_arr1_are_in_arr2(axes_other_output, axes_inserting_output))]

    shape_array_output = np.empty(n_axes_array_output, dtype=int)
    shape_array_output[axes_inserting_output] = n_conditions_variables_removing_table_input
    shape_array_output[axis_variables_table_output] = n_variables_staying_table_input
    shape_array_output[axis_samples_output] = \
        shape_array_input[axis_samples_input] / n_combinations_variables_removing_table_input
    shape_array_output[axes_other_output] = shape_array_input[axes_other_array_input]
    array_output = np.empty(shape_array_output, dtype=dtype)

    indexes_output = np.empty(n_axes_array_output, dtype=object)
    for a in range(n_axes_array_output):
        indexes_output[a] = np.arange(shape_array_output[a])

    indexes_input = np.empty(n_axes_array_input, dtype=object)
    for a in range(n_axes_array_input):   # this line may be removed
        indexes_input[a] = np.arange(shape_array_input[a])   # this line may be removed
    indexes_input[axis_variables_table_input] = variables_staying_table_input

    axes_inserting_output_sorted = np.sort(axes_inserting_output)

    if n_axes_other_array_input == 0:

        for c in range(n_combinations_variables_removing_table_input):

            indexes_combinations_removing[axis_combinations_in_combinations_removing] = c

            indexes_input[axis_samples_input] = np.all(
                array_variables_removing_input_1_case ==
                combinations_variables_removing_table_input[advanced_indexing(indexes_combinations_removing)],
                axis=axis_variables_in_combinations_removing)

            array_variables_staying_input_c = array_input[advanced_indexing(indexes_input)]
            for a in axes_inserting_output_sorted:
                array_variables_staying_input_c = np.expand_dims(array_variables_staying_input_c, axis=a)

            combinations_axes_inserting_output_c = combinations_axes_inserting_output[c]
            # combinations_axes_inserting_output_c = np.squeeze(
            #     combinations_axes_inserting_output_c, axis=axis_combinations_in_combinations_removing)

            indexes_output[axes_inserting_output] = combinations_axes_inserting_output_c
            array_output[advanced_indexing(indexes_output)] = array_variables_staying_input_c
    else:

        indexes_input_conditions = np.copy(indexes_input)
        indexes_input_conditions[axis_variables_table_input] = variables_removing_table_input

        combinations_axes_other_input = n_conditions_to_combinations(shape_array_input[axes_other_array_input])
        n_combinations_axes_other_input = len(combinations_axes_other_input)
        for i in range(n_combinations_axes_other_input):

            indexes_input_conditions[axes_other_array_input] = combinations_axes_other_input[i]
            # indexes_input_conditions_tuple = advanced_indexing(indexes_input_conditions)
            array_variables_removing_input_i = array_input[advanced_indexing(indexes_input_conditions)]
            # array_variables_removing_input_i = array_variables_removing_input_i[indexes_array_input_tuple_i]
            for a in axes_other_array_input_inverted:
                array_variables_removing_input_i = np.squeeze(array_variables_removing_input_i, axis=a)

            indexes_input[axes_other_array_input] = combinations_axes_other_input[i]
            indexes_output[axes_other_output] = combinations_axes_other_input[i]

            for c in range(n_combinations_variables_removing_table_input):

                indexes_combinations_removing[axis_combinations_in_combinations_removing] = c
                # combinations_removing_c_i = combinations_variables_removing_table_input[
                #     advanced_indexing(indexes_combinations_removing)]

                indexes_input[axis_samples_input] = np.all(
                    array_variables_removing_input_i ==
                    combinations_variables_removing_table_input[
                        advanced_indexing(indexes_combinations_removing)],
                    axis=axis_variables_in_combinations_removing)

                array_variables_staying_input_i_c = array_input[advanced_indexing(indexes_input)]
                # if array_variables_staying_input_i_c.shape[2] != 120:
                #     print('')
                for a in axes_inserting_output_sorted:
                    array_variables_staying_input_i_c = np.expand_dims(array_variables_staying_input_i_c, axis=a)

                combinations_axes_inserting_output_i_c = combinations_axes_inserting_output[c]
                # combinations_axes_inserting_output_i_c = np.squeeze(
                #     combinations_axes_inserting_output_i_c, axis=axis_combinations_in_combinations_removing)
                # combinations_axes_inserting_output_c_i = combinations_axes_inserting_output_c_i[
                #     indexes_combinations_removing_to_remove_axis_combinations]

                indexes_output[axes_inserting_output] = combinations_axes_inserting_output_i_c
                array_output[advanced_indexing(indexes_output)] = array_variables_staying_input_i_c

    return array_output


def safer_fast_balanced_2(
        array_input,
        axes_inserting_output=0,
        axis_samples_input=-2,
        axis_variables_table_input=-1,
        variables_removing_table_input=0,
        variables_staying_table_input=None,
        dtype=None):

    # Notes:
    # 1) it is safer than the faster version;
    # 2) it assumes that the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal;
    # 3) it does not assumes that the order of samples (or trials) in the axis_samples_input are is the same
    #    in each combination of variables' axes. The order is based on the order of the combinations
    #    of variables' conditions in axis_variables_table_input. In other words, the samples can be in random order
    #    (or in different order) in each combinations of variables axes/conditions.

    # Input requirements:
    # 1) axes_inserting_output cannot contain same values;
    # 2) variables_removing_table_input cannot contain same values;
    # 3) shapes of axes_inserting_output and variables_removing_table_input must be equal
    # 4) axis_samples_input != axis_variables_table_input
    # 5) the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal

    # Import requirements:
    # 1) import numpy as np
    # 2) from ccalafiore.combinations import n_conditions_to_combinations
    # 3) from ccalafiore.combinations import trials_to_conditions
    # 4) from ccalafiore.combinations import conditions_to_n_conditions
    # 5) from ccalafiore.combinations import conditions_to_combinations
    # 6) from ccalafiore.array import samples_in_arr1_are_in_arr2
    # 7) from ccalafiore.array import advanced_indexing

    # from ccalafiore.combinations import \
    #     trials_to_conditions, conditions_to_n_conditions, n_conditions_to_combinations, conditions_to_combinations
    # from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing

    # format axes_inserting_input
    try:
        n_axes_inserting_output = len(axes_inserting_output)
        axes_inserting_output = np.asarray(axes_inserting_output, dtype=int)
    except TypeError:
        axes_inserting_output = np.asarray([axes_inserting_output], dtype=int)
        n_axes_inserting_output = len(axes_inserting_output)

    # format variables_removing_in_axes_variables_output
    try:
        n_variables_removing_table_input = len(variables_removing_table_input)
        variables_removing_table_input = \
            np.asarray(variables_removing_table_input, dtype=int)
    except TypeError:
        variables_removing_table_input = \
            np.asarray([variables_removing_table_input], dtype=int)
        n_variables_removing_table_input = len(variables_removing_table_input)

    if dtype is None:
        dtype = array_input.dtype

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)
    n_variables_table_input = shape_array_input[axis_variables_table_input]

    if axis_variables_table_input < 0:
        axis_variables_table_input += n_axes_array_input
    if axis_samples_input < 0:
        axis_samples_input += n_axes_array_input

    variables_removing_table_input[variables_removing_table_input < 0] += n_variables_table_input

    n_axes_array_output = n_axes_array_input + n_axes_inserting_output
    axes_inserting_output[axes_inserting_output < 0] += n_axes_array_output

    # check point 1
    if np.sum(axes_inserting_output[0] == axes_inserting_output) > 1:
        raise Exception('axes_inserting_output cannot contain repeated values')
    # check point 2
    if np.sum(
            variables_removing_table_input[
                0] == variables_removing_table_input) > 1:
        raise Exception('variables_removing_table_input cannot contain repeated values')
    # check point 3
    if n_variables_removing_table_input != n_axes_inserting_output:
        raise Exception(
            'Shapes of axes_inserting_output and variables_removing_table_input must be equal')

    # check point 4
    if np.sum(axis_samples_input == axis_variables_table_input) > 0:
        raise Exception('axis_samples_input and axis_variables_table_input must be different')

    axes_inserting_output_sorted = np.sort(axes_inserting_output)
    for a in axes_inserting_output_sorted:
        array_input = np.expand_dims(array_input, axis=a)

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)

    axis_variables_table_input += np.sum(axes_inserting_output <= axis_variables_table_input)
    axis_samples_input += np.sum(axes_inserting_output <= axis_samples_input)
    while axis_variables_table_input in axes_inserting_output:
        axis_variables_table_input += 1
    while axis_samples_input in axes_inserting_output:
        axis_samples_input += 1

    if axis_variables_table_input == axis_samples_input:
        if axis_variables_table_input > axis_samples_input:
            axis_variables_table_input += 1
        elif axis_variables_table_input < axis_samples_input:
            axis_samples_input += 1

    axes = np.arange(n_axes_array_input)
    axes_non_axis_variables_table = axes[axes != axis_variables_table_input]
    axes_other_input = axes_non_axis_variables_table[
        axes_non_axis_variables_table != axis_samples_input]
    axes_other_output = axes_other_input[np.logical_not(
        samples_in_arr1_are_in_arr2(axes_other_input, axes_inserting_output))]

    variables_table_input = np.arange(n_variables_table_input)
    if variables_staying_table_input is None:
        variables_staying_table_input = variables_table_input[np.logical_not(
            samples_in_arr1_are_in_arr2(variables_table_input, variables_removing_table_input))]
    n_variables_staying_table_input = len(variables_staying_table_input)

    indexes_array_input_c = np.full(n_axes_array_input, 0, dtype=object)
    indexes_array_input_c[axis_variables_table_input] = variables_removing_table_input
    indexes_array_input_c[axis_samples_input] = np.arange(shape_array_input[axis_samples_input])
    indexes_input = advanced_indexing(indexes_array_input_c)
    array_variables_removing_input_1_case = array_input[indexes_input]

    axes_other_inverted_input = axes_other_input[::-1]
    for a in axes_other_inverted_input:
        array_variables_removing_input_1_case = np.squeeze(array_variables_removing_input_1_case, axis=a)

    axis_variables_in_combinations_removing = int(axis_variables_table_input > axis_samples_input)
    axis_combinations_in_combinations_removing = int(not (bool(axis_variables_in_combinations_removing)))
    conditions_variables_removing_table_input = trials_to_conditions(
        array_variables_removing_input_1_case, axis_combinations=axis_combinations_in_combinations_removing)
    n_conditions_variables_removing_table_input = conditions_to_n_conditions(
        conditions_variables_removing_table_input)
    n_combinations_variables_removing_table_input = int(np.prod(
        n_conditions_variables_removing_table_input))

    combinations_variables_removing_table_input = conditions_to_combinations(
        conditions_variables_removing_table_input,
        axis_combinations=axis_combinations_in_combinations_removing)

    combinations_axes_inserting_output = n_conditions_to_combinations(
        n_conditions_variables_removing_table_input)

    for a in axes_other_input:
        combinations_variables_removing_table_input = np.expand_dims(
            combinations_variables_removing_table_input, axis=a)

    # shape_array_output = np.empty(n_axes_array_output, dtype=int)
    shape_array_output = np.copy(shape_array_input)
    shape_array_output[axes_inserting_output] = n_conditions_variables_removing_table_input
    shape_array_output[axis_variables_table_input] = n_variables_staying_table_input
    shape_array_output[axis_samples_input] = (
        shape_array_input[axis_samples_input] / n_combinations_variables_removing_table_input
    )

    array_output = np.empty(shape_array_output, dtype=dtype)

    indexes_output = np.empty(n_axes_array_input, dtype=object)
    indexes_input_variables_removing = np.copy(indexes_output)

    for a in range(n_axes_array_input):
        indexes_output[a] = np.arange(shape_array_output[a])
        indexes_input_variables_removing[a] = np.arange(shape_array_input[a])

    indexes_input_variables_removing[axis_variables_table_input] = variables_removing_table_input
    array_input_variables_removing = array_input[advanced_indexing(indexes_input_variables_removing)]

    indexes_input_variables_staying = np.copy(indexes_input_variables_removing)
    indexes_input_variables_staying[axis_variables_table_input] = variables_staying_table_input
    array_input_variables_staying = array_input[advanced_indexing(indexes_input_variables_staying)]
    del array_input

    indexes_input_variables_staying[axis_variables_table_input] = np.arange(n_variables_staying_table_input)

    indexes_input_variables_removing[:] = 0
    indexes_combinations_removing = np.copy(indexes_input_variables_removing)
    indexes_input_variables_removing[axis_samples_input] = slice(None)
    indexes_combinations_removing[axis_variables_table_input] = np.arange(n_variables_removing_table_input)

    n_axes_other = len(axes_other_output)

    if n_axes_other > 0:

        combinations_axes_other = n_conditions_to_combinations(shape_array_input[axes_other_output])
        n_combinations_axes_other = len(combinations_axes_other)

        for i in range(n_combinations_variables_removing_table_input):

            indexes_combinations_removing[axis_samples_input] = i

            indexes_logical_array_input_variables_staying_i = np.all(
                array_input_variables_removing == combinations_variables_removing_table_input[
                    advanced_indexing(indexes_combinations_removing)], axis=axis_variables_table_input, keepdims=True)

            indexes_output[axes_inserting_output] = combinations_axes_inserting_output[i]

            for j in range(n_combinations_axes_other):

                combinations_axes_other_j = combinations_axes_other[j]

                indexes_output[axes_other_output] = combinations_axes_other_j

                indexes_input_variables_staying[axes_other_output] = combinations_axes_other_j

                indexes_input_variables_removing[axes_other_output] = combinations_axes_other_j

                indexes_input_variables_staying[axis_samples_input] = indexes_logical_array_input_variables_staying_i[
                    tuple(indexes_input_variables_removing)]

                array_output[advanced_indexing(indexes_output)] = array_input_variables_staying[advanced_indexing(
                    indexes_input_variables_staying)]

    elif n_axes_other == 0:

        indexes_input_variables_removing_tuple = tuple(indexes_input_variables_removing)

        for i in range(n_combinations_variables_removing_table_input):

            indexes_output[axes_inserting_output] = combinations_axes_inserting_output[i]

            indexes_combinations_removing[axis_samples_input] = i

            indexes_input_variables_staying[axis_samples_input] = np.all(
                array_input_variables_removing == combinations_variables_removing_table_input[
                    advanced_indexing(indexes_combinations_removing)],
                axis=axis_variables_table_input, keepdims=True)[indexes_input_variables_removing_tuple]

            array_output[advanced_indexing(indexes_output)] = array_input_variables_staying[advanced_indexing(
                indexes_input_variables_staying)]

    return array_output


def safer_fast_balanced_3(
        array_input,
        axes_inserting_output=0,
        axis_samples_input=-2,
        axis_variables_table_input=-1,
        variables_removing_table_input=0,
        variables_staying_table_input=None,
        dtype=None):
    # Notes:
    # 1) it is safer than the faster version;
    # 2) it assumes that the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal;
    # 3) it does not assumes that the order of samples (or trials) in the axis_samples_input are is the same
    #    in each combination of variables' axes. The order is based on the order of the combinations
    #    of variables' conditions in axis_variables_table_input. In other words, the samples can be in random order
    #    (or in different order) in each combinations of variables axes/conditions.

    # Input requirements:
    # 1) axes_inserting_output cannot contain same values;
    # 2) variables_removing_table_input cannot contain same values;
    # 3) shapes of axes_inserting_output and variables_removing_table_input must be equal
    # 4) axis_samples_input != axis_variables_table_input
    # 5) the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal

    # Import requirements:
    # 1) import numpy as np
    # 2) from ccalafiore.combinations import n_conditions_to_combinations
    # 3) from ccalafiore.combinations import trials_to_conditions
    # 4) from ccalafiore.combinations import conditions_to_n_conditions
    # 5) from ccalafiore.combinations import conditions_to_combinations
    # 6) from ccalafiore.array import samples_in_arr1_are_in_arr2
    # 7) from ccalafiore.array import advanced_indexing

    # from ccalafiore.combinations import \
    #     trials_to_conditions, conditions_to_n_conditions, n_conditions_to_combinations, conditions_to_combinations
    # from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing

    # format axes_inserting_input
    try:
        n_axes_inserting_output = len(axes_inserting_output)
        axes_inserting_output = np.asarray(axes_inserting_output, dtype=int)
    except TypeError:
        axes_inserting_output = np.asarray([axes_inserting_output], dtype=int)
        n_axes_inserting_output = len(axes_inserting_output)

    # format variables_removing_in_axes_variables_output
    try:
        n_variables_removing_table_input = len(variables_removing_table_input)
        variables_removing_table_input = \
            np.asarray(variables_removing_table_input, dtype=int)
    except TypeError:
        variables_removing_table_input = \
            np.asarray([variables_removing_table_input], dtype=int)
        n_variables_removing_table_input = len(variables_removing_table_input)

    if dtype is None:
        dtype = array_input.dtype

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)
    n_variables_table_input = shape_array_input[axis_variables_table_input]

    if axis_variables_table_input < 0:
        axis_variables_table_input += n_axes_array_input
    if axis_samples_input < 0:
        axis_samples_input += n_axes_array_input

    variables_removing_table_input[variables_removing_table_input < 0] += n_variables_table_input

    n_axes_array_output = n_axes_array_input + n_axes_inserting_output
    axes_inserting_output[axes_inserting_output < 0] += n_axes_array_output

    # check point 1
    if np.sum(axes_inserting_output[0] == axes_inserting_output) > 1:
        raise Exception('axes_inserting_output cannot contain repeated values')
    # check point 2
    if np.sum(
            variables_removing_table_input[
                0] == variables_removing_table_input) > 1:
        raise Exception('variables_removing_table_input cannot contain repeated values')
    # check point 3
    if n_variables_removing_table_input != n_axes_inserting_output:
        raise Exception(
            'Shapes of axes_inserting_output and variables_removing_table_input must be equal')

    # check point 4
    if np.sum(axis_samples_input == axis_variables_table_input) > 0:
        raise Exception('axis_samples_input and axis_variables_table_input must be different')

    axes_array_input = np.arange(n_axes_array_input)
    axes_non_axis_variables_table_input = axes_array_input[axes_array_input != axis_variables_table_input]
    axes_other_array_input = axes_non_axis_variables_table_input[
        axes_non_axis_variables_table_input != axis_samples_input]
    axes_other_array_input_inverted = axes_other_array_input[::-1]
    n_axes_other_array_input = len(axes_other_array_input)

    variables_table_input = np.arange(n_variables_table_input)
    if variables_staying_table_input is None:
        variables_staying_table_input = variables_table_input[np.logical_not(
            samples_in_arr1_are_in_arr2(variables_table_input, variables_removing_table_input))]
    n_variables_staying_table_input = len(variables_staying_table_input)

    indexes_array_input_c = np.full(n_axes_array_input, 0, dtype=object)
    indexes_array_input_c[axis_variables_table_input] = variables_removing_table_input
    indexes_array_input_c[axis_samples_input] = np.arange(shape_array_input[axis_samples_input])
    indexes_input = advanced_indexing(indexes_array_input_c)
    array_variables_removing_input_1_case = array_input[indexes_input]
    for a in axes_other_array_input_inverted:
        array_variables_removing_input_1_case = np.squeeze(array_variables_removing_input_1_case, axis=a)

    axis_variables_in_combinations_removing = int(axis_variables_table_input > axis_samples_input)
    axis_combinations_in_combinations_removing = int(not (bool(axis_variables_in_combinations_removing)))
    conditions_variables_removing_table_input = trials_to_conditions(
        array_variables_removing_input_1_case, axis_combinations=axis_combinations_in_combinations_removing)
    n_conditions_variables_removing_table_input = conditions_to_n_conditions(
        conditions_variables_removing_table_input)
    n_combinations_variables_removing_table_input = int(np.prod(
        n_conditions_variables_removing_table_input))

    combinations_variables_removing_table_input = conditions_to_combinations(
        conditions_variables_removing_table_input,
        axis_combinations=axis_combinations_in_combinations_removing)

    combinations_axes_inserting_output = n_conditions_to_combinations(
        n_conditions_variables_removing_table_input)

    for a in axes_other_array_input:
        combinations_variables_removing_table_input = np.expand_dims(
            combinations_variables_removing_table_input, axis=a)

    axis_variables_table_output = axis_variables_table_input + np.sum(
        axes_inserting_output <= axis_variables_table_input)
    axis_samples_output = axis_samples_input + np.sum(axes_inserting_output <= axis_samples_input)
    while axis_variables_table_output in axes_inserting_output:
        axis_variables_table_output += 1
    while axis_samples_output in axes_inserting_output:
        axis_samples_output += 1

    if axis_variables_table_output == axis_samples_output:
        if axis_variables_table_input > axis_samples_input:
            axis_variables_table_output += 1
        elif axis_variables_table_input < axis_samples_input:
            axis_samples_output += 1

    axes_array_output = np.arange(n_axes_array_output)
    axes_non_axis_variables_table_output = axes_array_output[axes_array_output != axis_variables_table_output]
    axes_other_output = axes_non_axis_variables_table_output[
        axes_non_axis_variables_table_output != axis_samples_output]
    axes_other_output = axes_other_output[np.logical_not(
        samples_in_arr1_are_in_arr2(axes_other_output, axes_inserting_output))]
    axes_inserting_output_sorted = np.sort(axes_inserting_output)

    shape_array_output = np.empty(n_axes_array_output, dtype=int)
    shape_array_output[axes_inserting_output] = n_conditions_variables_removing_table_input
    shape_array_output[axis_variables_table_output] = n_variables_staying_table_input
    shape_array_output[axis_samples_output] = (
            shape_array_input[axis_samples_input] / n_combinations_variables_removing_table_input
    )
    shape_array_output[axes_other_output] = shape_array_input[axes_other_array_input]
    array_output = np.empty(shape_array_output, dtype=dtype)

    indexes_output = np.empty(n_axes_array_output, dtype=object)
    for a in range(n_axes_array_output):
        indexes_output[a] = np.arange(shape_array_output[a])

    indexes_input_variables_removing = np.empty(n_axes_array_input, dtype=object)
    for a in range(n_axes_array_input):
        indexes_input_variables_removing[a] = np.arange(shape_array_input[a])

    indexes_input_variables_removing[axis_variables_table_input] = variables_removing_table_input
    array_input_variables_removing = array_input[advanced_indexing(indexes_input_variables_removing)]

    indexes_input_variables_staying = np.copy(indexes_input_variables_removing)
    indexes_input_variables_staying[axis_variables_table_input] = variables_staying_table_input
    array_input_variables_staying = array_input[advanced_indexing(indexes_input_variables_staying)]
    del array_input

    indexes_input_variables_staying[axis_variables_table_input] = np.arange(n_variables_staying_table_input)

    indexes_input_variables_removing[:] = 0
    indexes_combinations_removing = np.copy(indexes_input_variables_removing)
    indexes_input_variables_removing[axis_samples_input] = slice(None)
    indexes_combinations_removing[axis_variables_table_input] = np.arange(n_variables_removing_table_input)

    if n_axes_other_array_input > 0:

        combinations_axes_other = n_conditions_to_combinations(shape_array_input[axes_other_array_input])
        n_combinations_axes_other = len(combinations_axes_other)

        for i in range(n_combinations_variables_removing_table_input):

            indexes_combinations_removing[axis_samples_input] = i

            indexes_logical_array_input_variables_staying_i = np.all(
                array_input_variables_removing == combinations_variables_removing_table_input[
                    advanced_indexing(indexes_combinations_removing)], axis=axis_variables_table_input, keepdims=True)

            indexes_output[axes_inserting_output] = combinations_axes_inserting_output[i]

            for j in range(n_combinations_axes_other):

                combinations_axes_other_j = combinations_axes_other[j]

                indexes_output[axes_other_output] = combinations_axes_other_j

                indexes_input_variables_staying[axes_other_array_input] = combinations_axes_other_j

                indexes_input_variables_removing[axes_other_array_input] = combinations_axes_other_j

                indexes_input_variables_staying[axis_samples_input] = indexes_logical_array_input_variables_staying_i[
                    tuple(indexes_input_variables_removing)]

                array_input_variables_staying_i_j = array_input_variables_staying[advanced_indexing(
                    indexes_input_variables_staying)]

                for a in axes_inserting_output_sorted:
                    array_input_variables_staying_i_j = np.expand_dims(array_input_variables_staying_i_j, axis=a)

                array_output[advanced_indexing(indexes_output)] = array_input_variables_staying_i_j

    elif n_axes_other_array_input == 0:

        indexes_input_variables_removing_tuple = tuple(indexes_input_variables_removing)

        for i in range(n_combinations_variables_removing_table_input):

            indexes_output[axes_inserting_output] = combinations_axes_inserting_output[i]

            indexes_combinations_removing[axis_samples_input] = i

            indexes_input_variables_staying[axis_samples_input] = np.all(
                array_input_variables_removing == combinations_variables_removing_table_input[
                    advanced_indexing(indexes_combinations_removing)],
                axis=axis_variables_table_input, keepdims=True)[indexes_input_variables_removing_tuple]

            array_input_variables_staying_i = array_input_variables_staying[advanced_indexing(
                indexes_input_variables_staying)]

            for a in axes_inserting_output_sorted:
                array_input_variables_staying_i = np.expand_dims(array_input_variables_staying_i, axis=a)

            array_output[advanced_indexing(indexes_output)] = array_input_variables_staying_i

    return array_output


def safer_fast_balanced_4(
        array_input,
        axes_inserting_output=0,
        axis_samples_input=-2,
        axis_variables_table_input=-1,
        variables_removing_table_input=0,
        variables_staying_table_input=None,
        dtype=None):
    # Notes:
    # 1) it is safer than the faster version;
    # 2) it assumes that the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal;
    # 3) it does not assumes that the order of samples (or trials) in the axis_samples_input are is the same
    #    in each combination of variables' axes. The order is based on the order of the combinations
    #    of variables' conditions in axis_variables_table_input. In other words, the samples can be in random order
    #    (or in different order) in each combinations of variables axes/conditions.

    # Input requirements:
    # 1) axes_inserting_output cannot contain same values;
    # 2) variables_removing_table_input cannot contain same values;
    # 3) shapes of axes_inserting_output and variables_removing_table_input must be equal
    # 4) axis_samples_input != axis_variables_table_input
    # 5) the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal

    # Import requirements:
    # 1) import numpy as np
    # 2) from ccalafiore.combinations import n_conditions_to_combinations
    # 3) from ccalafiore.combinations import trials_to_conditions
    # 4) from ccalafiore.combinations import conditions_to_n_conditions
    # 5) from ccalafiore.combinations import conditions_to_combinations
    # 6) from ccalafiore.array import samples_in_arr1_are_in_arr2
    # 7) from ccalafiore.array import advanced_indexing

    # from ccalafiore.combinations import \
    #     trials_to_conditions, conditions_to_n_conditions, n_conditions_to_combinations, conditions_to_combinations
    # from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing

    # format axes_inserting_input
    try:
        n_axes_inserting_output = len(axes_inserting_output)
        axes_inserting_output = np.asarray(axes_inserting_output, dtype=int)
    except TypeError:
        axes_inserting_output = np.asarray([axes_inserting_output], dtype=int)
        n_axes_inserting_output = len(axes_inserting_output)

    # format variables_removing_in_axes_variables_output
    try:
        n_variables_removing_table_input = len(variables_removing_table_input)
        variables_removing_table_input = \
            np.asarray(variables_removing_table_input, dtype=int)
    except TypeError:
        variables_removing_table_input = \
            np.asarray([variables_removing_table_input], dtype=int)
        n_variables_removing_table_input = len(variables_removing_table_input)

    if dtype is None:
        dtype = array_input.dtype

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)
    n_variables_table_input = shape_array_input[axis_variables_table_input]

    if axis_variables_table_input < 0:
        axis_variables_table_input += n_axes_array_input
    if axis_samples_input < 0:
        axis_samples_input += n_axes_array_input

    variables_removing_table_input[variables_removing_table_input < 0] += n_variables_table_input

    n_axes_array_output = n_axes_array_input + n_axes_inserting_output
    axes_inserting_output[axes_inserting_output < 0] += n_axes_array_output

    # check point 1
    if np.sum(axes_inserting_output[0] == axes_inserting_output) > 1:
        raise Exception('axes_inserting_output cannot contain repeated values')
    # check point 2
    if np.sum(
            variables_removing_table_input[
                0] == variables_removing_table_input) > 1:
        raise Exception('variables_removing_table_input cannot contain repeated values')
    # check point 3
    if n_variables_removing_table_input != n_axes_inserting_output:
        raise Exception(
            'Shapes of axes_inserting_output and variables_removing_table_input must be equal')

    # check point 4
    if np.sum(axis_samples_input == axis_variables_table_input) > 0:
        raise Exception('axis_samples_input and axis_variables_table_input must be different')

    axes_array_input = np.arange(n_axes_array_input)
    axes_non_axis_variables_table_input = axes_array_input[axes_array_input != axis_variables_table_input]
    axes_other_array_input = axes_non_axis_variables_table_input[
        axes_non_axis_variables_table_input != axis_samples_input]
    axes_other_array_input_inverted = axes_other_array_input[::-1]
    n_axes_other_array_input = len(axes_other_array_input)

    variables_table_input = np.arange(n_variables_table_input)
    if variables_staying_table_input is None:
        variables_staying_table_input = variables_table_input[np.logical_not(
            samples_in_arr1_are_in_arr2(variables_table_input, variables_removing_table_input))]
    n_variables_staying_table_input = len(variables_staying_table_input)

    indexes_input_variables_removing = np.empty(n_axes_array_input, dtype=object)
    for a in range(n_axes_array_input):
        indexes_input_variables_removing[a] = np.arange(shape_array_input[a])

    indexes_input_variables_removing[axis_variables_table_input] = variables_removing_table_input
    array_input_variables_removing = array_input[advanced_indexing(indexes_input_variables_removing)]

    indexes_input_variables_staying = np.copy(indexes_input_variables_removing)
    indexes_input_variables_staying[axis_variables_table_input] = variables_staying_table_input
    array_input_variables_staying = array_input[advanced_indexing(indexes_input_variables_staying)]
    del array_input


    indexes_input_variables_staying[axis_variables_table_input] = np.arange(n_variables_staying_table_input)
    indexes_input_variables_removing[axis_variables_table_input] = np.arange(n_variables_removing_table_input)

    axis_variables_in_combinations_removing = int(axis_variables_table_input > axis_samples_input)
    axis_combinations_in_combinations_removing = int(not (bool(axis_variables_in_combinations_removing)))

    if n_axes_other_array_input > 0:

        indexes_input_variables_removing[axes_other_array_input] = 0

        array_input_variables_removing_1 = array_input_variables_removing[
            advanced_indexing(indexes_input_variables_removing)]
        for a in axes_other_array_input_inverted:
            array_input_variables_removing_1 = np.squeeze(array_input_variables_removing_1, axis=a)
        conditions_variables_removing_table_input = trials_to_conditions(
            array_input_variables_removing_1, axis_combinations=axis_combinations_in_combinations_removing)
    elif n_axes_other_array_input == 0:
        conditions_variables_removing_table_input = trials_to_conditions(
            array_input_variables_removing, axis_combinations=axis_combinations_in_combinations_removing)

    n_conditions_variables_removing_table_input = conditions_to_n_conditions(
        conditions_variables_removing_table_input)
    n_combinations_variables_removing_table_input = int(np.prod(
        n_conditions_variables_removing_table_input))

    combinations_variables_removing_table_input = conditions_to_combinations(
        conditions_variables_removing_table_input,
        axis_combinations=axis_combinations_in_combinations_removing)

    combinations_axes_inserting_output = n_conditions_to_combinations(
        n_conditions_variables_removing_table_input)

    axis_variables_table_output = axis_variables_table_input + np.sum(
        axes_inserting_output <= axis_variables_table_input)
    axis_samples_output = axis_samples_input + np.sum(axes_inserting_output <= axis_samples_input)
    changed = True
    while changed:
        changed = False
        while axis_variables_table_output in axes_inserting_output:
            axis_variables_table_output += 1
            changed = True
        while axis_samples_output in axes_inserting_output:
            axis_samples_output += 1
            changed = True
        if axis_variables_table_output == axis_samples_output:
            changed = True
            if axis_variables_table_input > axis_samples_input:
                axis_variables_table_output += 1
            elif axis_variables_table_input < axis_samples_input:
                axis_samples_output += 1

    axes_array_output = np.arange(n_axes_array_output)
    axes_non_axis_variables_table_output = axes_array_output[axes_array_output != axis_variables_table_output]
    axes_other_output = axes_non_axis_variables_table_output[
        axes_non_axis_variables_table_output != axis_samples_output]
    axes_other_output = axes_other_output[np.logical_not(
        samples_in_arr1_are_in_arr2(axes_other_output, axes_inserting_output))]
    axes_inserting_output_sorted = np.sort(axes_inserting_output)

    shape_array_output = np.empty(n_axes_array_output, dtype=int)
    shape_array_output[axes_inserting_output] = n_conditions_variables_removing_table_input
    shape_array_output[axis_variables_table_output] = n_variables_staying_table_input
    shape_array_output[axis_samples_output] = (
            shape_array_input[axis_samples_input] / n_combinations_variables_removing_table_input)
    shape_array_output[axes_other_output] = shape_array_input[axes_other_array_input]
    array_output = np.empty(shape_array_output, dtype=dtype)

    indexes_output = np.empty(n_axes_array_output, dtype=object)
    for a in range(n_axes_array_output):
        indexes_output[a] = np.arange(shape_array_output[a])

    indexes_combinations_removing = np.empty(2, dtype=object)
    indexes_combinations_removing[axis_variables_in_combinations_removing] = np.arange(
        n_variables_removing_table_input)

    if n_axes_other_array_input == 0:
        for i in range(n_combinations_variables_removing_table_input):
            indexes_output[axes_inserting_output] = combinations_axes_inserting_output[i]
            indexes_combinations_removing[axis_combinations_in_combinations_removing] = i
            indexes_input_variables_staying[axis_samples_input] = np.all(
                array_input_variables_removing == combinations_variables_removing_table_input
                [advanced_indexing(indexes_combinations_removing)],
                axis=axis_variables_in_combinations_removing)
            array_input_variables_staying_i = array_input_variables_staying[advanced_indexing(
                indexes_input_variables_staying)]
            for a in axes_inserting_output_sorted:
                array_input_variables_staying_i = np.expand_dims(array_input_variables_staying_i, axis=a)
            array_output[advanced_indexing(indexes_output)] = array_input_variables_staying_i

    elif n_axes_other_array_input > 0:
        combinations_axes_other = n_conditions_to_combinations(shape_array_input[axes_other_array_input])
        n_combinations_axes_other = len(combinations_axes_other)
        for j in range(n_combinations_axes_other):
            combinations_axes_other_j = combinations_axes_other[j]
            indexes_output[axes_other_output] = combinations_axes_other_j
            indexes_input_variables_staying[axes_other_array_input] = combinations_axes_other_j
            indexes_input_variables_removing[axes_other_array_input] = combinations_axes_other_j
            array_input_variables_removing_j = array_input_variables_removing[
                advanced_indexing(indexes_input_variables_removing)]
            for a in axes_other_array_input_inverted:
                array_input_variables_removing_j = np.squeeze(array_input_variables_removing_j, axis=a)
            for i in range(n_combinations_variables_removing_table_input):
                indexes_output[axes_inserting_output] = combinations_axes_inserting_output[i]
                indexes_combinations_removing[axis_combinations_in_combinations_removing] = i
                indexes_input_variables_staying[axis_samples_input] = np.all(
                    array_input_variables_removing_j == combinations_variables_removing_table_input
                    [advanced_indexing(indexes_combinations_removing)],
                    axis=axis_variables_in_combinations_removing)
                array_input_variables_staying_i_j = array_input_variables_staying[advanced_indexing(
                    indexes_input_variables_staying)]
                for a in axes_inserting_output_sorted:
                    array_input_variables_staying_i_j = np.expand_dims(array_input_variables_staying_i_j, axis=a)
                array_output[advanced_indexing(indexes_output)] = array_input_variables_staying_i_j



    return array_output


def safer_and_slow_balanced(
        array_input,
        axes_inserting_output=0,
        axis_samples_input=-2,
        axis_variables_table_input=-1,
        variables_removing_table_input=0,
        variables_staying_table_input=None,
        dtype=None):

    # Notes:
    # 1) it is safe and fast;
    # 2) it assumes that the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal;
    # 3) it does not assumes that the order of samples (or trials) in the axis_samples_input are is the same
    #    in each combination of variables' axes. The order is based on the order of the combinations
    #    of variables' conditions in axis_variables_table_input. In other words, the samples can be in random order
    #    (or in different order) in each combinations of variables axes/conditions.

    # Input requirements:
    # 1) axes_inserting_output cannot contain same values;
    # 2) variables_removing_table_input cannot contain same values;
    # 3) shapes of axes_inserting_output and variables_removing_table_input must be equal
    # 4) axis_samples_input != axis_variables_table_input
    # 5) the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input are equal

    # Import requirements:
    # 1) import numpy as np
    # 2) from ccalafiore.combinations import n_conditions_to_combinations
    # 3) from ccalafiore.combinations import trials_to_conditions
    # 4) from ccalafiore.combinations import conditions_to_n_conditions
    # 5) from ccalafiore.combinations import conditions_to_combinations
    # 6) from ccalafiore.array import samples_in_arr1_are_in_arr2
    # 7) from ccalafiore.array import advanced_indexing

    # from ccalafiore.combinations import \
    #     trials_to_conditions, conditions_to_n_conditions, n_conditions_to_combinations, conditions_to_combinations
    # from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing

    # format axes_inserting_input
    try:
        n_axes_inserting_output = len(axes_inserting_output)
        axes_inserting_output = np.asarray(axes_inserting_output, dtype=int)
    except TypeError:
        axes_inserting_output = np.asarray([axes_inserting_output], dtype=int)
        n_axes_inserting_output = len(axes_inserting_output)

    # format variables_removing_in_axes_variables_output
    try:
        n_variables_removing_table_input = len(variables_removing_table_input)
        variables_removing_table_input = \
            np.asarray(variables_removing_table_input, dtype=int)
    except TypeError:
        variables_removing_table_input = \
            np.asarray([variables_removing_table_input], dtype=int)
        n_variables_removing_table_input = len(variables_removing_table_input)

    if dtype is None:
        dtype = array_input.dtype

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)
    n_variables_table_input = shape_array_input[axis_variables_table_input]

    if axis_variables_table_input < 0:
        axis_variables_table_input += n_axes_array_input
    if axis_samples_input < 0:
        axis_samples_input += n_axes_array_input

    variables_removing_table_input[variables_removing_table_input < 0] += n_variables_table_input

    n_axes_array_output = n_axes_array_input + n_axes_inserting_output
    axes_inserting_output[axes_inserting_output < 0] += n_axes_array_output

    # check point 1
    if np.sum(axes_inserting_output[0] == axes_inserting_output) > 1:
        raise Exception('axes_inserting_output cannot contain repeated values')
    # check point 2
    if np.sum(
            variables_removing_table_input[
                0] == variables_removing_table_input) > 1:
        raise Exception('variables_removing_table_input cannot contain repeated values')
    # check point 3
    if n_variables_removing_table_input != n_axes_inserting_output:
        raise Exception(
            'Shapes of axes_inserting_output and variables_removing_table_input must be equal')

    # check point 4
    if np.sum(axis_samples_input == axis_variables_table_input) > 0:
        raise Exception('axis_samples_input and axis_variables_table_input must be different')

    axes_inserting_output_sorted = np.sort(axes_inserting_output)
    for a in axes_inserting_output_sorted:
        array_input = np.expand_dims(array_input, axis=a)

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)

    axis_variables_table_input += np.sum(axes_inserting_output <= axis_variables_table_input)
    axis_samples_input += np.sum(axes_inserting_output <= axis_samples_input)
    while axis_variables_table_input in axes_inserting_output:
        axis_variables_table_input += 1
    while axis_samples_input in axes_inserting_output:
        axis_samples_input += 1

    if axis_variables_table_input == axis_samples_input:
        if axis_variables_table_input > axis_samples_input:
            axis_variables_table_input += 1
        elif axis_variables_table_input < axis_samples_input:
            axis_samples_input += 1

    axes = np.arange(n_axes_array_input)
    axes_non_axis_variables_table = axes[axes != axis_variables_table_input]
    axes_other_input = axes_non_axis_variables_table[
        axes_non_axis_variables_table != axis_samples_input]
    axes_other_output = axes_other_input[np.logical_not(
        samples_in_arr1_are_in_arr2(axes_other_input, axes_inserting_output))]

    axes_other_inverted_input = axes_other_input[::-1]

    variables_table_input = np.arange(n_variables_table_input)
    if variables_staying_table_input is None:
        variables_staying_table_input = variables_table_input[np.logical_not(
            samples_in_arr1_are_in_arr2(variables_table_input, variables_removing_table_input))]
    n_variables_staying_table_input = len(variables_staying_table_input)

    indexes_array_input_c = np.full(n_axes_array_input, 0, dtype=object)
    indexes_array_input_c[axis_variables_table_input] = variables_removing_table_input
    indexes_array_input_c[axis_samples_input] = np.arange(shape_array_input[axis_samples_input])
    indexes_input = advanced_indexing(indexes_array_input_c)
    array_variables_removing_input_1_case = array_input[indexes_input]

    for a in axes_other_inverted_input:
        array_variables_removing_input_1_case = np.squeeze(array_variables_removing_input_1_case, axis=a)

    axis_variables_in_combinations_removing = int(axis_variables_table_input > axis_samples_input)
    axis_combinations_in_combinations_removing = int(not (bool(axis_variables_in_combinations_removing)))
    conditions_variables_removing_table_input = trials_to_conditions(
        array_variables_removing_input_1_case, axis_combinations=axis_combinations_in_combinations_removing)
    n_conditions_variables_removing_table_input = conditions_to_n_conditions(
        conditions_variables_removing_table_input)
    n_combinations_variables_removing_table_input = int(np.prod(
        n_conditions_variables_removing_table_input))

    combinations_variables_removing_table_input = conditions_to_combinations(
        conditions_variables_removing_table_input,
        axis_combinations=axis_combinations_in_combinations_removing)

    combinations_axes_inserting_output = n_conditions_to_combinations(
        n_conditions_variables_removing_table_input)

    for a in axes_other_input:
        combinations_variables_removing_table_input = np.expand_dims(
            combinations_variables_removing_table_input, axis=a)


    shape_array_output = np.empty(n_axes_array_output, dtype=int)
    shape_array_output[axes_inserting_output] = n_conditions_variables_removing_table_input
    shape_array_output[axis_variables_table_input] = n_variables_staying_table_input
    shape_array_output[axis_samples_input] = \
        shape_array_input[axis_samples_input] / n_combinations_variables_removing_table_input
    shape_array_output[axes_other_output] = shape_array_input[axes_other_output]
    array_output = np.empty(shape_array_output, dtype=dtype)

    indexes_combinations_removing = np.full(n_axes_array_input, 0, dtype=object)
    indexes_output = np.copy(indexes_combinations_removing)
    indexes_input_variables_removing = np.copy(indexes_combinations_removing)
    indexes_combinations_removing[axis_variables_table_input] = np.arange(
        n_variables_removing_table_input)
    for a in range(n_axes_array_input):
        indexes_output[a] = np.arange(shape_array_output[a])
        indexes_input_variables_removing[a] = np.arange(shape_array_input[a])

    indexes_input_variables_removing[axis_variables_table_input] = variables_removing_table_input
    array_input_variables_removing = array_input[advanced_indexing(indexes_input_variables_removing)]
    indexes_input_variables_removing[axis_variables_table_input] = np.arange(n_variables_removing_table_input)

    indexes_input_variables_staying = np.copy(indexes_input_variables_removing)
    indexes_input_variables_staying[axis_variables_table_input] = variables_staying_table_input
    indexes_input_variables_staying_adv = advanced_indexing(indexes_input_variables_staying)
    array_input_variables_staying = array_input[indexes_input_variables_staying_adv]
    indexes_input_variables_staying[axis_variables_table_input] = np.arange(n_variables_staying_table_input)
    indexes_input_variables_staying_adv = advanced_indexing(indexes_input_variables_staying)

    indexes_logical_array_input_variables_staying = np.empty(array_input_variables_staying.shape, dtype=bool)

    shape_array_input_variables_staying_c = np.copy(shape_array_output)
    shape_array_input_variables_staying_c[axes_inserting_output] = 1
    array_input_variables_staying_c = np.empty(shape_array_input_variables_staying_c, dtype=array_input_variables_staying.dtype)

    indexes_logical_array_input_variables_staying_c = np.full(shape_array_input_variables_staying_c, True, dtype=bool)
    # indexes_raw_array_input_variables_staying_c = np.copy(indexes_combinations_removing)
    # for a in axes:
    #     indexes_raw_array_input_variables_staying_c[a] = np.arange(shape_array_input_variables_staying_c[a])
    # indexes_tmp_1_adv = advanced_indexing(indexes_raw_array_input_variables_staying_c)
    # indexes_array_input_variables_staying_c_a = np.empty(shape_array_input_variables_staying_c, dtype=int)
    # indexes_array_input_variables_staying_c = np.copy(indexes_combinations_removing)
    # for a in axes:
    #     for e in axes:
    #         if e != a:
    #             indexes_raw_array_input_variables_staying_c[a] = np.expand_dims(
    #                 indexes_raw_array_input_variables_staying_c[a], axis=e)
    #     indexes_array_input_variables_staying_c_a[indexes_tmp_1_adv] = indexes_raw_array_input_variables_staying_c[a]
    #
    #     indexes_array_input_variables_staying_c[a] = np.copy(indexes_array_input_variables_staying_c_a)

    for c in range(n_combinations_variables_removing_table_input):

        indexes_combinations_removing[axis_samples_input] = c

        indexes_logical_array_input_variables_staying[indexes_input_variables_staying_adv] = np.all(
            array_input_variables_removing == combinations_variables_removing_table_input[
                advanced_indexing(indexes_combinations_removing)], axis=axis_variables_table_input, keepdims=True)

        # indexes_array_input_variables_staying_c[axis_samples_input] = np.argwhere(
        #     indexes_logical_array_input_variables_staying_c)[:, axis_samples_input].reshape(
        #     shape_array_input_variables_staying_c)

        # indexes_array_input_variables_staying_c[axis_samples_input] = np.where(
        #     indexes_logical_array_input_variables_staying_c)[axis_samples_input].reshape(
        #     shape_array_input_variables_staying_c)
        # a1 = array_input_variables_staying_c[array_input_variables_staying_c == array_input_variables_staying_c]
        # a2 = array_input_variables_staying[
        #     indexes_logical_array_input_variables_staying_c]

        array_input_variables_staying_c[indexes_logical_array_input_variables_staying_c] = (
            array_input_variables_staying[indexes_logical_array_input_variables_staying]
        )

        combinations_axes_inserting_output_i_c = combinations_axes_inserting_output[c]
        indexes_output[axes_inserting_output] = combinations_axes_inserting_output_i_c
        array_output[advanced_indexing(indexes_output)] = array_input_variables_staying_c

    return array_output


def unbalanced(
        array_input,
        axes_inserting_output=0,
        axis_samples_input=-2,
        axis_variables_table_input=-1,
        variables_removing_table_input=0,
        variables_staying_table_input=None,
        dtype=None):

    # Notes:
    # 1) it is safe;
    # 2) it does not assumes that the numbers of samples (or trials) in the axis_samples_input for all
    #    combinations of variables_removing_table_input are equal;
    # 3) it does not assumes that the order of samples (or trials) in the axis_samples_input are is the same
    #    in each combination of variables' axes. The order is based on the order of the combinations
    #    of variables' conditions in axis_variables_table_input. In other words, the samples can be in random order
    #    (or in different order) in each combinations of variables axes/conditions.

    # Input requirements:
    # 1) axes_inserting_output cannot contain same values;
    # 2) variables_removing_table_input cannot contain same values;
    # 3) shapes of axes_inserting_output and variables_removing_table_input must be equal;
    # 4) axis_samples_input != axis_variables_table_input;
    # 5) the numbers of samples (or trials) in the axis_samples_input for all combinations
    #    of variables_removing_table_input do not need to be equal.

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

    # format axes_inserting_input
    try:
        n_axes_inserting_output = len(axes_inserting_output)
        axes_inserting_output = np.asarray(axes_inserting_output, dtype=int)
    except TypeError:
        axes_inserting_output = np.asarray([axes_inserting_output], dtype=int)
        n_axes_inserting_output = len(axes_inserting_output)

    # format variables_removing_in_axes_variables_output
    try:
        n_variables_removing_table_input = len(variables_removing_table_input)
        variables_removing_table_input = \
            np.asarray(variables_removing_table_input, dtype=int)
    except TypeError:
        variables_removing_table_input = \
            np.asarray([variables_removing_table_input], dtype=int)
        n_variables_removing_table_input = len(variables_removing_table_input)

    # if dtype is None:
    #     dtype = array_input.dtype

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)
    n_variables_table_input = shape_array_input[axis_variables_table_input]

    axis_variables_table_input %= n_axes_array_input
    axis_samples_input %= n_axes_array_input
    variables_removing_table_input %= n_variables_table_input

    n_axes_array_output = n_axes_array_input + n_axes_inserting_output - 2
    # 2 axes, i.e. the axis_variables_table_input and the axis_samples_input will be put inside each element
    # of the object array "array_output".
    axes_inserting_output %= n_axes_array_output

    # check point 1
    if np.sum(axes_inserting_output[0] == axes_inserting_output) > 1:
        raise Exception('axes_inserting_output cannot contain repeated values')
    # check point 2
    if np.sum(
            variables_removing_table_input[
                0] == variables_removing_table_input) > 1:
        raise Exception('variables_removing_table_input cannot contain repeated values')
    # check point 3
    if n_variables_removing_table_input != n_axes_inserting_output:
        raise Exception(
            'Shapes of axes_inserting_output and variables_removing_table_input must be equal')

    # check point 4
    if np.sum(axis_samples_input == axis_variables_table_input) > 0:
        raise Exception('axis_samples_input and axis_variables_table_input must be different')

    axes_array_input = np.arange(n_axes_array_input)
    axes_non_axis_variables_table_input = axes_array_input[axes_array_input != axis_variables_table_input]
    axes_other_array_input = axes_non_axis_variables_table_input[
        axes_non_axis_variables_table_input != axis_samples_input]
    axes_other_array_input_inverted = axes_other_array_input[::-1]
    n_axes_other_array_input = len(axes_other_array_input)

    variables_table_input = np.arange(n_variables_table_input)
    if variables_staying_table_input is None:
        variables_staying_table_input = variables_table_input[np.logical_not(
            samples_in_arr1_are_in_arr2(variables_table_input, variables_removing_table_input))]
    # n_variables_staying_table_input = len(variables_staying_table_input)

    indexes_array_input_c = np.full(n_axes_array_input, 0, dtype=object)
    indexes_array_input_c[axis_variables_table_input] = variables_removing_table_input
    indexes_array_input_c[axis_samples_input] = np.arange(shape_array_input[axis_samples_input])
    indexes_input = advanced_indexing(indexes_array_input_c)
    array_variables_removing_input_1_case = array_input[indexes_input]
    # indexes_array_input_i = np.full(n_axes_array_input, 0, dtype=object)
    # indexes_array_input_i[axis_samples_input] = slice(None)
    # indexes_array_input_i[axis_variables_table_input] = slice(None)
    # indexes_array_input_tuple_i = tuple(indexes_array_input_i)
    for a in axes_other_array_input_inverted:
        array_variables_removing_input_1_case = np.squeeze(array_variables_removing_input_1_case, axis=a)

    axis_variables_in_combinations_removing = int(axis_variables_table_input > axis_samples_input)
    axis_combinations_in_combinations_removing = int(not (bool(axis_variables_in_combinations_removing)))
    conditions_variables_removing_table_input = trials_to_conditions(
        array_variables_removing_input_1_case, axis_combinations=axis_combinations_in_combinations_removing)
    n_conditions_variables_removing_table_input = conditions_to_n_conditions(
        conditions_variables_removing_table_input)
    n_combinations_variables_removing_table_input = int(np.prod(
        n_conditions_variables_removing_table_input))

    # axes_inserting_output_sorted = np.sort(axes_inserting_output) # ?????????         ???

    combinations_variables_removing_table_input = conditions_to_combinations(
        conditions_variables_removing_table_input, axis_combinations=axis_combinations_in_combinations_removing)
    # n_combinations_removing = combinations_variables_removing_table_input.shape[
    #     axis_combinations_in_combinations_removing]
    indexes_combinations_removing = np.empty(2, dtype=object)
    indexes_combinations_removing[axis_variables_in_combinations_removing] = np.arange(
        n_variables_removing_table_input)
    # indexes_combinations_removing_to_remove_axis_combinations = np.full(2, 0, dtype=object)
    # indexes_combinations_removing_to_remove_axis_combinations[axis_variables_in_combinations_removing] = slice(None)
    # indexes_combinations_removing_to_remove_axis_combinations = tuple(
    #     indexes_combinations_removing_to_remove_axis_combinations)

    combinations_axes_inserting_output = n_conditions_to_combinations(
        n_conditions_variables_removing_table_input, axis_combinations=axis_combinations_in_combinations_removing)

    # n_variables_table_output = \
    #     n_variables_table_input - n_variables_removing_table_input

    # if axis_variables_table_input > axis_samples_input:
    #     axis_variables_table_output = 1
    #     axis_samples_output = 0
    # elif axis_variables_table_input < axis_samples_input:
    #     axis_variables_table_output = 0
    #     axis_samples_output = 1

    axes_array_output = np.arange(n_axes_array_output)
    shape_array_output = np.empty(n_axes_array_output, dtype=int)
    shape_array_output[axes_inserting_output] = n_conditions_variables_removing_table_input
    axes_other_output = axes_array_output[np.logical_not(
        samples_in_arr1_are_in_arr2(axes_array_output, axes_inserting_output))]
    shape_array_output[axes_other_output] = shape_array_input[axes_other_array_input]
    array_output = np.empty(shape_array_output, dtype=object)

    indexes_output = np.empty(n_axes_array_output, dtype=object)
    indexes_input = np.empty(n_axes_array_input, dtype=object)
    for a in range(n_axes_array_input):
        indexes_input[a] = np.arange(shape_array_input[a])
    indexes_input[axis_variables_table_input] = variables_staying_table_input

    if n_axes_other_array_input == 0:

        for c in range(n_combinations_variables_removing_table_input):

            indexes_combinations_removing[axis_combinations_in_combinations_removing] = c

            indexes_input[axis_samples_input] = np.all(
                array_variables_removing_input_1_case ==
                combinations_variables_removing_table_input[advanced_indexing(indexes_combinations_removing)],
                axis=axis_variables_in_combinations_removing)

            array_variables_staying_input_c = array_input[advanced_indexing(indexes_input)]
            for a in axes_other_array_input_inverted:
                array_variables_staying_input_c = np.squeeze(array_variables_staying_input_c, axis=a)

            combinations_axes_inserting_output_c = combinations_axes_inserting_output[advanced_indexing(
                indexes_combinations_removing)]
            combinations_axes_inserting_output_c = np.squeeze(
                combinations_axes_inserting_output_c, axis=axis_combinations_in_combinations_removing)

            indexes_output[axes_inserting_output] = combinations_axes_inserting_output_c
            array_output[tuple(indexes_output)] = array_variables_staying_input_c
    else:

        indexes_input_conditions = np.copy(indexes_input)
        indexes_input_conditions[axis_variables_table_input] = variables_removing_table_input

        combinations_axes_other_input = n_conditions_to_combinations(shape_array_input[axes_other_array_input])
        n_combinations_axes_other_input = len(combinations_axes_other_input)
        for i in range(n_combinations_axes_other_input):

            indexes_input_conditions[axes_other_array_input] = combinations_axes_other_input[i]
            # indexes_input_conditions = advanced_indexing(indexes_input_conditions)
            array_variables_removing_input_i = array_input[advanced_indexing(indexes_input_conditions)]
            for a in axes_other_array_input_inverted:
                array_variables_removing_input_i = np.squeeze(array_variables_removing_input_i, axis=a)

            indexes_input[axes_other_array_input] = combinations_axes_other_input[i]
            indexes_output[axes_other_output] = combinations_axes_other_input[i]

            for c in range(n_combinations_variables_removing_table_input):

                indexes_combinations_removing[axis_combinations_in_combinations_removing] = c

                indexes_input[axis_samples_input] = np.all(
                    array_variables_removing_input_i ==
                    combinations_variables_removing_table_input[advanced_indexing(indexes_combinations_removing)],
                    axis=axis_variables_in_combinations_removing)

                array_variables_staying_input_i_c = array_input[advanced_indexing(indexes_input)]
                for a in axes_other_array_input_inverted:
                    array_variables_staying_input_i_c = np.squeeze(array_variables_staying_input_i_c, axis=a)

                combinations_axes_inserting_output_i_c = combinations_axes_inserting_output[advanced_indexing(
                    indexes_combinations_removing)]
                combinations_axes_inserting_output_i_c = np.squeeze(
                    combinations_axes_inserting_output_i_c, axis=axis_combinations_in_combinations_removing)
                indexes_output[axes_inserting_output] = combinations_axes_inserting_output_i_c

                array_output[tuple(indexes_output)] = array_variables_staying_input_i_c

    return array_output
