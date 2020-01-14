import sys  # noqa

from dynaconf import LazySettings, Validator

settings = LazySettings(ENVVAR_PREFIX_FOR_DYNACONF="AFFO_SMS", ENVVAR_FOR_DYNACONF="AFFO_SMS_SETTINGS")

# Register validators
settings.validators.register(
    Validator(
        "DATABASE_URI",
        "TWILIO_ACCOUNT_SID",
        "TWILIO_AUTH_TOKEN",
        "TWILIO_FALLBACK_FROM_PHONE",
        "TWILIO_PHONE",
        "TWLIIO_SENDER",
        "CLICKATELL_API_KEY",
        must_exist=True,
    )
)

# Fire the validator
settings.validators.validate()

# SECRET CONFIGURATION
SECRET_KEY = getattr(settings, "SECRET_KEY", "")

# DEBUG CONFIGURATION
DEBUG = getattr(settings, "DEBUG", False)

# SQLALCHEMY CONFIGURATION
SQLALCHEMY_DATABASE_URI = settings.DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MODEL_IMPORTS = ("affo_sms_service.models.sms_message",)

# SMS CONFIGURATION
SMS_RETRY_TIMEOUT = 60  # seconds
SMS_GATEWAYS = (
    "affo_sms_service.sms.gateways.twilio.TwilioGateway",
    "affo_sms_service.sms.gateways.clickatell.ClickatellGateway",
)

settings.populate_obj(sys.modules[__name__])
