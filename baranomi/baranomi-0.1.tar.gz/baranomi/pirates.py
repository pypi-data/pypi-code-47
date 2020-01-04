from typing import List, Any
from pathlib import Path


class Baranomi(object):
    def __init__(self, extension:str="bpirate", batch_size=10000):
        self._extension = extension
        self.file_data = None
        self.batch_size = batch_size
        self._split_file_data = []
        self._original_ext = ""
        self.total_bytes = None
        self._suffixes = []


    @property
    def split_data(self):
        return self._split_file_data
    
    @property
    def split_data_count(self):
        return len(self._split_file_data)

    @property
    def suffix(self):
        return "".join(self._suffixes)

    def _join_m3u8(self, m3u8_list:List[bytearray]):
        if len(m3u8_list) == 0:
            raise AttributeError("You didn't supply any m3u8 files (information).")

    def _join_normal(self, bytearray_list:List[bytearray]):
        if len(bytearray_list) == 0:
            raise AttributeError("You didn't supply any bytes.")
        
    
    def _split_normal(self, normal_data):
        byte = normal_data.read(self.batch_size)
        if byte != b"":
            byte_array = bytearray(byte)
            self._split_file_data.append(byte_array)


        while byte != b"":
            # Do stuff with byte.
            byte = normal_data.read(self.batch_size)
            byte_array = bytearray(byte)
            self._split_file_data.append(byte_array)
    
    def _split_m3u8(self, m3u8_data):
        byte = m3u8_data.read(self.batch_size)
        if byte != b"":
            byte_array = bytearray(byte)
            self._split_file_data.append(byte_array)

        while byte != b"":
            # Do stuff with byte.
            byte = m3u8_data.read(self.batch_size)
            byte_array = bytearray(byte)
            self._split_file_data.append(byte_array)


    def split(self):
        """ Get a blob of information and split it into multiple parts"""
        if self.file_data is None:
            raise AttributeError("Data not loaded yet")

        if self.suffix == "m3u8":
            self._split_m3u8(self.file_data)
        else:
            self._split_normal(self.file_data)

        return self

    def join(self):
        # Get all of the bytes from the 
        total_bytes = bytearray()
        for barr in self._split_file_data:
            total_bytes += barr
        self.total_bytes = total_bytes
        return self

    def load(self, file_name:str):
        """ Load a file. If it doesn't exist it'll raise an error."""

        current_file = Path(file_name)
        if not current_file.is_file():
            raise FileNotFoundError(f"{file_name} not found")


        self._original_ext = current_file.suffixes
        self.file_data = open(file_name, mode="rb")
        return self
    
    def load_file_list_as_bytes(self, file_names:List[str]):
        """ Load a list of files. If it doesn't exist it'll raise an error. Make sure to """
        if len(file_names) == 0:
            raise AttributeError("You didn't add any files")

        file_data_list = []
        
        for _file in file_names:
            current_file = Path(_file)
            if not current_file.is_file():
                continue
            self._suffixes = current_file.suffixes

            as_bytes = current_file.read_bytes()
            file_data_list.append(bytearray(as_bytes))
            

        self._split_file_data = file_data_list
        return self

    def save(self, file_name:str):
        """ Sve all of the byte arrays we've already split into a set of files """
        if self.total_bytes is None:
            raise AttributeError("No data saved")

        with open(file_name, 'wb') as f:
            f.write(self.total_bytes)
        return self

    def _write_one(self, save_location, data):
        with open(save_location, 'wb') as f:
            f.write(data)

    def save_split_files(self, file_name):
        """ Get the split files and save them under the file_name + item_number + suffixes"""
        if len(self._split_file_data) == 0:
            raise AttributeError("No split file data")

        current_file = Path(file_name)
        current_suffixes = current_file.suffixes
        current_stem = current_file.stem
        for suffix in current_suffixes:
            current_stem = current_stem.replace(suffix, '')
        
        parents = current_file.parents
        first_parent = parents[0]
        joined = "".join(current_suffixes)
        for index, blob in enumerate(self._split_file_data):
            file_string = f"{current_stem}-{index}{joined}"
            save_location = f"{first_parent}/{file_string}"
            self._write_one(save_location, blob)
        return self