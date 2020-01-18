from django import forms
from ..models import MedicationAdherence
from .form_mixins import SubjectModelFormMixin
from .slider_widget import SliderWidget
from edc_form_validators.form_validator import FormValidator
from edc_constants.constants import OTHER, NEVER


class MedicationAdherenceFormValidator(FormValidator):
    def clean(self):

        confirmed = self.cleaned_data.get("visual_score_confirmed")
        if confirmed is not None:
            if int(self.cleaned_data.get("visual_score_slider", "0")) != confirmed:
                raise forms.ValidationError(
                    {"visual_score_confirmed": "Does not match visual score above."}
                )

        if self.cleaned_data.get("last_missed_pill"):
            if self.cleaned_data.get("last_missed_pill") == NEVER:
                self.m2m_not_required("missed_pill_reason")
            else:
                self.m2m_required("missed_pill_reason")

        self.m2m_other_specify(
            OTHER,
            m2m_field="missed_pill_reason",
            field_other="other_missed_pill_reason",
        )


class MedicationAdherenceForm(SubjectModelFormMixin):

    form_validator_cls = MedicationAdherenceFormValidator

    visual_score_slider = forms.CharField(
        label="Visual Score", widget=SliderWidget(attrs={"min": 0, "max": 100})
    )

    class Meta:
        model = MedicationAdherence
        fields = "__all__"
