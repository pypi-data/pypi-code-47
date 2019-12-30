import datetime
import logging
import os
from collections import defaultdict
from logging import Logger, getLogger
from typing import Dict, List, Optional, Set

from pandas import DataFrame

logger: Logger = getLogger()


def get_now_str():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")


def get_file_name_root(file_path: str) -> str:
    return os.path.splitext(os.path.split(file_path)[1])[0]


def make_log_dir(log_dir: Optional[str] = None) -> str:
    if log_dir is None:
        log_dir = os.path.join(os.curdir, "log")

    if os.path.exists(log_dir):
        if not os.path.isdir(log_dir):
            raise Exception(f"{log_dir} exists, but not a directory.")
    else:
        os.mkdir(log_dir)

    return log_dir


def set_logging_basic_config(
        main_python_file_name: str,
        level: int = logging.INFO,
        format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        log_dir: Optional[str] = None,
) -> None:
    """
    Sets basic logging configuration.
    """
    main_python_file_name_root = get_file_name_root(main_python_file_name)
    log_dir: str = make_log_dir(log_dir)
    log_file_full_path = os.path.join(log_dir, f"{main_python_file_name_root}_{get_now_str()}.log")

    logging.basicConfig(
        level=level,
        format=format,
        handlers=[
            logging.FileHandler(log_file_full_path),
            logging.StreamHandler(),
        ],
    )

    logger.info("logging basic configuration has been set up!")
    logger.info(f"Level: {level}")
    logger.info(f"format: {format}")
    logger.info(f"log_dir: {log_dir}")
    logger.info(f"log_file_full_path: {log_file_full_path}")


def input_event_list_to_csv_file(input_event_list: list, filename: str) -> DataFrame:
    """
    Parameters
    ----------
    input_event_list:
        List of droidbot.input_event.InputEvent's.
    filename:
        The name of the file to which the contents of droidbot.input_event.InputEvent's are written.

    Returns
    -------
    input_event_data_frame:
        pandas.DataFrame containing information of each droidbot.input_event.InputEvent.
    """

    field_set: Set[str] = set()

    for input_event in input_event_list:
        for key, value in input_event.to_dict().items():
            if key == "view":
                for k, v in value.items():
                    field_set.add(k)
            else:
                field_set.add(key)

    field_value_list_dict: Dict[str, List[str]] = defaultdict(list)

    for input_event in input_event_list:
        field_assigned_set: Set[str] = set()
        for key, value in input_event.to_dict().items():
            if key == "view":
                for k, v in value.items():
                    if k in field_assigned_set:
                        field_value_list_dict[k][-1] += "///" + v
                    else:
                        field_value_list_dict[k].append(v)


def set_logger_config(
        logger: logging.Logger,
        main_python_file_name: str,
        level: int = logging.INFO,
        format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        log_dir: Optional[str] = None,
):
    """
    Sets basic logging configuration.
    """
    main_python_file_name_root = get_file_name_root(main_python_file_name)
    log_dir: str = make_log_dir(log_dir)
    log_file_full_path = os.path.join(log_dir, f"{main_python_file_name_root}_{get_now_str()}.log")

    logger.setLevel(level)

    file_handler: logging.FileHandler = logging.FileHandler(log_file_full_path)
    stream_handler: logging.StreamHandler = logging.StreamHandler()

    formatter: logging.Formatter = logging.Formatter(format)
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
