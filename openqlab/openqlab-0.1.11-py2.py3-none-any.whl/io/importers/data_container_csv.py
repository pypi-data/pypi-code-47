from openqlab.io.base_importer import StreamImporter
from openqlab.io.data_container import DataContainer


class DataContainerCSV(StreamImporter):
    NAME = "DataContainerCSV"
    AUTOIMPORTER = True
    STARTING_LINES = [DataContainer.json_prefix]

    def read(self):
        self._stream.seek(0)
        output = DataContainer.from_csv(self._stream, parse_dates=True)
        return output
