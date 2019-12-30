"""Main module."""

import re, sys

SIZE_COL_WIDTH = 12
MULTI_COL_WIDTH = 20 + SIZE_COL_WIDTH
LINE_REGEX = re.compile(r"\s*\S+")


def tweak(s, n=0):
    if not s:
        return 0, ""
    else:
        count, s_prime = tweak(s[1:], n+1)
        # Odd modulo 3
        if int(count / 3) % 2 == 1 and s_prime:
            return count + 1, s[0] + "\b_" + s_prime
        else:
            return count + 1, s[0] + s_prime


def colorise(s):
    """Colorise integer values using underlines and colorise values with a suffix
    as ...  ."""
    import colored

    COLOURS = {"E": "purple_1b", "P": "deep_pink_2", "G": "magenta_2b", "M": "indian_red_1c", "K": "tan"}
    try:
        # See if the size is an integer values
        int(s) 

        ## return s + "\b_"
        length, string = tweak(s)
        return string
    except ValueError:
        # Size is a string, e.g. "3.5M"
        suffix = s[-1]
        try:
            colour = COLOURS[suffix]
            return "%s%s%s%s" % (colored.fg(colour), s[0:-1], colored.attr("reset"), suffix)
        except KeyError:
            return s


def cols_format(cols, ownership_cols, size_column, dir_column, blend):
    ISDIR_REGEX = re.compile(r"\s*d")

    size_str = cols[size_column].strip()
    if ISDIR_REGEX.match(cols[dir_column]):
        size_output = size_str
    else:
        size_output = colorise(size_str)
    if ownership_cols == 0:
        # no owner/group column blending for size
        return "%s %*s%s" % ("".join(cols[0:size_column]), SIZE_COL_WIDTH,
                             size_output, "".join(cols[size_column+1:]))
    else:
        # owner/group column blending for size
        ownership_output = "".join(cols[size_column-ownership_cols:size_column])
        sep_str = " " * (MULTI_COL_WIDTH - len(ownership_output + size_str))
        multicol_output = ownership_output + sep_str + size_output
        return "%s%s%s" % ("".join(cols[0:size_column-ownership_cols]),
                           multicol_output, "".join(cols[size_column+1:]))

    
def main(args):
    size_column = int(args[1]) - 1
    inums_on = args[2] == "y"
    ownership_cols = int(args[3])
    if inums_on:
        dir_column = 1
    else:
        dir_column = 0

    ## print(len(args))
    for line in sys.stdin:
        cols = LINE_REGEX.findall(line)
        if len(cols) >= size_column + 3:
            # Check for column blending, i.e. owner/group suffix blends in with size prefix
            blend = (inums_on and size_column == 3) or size_column == 2
            print(cols_format(cols, ownership_cols, size_column, dir_column, blend))
        else:
            print(line, end='')
    return 0


# *** MAINLINE ***
if __name__ == '__main__':
   sys.exit(main(sys.argv))
