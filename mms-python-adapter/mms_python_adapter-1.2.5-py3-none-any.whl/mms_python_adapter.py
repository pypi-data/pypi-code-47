from mms_python_client import ApiClient, Configuration
from mms_python_client.api import TicketApi, ElementApi, ArtifactApi
from mms_python_client.models import Element, Elements, LoginRequest, LoginResponse
from mms_python_client.rest import ApiException


class MMSAdapter(object):

    def __init__(self, server, project_id, ref_id):
        self.config = Configuration()
        self.config.host = server
        self.prefix = self.config.auth_settings()['Ticket']['key']  # key value to access config Ticket

        self.client = ApiClient(self.config)

        self.ticket_api = TicketApi(self.client)
        self.elem_api = ElementApi(self.client)
        self.art_api = ArtifactApi(self.client)

        self.project_id = project_id
        self.ref_id = ref_id
        
    def login(self, username, password):
        ticket_request = LoginRequest(username, password)
        del password
        
        ticket = self.ticket_api
        
        try:
            creds = ticket.post_ticket(ticket_request)  # type: login_response
        except ApiException as login_exception:
            print(login_exception.body)
            return login_exception

        ticket_response = self.ticket_api.post_ticket(ticket_request)  # type: LoginResponse
        self.config.api_key[self.prefix] = ticket_response.data.ticket
        del ticket_request, ticket_response
        
        return "Logged in as " + username

    def logout(self):
        self.config.api_key.clear()

    # depth= -1 same as recurse=true
    def get_element(self, element_id, depth=0):
        return self.elem_api.get_element(self.project_id, self.ref_id, element_id, depth=depth)

    def update_element_type(self, element_id, new_type):
        defaultvalue_value = self.get_element(element_id).to_dict().get('elements')[0].get('defaultValue')
        defaultvalue_value['instanceId'] = new_type
        target = {'id': element_id, 'defaultValue': defaultvalue_value}
        payload = {'elements': [target]}
        return self.elem_api.post_elements(self.project_id, self.ref_id, payload)

    def update_element_documentation(self, element_id, content):
        # target = Element(element_id)
        # target['documentation'] = content
        # hardcoding this because the Element class doesn't commit properly
        target = {'id': element_id, 'documentation': content}
        payload = Elements([target])
        return self.elem_api.post_elements(self.project_id, self.ref_id, payload)

    def update_element_name(self, element_id, name):
        target = {'id': element_id, 'name': name}
        payload = Elements([target])
        return self.elem_api.post_elements(self.project_id, self.ref_id, payload)

    def publish_table(self, element_id, table):
        # table should be in html
        return self.update_element_documentation(element_id, table)

    def update_element_value(self, element_id, content):
        # hardcoding this because the Element class doesn't commit properly
        target = {'id': element_id, 'defaultValue': content}
        payload = Elements([target])
        return self.elem_api.post_elements(self.project_id, self.ref_id, payload)
        