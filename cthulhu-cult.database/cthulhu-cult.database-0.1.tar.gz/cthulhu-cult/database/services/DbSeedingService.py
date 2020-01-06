from database.models.DistrictType import DistrictType
from database.services.DbService import db_service
from database.models.Mana import Mana


class DbSeedingService:
    class __DbSeedingService:
        def init_seeding(self):
            self.__create_mana()
            self.__create_district_types()

        def __create_mana(self):
            for mana_type in Mana.TYPES:
                mana = Mana()
                mana.set_name(mana_type)
                db_service.add(mana)

        def __create_district_types(self):
            for type_category in DistrictType.TYPES:
                for type in DistrictType.TYPES[type_category]:
                    mana = db_service.select(Mana, {"name": type_category}, True)
                    district_type = (DistrictType()).set_name(type).set_mana(mana)
                    if type in DistrictType.WILDERNESS_TYPES:
                        district_type.set_is_wilderness(True)
                    else:
                        district_type.set_is_wilderness(False)
                    db_service.add(district_type)

    instance = None

    def __init__(self):
        if not DbSeedingService.instance:
            DbSeedingService.instance = DbSeedingService.__DbSeedingService()

    def init_seeding(self):
        DbSeedingService.instance.init_seeding()


db_seeding_service = DbSeedingService()
