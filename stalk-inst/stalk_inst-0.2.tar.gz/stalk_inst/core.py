import requests
import json
import os
import platform


class WrongUserID(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


def get_inf():
    pass



def iniz(user_id:str) -> 'JSON dict':
    req = requests.get('https://instagram.com/{}/?__a=1'.format(user_id))
    if req.status_code == 404:
        raise WrongUserID(user_id)
    inst = dict(json.loads(req.content.decode('utf-8')))['graphql']['user']
    print(
        '''
Name:{}
Status:{}
Username:{}'''.format(inst['full_name'], inst['biography'], inst['username'])
    )
    inst_post = inst['edge_owner_to_timeline_media']
    i = 11 if inst_post['count'] > 10 else inst_post['count']
    for z in range(0, 11):
        print('[{}] {}'.format(z, inst['edge_owner_to_timeline_media']['edges'][z]['node']['display_url']))


def check_OS():
    OS_pl = platform.system()
    global CLEAR
    if OS_pl == 'Linux':
        CLEAR = 'clear'
    elif OS_pl == 'Windows':
        CLEAR = 'CLS'
    

def main():
    check_OS()
    os.system(CLEAR)
    try:
        user_id = input('Введите ID > ')
        iniz(user_id)

    except WrongUserID as e:
        print('Не найден пользователт с ID {}'.format(e.user_id))


if __name__ == '__main__':
    main()