import typing
from loguru import logger

from j2db import errors
from j2db.db import BaseManager
from j2db import toolbox
from j2db.models import EventModel
from j2db.auth import AuthManager


class BaseHandler(object):
    def __init__(self, db_manager: BaseManager):
        self.db_manager = db_manager

    def handle(self, *_, **__):
        raise NotImplementedError


class InfoHandler(BaseHandler):
    # all the flags should be placed here
    FLAG_TABLE: str = "table"

    def handle(self, info_flag: str) -> typing.Union[list, dict]:
        info_flag_dict = {self.FLAG_TABLE: self._handle_table}

        # check
        if info_flag not in info_flag_dict:
            return errors.InfoFlagNotFoundError(
                f"{info_flag} is not in {info_flag_dict.keys()}"
            )

        return info_flag_dict[info_flag]()

    def _handle_table(self) -> typing.List[str]:
        return list(self.db_manager.models.keys())


class EventHandlerHookMixin(object):
    def _default_hook(self, em: EventModel) -> EventModel:
        return em

    before_auth = _default_hook
    after_auth = _default_hook
    before_format_check = _default_hook
    after_format_check = _default_hook
    before_table_check = _default_hook
    after_table_check = _default_hook
    before_operation = _default_hook
    after_operation = _default_hook


class EventHandler(BaseHandler, EventHandlerHookMixin):
    def auth(self, event: EventModel) -> bool:
        # secret eg: YOURNAME:YOURPWD
        secret_str: str = event.secret
        target_table: str = event.table

        if ":" not in secret_str:
            logger.warning("no `:` found in secret, eg: YOURNAME:YOURPWD")
            return False
        user, secret, *_ = secret_str.split(":")

        # auth check
        if not AuthManager.is_allowed(user, secret, target_table):
            logger.warning(f"user {user} is not allowed to access table {target_table}")
            return False
        return True

    def handle(self, event: EventModel) -> typing.Dict:
        logger.info(f"event received: {event}")
        # auth
        event = self.before_auth(event)
        if not self.auth(event):
            return errors.AuthInvalidError(event)
        event = self.after_auth(event)

        # format check
        event = self.before_format_check(event)
        logger.debug("format check ...")
        if not event.is_content_valid():
            logger.warning("json invalid")
            return errors.JsonInvalidError(event)
        event = self.after_format_check(event)

        # table name check
        event = self.before_table_check(event)
        logger.debug("table name check ...")
        if event.table not in self.db_manager.models:
            return errors.TableInvalidError(event)
        model = self.db_manager.models[event.table]
        event = self.after_table_check(event)

        # operation
        event = self.before_operation(event)
        logger.debug("db operation ...")
        content_dict = toolbox.json2dict(event.content)
        data = model(**content_dict)
        operate_result = self.db_manager.apply_action(event.action, data)

        # some error happened
        if operate_result:
            logger.error(operate_result)
            return errors.DBOperatorError(event, operate_result)
        event = self.after_operation(event)
        logger.info(f"handler end: {event}")

        return errors.NullError(event)
