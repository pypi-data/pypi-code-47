from django.conf import settings
from django.forms import CharField, EmailField, Form, Textarea

from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Layout, Row
from csp_helpers.mixins import CSPFormMixin


class ContactForm(CSPFormMixin, Form):
    if settings.RECAPTCHA_ENABLED:
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

        if settings.RECAPTCHA_ENABLED:
            self.fields['captcha'].label = False

        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),
                Column('email', css_class='col-md-6')
            ),
            Row(
                Column('message', css_class='col-md-12'),
            ),
            Row(
                Column('captcha', css_class='col-md-12'),
            ) if settings.RECAPTCHA_ENABLED else HTML('<!-- security! -->')
        )
