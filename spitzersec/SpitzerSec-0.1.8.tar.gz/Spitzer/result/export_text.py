from Spitzer.result import  result

def export(path):
    results = result.get_result()
    text = ''

    for host, finds in results:
        text += host + '\n\n'
        if finds['webpages'] != []:
            text += 'Found Webpages'
            for page in finds['webpages']:
                text += page + '\n'

        if finds['findings'] != []:
            for finding in finds['findings']:
                text += '\n' + next(iter(finding)) + '\n'
                text += finding[next(iter(finding))] + '\n'

        text += '======================================================\n'

    f = open(path, 'a+')
    f.write(text)
    f.close()

