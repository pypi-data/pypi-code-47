from sync import BaseSync
from classcard_dataclient.models.clas import Class
from utils.loggerutils import logging

logger = logging.getLogger(__name__)


class ClassSync(BaseSync):
    def __init__(self, *args, **kwargs):
        super(ClassSync, self).__init__(*args, **kwargs)
        self.class_entrance = {}

    def sync(self):
        study_year = {"小学": 6, "初中": 3, "高中": 3}
        res = self.nice_requester.get_class_list()
        res_data = res.get('classes', [])
        for index, rd in enumerate(res_data):
            try:
                principal_number = rd['classTeacher']['teacherEID']
            except (Exception,):
                principal_number = None
            section = Class(number=rd['qualifiedClassID'], name=rd['classFullName'], grade=rd['gradeName'],
                            principal_number=principal_number, school=self.school_id)
            if rd['entranceYear'] and rd['entranceYear'].isdigit():
                entrance_info = {"classof": int(rd['entranceYear']),
                                 "graduateat": int(rd['entranceYear']) + study_year[rd["eduStage"]]}
            else:
                entrance_info = {"classof": None, "graduateat": None}
            self.class_entrance[rd['qualifiedClassID']] = entrance_info
            code, data = self.client.create_section(section)
            if code:
                logger.error("Code: {}, Msg: {}".format(code, data))
            print(">>> Already create {}/{} class".format(index + 1, len(res_data)))
            logger.info(">>> Already create {}/{} class".format(index + 1, len(res_data)))
