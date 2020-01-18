from edc_constants.constants import YES
from edc_form_validators import FormValidator

from .form_mixins import SubjectModelFormMixin
from ..models import PhysicalExam


class PhysicalExamFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            YES,
            field="irregular_heartbeat",
            field_required="irregular_heartbeat_description",
        )

        self.required_if(
            YES,
            field="abdominal_tenderness",
            field_required="abdominal_tenderness_description",
        )


class PhysicalExamForm(SubjectModelFormMixin):

    form_validator_cls = PhysicalExamFormValidator

    class Meta:
        model = PhysicalExam
        fields = "__all__"
