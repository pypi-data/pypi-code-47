import inspect


class FileWriter:

    def __init__(self):
        '''
        '''
        pass

    def write_to_file(self, output_file, subtrack=False):
        '''
        In python > 3.5, attribute order is preserved when calling inspect.getmembers
        '''
        for attribute, value in inspect.getmembers(self, lambda a: a is not None and not callable(a))[0][1].items():
            if (attribute[:2] != '__' and value is not None):
                string = f'    ' if subtrack else f''
                string += f'{attribute} {value}\n'
                output_file.write(string)
