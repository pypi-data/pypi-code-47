from sync import BaseSync
from classcard_dataclient.models.classroom import Classroom, RoomType
from utils.loggerutils import logging

logger = logging.getLogger(__name__)


class ClassroomSync(BaseSync):
    def sync(self):
        res = self.nice_requester.get_classroom_list()
        res_data = res.get('locations', [])
        classroom_list = []
        for rd in res_data:
            building = rd['building'] or "教学楼"
            try:
                floor = int(rd['building'][-3])
            except (Exception, ):
                floor = 0
            classroom = Classroom(number=rd['locationID'], name=rd['locationName'], building=building,
                                  floor=floor, school=self.school_id, category=RoomType.TYPE_PUBLIC)
            classroom_list.append(classroom)
        self.client.create_classrooms(self.school_id, classroom_list)
