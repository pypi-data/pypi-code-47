from thegeotarginator_back_interface.geotargeting_event import GeotargetingEvent


class OrganisationGeotargetingRemovedEvent(GeotargetingEvent):

    def __init__(self, campaign_id: int, organisation_id: int):
        self.campaign_id: int = campaign_id
        self.organisation_id: int = organisation_id
        self.__is_organisation_geotargeting_removed_event__: bool = True

    @staticmethod
    def from_dict(data: dict):
        return OrganisationGeotargetingRemovedEvent(data['campaign_id'], data['organisation_id'])
