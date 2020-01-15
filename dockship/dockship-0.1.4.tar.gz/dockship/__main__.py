#!/usr/bin/env python3.6

"""
Usage:
------

    $ dockship [option] [modelID]

  Run model in docker container:

    $ dockship run <modelID> <port> (optional)

    where <modelID> is model's unique ID taken from https://dockship.io

  Stop already running model:

    $ dockship stop <modelID>


Contact:
--------

- Mail us at contact@dockship.io
- Chat with us on website.

"""

import fire
import requests
from requests.exceptions import Timeout
from getpass import getpass
import os
import tqdm
import shutil
import subprocess
import zipfile
import json
from pathlib import Path
from alive_progress import alive_bar

def run( modelID, port='5381' ):
  """
  Main function for running Dockship models.

  Args:
      modelID (string) : Model's unique id shown at dockship.io
      port (string)    : Port number for running model
  """
  print("\
             _            _        _     _\n\
  __| | ___   ___| | _____| |__ (_)_ __\n\
 / _` |/ _ \ / __| |/ / __| '_ \| | '_ \\ \n\
| (_| | (_) | (__|   <\__ \ | | | | |_) |\n\
 \__,_|\___/ \___|_|\_\___/_| |_|_| .__/\n\
                                  |_|\n\
        ")
  # Check if docker exists
  try:
    if shutil.which('docker') is None:
      raise RuntimeError("Docker not installed. To install run commands - \n\
      ` sudo apt-get update && \n \
       sudo apt install docker.io && \n \
       sudo systemctl start docker && \n \
       sudo systemctl enable docker` ")

  except Exception as err_msg:
    print(err_msg)
    exit(0)

  # Create configuration file containing API key if does not already exists.
  confPath = Path.home() / '.dockship/config'
  if not confPath.is_file() or (confPath.is_file() and os.path.getsize(confPath) == 0):
    confPath.parent.mkdir(parents=True, exist_ok=True)
    confPath.touch(exist_ok=True)
    APIkey = getpass("Your API key: ")
    with confPath.open('w') as confFile:
      confFile.write("APIkey: "+ APIkey)

  with confPath.open('r') as confFile:
    APIkey = confFile.readline().split()[-1]

  # Verify APIkey by server and get URL for downloading model.
  try:
    headers = {"apikey": APIkey}
    payload = {'modelID': modelID}
    resp = requests.request('GET', 'https://atlas-server.dockship.io/api/downloadModelByID',
                            headers = headers, data = payload,
                            allow_redirects = False, timeout=5)

    if resp.status_code == 200:
      modelInfo = resp.json()
      modelName = modelInfo["modelname"]
      modelLink = modelInfo["url"]
      modelName = modelName.replace(" ", "").lower()

    elif resp.status_code == 400:
      print("Incorrect API key. Please retry with correct API key.")
      os.remove(confPath)
      exit(0)

    else:
      print(f"Error occured: {resp.json()['message']}")
      exit(0)

  except Timeout:
    print("Request Timed Out. Please retry. If probleme persists, contact us.")
    exit(0)

  except Exception as err:
    # TODO: Send Bug report to Dockship
    print(f'{err}. Seems like our code broke (-_-;) . Please contact us.')
    exit(0)

  # If model is not already downloaded, download and unzip.
  modelPath = Path.home() / '.dockship/Models'
  if not (modelPath / modelID).is_dir():
    zipPath = modelPath / f'{modelID}.zip'
    try:
      print('-'*12, f" Downloading '{modelName}' model ", '-'*12, sep='')
      with requests.get(modelLink, stream=True) as r:
        file_size = int(r.headers.get('content-length',0))
        chunk, chunk_size = 1, 1024
        num_bars = int(file_size / chunk_size)
        zipPath.parent.mkdir(parents=True, exist_ok=True)
        zipPath.touch()
        with zipPath.open('wb') as f:
          for chunk in tqdm.tqdm(
                              r.iter_content(chunk_size=chunk_size)
                              , total= num_bars
                              , unit = 'KB'
                              , desc = str(zipPath)
                              , leave = True # progressbar stays
                              ):
            f.write(chunk)
    except Exception as err:
      # TODO: Send Bug report to Dockship
      print(f'{err}. Seems like our code broke (-_-;) . Please contact us.')
      exit(0)

    with zipfile.ZipFile(zipPath, 'r') as zip_ref:
      zip_ref.extractall(modelPath / modelID)
      os.remove(zipPath)

  dir = os.listdir(modelPath / modelID)[0]
  os.chdir(modelPath / modelID / dir)

  # Creating following files -
  #   info.json - Containing information about model.
  #   dockship_launch.py - For running flask code
  #   wsgi.py - For gunicorn

  with open('info.json', 'w') as f: json.dump(modelInfo, f)
  temp_url = "https://gist.github.com/i-amgeek/cf181dcf9f8a5611f72c2c73c65c5795/raw/dockship_launch.py"
  launch_file = requests.get(temp_url).text.replace("56733", port)
  with open('dockship_launch.py', 'w') as file:
    file.write(launch_file)
  temp_url = "https://gist.github.com/i-amgeek/e01a929e1d1882e5d8142a5bad409f3e/raw/wsgi.py"
  wsgi_file = requests.get(temp_url)
  with open('wsgi.py', 'w') as file:
    file.write(wsgi_file.text)

  # Add hosting information in Dockerfile
  dockerfile_by_model_provider = open("Dockerfile", 'r').read()
  dockerfile_by_dockship = f'\nEXPOSE {port} \n\
RUN pip3 install dockship gunicorn Flask==1.1.1\n\
CMD ["gunicorn","--workers", "3", "-b", "0.0.0.0:{port}", "wsgi:app"]\n'
  dockerfile = dockerfile_by_model_provider + dockerfile_by_dockship
  with open("Dockerfile", "w") as file:
    file.write(dockerfile)

  with open("requirements.txt", "a") as file:
    file.write("\ndockship")

  # Build docker image- {modelName} and run docker container- {modelID}_app
  password = getpass("Password for Sudo: ")
  docker_build = f"sudo -S docker build -t {modelName} -f Dockerfile . "
  docker_run = f"sudo -S docker run -dp {port}:{port} --name {modelID}_app {modelName}"
  result = os.popen(f"echo {password} | sudo -S docker ps -a").read()
  if f"{modelID}_app" in result:
    result = os.popen(f"echo {password} | sudo -S docker start {modelID}_app").read()
  else:
    with alive_bar() as bar:
      print("Docker Image building. It may take some time")
      result = os.popen(f"echo {password} | {docker_build}").read()
      bar()

    if "Successfully tagged" in result:         # TODO: Use returncode instead
        print("Docker image built successfully")
    else:
        print(f"{result} \nDocker image couldn't be built")
        exit(0)
    try:
        result = os.popen(f"echo {password} | {docker_run}").read()
    except:
        print(f"{result} \nDocker container couldn't initiate successfully")
        exit(0)


def stop(modelID):
  password = getpass("Password for sudo: ")
  try:
    result = os.system(f"echo {password} | sudo -S docker stop {modelID}_app")
    print(f"Container with ModelID - {modelID} stopped successfully.")
  except:
    print("Can't stop container.")


def main():
  fire.Fire({"run":run,
              "stop":stop})

if __name__ == '__main__':
  main()
