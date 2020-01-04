import configparser
from pathlib import Path
from shutil import copyfile


class ConfigurationError(Exception):
    """An error with your configuration file."""


class ConfigFile:
    """
    Parses the configuration file to get, set, and delete values in it or output the whole thing.
    It also allows you to reset the configuration file back to the original or output it.

    This ConfigFile relies on an adaptor pattern to swap in the correct parser for the given file.
    """

    def __init__(self, path, file_format=None):
        """
        Sets up the config parser to read the configuration file from
        the specified path.

        :param path: The absolute path to the configuration file.
        :type: Path or str

        :raises ParsingError: If unable to parse the configuration file.
        """
        self.original_path = self.__create_original_config()

        if file_format is None:
            self.__determine_file_format()

        if isinstance(str, path):
            self.path = Path(path)
        else:
            self.path = path

        self.parser = self.__determine_parser(file_format)
        self.parser.read(path)

    def get(self, section_key: str, type_=str):
        """
        Read the value of `section.key` of the hc config file.

        :param section_key: The section and key to read from in the hc config file.
        e.g. 'ocr.engine'
        :param type_: Coerces the return value to this value_type.

        :return: The value of the key
        :rtype: value_type

        :raises ConfigurationError: The specified `section.key` is not found, in an
        invalid format, or if we are unable to coerce the return value to value_type.
        """
        if section_key.rfind(".") == -1:
            raise ConfigurationError(
                "section_key must contain the section and key separated by a dot. "
                + "e.g. 'ocr.engine'"
            )

        section, key = section_key.rsplit(".", 1)

        try:
            return type_(self.parser.get(section, key))
        except configparser.Error as error:
            raise ConfigurationError(error.message)
        except ValueError:
            raise ConfigurationError(
                f"{section}.{key} invalid type (should be of type {type_})"
            )

    def set(self, section_key: str, value):
        """
        Sets the value of 'section.key' of the hc config file.

        :param section_key: The key to set from the hc config file. e.g. 'ocr.engine'
        :param value: The value to set the key to.

        :return: True if the setting was successful.
        :rtype: boolean

        :raises ConfigurationError: If there is no dot (.) in section_key
        """
        if section_key.rfind(".") == -1:
            raise ConfigurationError(
                "section_key must contain the section and key separated by a dot. "
                + "e.g. 'ocr.engine'"
            )

        section, key = section_key.rsplit(".", 1)

        if value is not None and not self.parser.has_section(section):
            self.parser.add_section(section)

        self.parser.set(section, key, value)
        self.parser.write(open(self.path, "w"))
        return True

    def delete(self, section_key: str):
        """
        Deletes a key or an entire section.

        :param section_key: The key to delete from the hc config file.
        e.g. 'ocr.engine'. If no dot (.) is present, it will assume you are trying
        to delete the entire section.

        :return: True if the deletion succeeded.
        :rtype: boolean

        :raise ConfigurationError: If the section does not exist in the config file or
        the key does not exist in the section.
        """
        if section_key.rfind(".") == -1:
            if not self.parser.has_section(section_key):
                raise ConfigurationError(
                    f"Cannot delete {section_key} because it is "
                    f"not in the config file."
                )

            self.parser.remove_section(section_key)
            self.parser.write(open(self.path, "w"))
            return True

        section, key = section_key.rsplit(".", 1)
        if key not in self.parser[section]:
            raise ConfigurationError(
                f"Cannot delete {section}.{key} because {key} is " f"not in {section}."
            )

        self.parser.remove_option(section, key)
        self.parser.write(open(self.path, "w"))
        return True

    def reset(self):
        """
        Resets the config file by deleting it and copying the original back
        in it's place.

        :return: True if the reset succeeded
        :rtype: boolean

        :raises OSError: If an error occurred when trying to copy the file.
        """
        Path(self.path).unlink(missing_ok=True)
        copyfile(self.original_path, self.path)
        return True

    def output(self):
        """
        Output the configuration file to STDOUT.

        :raises OSError: If the file cannot be opened.
        """
        with open(self.path, "r") as file:
            print(file.read())
