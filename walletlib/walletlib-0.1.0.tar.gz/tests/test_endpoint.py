import requests
import random
from typing import Dict
import json
import time

apikeys = ["55531b01ed804d7e8ac642fed5586b62",
"026ef6b032f24670969621c3c50f292c",
"2fb5bd3c929741f9a67be3be85b3e161"]


def check_doge(key):
    r = requests.get("https://api.blockcypher.com/v1/doge/main/addrs/" + key + "/full", params={"token": random.choice(apikeys)})
    print(r.text)
    time.sleep(1)
    if r.status_code is not 429:
        if "n_tx" in r.json().keys():
            if r.json()["n_tx"] > 0:
                return r.json()
            else:
                return None
        else:
            return None
    else:
        r = requests.get("http://dogechain.info/chain/Dogecoin/q/addressbalance/" + key)
        print(r.text)
        if float(r.text) > 0:
            return r.text
        else:
            return None


with open("../user/dogeewallet.txt", "r") as fq:
    for line in fq:
        line = line.strip()
        l = line.split(":")
        t = check_doge(l[0])

        if t is not None:
            with open("kd.txt", "a") as fz:
                if isinstance(t, Dict):
                    t["privkey"] = l[1]
                    fz.write(json.dumps(t) + "\n")
                else:
                    fz.write(l[0] + ":" + l[1] + "-" + t + "\n")








