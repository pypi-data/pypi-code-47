import logging

from pyqalx.core.adapters.adapter import (
    QalxSignalAdapter,
    QalxUpdateStatusAdapter,
)
from pyqalx.core.entities.worker import Worker
from pyqalx.core.signals import QalxWorkerSignal

logger = logging.getLogger(__name__)


class QalxWorker(QalxSignalAdapter, QalxUpdateStatusAdapter):
    _entity_class = Worker
    signal_class = QalxWorkerSignal

    def list_endpoint(self, *args, __bot_entity, **kwargs):
        """
        Builds the list_endpoint for workers.  This requires the bot_entity
        which will get passed down from the calling method via kwargs.  We
        mangle the name so that we can identify this specific kwarg compared to
        normal filter kwargs
        :param __bot_entity:An instance of ~entities.bot.Bot
        :type __bot_entity:~entities.bot.Bot
        :return:The Worker list endpoint
        """
        bot_endpoint = self.session.bot.detail_endpoint(
            guid=__bot_entity["guid"]
        )
        return f"{bot_endpoint}/{self.entity_class.entity_type}"

    def detail_endpoint(self, guid, *args, __bot_entity, **kwargs):
        """
        Builds the list_endpoint for workers.  This requires the bot_entity
        which will get passed down from the calling method via kwargs.  We
        mangle the name so that we can identify this specific kwarg compared to
        normal filter kwargs
        :param guid:The guid of the Worker
        :type guid:guid
        :param __bot_entity:An instance of ~entities.bot.Bot
        :type __bot_entity:~entities.bot.Bot
        :return:The Worker list endpoint
        """
        # Because the list endpoint expects a mangled name we need to pass
        # the bot_entity through to a mangled parameter.
        bot_endpoint = self.list_endpoint(_QalxWorker__bot_entity=__bot_entity)
        return f"{bot_endpoint}/{guid}"

    def get(self, guid, bot_entity, *args, **kwargs):
        """
        Gets an individual worker.
        :param guid:The guid of the Worker
        :type guid: guid
        :param bot_entity:An instance of ~entities.bot.Bot
        :type bot_entity:~entities.bot.Bot
        """
        # The bot entity is passed through to a mangled parameter as this gets
        # sent to the `detail_endpoint` method in the base `get` method
        return super(QalxWorker, self).get(
            guid, _QalxWorker__bot_entity=bot_entity, *args, **kwargs
        )

    def find(self, bot_entity, *args, **kwargs):
        """
        Finds workers.
        :param bot_entity:An instance of ~entities.bot.Bot
        :type bot_entity:~entities.bot.Bot
        """
        # The bot entity is passed through to a mangled parameter as this gets
        # sent to the `list_endpoint` method in the base `get` method
        return super(QalxWorker, self).find(
            _QalxWorker__bot_entity=bot_entity, *args, **kwargs
        )

    def get_signal(self, entity, bot_entity, *args, **kwargs):
        """
        Gets the signal for a specific entity
        :param entity:An instance of ~entities.worker.Worker
        :type entity:~entities.worker.Worker
        :param bot_entity:An instance of ~entities.bot.Bot
        :type bot_entity:~entities.bot.Bot
        """
        # We don't pass `bot_entity` through to a mangled parameter as
        # `get_signal` calls `get` internally which handles name mangling
        return super(QalxWorker, self).get_signal(
            entity=entity, bot_entity=bot_entity, *args, **kwargs
        )

    def terminate(self, entity, bot_entity, *args, **kwargs):
        """
        Terminates a specific entity
        :param entity:An instance of ~entities.worker.Worker
        :type entity:~entities.worker.Worker
        :param bot_entity:An instance of ~entities.bot.Bot
        :type bot_entity:~entities.bot.Bot
        """
        # Don't pass `bot_entity` through to a mangled parameter as
        # `terminate` calls `get` internally which handles name mangling
        return super(QalxWorker, self).terminate(
            entity=entity, _QalxWorker__bot_entity=bot_entity, *args, **kwargs
        )

    def _stop_or_resume(self, entity, stop, bot_entity, **kwargs):
        """
        Stops or resumes a specific entity
        :param entity:An instance of ~entities.worker.Worker
        :type entity:~entities.worker.Worker
        :param stop:Whether we should stop or resume
        :type stop:bool
        :param bot_entity:An instance of ~entities.bot.Bot
        :type bot_entity:~entities.bot.Bot
        """
        # The bot entity is passed through to a mangled parameter as this gets
        # sent to the `detail_endpoint` method in the base `get` method
        return super(QalxWorker, self)._stop_or_resume(
            entity=entity,
            stop=stop,
            _QalxWorker__bot_entity=bot_entity,
            **kwargs,
        )

    def reload(self, entity, bot_entity, **kwargs):
        """
        Reloads the current entity from the API
        :param entity: An instance of ~entities.worker.Worker
        :type entity:~entities.worker.Worker
        :param bot_entity: An instance of ~entities.bot.Bot
        :type bot_entity:~entities.bot.Bot
        :return: A refreshed instance of `self.entity`
        """
        # Don't pass `bot_entity` to a mangled parameter as the `reload` method
        # handles that in the superclass
        return super(QalxWorker, self).reload(
            entity=entity, bot_entity=bot_entity
        )

    def update_status(self, entity, bot_entity, status):
        """
        Updates the workers status
        :param entity: An instance of ~entities.worker.Worker
        :type entity:~entities.worker.Worker
        :param bot_entity: An instance of ~entities.bot.Bot
        :type bot_entity:~entities.bot.Bot
        :param status: The status to update to
        :type status: str
        """
        # The bot entity is passed through to a mangled parameter as this gets
        # sent to the `detail_endpoint` method in the base `get` method
        return super(QalxWorker, self).update_status(
            entity=entity, _QalxWorker__bot_entity=bot_entity, status=status
        )

    def stop(self, entity, bot_entity, **kwargs):
        """
        Sends a stop signal to the worker
        :param entity: An instance of ~entities.worker.Worker
        :type entity:~entities.worker.Worker
        :param bot_entity: An instance of ~entities.bot.Bot
        :type bot_entity:~entities.bot.Bot
        """
        return super(QalxWorker, self).stop(
            entity=entity, bot_entity=bot_entity, **kwargs
        )

    def resume(self, entity, bot_entity, **kwargs):
        """
        Sends a resume signal to the worker
        :param entity: An instance of ~entities.worker.Worker
        :type entity:~entities.worker.Worker
        :param bot_entity: An instance of ~entities.bot.Bot
        :type bot_entity:~entities.bot.Bot
        """
        return super(QalxWorker, self).resume(
            entity=entity, bot_entity=bot_entity, **kwargs
        )

    def save(self, entity, bot_entity, *args, **kwargs):
        return super(QalxWorker, self).save(
            entity=entity, _QalxWorker__bot_entity=bot_entity, *args, **kwargs
        )
