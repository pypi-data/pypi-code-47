import os
import docker
from .docker_util import docker_login, docker_pull_image, get_timestamp

def run_sca_scanner(params):
    client = docker_login(params['scan_info'])
    variables = params['variables']
    scanner = params['scanner']
    build_dir = params['build_dir']
    data_dir = variables['SCA_DATA_DIR']
    report_dir = variables['SCA_REPORT_DIR']

    if not report_dir.endswith(os.path.sep):
        report_dir = report_dir + os.path.sep

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        os.chmod(data_dir, 0o777)
    
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
        os.chmod(report_dir, 0o777)

    print('Launching scanner %s ' % params['scanner'])

    output_file = report_dir + 'dependency-check-report.json'

    docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/dependency-check:latest'
    print('Pulling latest image for %s ' % scanner)
    docker_pull_image(client, docker_image)
    print('Scanning started')
    scan_start = get_timestamp()
    container = client.containers.run(
        docker_image, 
        volumes={
            build_dir: {'bind': '/scan', 'mode': 'rw'},
            data_dir: {'bind': '/usr/share/dependency-check/data', 'mode': 'rw'},
            report_dir: {'bind': '/report', 'mode': 'rw'}
        }, 
        detach=True, tty=False, stdout=True)
    container.wait()
    scan_end = get_timestamp()
    print('Scanning completed. Output file: ' + output_file)
    
    return output_file, scan_start, scan_end
