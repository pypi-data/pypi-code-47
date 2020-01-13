import logging

from events.events_manager import EventsManager

logger = logging.getLogger(__name__)


class EventStack:
    eventsManager = EventsManager()

    def __init__(self):
        self.EVENTS_TEST = self.eventsManager.get_event('events.test', 'События.Test', compulsory_reading=True)

        self.EVENTS_UPLOAD_PDF_NEW = self.eventsManager.get_event('events.upload.pdf.new', 'События.Закачка.PDF.Новый', compulsory_reading=True)
        self.EVENTS_UPLOAD_PDF_MODIFIED = self.eventsManager.get_event('events.upload.pdf.modified', 'События.Закачка.PDF.Исправленный', compulsory_reading=True)
        self.EVENTS_UPLOAD_KOMPAS_NEW = self.eventsManager.get_event('events.upload.kompas.new', 'События.Закачка.КОМПАС.Новый', compulsory_reading=True)
        self.EVENTS_UPLOAD_KOMPAS_MODIFIED = self.eventsManager.get_event('events.upload.kompas.modified', 'События.Закачка.КОМПАС.Исправленный', compulsory_reading=True)

        self.EVENTS_PRODUCTION_READY_2_LAUNCH = self.eventsManager.get_event('events.production.ready2Launch', 'События.Производство.Выполнен расчет готовности к запуску', compulsory_reading=False)

        self.EVENTS_PRODUCTION_MAKE_LAUNCH = self.eventsManager.get_event('events.production.launch.make', 'События.Производство.Запуск.Формирование', compulsory_reading=True)
        self.EVENTS_PRODUCTION_RE_MAKE_LAUNCH = self.eventsManager.get_event('events.production.launch.remake', 'События.Производство.Запуск.Переформирование', compulsory_reading=True)
        self.EVENTS_PRODUCTION_DELETE_LAUNCH = self.eventsManager.get_event('events.production.launch.delete', 'События.Производство.Запуск.Удаление', compulsory_reading=True)
        self.EVENTS_PRODUCTION_CHANGE_LAUNCH = self.eventsManager.get_event('events.production.launch.chancge_status', 'События.Производство.Запуск.Изменение статуса', compulsory_reading=True)
        self.EVENTS_PRODUCTION_CHANGE_ITEM = self.eventsManager.get_event('events.production.launch.chancge_item', 'События.Производство.Запуск.Изменение товарной позиции', compulsory_reading=True)
        self.EVENTS_PRODUCTION_ADD_ITEM = self.eventsManager.get_event('events.production.launch.add_item', 'События.Производство.Запуск.Добавление товарной позиции', compulsory_reading=True)
        self.EVENTS_PRODUCTION_DELETE_ITEM = self.eventsManager.get_event('events.production.launch.delete_item', 'События.Производство.Запуск.Удаление товарной позиции', compulsory_reading=True)

        self.EVENTS_PLANING_CALC_TIMING = self.eventsManager.get_event('events.planing.calc_timing', 'События.Планирование.Расчет временных параметров', compulsory_reading=False)
