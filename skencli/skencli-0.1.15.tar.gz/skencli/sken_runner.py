from __future__ import absolute_import

import os
import sys
import argparse
import logging
import ntpath
import json
import requests
import base64
import yaml
import docker
import boto3

from .launchers.launch_sast_scanner import run_sast_scanner
from .launchers.launch_dast_scanner import run_dast_scanner
from .launchers.launch_sca_scanner import run_sca_scanner
from .launchers.docker_util import get_formated_timestamp

SKEN_SERVER_BASE_URL = 'https://cli.sken.ai/api'
#SKEN_SERVER_BASE_URL = 'http://localhost:8080/api'
LANGUAGES = ['ruby', 'javascript', 'python',
             'java', 'nodejs', 'license', 'go', 'python2']
SCANNERS = ['sast', 'dast', 'sca']
config = {}
parsed_args = {}
scan_info = {}

def get_scan_info():
    try:
        payload = {'projectId': config['projectid']}
        resp = requests.get(SKEN_SERVER_BASE_URL + "/cli/getScanData", params=payload)
        global scan_info
        scan_info = resp.json()

        if not scan_info['success']:
            print('Failed to get scan info from sken server, ' + scan_info['message'])
            exit(0)
    except Exception as e:
        print('Failed to get scan info from sken server.')
        logging.exception(e)
        exit(0)

def read_config():
    build_dir = get_build_dir()
    if os.path.exists(build_dir + 'sken.yaml'):
        with open(build_dir + 'sken.yaml', 'r') as stream:
            try:
                global config
                config = yaml.safe_load(stream)
                config['build_dir'] = build_dir
            except yaml.YAMLError as exc:
                logging.exception(exc)
                exit(0)
    else:
        print('File not found: %s' % (build_dir + 'sken.yaml'))
        exit(0)


def get_build_dir():
    if  'build_dir' in config:
        return config['build_dir']

    build_dir = ''
    if parsed_args.path is not None:
        build_dir = parsed_args.path
    elif 'WORKSPACE3' in os.environ:
        build_dir = os.environ['WORKSPACE']
    elif 'TRAVIS_BUILD_DIR' in os.environ:
        build_dir = os.environ['TRAVIS_BUILD_DIR']
    else:
        build_dir = os.getcwd()

    if not build_dir.endswith(os.path.sep):
        build_dir = build_dir + os.path.sep

    return build_dir

def select_scanner():
    if parsed_args.scanner is not None:
        scanner = parsed_args.scanner
    elif 'scanner' in config:
        scanner = config['scanner']
    else:
        print('Please specify "scanner" in sken.yaml')
        exit(0)

    scanners = scanner.split(',')
    for scanner in scanners:
        scanner = scanner.lower()

        if not scanner in SCANNERS:
            print("Scanner for %s hasn't been supported." % scanner)
            exit(0)
        
        if scanner == 'sast':
            print('SAST scanner selected')
            run_sast()
        elif scanner == 'license':
            print('License scanner selected')
            run_sast('license')
        elif scanner == 'dast':
            print('DAST scanner selected')
            code_lang = 'dast'
            dast_vars = config['variables']
            run_dast(dast_vars)
        elif scanner == 'sca':
            print('SCA scanner selected')
            if not 'variables' in config:
                print("Please specify variables for SCA in sken.yaml")
                exit(0)

            run_sca(config['variables'])
        else:
            print("Scanner for %s hasn't been supported." % scanner)
            exit(0)

def run_dast(dast_vars):
    dast_url = dast_vars['DAST_URL']
    is_dast_full_scan = dast_vars['DAST_FULL_SCAN']
    out_file = run_dast_scanner(dast_url, is_dast_full_scan, config['buildtool'])
    upload_output(out_file)

def run_sca(sca_vars):
    if not 'SCA_DATA_DIR' in sca_vars:
        print("Please specify SCA_DATA_DIR variable for SCA in sken.yaml")
        exit(0)
    if not 'SCA_REPORT_DIR' in sca_vars:
        print("Please specify SCA_REPORT_DIR variable for SCA in sken.yaml")
        exit(0)

    build_dir = get_build_dir()
    out_file, scan_start, scan_end = run_sca_scanner({'scanner': 'dependency-check' , 'build_dir': build_dir, 'scan_info': scan_info, 'variables': sca_vars})
    timing_file = generate_scan_result_file(build_dir, scan_start, scan_end)
    timestamp = upload_output(out_file, timing_file)

def run_sast(p_code_lang=None):
    if p_code_lang:
        code_lang = p_code_lang
    else: 
        code_lang = ''
        build_dir = get_build_dir()

        # read language from sken.yaml or command line args
        if parsed_args.lang is not None:
            code_lang = parsed_args.lang
        else:
            if 'language' in config:
                code_lang = config['language']
            else:
                print('Please specify "language" in sken.yaml')
                exit(0)

    code_lang = code_lang.lower()
    languages = code_lang.split(',')

    for code_lang in languages:
        if code_lang in LANGUAGES:
            print('Supported language %s found' % code_lang)
            scanner = ''
            if code_lang == 'ruby':
                scanner = 'brakeman'
            elif code_lang in ['nodejs', 'javascript']:
                scanner = 'nodejsscan'
            elif code_lang == 'license':
                scanner = 'licensescan'
            elif code_lang == 'go':
                scanner = 'gosec'
            elif code_lang == 'python2':
                scanner = 'banditpy2'
            elif code_lang == 'python':
                scanner = 'banditpy3'
            elif code_lang == 'java':
                scanner = 'findsecbugs'
            
            if scanner:
                out_file, scan_start, scan_end = run_sast_scanner({'scanner': scanner , 'build_dir': build_dir, 'scan_info': scan_info})
                timing_file = generate_scan_result_file(build_dir, scan_start, scan_end)
                timestamp = upload_output(out_file, timing_file)
                trigger_etl(timestamp, ntpath.basename(out_file), scanner)
            else:
                print("Scanner for %s hasn't been supported." % code_lang)
                exit(0)
        else:
            print('Language not supported')
            exit(0)

def generate_scan_result_file(build_dir, scan_start, scan_end):
    data = {
        'scanStart': scan_start,
        'scanEnd': scan_end
    }

    if not build_dir.endswith(os.path.sep):
        build_dir = build_dir + os.path.sep

    with open(build_dir + 'scan-timing.json', 'w') as f:
        f.write(json.dumps(data))
    
    return build_dir + 'scan-timing.json'

def upload_output(output_file, timing_file):
    print('Uploading output file...')
    timestamp = get_formated_timestamp()
    file_name = ''

    try:
        session = boto3.Session(
            aws_access_key_id=scan_info['awsAccessKeyId'], 
            aws_secret_access_key=scan_info['awsSecretAccessKey'], 
            region_name=scan_info['awsRegion'])

        s3 = session.resource('s3')
        file_name = ntpath.basename(output_file)
        data = open(output_file, 'rb')
        s3.Bucket('sken-scanner-output').put_object(Key=config['projectid'] + '/' + timestamp + '/' + file_name, Body=data)
        
        file_name = ntpath.basename(timing_file)
        data = open(timing_file, 'rb')
        s3.Bucket('sken-scanner-output').put_object(Key=config['projectid'] + '/' + timestamp + '/' + file_name, Body=data)
    except Exception as e:
        print('Failed to upload output file')
        logging.exception(e)

    print('Output file uploaded')
    return timestamp

def trigger_etl(timestamp, fileName, scanner):
    print('ETL started')
    try:
        payload = {'projectId': config['projectid'], 'timestamp': timestamp, 'fileName': fileName, 'scanner': scanner}
        resp = requests.get(SKEN_SERVER_BASE_URL + "/cli/doETL", params=payload)
        etl_result = resp.json()

        if not etl_result['success']:
            print(etl_result['message'])
            exit(0)
    except Exception as e:
        print('Failed to trigger ETL.')
        logging.exception(e)
        exit(0)

    print('ETL Succeeded')

def main():
    parser = argparse.ArgumentParser(description='Sken Runner.')
    parser.add_argument('-s', '--scanner', metavar='scanner', choices=SCANNERS, help='support scanners: ' + ','.join(SCANNERS))
    parser.add_argument('-l' ,'--lang', metavar='language', choices=LANGUAGES, help='support languages: ' + ','.join(LANGUAGES))
    parser.add_argument('-p' ,'--path', metavar='project path', help='path of the project to be scanned.')
    global parsed_args
    parsed_args = parser.parse_args()

    read_config()
    get_scan_info()
    select_scanner()

# todo: more error handling needed
if __name__ == "__main__":
    main()
