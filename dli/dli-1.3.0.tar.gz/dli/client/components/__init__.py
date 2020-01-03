import types
import inspect
from functools import wraps


class LoggingAspect:

    def invoke_pre_call_aspects(self, wrapped_object, metadata):
        if getattr(wrapped_object, 'logger', None):
            wrapped_object.logger.info('Client Function Called', extra=metadata)

    def invoke_post_call_aspects(self, wrapped, metadata):
        pass

    def invoke_after_exception_aspects(
            self, wrapped_object, metadata, exception):
        if getattr(wrapped_object, 'logger', None):
            wrapped_object.logger.exception(
                'Unhandled Exception', stack_info=True, extra={
                    'locals': inspect.trace()[-1][0].f_locals
                })


class AnalyticsAspect:

    def invoke_pre_call_aspects(self, wrapped_object, metadata):
        pass

    def invoke_post_call_aspects(self, wrapped_object, metadata):
        if getattr(wrapped_object, '_analytics_handler', None):
            wrapped_object._analytics_handler.create_event(
                metadata['subject'], metadata['organisation_id'],
                metadata['func'].__qualname__.split('.')[0],
                metadata['func'].__name__,
                {**metadata['arguments'], **metadata['kwargs']},
                result_status_code=200
            )

    def invoke_after_exception_aspects(self, wrapped_object, metadata, exception):
        if getattr(wrapped_object, '_analytics_handler', None):
            status_code = self._retrieve_status_code_from_exception(exception)
            wrapped_object._analytics_handler.create_event(
                metadata['subject'], metadata['organisation_id'],
                metadata['func'].__qualname__.split('.')[0],
                metadata['func'].__name__,
                {**metadata['arguments'], **metadata['kwargs']},
                result_status_code=status_code
            )

    @staticmethod
    def _retrieve_status_code_from_exception(exception):
        try:
            return exception.response.status_code
        except AttributeError:
            return 500


class ComponentsAspectWrapper(type):
    """
    This decorates all functions in a Component with a logging function.
    """
    __aspects = [LoggingAspect(), AnalyticsAspect()]

    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, types.FunctionType):
                attrs[attr_name] = cls._wrap_call_with_aspects(attr_value)

        return super(ComponentsAspectWrapper, cls).__new__(cls, name, bases, attrs)

    @classmethod
    def _wrap_call_with_aspects(cls, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                metadata = cls._extract_metadata(
                    self, func, self._session, *args, **kwargs
                )
            except Exception as e:
                if getattr(self, 'logger', None):
                    self.logger.exception(
                        'Error while reading function metadata.', e
                    )
                return func(self, *args, **kwargs)

            try:
                cls._invoke_pre_call_aspects(self, metadata)
                result = func(self, *args, **kwargs)
                cls._invoke_post_call_aspects(self, metadata)
                return result
            except Exception as e:
                cls._invoke_after_exception_aspects(self, metadata, e)
                raise e

        return wrapper

    @classmethod
    def _extract_metadata(cls, self, func, session, *args, **kwargs):
        # Get the user calling the function
        org_id, subject = cls._retrieve_user_details(self, session)

        # This is to find out what the 'arg' names are.
        argspec = inspect.getfullargspec(func)
        args_dict = dict(zip(argspec.args, [self, *args]))

        if not subject:
            if args_dict.get('api_key'):
                subject = '***' + args_dict.get('api_key')[:6]
            else:
                subject = 'UNKNOWN USER'

        return {
            'func': func,
            'subject': subject,
            'organisation_id': org_id,
            'arguments': args_dict,
            'kwargs': dict(kwargs)
        }

    @classmethod
    def _retrieve_user_details(cls, wrapped_object, session):
        org_id = None
        user_id = getattr(wrapped_object, 'api_key', '')[:6]
        try:
            org_id = session.decoded_token.get('datalake').get('tenant_id')
            if not org_id:
                org_id = session.decoded_token.get('datalake').get(
                    'organisation_id'
                )
            user_id = session.decoded_token.get('sub', 'UNKNOWN USER')
        except AttributeError:
            pass

        return org_id, user_id

    @classmethod
    def _invoke_pre_call_aspects(cls, wrapped_object, metadata):
        for aspect in cls.__aspects:
            try:
                aspect.invoke_pre_call_aspects(wrapped_object, metadata)
            except Exception as e:
                if getattr(wrapped_object, 'logger', None):
                    wrapped_object.logger.exception(
                        'Error while invoking pre-call aspects.', e
                    )

    @classmethod
    def _invoke_post_call_aspects(cls, wrapped_object, metadata):
        for aspect in cls.__aspects:
            try:
                aspect.invoke_post_call_aspects(wrapped_object, metadata)
            except Exception as e:
                if getattr(wrapped_object, 'logger', None):
                    wrapped_object.logger.exception(
                        'Error while invoking post-call aspects.', e
                    )

    @classmethod
    def _invoke_after_exception_aspects(
        cls, wrapped_object, metadata, exception
    ):
        for aspect in cls.__aspects:
            try:
                aspect.invoke_after_exception_aspects(
                    wrapped_object, metadata, exception)
            except Exception as e:
                if getattr(wrapped_object, 'logger', None):
                    wrapped_object.logger.exception(
                        'Error while invoking after-exception aspects.', e
                    )


class SirenComponent(metaclass=ComponentsAspectWrapper):

    def __init__(self, client=None):
        self.client = client
