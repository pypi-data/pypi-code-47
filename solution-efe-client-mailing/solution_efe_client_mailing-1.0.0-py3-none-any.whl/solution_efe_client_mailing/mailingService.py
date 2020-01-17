import socket
import json
from solution_efe_config import configConstants

CLIENT_MAILING=configConstants.CLIENTS['mailing']

def mailingServiceSendMessage(data):
    try:
        event = {'event':'mail-service-send-message','data': data}
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((CLIENT_MAILING['host'], CLIENT_MAILING['port']))
            sock.sendall(bytes(json.dumps(event) + "\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")
        response=json.loads(received)
        return {'status': response['status']}  
    except Exception as e:
        return {'status': False,'data':str(e)}

def mailServiceSendMessageCreatePassword(data):
    try:
        event = {'event':'mail-service-send-message-create-password','data': data}
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((CLIENT_MAILING['host'], CLIENT_MAILING['port']))
            sock.sendall(bytes(json.dumps(event) + "\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")
        response=json.loads(received)
        return {'status': response['status']}  
    except Exception as e:
        return {'status': False,'data':str(e)}

def mailServiceSendMessageRecoveryPassword(data):
    try:
        event = {'event':'mail-service-send-message-recovery-password','data': data}
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((CLIENT_MAILING['host'], CLIENT_MAILING['port']))
            sock.sendall(bytes(json.dumps(event) + "\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")
        response=json.loads(received)
        return {'status': response['status']}  
    except Exception as e:
        return {'status': False,'data':str(e)}
