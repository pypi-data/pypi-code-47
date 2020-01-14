from time import sleep

import json
import pyxhook
from argparse import ArgumentParser
from os.path import isfile


def main():
    parser = ArgumentParser(description="A tool to track system-wide keypress frequencies")
    parser.add_argument('json_file', help='Json file to write frequency data to')
    parser.add_argument('--write-freq', type=float, default=1, help='Minutes between writes')
    parser.add_argument('--min-presses', type=float, default=20,
                        help='Minimum number of presses before a write can occur')
    args = parser.parse_args()

    if not isfile(args.json_file):
        with open(args.json_file, 'w') as f:
            json.dump({}, f)
    with open(args.json_file) as f:
        freq = json.load(f)

    updates_since_save = 0

    def on_key_press(event):
        nonlocal updates_since_save
        updates_since_save += 1
        freq[event.Key] = freq.get(event.Key, 0) + 1

    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = on_key_press
    new_hook.HookKeyboard()
    new_hook.start()

    try:
        while True:
            if updates_since_save > args.min_presses:
                with open(args.json_file, 'w') as f:
                    json.dump(freq, f)
            sleep(args.write_freq * 60)
    except KeyboardInterrupt:
        print()
    finally:
        if updates_since_save > 0:
            with open(args.json_file, 'w') as f:
                json.dump(freq, f)
        new_hook.cancel()


if __name__ == '__main__':
    main()
