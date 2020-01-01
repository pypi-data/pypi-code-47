import koconf.common as common

from beautifultable import BeautifulTable
from colored import attr, stylize
from pathlib import Path
from tinydb import TinyDB, Query


class DataBaseManager():
    def __init__(self):
        path = Path.home().joinpath('.koconf', 'conference.json')
        is_not_initialized = not path.exists()

        if is_not_initialized:
            path.parent.mkdir(exist_ok=True)
            path.touch(exist_ok=True)

        self.__db = TinyDB(str(path), indent=4, separators=(',', ': '))
        self.__query = Query()

        if is_not_initialized:
            self.refresh()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__db.close()

    def show_by_id(self, _id):
        return self.__format_show(self.__db.search(self.__query['id'] == _id))

    def show_by_title(self, title):
        return self.__format_show(self.__db.search(self.__query['title'].search(title)))

    def show_by_city(self, city):
        return self.__format_show(self.__db.search(self.__query['city'].search(city)))

    def show_by_tag(self, tag):
        return self.__format_show(self.__db.search(self.__query['tag'].search(tag)))

    def show_by_applies(self, applies):
        query = self.__query
        for apply in applies:
            if '<=' in apply:
                query &= (self.__query['apply_end'] <= apply[2:].strip())
            elif '<' in apply:
                query &= (self.__query['apply_end'] < apply[1:].strip())
            elif '>=' in apply:
                query &= (self.__query['apply_start'] >= apply[2:].strip())
            elif '>' in apply:
                query &= (self.__query['apply_start'] > apply[1:].strip())

        return self.__format_show(self.__db.search(query))

    def show_by_applicable(self):
        return self.__format_show(self.__db.search(common.now() < self.__query['apply_start']))

    def show_by_events(self, events):
        query = self.__query
        for event in events:
            if '<=' in event:
                query &= (self.__query['event_end'] <= event[2:].strip())
            elif '<' in event:
                query &= (self.__query['event_end'] < event[1:].strip())
            elif '>=' in event:
                query &= (self.__query['event_start'] >= event[2:].strip())
            elif '>' in event:
                query &= (self.__query['event_start'] > event[1:].strip())

        return self.__format_show(self.__db.search(query))

    def show(self):
        return self.__format_show(self.__db.search(self.__query))

    def clean(self):
        self.__db.remove(self.__query)

    def expire(self):
        self.__db.remove(self.__query['event_end'] < common.now())

    def refresh(self):
        for row in common.request():
            # TODO : Verify 'upsert and update' is better way
            doc = self.__db.get(self.__query['id'] == row['id'])
            if doc is None:
                row.update({'is_remind': False})
                self.__db.insert(row)
            else:
                for key, value in row.items():
                    doc[key] = value
                self.__db.write_back([doc])

    def add_remind(self, _id):
        self.__db.update({'is_remind': True}, self.__query['id'] == _id)

    def remove_remind(self, _id):
        self.__db.update({'is_remind': False}, self.__query['id'] == _id)

    def remind(self):
        return self.__format_remind(self.__db.search(self.__query['is_remind'] == True))

    @staticmethod
    def __format_show(data):
        if not data:
            return 'There is no such event list !'

        table = BeautifulTable(max_width=200)
        table.set_style(BeautifulTable.STYLE_BOX)
        table.column_headers = list(map(
            lambda header: '\n'.join(map(
                lambda row: stylize(row, attr('bold')),
                header.split('\n')
            )),
            [
                '[id] - title\n(tags)',
                'location\n(homepage)',
                'apply period\n(from - to)',
                'event period\n(from - to)',
            ]
        ))

        for row in data:
            table.append_row([
                '[%s] - %s\n(%s)' % (row['id'], row['title'], row['tag']),
                '%s, %s\n(%s)' % (row['address'], row['city'], row['homepage']),
                '%s\n%s' % (row['apply_start'], row['apply_end']),
                '%s\n%s' % (row['event_start'], row['event_end']),
            ])

        return table

    @staticmethod
    def __format_remind(data):
        if not data:
            return 'There is no remind event list !'

        table = BeautifulTable(max_width=200)
        table.set_style(BeautifulTable.STYLE_BOX)
        table.column_headers = list(map(
            lambda header: stylize(header, attr('bold')),
            [
                '[id] - title',
                'homepage',
                'deadline',
            ]
        ))

        now = common.now()
        for row in data:
            if now < row['apply_start']:
                deadline = 'Apply will be started after %s' % (common.difftime(now, row['apply_start']))
            elif now < row['apply_end']:
                deadline = 'You can apply now !'
            elif now < row['event_start']:
                deadline = 'Event will be started after %s' % (common.difftime(now, row['event_start']))
            elif now < row['event_end']:
                deadline = 'You can enjoy event now !'
            else:
                pass

            table.append_row([
                '[%s] - %s' % (row['id'], row['title']),
                row['homepage'],
                deadline,
            ])

        return table
