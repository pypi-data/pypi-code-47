import configparser
import redcapy
import datetime

config = configparser.ConfigParser()
config.read("config.cfg")

redcap_config = config["REDCAP"]
api_url = redcap_config["url"]
token = redcap_config["token"]

redcap_handler = redcapy.request.APIHandler(api_url=api_url, token=token)
#metadata = redcap_handler.get_metadata()
#redcap_version = redcap_handler.get_redcap_version()
#users = redcap_handler.get_users()
# arms = redcap_handler.get_arms()
# events = redcap_handler.get_events()
#field_names = redcap_handler.get_field_names()
#file = redcap_handler.get_file(record=1)
#form_event_mapping = redcap_handler.get_form_event_mapping()
#instruments_pdf = redcap_handler.get_instruments_pdf(output_file="./instruments.pdf")
#instruments = redcap_handler.get_instruments()
#project = redcap_handler.get_project_info()
records = redcap_handler.get_records()
print(len(records), len(records[0]))
#report = redcap_handler.get_reports(1)
#participant_list = redcap_handler.get_participant_list(instrument=instruments[-1]['instrument_name'])
date_range_begin = datetime.datetime.strptime("2019-10-10", "%Y-%m-%d")
date_range_end = datetime.datetime.strptime("2019-12-10", "%Y-%m-%d")
records = redcap_handler.get_records(date_range_begin=date_range_begin, date_range_end=date_range_end)
print(len(records), len(records[0]))