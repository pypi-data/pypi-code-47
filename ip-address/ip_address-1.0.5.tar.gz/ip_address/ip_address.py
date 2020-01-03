import requests

def get():
    try:
        ip = requests.get("https://ident.me")

        if ip != "" or ip != None:
            return ip

    except:
        pass
