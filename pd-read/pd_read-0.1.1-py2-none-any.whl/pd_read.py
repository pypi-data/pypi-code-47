from .read_csv import ReadCSV

class PDRead(object):
    def __init__(self, filename):
        self.filename = filename

    def get_file_extension(self):
	    return self.filename.rsplit('.', 1)[1].lower() if '.' in self.filename else ''

    def get_dataframe(self):
        ext = self.get_file_extension()
        if ext == 'csv':
            obj = ReadCSV(self.filename)
            return obj.get_data(rows=10, columns=['policyID', 'statecode'])

