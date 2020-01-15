from sspo_db.model.core.models import ApplicationReference
from sspo_db.service.core.service import ApplicationReferenceService, ApplicationService

class ApplicationApplicationReference():

    def __init__(self):
        self.application_reference_service = ApplicationReferenceService()

    
    def create(self,name, description, application, external_id, external_type_entity, external_url,internal_uuid, entity_name ):

        application_reference = ApplicationReference()
        application_reference.name = entity_name+ " - "+name
        application_reference.description = description
        application_reference.application = application.id
        application_reference.external_id = external_id
        application_reference.external_url = external_url
        application_reference.external_type_entity = external_type_entity
        application_reference.internal_uuid = internal_uuid
        application_reference.entity_name = entity_name

        self.application_reference_service.create(application_reference)

        return application_reference

    def get_by_external_uuid(self,external_id):
        return self.application_reference_service.retrive_by_external_id(external_id)

    def get_by_external_uuid_and_seon_entity_name(self,external_id,seon_entity_name):
        return self.application_reference_service.retrive_by_external_id_and_seon_entity_name(external_id, seon_entity_name)
                    
                    