import os
import sys
from datetime import datetime
import subprocess
import threading
from hashlib import sha256
import random
import string

class Box(object):
    def __init__(self, config):
        self.filename = sha256((datetime.now().strftime("%Y%m%d%H%M%S")+config['filename']).encode('utf-8')).hexdigest()[-30:]+'_'+''.join(random.sample(string.ascii_letters + string.digits, 8))
        self.box_name = self.filename[:-3]
        # user's code
        self.code = config['code']
        # std_input
        self.input = config['input']
        self.input_name = 'input_' + self.filename[:-3]
        self.memory = config['memory']
        self.timeout = config['timeout']
        self.type = config['type']
        self.dependency = config['dependency']
        self.cpu = config['cpu']
        self.pids_limit = config['pids_limit']
        self.host_path = config['host_path']
        self.container_path = config['container_path']
        self.image = config['image']

    def check_path_exist(self):
        assert os.path.exists(self.host_path), f'Path {self.host_path} not found'
        return True

    def prepare(self):
        if self.check_path_exist():
            # code file
            with open(self.host_path+'/'+self.filename, 'w') as f:
                f.write(self.code)
            # challenge input
            if self.input:
                with open(self.host_path+'/'+self.input_name, 'w') as f:
                    f.write(self.input)
        return 'create file success'

    def run(self):
        #TODO: create code file
        self.prepare()
        #TODO: docker run parameters
        cmd = (
            f"sudo /usr/bin/docker run --rm -i "
            f"--memory {self.memory} "
            f"--cpus {self.cpu} "
            f"--pids-limit {self.pids_limit} "
            f"-v {self.host_path}:{self.container_path} "
            f"--name {self.box_name} "
        )
        if self.input:
            cmd = cmd + f"{self.image} /bin/sh -c \"cat /tmp/{self.input_name} | {self.type} /tmp/{self.filename}\"" # cat "/tmp/inputname | python3 "/tmp/filename"
        else:
            cmd = cmd + f"{self.image} {self.type} /tmp/{self.filename}" # python3 "/tmp/filename"
        
        def kill_docker():
            nonlocal timeout_flag
            try:  # catch race 
                timeout_flag = True
                subprocess.check_output(f"/usr/bin/docker kill {self.box_name}", stderr=subprocess.STDOUT, shell=True)
            except:
                return "are you kidding me?"
        timeout_flag = False

        t = threading.Timer(self.timeout, kill_docker)
        t.start()
        return_job = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, check=False)
        stdout = return_job.stdout
        stderr = return_job.stderr
        # clear file
        os.system(f"rm {self.host_path}/{self.filename}")
        if self.input:
            os.system(f"rm {self.host_path}/{self.input_name}")
        try: # container killed 
            t.cancel()
        except:
            pass
        if timeout_flag: # timeout
            return {"stdout": 'timeout! maybe you forget to stop a loop', "stderr": ""}, self.filename # 超时
        return {"stdout": stdout.decode().strip(), "stderr": stderr.decode().strip()}, self.filename  # 正常或运行出错

    def clear_file(self):
        return f"rm {self.host_path}/{self.filename}"
        os.system(f"rm {self.host_path}/{self.filename}")
        if self.input:
            os.system(f"rm {self.host_path}/{self.input_name}")

