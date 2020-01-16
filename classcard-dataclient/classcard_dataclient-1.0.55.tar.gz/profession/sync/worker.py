from sync.student import StudentSync
from sync.teacher import TeacherSync
from sync.clas import ClassSync
from sync.classroom import ClassroomSync
from sync.course2 import CourseSyncV2
from sync.course import CourseSyncV1
from sync.subject import SubjectSync
from sync.school import SchoolSync
from utils.loggerutils import logging

logger = logging.getLogger(__name__)


def start_sync():
    special_number = "1165"
    logger.info(">>>Start profession sync")
    school_sync = SchoolSync(special_number=special_number)
    school_sync.start()
    index, total = 0, len(school_sync.school_map)
    for name, number in school_sync.school_map.items():
        index += 1
        logger.info(">>> Start Sync {} Data, Process {}/{}".format(name, index, total))
        print(">>> Start Sync {} Data, Process {}/{}".format(name, index, total))
        if special_number and number != special_number:
            continue
        school_info = {"school_name": name, "school_number": number}
        # teacher_sync = TeacherSync(**school_info)
        # teacher_sync.start()
        # class_sync = ClassSync(**school_info)
        # class_sync.start()
        # student_sync = StudentSync(class_entrance=class_sync.class_entrance, **school_info)
        # student_sync.start()
        # classroom_sync = ClassroomSync(**school_info)
        # classroom_sync.start()
        # subject_sync = SubjectSync(**school_info)
        # subject_sync.start()
        course_sync = CourseSyncV2(**school_info)
        course_sync.start()
