import os
import docker
from .docker_util import docker_login, docker_pull_image, get_timestamp

def run_sast_scanner(params):
    client = docker_login(params['scan_info'])
    scanner = params['scanner']
    build_dir = params['build_dir']
    print('Launching scanner %s ' % scanner)

    output_file = build_dir + 'sken-'+scanner+'-output.json'

    docker_image = ''
    if scanner == 'brakeman':
        docker_image = 'nixsupport/brakeman:v4'
    elif scanner == 'nodejsscan': 
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/nodejsscan:latest'       
    elif scanner == 'gosec':
        docker_image = 'nixsupport/gosec:v2'
    elif scanner == 'banditpy2':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/bandit-python2:latest'
    elif scanner == 'banditpy3':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/bandit-python3:latest'
        output_file = build_dir + 'sken-bandit3-output.json'
    elif scanner == 'findsecbugs':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/findsecbugs:latest'
        output_file = build_dir + 'sken-secbugs-output.xml'

    print('Pulling latest image for %s ' % scanner)
    docker_pull_image(client, docker_image)
    print('Scanning started')
    scan_start = get_timestamp()
    container = client.containers.run(docker_image, volumes={build_dir: {
                                          'bind': '/scan', 'mode': 'rw'}}, detach=True, tty=False, stdout=True)
    container.wait()
    scan_end = get_timestamp()
    print('Scanning completed. Output file: ' + output_file)
    
    return output_file, scan_start, scan_end
