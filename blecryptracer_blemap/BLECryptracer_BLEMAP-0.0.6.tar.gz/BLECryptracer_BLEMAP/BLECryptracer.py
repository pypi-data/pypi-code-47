import argparse
import json
from common import hash
from common import constants
from getvalue import worker_getvalue as getvalue
from setvalue import worker_setvalue as setvalue
from uuids import worker_uuid

VERSION_NUMBER = '0.1'

argparser = argparse.ArgumentParser(
    description='BLE-Cryptography Analysis')

argparser.add_argument(
    '-i',
    '--apk',
    required=True,
    help='File with UUID data')

argparser.add_argument(
    '-o',
    '--output',
    default='output.json',
    help='path to output file')


def analyse_file(apk, output):
    result = {}
    print('Calculating Hash...')
    result.update({constants.SHA256: hash.sha256sum(apk)})
    print('Analysing BLE Writes...')
    result = setvalue.WorkerSetvalue().analyse_apk(filename=apk)
    print('Analysing BLE Reads...')
    result.update(getvalue.WorkerGetvalue().analyse_apk(filename=apk))
    print('Extracting Bluetooth UUIDs from APK...')
    result.update(worker_uuid.main(apk))
    print('Finishing up...')
    result.update({constants.VERSION: VERSION_NUMBER})
    with open(output, "w") as file:
        file.write(json.dumps(result, indent=4))
    print('Finished Execution')


def main():
    args = argparser.parse_args()
    analyse_file(args.apk, args.output)


if __name__ == '__main__':
    main()
