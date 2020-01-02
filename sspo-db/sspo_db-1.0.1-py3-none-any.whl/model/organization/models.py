from sspo_db.config.base import Entity

class Organization(Entity):
     
    __tablename__ = "organization"

    is_instance_of = "eo.organization"
    

    