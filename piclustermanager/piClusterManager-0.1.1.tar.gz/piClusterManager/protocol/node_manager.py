import paramiko

class node_manager:
    '''
    exec command on ssh client
    @param self
    @param command - command to execute
    @return stdout form ssh
    '''
    def exec(self, command):
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(command)
        #wait to complete
        return ssh_stdout.read()
    
    '''
    close ssh client
    @param self
    @param command - command to execute
    @return None
    '''
    def close(self):
        self.ssh.close()

    '''
    init ssh client
    @param self
    @param ip
    @param username
    @param password
    @return None
    '''
    def __init__(self, ip, username, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, username=username, password=password)

    '''
    disable send hello
    @param self
    @return None
    '''
    def no_hello(self):
        self.exec("sudo touch /no-hello")

    '''
    set new hostname
    @param self
    @param name - new hostname
    @return None
    '''
    def set_hostname(self, name):
        self.exec("sudo sethostname {}".format(name))

    '''
    reboot ssh server
    @param self
    @return None
    '''
    def reboot(self):
        self.exec("sudo reboot")

    '''
    enable send hello
    @param self
    @return None
    '''
    def yes_hello(self):
        self.exec("sudo rm /no-hello")

    '''
    set new password for pi and root
    @param self
    @param password
    @return None
    '''
    def set_password(self, password):
        self.exec("echo 'pi:{}' | sudo chpasswd".format(password))
        self.exec("echo 'root:{}' | sudo chpasswd".format(password))

    '''
    update node (update && upgrade)
    @param self
    @return None
    '''
    def update(self):
        self.exec("sudo apt update && sudo apt upgrade -y")

    '''
    install docker on node
    @param self
    @return None
    '''
    def docker_install(self):
        self.exec("curl -sSL https://get.docker.com | sudo sh")

    '''
    setup node as docker swarm master
    @param self
    @param out_ip - IP of this node
    @return None
    '''
    def docker_setup_master(self, out_ip):
        self.exec("sudo usermod -aG docker pi")
        self.exec("sudo docker swarm init --advertise-addr {}".format(out_ip))
        return self.exec("sudo docker swarm join-token -q")

    '''
    setup node as docker swarm worker
    @param self
    @param token - join token
    @param master-ip - IP of docker swarm master
    @return None
    '''
    def docker_setup_worker(self, token, master_ip):
        self.exec("sudo docker swarm join --token {} {}:2377".format(token, master_ip))

    '''
    install docker compose on node
    @param self
    @return None
    '''
    def docker_compose_install(self):
        self.exec("sudo apt-get install libffi-dev libssl-dev -y")
        self.exec("sudo apt-get install -y python python-pip -y")
        self.exec("sudo apt-get remove python-configparser -y")
        self.exec("sudo pip install docker-compose")