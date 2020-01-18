from django.test import TestCase, tag
from edc_constants.constants import YES, NO, NOT_APPLICABLE, OTHER, NONE
from edc_utils.date import get_utcnow
from meta_lists.models import (
    BaselineSymptoms,
    ArvRegimens,
    OiProphylaxis,
    DiabetesSymptoms,
)
from meta_screening.tests.meta_test_case_mixin import MetaTestCaseMixin

from ..forms import PatientHistoryForm
from pprint import pprint


class TestPatientHistory(MetaTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_visit = self.get_subject_visit()
        symptoms = BaselineSymptoms.objects.filter(name=NONE)
        arv_regimen = ArvRegimens.objects.get(name="TDF_3TC_ATV_r")
        oi_prophylaxis = OiProphylaxis.objects.filter(
            name__in=["fluconazole", "isoniazid"]
        )
        diabetes_symptoms = DiabetesSymptoms.objects.all()
        self.options = {
            "current_arv_regimen": arv_regimen.id,
            "current_smoker": YES,
            "dia_blood_pressure": 80,
            "diabetes_in_family": NO,
            "diabetes_symptoms": diabetes_symptoms,
            "family_diabetics": NO,
            "former_smoker": NOT_APPLICABLE,
            "has_abdominal_tenderness": NO,
            "has_enlarged_liver": NO,
            "has_previous_arv_regimen": NO,
            "heart_rate": 65,
            "hypertension_diagnosis": NO,
            "hypertension_treatment": None,
            "is_heartbeat_regular": YES,
            "jaundice": YES,
            "oi_prophylaxis": oi_prophylaxis,
            "on_hypertension_treatment": NO,
            "on_oi_prophylaxis": YES,
            "other_diabetes_symptoms": "erik",
            "past_year_symptoms": None,
            "peripheral_oedema": YES,
            "previous_arv_regimen": None,
            "previous_arv_regimen": [],
            "report_datetime": get_utcnow(),
            "respiratory_rate": 12,
            "subject_visit": self.subject_visit.pk,
            "symptoms": None,
            "symptoms": symptoms,
            "sys_blood_pressure": 120,
            "taking_statins": YES,
            "temperature": 37,
            "waist_circumference": 61,
            "weight": 65,
        }

    @tag("1")
    def test_ok(self):

        data = {k: v for k, v in self.options.items()}
        form = PatientHistoryForm(data=data)
        form.is_valid()
        pprint(form._errors)
        self.assertEqual(form._errors, {})
