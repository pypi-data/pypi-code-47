import os
import yaml

import numpy as np
import pandas as pd

from minio import Minio
from minio.error import ResponseError

def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')

yaml.add_representer(type(None), represent_none)
yaml.Dumper.ignore_aliases = lambda *args : True

lst_file = ['services', 'providers_ingest', 'providers_etl']

def get_config_files_from_Minio():
    MINIO_USERNAME = os.environ.get('MINIO_USERNAME', '')
    MINIO_PASSWORD = os.environ.get('MINIO_PASSWORD', '')
    
    client = Minio('data.teko.vn:9091', access_key=MINIO_USERNAME, secret_key=MINIO_PASSWORD, secure=False)
    
    for filename in lst_file:
        try:
            data = client.get_object('phongvu-prod', f'auto-config/{filename}.csv')
            with open(f'{filename}.csv', 'wb') as file_data:
                for d in data.stream(32*1024):
                    file_data.write(d)
        except Exception as err:
            print(err)
            
            return err
    
    return None

def get_services():
    services = {}
    for index, row in pd.read_csv('services.csv', header=0).iterrows():
        service = row['name']
        services[service] = {}
    
        for field in row.index[1:]:
            if field not in ['username', 'password'] or not pd.isnull(row[field]):
                services[service][field] = row[field]
                
    service_default = os.environ.get('SERVICE', 'minio')
    if service_default == 'minio':
        service_alternate = 'hdfs'
    else:
        service_alternate = 'minio'
                
    return services, service_default, service_alternate

def get_providers():
    providers_ingest = pd.read_csv('providers_ingest.csv', header=0)
    
    providers_etl = pd.read_csv('providers_etl.csv', header=0)
    providers_etl['format'] = 'parquet'
    
    providers = pd.concat([providers_ingest, providers_etl])
    
    return providers

def remove_files():
    for filename in lst_file:
        file_path = f'{filename}.csv'
        
        if os.path.exists(file_path):
            os.remove(file_path)
            
def create_profiles(metadata_default):    
    services, service_default, service_alternate = get_services()
    providers = get_providers()
    
    profiles = {}
    for profile in metadata_default:
        profiles[profile['profile']] = profile
        
    # Get info for all providers in profile default
    for provider_name in profiles['default']['providers'].keys():
        lst_provider = providers[(providers['name'] == provider_name) & (~pd.isnull(providers['path']))]

        if len(lst_provider[lst_provider['service'] == service_default]) != 0:
            service = service_default
        elif len(lst_provider[lst_provider['service'] == service_alternate]) != 0:
            service = service_alternate
        else:
            service = 'mysql'

        provider = lst_provider[lst_provider['service'] == service]

        info_provider = services[service]
        if service == 'mysql':
            info_provider['database'] = provider['path'].values[0]
        else:
            info_provider['path'] = provider['path'].values[0]

        info_provider['format'] = provider['format'].values[0]
        
        profiles['default']['providers'][provider_name] = dict()
        profiles['default']['providers'][provider_name]['service'] = service
        for key in info_provider.keys():
            profiles['default']['providers'][provider_name][key] = info_provider[key]
            
    # Change path for profile test and staging
    for profile in ['test', 'stag']:
        for provider_name in profiles[profile]['providers'].keys():
            if not provider_name in profiles['default']['providers'].keys():
                continue

            profiles[profile]['providers'][provider_name] = dict()

            if profiles['default']['providers'][provider_name]['service'] == 'mysql':
                key_path = 'database'
            else:
                key_path = 'path'

            profiles[profile]['providers'][provider_name][key_path] = profiles['default']['providers'][provider_name][
                key_path].replace('prod/', f'{profile}/')
            
    # Write metadata file
    lst_profile = [None]
    for profile in profiles.keys():
        lst_profile.append(profiles[profile])
        
    return lst_profile

def dump_yaml(lst_profile):
    file_name = 'metadata.yml'
    
    with open(file_name, 'w') as file:
        yaml.dump_all(lst_profile, file, sort_keys=False)
        
    with open(file_name, 'r') as file:
        lines_in = file.readlines()

    lines_out = []
    is_in_keyword = False
    for index, line in enumerate(lines_in):
        if index == 0:
            lines_out.append(line)
            continue

        if lines_in[index - 1].startswith('---'):
            lines_out.append(line)
            continue

        if line.startswith('---'):
            lines_out.append('\n')
            lines_out.append(line)
            continue

        if not line.startswith(' '):
            lines_out.append('\n')
            lines_out.append(line)
            for keyword in ['providers', 'resources', 'loggers']:
                if line.startswith(keyword):
                    is_in_keyword = True
                    break
            continue
        else:
            is_in_key_word = False

        if is_in_keyword and line.startswith('  ') and not line.startswith('   ') and lines_in[index - 1].startswith(
                ' '):
            lines_out.append('\n')
            lines_out.append(line)
            continue

        lines_out.append(line)

    with open(file_name, 'w') as file:
        file.writelines(lines_out)
        
def create_metadata():
    # Get config info
    err = get_config_files_from_Minio()
    if err is not None:
        print("Error getting config files from Minio")
        return
    
    # Read file metadata default
    with open('metadata_default.yml', 'r') as file:
        metadata_default = file.read()
    
    metadata_default = yaml.load_all(metadata_default, Loader=yaml.FullLoader)


    lst_profile = create_profiles(metadata_default)
    
    dump_yaml(lst_profile)
        
    # Remove created csv files
    remove_files()