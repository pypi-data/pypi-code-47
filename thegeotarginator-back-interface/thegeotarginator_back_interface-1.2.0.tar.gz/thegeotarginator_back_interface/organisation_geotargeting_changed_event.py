from thegeotarginator_back_interface.geotargeting_event import GeotargetingEvent


class OrganisationGeotargetingChangedEvent(GeotargetingEvent):

    def __init__(self, campaign_id: int, organisation_id: int, targeted_countries_sp: [int], targeted_countries_p: [int],
                 targeted_countries_lp: [int], update_date: int, expiry_date: int = None):
        self.campaign_id: int = campaign_id
        self.organisation_id: int = organisation_id
        self.targeted_countries_sp: [int] = targeted_countries_sp
        self.targeted_countries_p: [int] = targeted_countries_p
        self.targeted_countries_lp: [int] = targeted_countries_lp
        self.expiry_date: int = expiry_date
        self.update_date: int = update_date

        self.__is_organisation_geotargeting_changed_event__: bool = True

    @staticmethod
    def from_dict(data: dict):
        expiry_date = data['expiry_date'] if 'expiry_date' in data else None
        return OrganisationGeotargetingChangedEvent(campaign_id=data['campaign_id'],
                                             organisation_id=data['organisation_id'],
                                             targeted_countries_sp=data['targeted_countries_sp'],
                                             targeted_countries_p=data['targeted_countries_p'],
                                             targeted_countries_lp=data['targeted_countries_lp'],
                                             update_date=data['update_date'],
                                             expiry_date=expiry_date)
