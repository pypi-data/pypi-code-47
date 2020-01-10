#!/usr/bin/env python3

import json
import sys
import os
from time import sleep


def main():
    if len(sys.argv) != 4:
        raise Exception('Specify URL, IP, and Port.')
    try:
        url = sys.argv[1]
        if len([int(x) for x in sys.argv[2].split('.')]) == 4:
            sip = sys.argv[2]
        spp = int(sys.argv[3])
    except Exception:
        raise Exception('Specify URL, IP, and Port.')

    try:
        runtime = 10
        timedout = False
        tcp_res = os.system('nc -z {} {}'.format(sip, spp))
        while tcp_res != 0:
            runtime = runtime - 1
            if not runtime:
                timedout = True
                break
            sleep(1)
            tcp_res = os.system('nc -z {} {}'.format(sip, spp))
    except Exception:
        tcp_res = 1
        timedout = False

    curl_data = [
        'content_type', 'http_code', 'num_connects', 'num_redirects', 'redirect_url',
        'remote_ip', 'remote_port', 'size_header', 'size_request', 'ssl_verify_result'
    ]
    try:
        if tcp_res == 0:
            for item in curl_data:
                tcp_res = os.system('curl --connect-timeout 2 -m 5 -s -o /dev/null -w "{}" {}'.format(
                    '%{' + item + '}', url
                ))
    except Exception:
        pass

    test_vars = {
        'tcp': tcp_res == 0,
        'timeout': timedout,
    }

    print(json.dumps(test_vars))
    sys.exit(0)


if __name__ == "__main__":
    main()
