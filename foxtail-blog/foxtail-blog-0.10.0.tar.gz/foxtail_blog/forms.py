from django.conf import settings
from django.forms import ModelForm, Textarea

from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from csp_helpers.mixins import CSPFormMixin

from .models import Comment


class CommentForm(CSPFormMixin, ModelForm):
    if settings.RECAPTCHA_ENABLED:
        captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.error_text_inline = False
        self.helper.help_text_inline = False

        self.helper.layout = Layout(
            'text',
            'captcha' if settings.RECAPTCHA_ENABLED else None,
            Submit('submit', 'Post Comment')
        )

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'rows': 4})
        }
