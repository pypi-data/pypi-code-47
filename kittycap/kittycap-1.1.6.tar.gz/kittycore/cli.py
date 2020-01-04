from .kittycap import KittyCap, KittyWait
import time
import sys
import argparse
import appdirs
import os
import requests
import re 

session_path = None
app_path = None
def banner():
    print('''
         _   __    _    _           _____   ___  ______ 
        | | / /( )| |  | |         /  __ \ / _ \ | ___ \\
        | |/ /  _ | |_ | |_  _   _ | /  \// /_\ \| |_/ /
        |    \ | || __|| __|| | | || |    |  _  ||  __/ 
        | |\  \| || |_ | |_ | |_| || \__/\| | | || |    
        \_| \_/|_| \__| \__| \__, | \____/\_| |_/\_|    
                            __/ |                     
                            |___/                    
                    < KittyCap-CLI v1.1.6 >
    ''')


def arg_credit(args):
    kittycore = login()
    credit = kittycore.credit()
    try:
        print(f'\t[+] Your credit is {credit}\n')
    except Exception as error:
        print(f'\t[-] Error : {error}\n')

def arg_recaptcha(args):
    if not args.sitekey:
        print(f'\t[~] Trying to get target website google sitekey automatically...')
        response_html = requests.get(args.url).content
        try:
            site_key = re.search('data-sitekey="(.+?)"', str(response_html)).group(1)
            print(f'\t[+] Target website google sitekey is {site_key}')
        except:
            print(f'\t[-] Automatically getting sitekey failed.')
            site_key = input('\t[+] Please input target website google sitekey : ')
    else:
        site_key = args.sitekey
    
    try:
        kittycore = login()
        kitty_ticket = kittycore.recaptcha2(site_key, args.url)
    except Exception as error:
        print(f'\t\t [-] {error}')
        sys.exit()

    print(f'\t[+] Kitty Ticket : {kitty_ticket}')

    sleep_time = 10
    print(f'\t[+] Getting Ticket Response ...')

    print(f'\t\t[~] Waiting for kitty response key being ready...')
    time.sleep(sleep_time * 2.5)

    retry = True
    while retry:
        try:
            kitty_ticket_response = kittycore.get_ticket_response(kitty_ticket)
            print(f'\t\t[+] Kitty Response Key : {kitty_ticket_response}')
            retry = False
        except KittyWait:
            time.sleep(sleep_time)

def arg_login(args):
    try_login = login(args.username, args.api_key)
    if try_login == True:
        print('\t[+] You have successfully signed in kittycap.')
    else:
        print(f'\t[-] {try_login}')

def login(username=None, api_key=None):
    if username:
        kittycore = KittyCap(username, api_key)
        if kittycore.is_authenticated:
            with open(session_path, 'w+') as session_file:
                session_file.write(f'{username},{api_key}')
            return True
        else:
            return kittycore.error
    else:
        if not os.path.exists(session_path):
            print('\t[-] Session not found please login again.')
            sys.exit()
        else:
            with open(session_path, 'r') as session_file:
                username, api_key = str(session_file.read()).split(',')
            kittycore = KittyCap(username, api_key)
            if kittycore.is_authenticated:
                return kittycore
            else:
                print(f'\t[-] {kittycore.error["message"]}')
                if kittycore.error['code'] == 403:
                    try:
                        os.remove(session_path)
                    except:
                        pass
                sys.exit()

def arg_logout(args):
    try_logout = logout()
    if try_logout == True:
        print('\t[+] You have successfully signed out.')
    else:
        print(f'\t[-] Problem occurred in removing session, please try login again.')

def logout():
    try:
        os.remove(session_path)
        return True
    except:
        return False

def main():
    global session_path, app_path
    try:
        banner()

        app_path = appdirs.user_data_dir('KittyCap','KittyApps')
        session_path = os.path.join(app_path, 'session')

        if not os.path.exists(app_path):
            os.makedirs(app_path)
        
        # parser
        cli_parser = argparse.ArgumentParser(prog='kittycap', description='KittyCap cli.')
        cli_subparsers = cli_parser.add_subparsers()

        login_command = cli_subparsers.add_parser('login')
        login_command.add_argument('username')
        login_command.add_argument('api_key')
        login_command.set_defaults(func=arg_login)

        recaptcha_command = cli_subparsers.add_parser('recaptcha')
        recaptcha_command.add_argument('url')
        recaptcha_command.add_argument('--sitekey', nargs=1, metavar=('sitekey'))
        recaptcha_command.set_defaults(func=arg_recaptcha)

        logout_command = cli_subparsers.add_parser('logout')
        logout_command.set_defaults(func=arg_logout)

        credit_command = cli_subparsers.add_parser('credit')
        credit_command.set_defaults(func=arg_credit)

        if len(sys.argv) <= 1:
            sys.argv.append('--help')

        # Execute parse_args()
        args = cli_parser.parse_args()
        args.func(args)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()