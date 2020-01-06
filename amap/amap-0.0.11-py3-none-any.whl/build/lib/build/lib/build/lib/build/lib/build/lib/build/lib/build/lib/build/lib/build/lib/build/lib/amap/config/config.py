import platform
from configobj import ConfigObj


__os_folder_names = {"Linux": "linux_x64", "Darwin": "osX", "Windows": "win64"}

try:
    os_folder_name = __os_folder_names[platform.system()]
except KeyError:
    raise ValueError(
        "Platform {} is not recognised as a valid platform. "
        "Valid platforms are : {}".format(
            platform.system(), __os_folder_names.keys()
        )
    )


def get_binary(binaries_folder, program_name):
    path = "{}/{}/{}".format(binaries_folder, os_folder_name, program_name)
    return path


def get_config_ob(config_path):
    config_obj = ConfigObj(config_path, encoding="UTF8", indent_type="    ",)
    return config_obj
