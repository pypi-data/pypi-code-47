"""I/O interfaces."""
import csv
import pprint


def extract_labels_data(*data_files):
    """
    list (Paths) -> tuple (list(floats), list (str))
    
    Extracts labels from data file(s).

    Parameters
    ----------
    data_files : list
        The files to extract labels.

    Raises
    ------
    ValueError
        If labels are not all the same.
    """
    data = []
    labels = []
    for file_ in data_files:
        with open(file_, 'r') as csv_file:
            
            data_lines = filter(
                lambda x: not x.startswith('#'),
                csv_file,
                )

            data_fields = (line.split(',') for line in data_lines)
            file_labels = []
            file_data = []
            for row in data_fields:
               file_labels.append(row[0])
               file_data.append(float(row[1]))

            labels.append(file_labels)
            data.append(file_data)

    if len(labels) > 1 and not all(labels[0] == i for i in labels[1:]):
        raise ValueError('Not all labels are the same among series')

    return data, labels[0]

    
    
