from django.forms import CharField, EmailField, Form, Textarea

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Layout, Row
from csp_helpers.mixins import CSPFormMixin

from . import settings as app_settings


class ContactForm(CSPFormMixin, Form):
    if app_settings.RECAPTCHA_ENABLED:
        if app_settings.RECAPTCHA_INVISIBLE:
            captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
        else:
            captcha = ReCaptchaField()

    name = CharField(required=True)
    email = EmailField(required=True)
    message = CharField(
        required=True,
        widget=Textarea
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.error_text_inline = False

        if app_settings.RECAPTCHA_ENABLED:
            self.fields['captcha'].label = False

        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),
                Column('email', css_class='col-md-6')
            ),
            Row(
                Column('message', css_class='col-md-12'),
            ),
            'captcha' if app_settings.RECAPTCHA_ENABLED else HTML('<!-- security! -->')
        )
