import os
from datetime import datetime, timedelta
from flask import jsonify, request


_DATE_FORMAT = "%Y-%m-%d"


class _RequestLevels:
    DEBUG = "debug.log"
    ERROR = "error.log"
    INFO = "info.log"


def _get_available_log_files(log_folder, log_level):
    """
    Filters the list of possible log files by the log filter.
    :param log_folder: the folder name where the log files are located
    :param log_level: the log level, one of the _RequestLevels
    :return: a list of strings representing the file names of log files matching the log level.
    """
    result = []
    for _, _, files in os.walk(log_folder):
        for f in files:
            if log_level in f and ".log" in f:
                result.append(f)
    return result


def _find_log_candidates(available_log_files, request_date, log_file_name):
    """
    Helper function to find log file candidates by checking which files could cover the requested date interval
    :param available_log_files: a list of available log files of the requested level
    :param request_date: the date for which the log file is requested
    :param log_file_name: the name prefix of the log files (e.g. debug.log, which prefixes e.g. debug.log.2019-12-24)
    :return: a list of log file names that most likely will contain the requested log date
    """
    parsed_request_date = datetime.strptime(request_date, _DATE_FORMAT)
    interval = [parsed_request_date.timestamp(), (parsed_request_date + timedelta(days=1)).timestamp()]

    # find log files that are at least after the requested date
    candidates = []
    for log_file in available_log_files:
        suffix = log_file.replace(log_file_name, "")
        if suffix == "":
            # current day
            end_time = datetime.now().timestamp()
        else:
            end_time = datetime.strptime(suffix[1:], _DATE_FORMAT).timestamp()

        if end_time < interval[0]:
            # too early
            continue
        candidates.append({
            "end_time": end_time,
            "file": log_file,
        })

    # no log files after request date, use latest
    if len(candidates) == 0:
        return [log_file_name]
    if len(candidates) == 1:
        return [candidates[0]["file"]]

    # check if we have to add additional files
    sorted_files = list(sorted(candidates, key=lambda x: x["end_time"]))
    result = [sorted_files[0]["file"]]
    # init iteration variables
    last_seen_date = sorted_files[0]["end_time"]
    index = 1
    while last_seen_date < interval[1]:
        # add next log file
        result.append(sorted_files[index]["file"])
        # update iteration variables
        last_seen_date = sorted_files[index]["end_time"]
        index += 1
    return result


def _parse_date(line):
    """
    Attempts to parse a date out of a log line. The date format to check for is "%Y-%m-%d %H:%M:%S". If no date can be
    parsed, no date and the message is returned. If a date is found, the date and the message (separately) are returned.
    :param line: a line from a log file
    :return: a tuple of datetime and string, where the datetime represents the parsed date (or is None) and the string
    representing the message (anything after the date).
    """
    if len(line) < 24:
        return None, line
    try:
        sub = line[0:19]
        message = line[24:]
        date = datetime.strptime(sub, "%Y-%m-%d %H:%M:%S")
        # was able to parse date, return it
        return date, message
    except ValueError:
        # could not parse date, no start of log message
        return None, line


def _get_log_messages(log_folder, candidates, log_date):
    """
    Naive function to extract sorted log messages from the provided candidate files for the given date. Any log message
    in between the log date and the day after the log date are captured from the list of candidate files read from the
    provided log folder.
    :param log_folder: a string representing the path to the log folder
    :param candidates: a list of file names in the log folder that are likely to contain matching log messages for the
    requested date
    :param log_date: the log date to filter for
    :return: a list of dictionaries containing "timestamp" and "message" keys, where the timestamp is a Unix timestamp
    of the message and the message is a list of strings representing all the lines of the log messages (or just one, if
    it's a one liner log message)
    """
    parsed_start = datetime.strptime(log_date, _DATE_FORMAT)
    parsed_end = parsed_start + timedelta(days=1)

    result = []
    for candidate_file in candidates:
        fr = open(os.path.join(log_folder, candidate_file), "r")
        current_entry = {
            "timestamp": 0,
            "message": [],
        }
        skip_current = False
        for line in fr:
            line = line.replace("\r\n", "").replace("\n", "")
            parse_date, message = _parse_date(line)
            if parse_date is not None:
                if parsed_start.timestamp() > parse_date.timestamp() or parse_date.timestamp() > parsed_end.timestamp():
                    skip_current = True
                else:
                    skip_current = False

            if skip_current:
                continue

            if parse_date is None:
                if current_entry["timestamp"] != 0:
                    # next line of a message
                    current_entry["message"].append(message)
            else:
                if current_entry["timestamp"] != 0:
                    # append previous entry and start new one
                    result.append(current_entry)

                # init new entry
                current_entry = {
                    "timestamp": round(parse_date.timestamp()),
                    "message": [message]
                }

        fr.close()
        # append current entry at the end of the log file
        if current_entry["timestamp"] != 0:
            result.append(current_entry)

    return list(sorted(result, key=lambda x: x["timestamp"]))


def register_endpoint(app, log_folder="./_logs", api_prefix="/api", log_file_mapping=None, login_check=None):
    """
    Registers the endpoint to retrieve log files via the API. This will create a new endpoint `/_logs` prefixed by
    whatever prefix is provided.
    :param app: a flask app instance
    :param log_folder: a string representing the folder name where log files are stored
    :param api_prefix: an endpoint prefix to use for the /_logs endpoint (default: /api)
    :param log_file_mapping: a mapping (dict) that maps from log level (see _RequestLevels) to the file name that is
    :param login_check: a function that will check the request and perform authentication and potentially abort the
    request. If none is provided, no auth check is performed.
    used. If no mapping is provided, _RequestLevels will be used. Example {"info.log": "custom-log-name.log"}
    """

    @app.route("{}{}".format(api_prefix, "/_logs"))
    def retrieve_log():
        """
        Retrieves logs from the server as JSON response. Each log message will be parsed and returned as structured
        entry with a timestamp and a message. The request needs to contain a query parameter ?date=YY-MM-DD.
        Additionally a query parameter &level=error.log can be provided to filter the log level. The default is to
        return INFO logs.
        :return: a JSON response with a list of objects representing each log message.
        """
        if login_check is not None:
            login_check()

        request_date = request.args.get("date")
        request_level = request.args.get("level")
        if request_level is None:
            request_level = _RequestLevels.INFO

        available = _get_available_log_files(log_folder, request_level)
        if len(available) == 0:
            return jsonify([])

        if log_file_mapping is not None:
            request_level = log_file_mapping[request_level]

        candidates = _find_log_candidates(available, request_date, request_level)
        log_messages = _get_log_messages(log_folder, candidates, request_date)
        return jsonify(log_messages)
