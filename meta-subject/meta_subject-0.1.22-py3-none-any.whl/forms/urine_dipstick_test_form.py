from edc_constants.constants import NO, YES
from edc_form_validators import FormValidator

from ..models import UrineDipstickTest
from .form_mixins import SubjectModelFormMixin


class UrineDipstickTestFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            NO, field="performed",
            field_required="not_performed_reason")

        self.applicable_if(
            YES, field="performed",
            field_applicable="ketones")

        self.applicable_if(
            YES, field="performed",
            field_applicable="protein")

        self.applicable_if(
            YES, field="performed",
            field_applicable="glucose")


class UrineDipstickTestForm(SubjectModelFormMixin):

    form_validator_cls = UrineDipstickTestFormValidator

    class Meta:
        model = UrineDipstickTest
        fields = "__all__"
