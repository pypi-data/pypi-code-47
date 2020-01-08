"""
Created by adam on 1/6/20
"""
__author__ = 'adam'



def clean_string_columns( frame ):
    """Removes excess whitespace from column names.
    (I always have to look this up otherwise)
    """
    return frame.columns.str.strip()


def detect_non_float_columns(frame):
    """Determine which columns are not cast to float64"""
    nonfloats = []
    for c in frame.columns:
        if frame[c].dtype != 'float64':
            nonfloats.append(c)
    print("These columns have a non-float dtype: ", nonfloats)
    return nonfloats


def typecast_columns(frame, columns):
    """Transforms the given columns to float64 type"""
    frame[columns] = frame[columns].astype('float64')


if __name__ == '__main__':
    pass