import datetime
from classcard_dataclient.models.course import CourseTableManager, Course
from sync.base import BaseSync
from utils.loggerutils import logging
from utils.dateutils import date2str, str2datetime
from config import TABLE_BEGIN_DATE, TABLE_END_DATE

logger = logging.getLogger(__name__)

class 