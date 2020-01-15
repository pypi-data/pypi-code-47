from .base import InventoryAPI


class LocationAPI(InventoryAPI):
    resource = 'location'


class CreateInventoryLocation(LocationAPI):
    method_type = 'POST'
    required_path_params = ['merchantLocationKey']

    def get_success_message(self):
        return f"Склад успешно добавлен на eBay (ID: {self.path_params['merchantLocationKey']})"

    def get_error_message(self):
        return f"Не удалось добавить склад на eBay (ID: {self.path_params['merchantLocationKey']})"


class DeleteInventoryLocation(LocationAPI):
    method_type = 'DELETE'
    required_path_params = ['merchantLocationKey']

    def get_success_message(self):
        return f"Склад успешно удалён с eBay (ID: {self.path_params['merchantLocationKey']})"

    def get_error_message(self):
        return f"Не удалось удалить склад с eBay (ID: {self.path_params['merchantLocationKey']})"


class DisableInventoryLocation(LocationAPI):
    method_type = 'POST'
    url_postfix = 'disable'
    required_path_params = ['merchantLocationKey']


class EnableInventoryLocation(LocationAPI):
    method_type = 'POST'
    url_postfix = 'enable'
    required_path_params = ['merchantLocationKey']


class GetInventoryLocation(LocationAPI):
    method_type = 'GET'
    required_path_params = ['merchantLocationKey']


class GetInventoryLocations(LocationAPI):
    method_type = 'GET'
    allowed_query_params = ['offset', 'limit']

    def get_success_message(self):
        return f"Все склады были успешно загружены с eBay"

    def clean_offset(self, offset):
        return super().clean_offset(offset, max_num=99)

    def clean_limit(self, limit):
        return super().clean_limit(limit, max_num=100)


class UpdateInventoryLocation(LocationAPI):
    method_type = 'POST'
    url_postfix = 'update_location_details'
