import os
import pickle
import sys
import webbrowser
import stalk

from datetime import datetime
from requests import get
from vk_api import BadPassword
from vk_api import VkApi
from time import sleep
from vk_api.exceptions import ApiError, Captcha


FIRST_OP = 1
HELLO_MESS = '''
~####~~~######~~~####~~~##~~~~~~##~~##
##~~~~~~~~##~~~~##~~##~~##~~~~~~##~##
~####~~~~~##~~~~######~~##~~~~~~####
~~~~##~~~~##~~~~##~~##~~##~~~~~~##~##
~####~~~~~##~~~~##~~##~~######~~##~~##

##~~##~~##~~##
##~~##~~##~##
##~~##~~####
~####~~~##~##
~~##~~~~##~~##
'''

arb_dir = ''


class Beobachtung:
    def __init__(self, login, password, us_id) -> VkApi:
        self.vk_session = VkApi(login, password)
        self.vk_session.auth()
        self.user_id = us_id
        self.vk = self.vk_session.get_api()

    def color(self, text, clr):
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGNETA = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        GREY = '\033[90m'
        BOLD = '\033[1m'
        ITALIC = '\033[3m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

        if clr == 'red':
            return RED + text + END
        elif clr == 'green':
            return GREEN + text + END
        elif clr == 'yellow':
            return YELLOW + text + END
        elif clr == 'blue':
            return BLUE + text + END
        elif clr == 'magneta':
            return MAGNETA + text + END
        elif clr == 'cyan':
            return CYAN + text + END
        elif clr == 'white':
            return WHITE + text + END
        elif clr == 'grey':
            return GREY + text + END
        elif clr == 'bold':
            return BOLD + text + END
        elif clr == 'italic':
            return ITALIC + text + END
        elif clr == 'underline':
            return UNDERLINE + text + END
        else:
            raise WrongCollor


class WrongCollor(Exception):
    pass


def upd_str(mess: str):
    print(" " * 100, end='')
    print('\r' + str(mess), end='')


def get_info(a: Beobachtung):
    fields = 'online,last_seen,counters,is_favorite,photo_max_orig,status'
    data = a.vk.users.get(user_id=a.user_id, name_case='abl', fields=fields)[0]
    print('{:_^50}'.format('Информация о ' + data['first_name'] + ' ' + data['last_name']))
    print('ID: {}'.format(data['id']))
    if data['online']:
        print('Состояние: ' + a.color('Online', 'green'))
    else:
        print('Состояние: ' + a.color('Offline', 'red'))
        print('Последнее посещение: ' + datetime.fromtimestamp(int(data['last_seen']['time'])).strftime('%Y-%m-%d %H:%M:%S'))
    print('Статус: '+data['status']) if not data['status'] == '' else print(end='')
    groups = a.vk.groups.get(user_id=a.user_id)
    if groups['count'] < 30:
        group_info_list = [a.vk.groups.getById(group_id=group) for group in groups['items']]
        print('Группы '+str(groups['count'])+':')
        for group_name in group_info_list:
            print('------- ' + group_name[0]['name'])
    else:
        print("Слишком много групп! Всего " + str(groups['count']))


def get_photo(obj: Beobachtung):
    os.chdir(arb_dir+'/AppData_vk')
    try:
        os.mkdir('photo')
    except FileExistsError:
        pass
    i = 0
    list_photos = obj.vk.photos.getAll(owner_id=obj.user_id, count=200)
    c = list_photos['count']
    list_photos = list_photos['items']
    for url in list_photos:
        con = get(url['sizes'][-1]['url']).content
        with open('./photo/'+str(i)+'.jpg', 'wb+') as ph:
            ph.write(con)
        i += 1
    print('\nЗавершено!')


def like(obj: Beobachtung):
    vk = obj.vk
    ph = vk.photos.getAll(owner_id=obj.user_id, count=200)
    print('Всего фото: '+str(ph['count']))
    print('ВНИМАНИЕ! Максимальное кол-во фото, которые можно пролайкать, огрничивается всего 50.')
    max = ph['count'] if ph['count'] <= 50 else 50
    for i in range(0,50):
        c_like = vk.likes.add(type='photo', owner_id=obj.user_id, item_id=ph['items'][i]['id'])['likes']
        upd_str('{}/{} {}'.format(i+1, max, c_like))
    print('')


def main():
    global FIRST_OP
    if FIRST_OP:
        print(HELLO_MESS)
        FIRST_OP = 0
    global arb_dir
    try:
        try:
            arb_dir = os.path.expanduser('~')
            os.chdir(arb_dir)
            auth_status = input('Вы уже авторизировались?(y/n): ')
            if auth_status.upper() == 'N':
                print('''
                        Сейчас в папке \'AppData_vk\' будет создан конфигурационный файл.
                        Если не хотите еще раз вводить данные, то, пожалуйста, не удаляйте его.
                ''')
                login = input('Login > ')
                password = input('Password > ')
                id_vk = input('ID для наблюдения > ')
                base = {'login': login, 'password': password, 'id_vk': id_vk}
                try:
                    os.mkdir('AppData_vk')
                except OSError:
                    pass
                os.chdir('AppData_vk')
                try:
                    os.remove(os.getcwd() + '/vk_config.v2.json')
                except FileNotFoundError:
                    pass
                with open('vk_db.cfg', 'wb') as vk_db:
                    pickle.dump(base, vk_db)
            elif auth_status.upper() == 'Y':
                os.chdir('AppData_vk')
                with open('vk_db.cfg', 'rb') as vk_db:
                    base = pickle.load(vk_db)
                login = base['login']
                password = base['password']
                id_vk = base['id_vk']
            else:
                main()
        except KeyboardInterrupt:
            sys.exit()
        except FileNotFoundError:
            print('Не найден файл конфигурации, запустите приложение с параметром \'n\'')
            os.chdir(arb_dir)
            main()
            sys.exit()
        try:
            b = Beobachtung(login, password, id_vk)
        except BadPassword:
            print('Ошибка авторизации. Повторите ввод данных')
            os.chdir(arb_dir)
            main()
            sys.exit()
        print('Для помощи введите help')
        while True:
            command = input('> ').upper()
            if command == 'HELP':
                print('''
                photo - скачать фотографии объекта
                get_inf - получить информацию об объекте
                data - данные авторизации
                id_r - изменить ID наблюдения
                e - выход из программыv
                clear - отчистить панель
                page - открыть страницу ВК в браузере
                vers- версия программы
                like - поставить лайки на все фотографии(max = 50)
                ''')
            elif command == 'PHOTO':
                get_photo(b)
            elif command == 'DATA':
                print('Login: {}\nPassword: {}\nID объекта: {}'.format(login, password, b.user_id))
            elif command == 'E':
                sys.exit()
            elif command == 'ID_R':
                base['id_vk'] = b.user_id = input('Введите новый ID > ')
                with open('vk_db.cfg', 'wb') as vk_db:
                    pickle.dump(base, vk_db)
            elif command == 'GET_INF':
                get_info(b)
            elif command == 'CLEAR':
                os.system('clear')
            elif command == 'PAGE':
                webbrowser.open_new_tab('https://vk.com/id'+id_vk)
            elif command == 'VERS':
                print(stalk.__version__)
            elif command == 'LIKE':
                like(b)
            else:
                print('Неизвестная команда '+command)
    except KeyboardInterrupt:
        print()
        sys.exit()
    except ApiError:
        print('VK error!')
    except Captcha:
        print('VK требует ввод капчи. Подождите некоторое время и потом можете продолжить')


if __name__ == '__main__':
    try:
        os.system('clear')
    except Exception:
        os.system('clr')
    main()
