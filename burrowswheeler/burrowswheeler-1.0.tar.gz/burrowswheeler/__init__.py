START_CHAR = '^'
END_CHAR = '|'


def inverse(string):
    length = len(string)
    table = ['' for x in range(length)]

    for j in range(length):
        for i in range(length):
            table[i] = string[i] + table[i]
        table = sorted(table)

    return_string = ''
    for s in table:
        if s[0] == START_CHAR and s[-1] == END_CHAR:
            return_string = s
            break
    return return_string[1:-1]


def transform(string):
    string = '{}{}{}'.format(START_CHAR, string, END_CHAR)
    length = len(string)

    table = []

    # Rotations (one way)
    # for i in range(length):
    #     rotated = string[length-i:length] + string[0:length-i]
    #     table.append(rotated)

    # Rotations (other way)
    for i in range(length):
        rotated = string[i:] + string[:i]
        table.append(rotated)

    table = sorted(table)

    last_column = ''.join([x[-1] for x in table])

    return last_column


if __name__ == '__main__':
    initial_string = 'banana'
    transformed_string = transform(initial_string)
    final_string = inverse(transformed_string)

    print('"{}" was transformed to "{}" and then back to "{}"'.format(
        initial_string, transformed_string, final_string,
    ))
