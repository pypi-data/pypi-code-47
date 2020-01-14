from Spitzer import command


def find(host, nmap):
    for value in nmap[host]['tcp'].items():
        product = value[1]['product']
        version = value[1]['version']

        #check if one is empty
        if product == '':
            continue

        result = command.run(['searchsploit', product, version], True)

        #found no sploits
        if 'Exploits: No Result' in result and 'Shellcodes: No Result' in result:
            continue

        #count found sploits
        count = 0
        for line in result.splitlines():

            if '--------' in line or 'Exploit Title' in line or 'No Result' in line or '(/usr/share/exploitdb/)' in line:
                continue
            else:
                print(line)
                count += 1

        s = ''
        if count > 1:
            s = 's'

        print('[-] Found ' + str(count) + ' exploit' + s + ' for ' + product + ' ' + version +' on ' + host)