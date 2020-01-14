import sys

import os
import tempfile
from argparse import ArgumentParser
from subprocess import check_output, call, PIPE

systemd_file = '''
[Unit]
Description=Key frequency analyzer
After=syslog.target network.target multi-user.target

[Service]
Type=simple
ExecStart={executable_command} {json_file} --write-freq {write_freq} --min-presses {min_presses}
Restart=always
RestartSec=30

[Install]
WantedBy=default.target
'''
out_file = '/etc/systemd/user/kefrey.service'


def main():
    parser = ArgumentParser(description="A simple script to install a systemd service file")
    parser.add_argument('--json-file-location', default='~/.kefrey.json', help='Json file location')
    parser.add_argument('--write-freq', type=float, default=1, help='Minutes between writes')
    parser.add_argument('--min-presses', type=float, default=20,
                        help='Minimum number of presses before a write can occur')
    args = parser.parse_args()

    user = check_output('who').decode().split()[0]
    data = systemd_file.format(
        **vars(args), user=user, json_file=args.json_file_location.replace('~', '/home/' + user),
        executable_command='{} -m kefrey'.format(sys.executable)
    )

    run_user = os.environ.get('USER')
    with tempfile.NamedTemporaryFile('w') as tf:
        tf.write(data)
        tf.flush()
        if run_user and run_user != 'root':
            print('Install script needs root to write to {out_file}.'.format(out_file=out_file))
            print('Running with sudo...')
            sudo_arg = ['sudo']
        else:
            sudo_arg = []
        call(sudo_arg + ['cp', tf.name, out_file])
        call(sudo_arg + ['chmod', '644', out_file])
        call(sudo_arg + ['systemctl', 'daemon-reload'])

    print('Service successfully installed at {out_file}.'.format(out_file=out_file))
    print()
    print('Enable service with "systemctl enable --user kefrey"')
    print('Start service with "systemctl start --user kefrey"')
    print()
    print('Service will log to {}'.format(args.json_file_location))


if __name__ == '__main__':
    main()
