__author__ = "Unai Saralegui"
__copyright__ = "Copyright 2019, Unai Saralegui"
__credits__ = ["Unai Saralegui", "Josu Gomez"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Unai Saralegui"
__email__ = "usaralegui@gmail.com"
__status__ = "Development"


from . import keywords
from .error import RedCapError
import requests
import json
import datetime
from lxml import etree


def format_date(datee: datetime.datetime):
    """
    Get date formatted to use in REDCAP API
    :param datee: datetime.datetime object
    :return:
    """
    try:
        date_format = "%Y-%m-%d %H:%M:%S"
        datee = datee.strftime(date_format)
        return datee
    except Exception as ex:
        raise RedCapError("Error formatting date. Provide datetime.datetime date")


class APIHandler:
    """Class to interact with RedCap API"""

    def __init__(self, api_url, token, name='', verify_ssl=True):
        """
        Main function to load APIHandler class
        :param api_url: API URL to the REDCap server
        :param token: API token for the project
        :param name: name of the project (optional)
        :param verify_ssl: Verify SSL, default True.
        """
        self.__api_url = api_url
        self.__token = token
        self.__name = name
        self.__verify_ssl = verify_ssl
        self.metadata = None
        self.redcap_version = None
        self.__check_configuration()

    def __check_configuration(self):
        """
        Check the URL and token are valid with API calls to obtain metadata and REDCAP version
        :return: None (raises redcapy.RedCapError if the configuration is not OK)
        """
        content = keywords.CONTENT_METADATA
        data_format = keywords.FORMAT_JSON
        payload = self.__construct_payload(content=content, data_format=data_format)
        request_data = self.__call_api(payload=payload)
        if request_data.status_code == 501:
            raise RedCapError("Error obtaining metadata. Check your URL.")
        elif request_data.status_code == 403:
            raise RedCapError("Error obtaining metadata. Check your token.")
        self.metadata = self.__get_data_from_request(request_data=request_data)
        self.redcap_version = self.get_redcap_version()

    def __call_api(self, payload):
        """
        Function to call the api with the specifiec payload
        :param payload: payload in dictionary format
        :return: return of the request call
        """
        data = list(payload.items())
        request_data = requests.post(self.__api_url, data=data)
        return request_data

    def __construct_payload(self, content, data_format=None, action=None, record=None, typee=None, report_id=None,
                            instrument=None, date_range_begin=None, date_range_end=None):
        """
        Construct the payload with specified content and data_format
        :param content: content to obtain from API
        :param data_format: format of data to obtain (default json)
        :return: payload in dict
        """
        payload = {
            keywords.TOKEN: self.__token,
            keywords.CONTENT: content,
            keywords.FORMAT: data_format,
        }
        if data_format is not None:
            payload[keywords.FORMAT] = data_format
        if action is not None:
            payload[keywords.ACTION] = action
        if record is not None:
            payload[keywords.RECORD] = record
        if typee is not None:
            payload[keywords.TYPE] = typee
        if report_id is not None:
            payload[keywords.REPORT_ID] = report_id
        if instrument is not None:
            payload[keywords.INSTRUMENT] = instrument
        if date_range_begin is not None:
            payload[keywords.DATE_RANGE_BEGIN] = date_range_begin
        if date_range_end is not None:
            payload[keywords.DATE_RANGE_END] = date_range_end
        return payload

    def __get_data_from_request(self, request_data):
        """
        Function to obtain the data from the request
        :param request_data: request return obtained fro API call
        :return: data in python format (str, json or lxml.etree)
        """
        if request_data.status_code != 200:
            raise RedCapError(f"status_code={request_data.status_code} {request_data.content}")
        try:
            data = request_data.json()
            return data
        except json.decoder.JSONDecodeError as e:
            pass
        try:
            data = etree.fromstring(request_data.content)
            return data
        except etree.XMLSyntaxError as ex:
            pass
        data = request_data.content
        return data

    def __get_data(self, content, data_format=None, action=None, record=None, typee=None, report_id=None,
                   instrument=None, date_range_begin=None, date_range_end=None):
        """
        Obtain data for content and data_format
        :param content: content to obtain
        :param data_format: format of the data to obtain
        :param action: action to obtain
        :param record: record to obtain
        :param typee: type of the data to obtain
        :return: data obtained from server formatted to use inside python
        """
        payload = self.__construct_payload(content=content, data_format=data_format,
                                           action=action, record=record, typee=typee,
                                           report_id=report_id, instrument=instrument,
                                           date_range_begin=date_range_begin, date_range_end=date_range_end)
        request_data = self.__call_api(payload=payload)
        data = self.__get_data_from_request(request_data=request_data)
        return data

    def get_metadata(self, data_format=None):
        """
        Get metadata for REDCAP project
        :param data_format: (default json) format of the data to obtain
        :return: metadata for the REDCAP project
        """
        if self.metadata is not None:
            return self.metadata
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_METADATA
        metadata = self.__get_data(content=content, data_format=data_format)
        self.metadata = metadata
        return metadata

    def get_redcap_version(self):
        """
        Get the version of the REDCAP project
        :return: redcap version
        """
        if self.redcap_version is not None:
            return self.redcap_version
        content = keywords.CONTENT_VERSION
        redcap_version = self.__get_data(content=content, data_format=None)
        self.redcap_version = redcap_version
        return redcap_version

    def get_users(self, data_format=None):
        """
        Get users for REDCAP project
        :param data_format: (default json) format of the data to obtain
        :return: users in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_USER
        data = self.__get_data(content=content, data_format=data_format)
        return data

    def get_arms(self, data_format=None):
        """
        Get arms for REDCAP project
        :param data_format: (default json) format of the data to obtain
        :return: arms in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_ARM
        data = self.__get_data(content=content, data_format=data_format)
        return data

    def get_events(self, data_format=None):
        """
        Get events for REDCAP project
        :param data_format: (default json) format of the data to obtain
        :return: events in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_EVENT
        data = self.__get_data(content=content, data_format=data_format)
        return data

    def get_field_names(self, data_format=None):
        """
        Get field names for REDCAP project
        :param data_format: (default json) format of the data to obtain
        :return: field names in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_FIELD_NAMES
        data = self.__get_data(content=content, data_format=data_format)
        return data

    '''
    def get_file(self, record):
        """
        Get file for REDCAP project
        :return: file in the REDCAP project
        """
        content = keywords.CONTENT_FILE
        action = keywords.ACTION_EXPORT
        data = self.__get_data(content=content, action=action, record=record)
        return data
    '''

    def get_form_event_mapping(self, data_format=None):
        """
        Get form event mapping names for REDCAP project
        :param data_format: (default json) format of the data to obtain
        :return: field names in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_FIELD_NAMES
        data = self.__get_data(content=content, data_format=data_format)
        return data

    def get_instruments_pdf(self, data_format=None, output_file=None):
        """
        Get pdf in binary format with instruments (or save directly to file)
        :param data_format: (default json) format of the data to obtain
        :param output_file: (optional) file to save pdf to
        :return: pdf in binary format
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_PDF
        data = self.__get_data(content=content, data_format=data_format)
        if output_file is not None:
            with open(output_file, "wb") as f:
                f.write(data)
        return data

    def get_instruments(self, data_format=None):
        """
        Get instruments for REDCAP project
        :param data_format: (default json) format of the data to obtain
        :return: instruments in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_INSTRUMENT
        data = self.__get_data(content=content, data_format=data_format)
        return data

    def get_project_info(self, data_format=None):
        """
        Get project info for REDCAP project
        :param data_format: (default json) format of the data to obtain
        :return: project info in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_PROJECT
        data = self.__get_data(content=content, data_format=data_format)
        return data

    def get_records(self, data_format=None, date_range_begin: datetime.datetime = None,
                    date_range_end: datetime.datetime = None):
        """
        Get project for REDCAP project
        :param data_format: (default json) format of the data to obtain
        :param date_range_end: [optional] get only records registered before data in server time
        (date format YYYY-MM-DD HH:MM:SS)
        :param date_range_begin: [optional] get only records registered after data in server time
        (date format YYYY-MM-DD HH:MM:SS)
        :return: records in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        if date_range_begin is not None:
            date_range_begin = format_date(datee=date_range_begin)
        if date_range_end is not None:
            date_range_end = format_date(datee=date_range_end)
        content = keywords.CONTENT_RECORD
        typee = keywords.TYPE
        data = self.__get_data(content=content, data_format=data_format, typee=typee,
                               date_range_begin=date_range_begin, date_range_end=date_range_end)
        return data

    def get_reports(self, report_id, data_format=None):
        """
        Get report for REDCAP project
        :param report_id: report id to obtain
        :param data_format: (default json) format of the data to obtain
        :return: report for specified id in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_REPORT
        data = self.__get_data(content=content, data_format=data_format, report_id=report_id)
        return data

    def get_participant_list(self, instrument, data_format=None):
        """
        Get participant list for REDCAP project
        :param instrument: instrument to obtain participant list from
        :param data_format: (default json) format of the data to obtain
        :return: participant list in the REDCAP project
        """
        if data_format is None:
            data_format = keywords.FORMAT_JSON
        content = keywords.CONTENT_PARTICIPANT_LIST
        data = self.__get_data(content=content, data_format=data_format, instrument=instrument)
        return data
