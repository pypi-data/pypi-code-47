from ..requester import Requester
from ..settings import EDTECH_SERVER_TOKEN, CLASS_CARD_SCHOOL


class EDTechRequester(Requester):
    def __init__(self, *args, **kwargs):
        super(EDTechRequester, self).__init__(*args, **kwargs)
        self.headers = {"X-Custom-Header-3School": kwargs.get('school_id', CLASS_CARD_SCHOOL),
                        "X-Custom-Header-3App": "classcard",
                        "Authorization": EDTECH_SERVER_TOKEN}

    def get_class_list(self, school_id, params={}):
        route = "/api/v1/schools/{}/sections/simple/".format(school_id)
        res = self._get_method(route, params=params)
        return res

    def get_teacher_list(self, school_id, params={}):
        route = "/api/v1/schools/{}/teachers/".format(school_id)
        res = self._get_method(route, params=params)
        return res

    def get_student_list(self, school_id, params={}):
        route = "/api/v1/schools/{}/students/".format(school_id)
        res = self._get_method(route, params=params)
        return res
