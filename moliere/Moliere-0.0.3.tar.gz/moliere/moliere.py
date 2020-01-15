""" Модуль для работы с PostgreSQL """
import os
import re

import dotenv
import psycopg2
import psycopg2.extras

dotenv.load_dotenv()

class Pgdb:
    """
    Обертка для работы с PGSQL
    """

    def __init__(self):
        self.__connection = None

        # выбор переменных окружения со специальным окончанием
        # применяется для унификации использования в других проектах
        creds = {
            '_'.join(key.split('_')[-2:]):value
            for key, value in os.environ.items()
            if re.search('(DB_NAME|DB_HOST|DB_USER|DB_PWD)$', key)
            }

        # подключение
        self.connect(
            creds['DB_HOST'],
            creds['DB_NAME'],
            creds['DB_USER'],
            creds['DB_PWD']
            )

    def connect(self,
                host,
                db_name,
                user,
                pwd,
                autocommit=True
                ):
        """ Подключение к базе данных """
        try:
            self.__connection = psycopg2.connect(
                host=host,
                dbname=db_name,
                user=user,
                password=pwd)

            self.__connection.autocommit = autocommit
        except psycopg2.Error as exc:
            print(f'===PGDBERR: {exc}')

    def disconnect(self):
        """ Закрытие соединения с БД """
        if self.__connection:
            self.__connection.close()

    def execute(self, query, pars=None):
        """ Исполнение запроса к БД """
        cursor = self.__connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        # Попытка исполнения запроса, в случае ошибки возвращается исключение
        try:
            cursor.execute(query, pars)
        except psycopg2.ProgrammingError as exc:
            print(exc)
            raise exc
        # Попытка получения данных по результатам запроса.
        # Если данных нет (например для DELETE) возвращается None
        try:
            return cursor.fetchall()
        except psycopg2.ProgrammingError as exc:
            if str(exc) != 'no results to fetch':
                print('===PGDBERR: ', exc, '\n', query)
        finally:
            cursor.close()
        return None

DB_OBJ = Pgdb()
