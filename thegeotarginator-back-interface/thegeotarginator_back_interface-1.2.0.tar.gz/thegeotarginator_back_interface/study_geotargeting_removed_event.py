from thegeotarginator_back_interface.geotargeting_event import GeotargetingEvent


class StudyGeotargetingRemovedEvent(GeotargetingEvent):

    def __init__(self, campaign_id: int, study_id: int):
        self.campaign_id: int = campaign_id
        self.study_id: int = study_id
        self.__is_study_geotargeting_removed_event__: bool = True

    @staticmethod
    def from_dict(data: dict):
        return StudyGeotargetingRemovedEvent(data['campaign_id'], data['study_id'])
