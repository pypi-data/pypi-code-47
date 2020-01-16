from simple_test_generator.constants import serialisation_type, test_data_directory


def get_test_data_filename(subdir, filename):
    return f'{test_data_directory}/{subdir}/{filename}.{serialisation_type}'
