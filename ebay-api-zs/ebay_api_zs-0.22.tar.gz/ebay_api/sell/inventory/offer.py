import json

from .base import InventoryAPI


class OfferAPI(InventoryAPI):
    resource = 'offer'


class CreateOffer(OfferAPI):
    method_type = 'POST'

    def get_success_message(self):
        sku = json.loads(self.payload)['sku']
        return f"Предложение успешно создано (SKU товара: {sku})"

    def get_error_message(self):
        sku = json.loads(self.payload)['sku']
        return f"Не удалось создать предложение (SKU товара: {sku})"


class UpdateOffer(OfferAPI):
    method_type = 'PUT'
    required_path_params = ['offerId']


class GetOffers(OfferAPI):
    method_type = 'GET'
    required_query_params = ['sku']
    allowed_query_params = ['marketplace_id', 'offset', 'limit']

    def clean_sku(self, sku):
        if not (1 <= len(sku) <= 50):
            is_valid = False
            message = f'Количество символов в sku должно лежать в диапазоне [1:50].'
        else:
            is_valid = True
            message = ''
        return is_valid, sku, message


class GetOffer(OfferAPI):
    method_type = 'GET'
    required_path_params = ['offerId']


class DeleteOffer(OfferAPI):
    method_type = 'DELETE'
    required_path_params = ['offerId']

    def get_success_message(self):
        return f"Предложение успешно удалено (offerId: {self.path_params['offerId']})"

    def get_error_message(self):
        return f"Не удалось удалить предложение (offerId: {self.path_params['offerId']})"


class PublishOffer(OfferAPI):
    method_type = 'POST'
    required_path_params = ['offerId']
    url_postfix = 'publish'

    def get_success_message(self):
        return f"Предложение успешно опубликовано (offerId: {self.path_params['offerId']})"

    def get_error_message(self):
        return f"Не удалось опубликовать предложение (offerId: {self.path_params['offerId']})"


class WithdrawOffer(OfferAPI):
    method_type = 'POST'
    required_path_params = ['offerId']
    url_postfix = 'withdraw'


class GetListingFees(OfferAPI):
    method_type = 'POST'
    url_postfix = 'get_listing_fees'


class BulkOfferAPI(InventoryAPI):
    resource = ''

    def error_handler(self, response):
        objects = response.json()
        if 'responses' in objects:
            message = ''
            for error_num, error in enumerate(objects['responses']):
                errors = error.get('errors', [])
                if errors:
                    message += f'{error_num+1}) {errors[0]["message"]}'
                    if error.get('sku', None):
                        message += ' (SKU: {error["sku"]})'
                    message += '.\n'
            return message, objects
        return super().error_handler(response)


class BulkCreateOffer(BulkOfferAPI):
    method_type = 'POST'
    url_postfix = 'bulk_create_offer'

    def get_success_message(self):
        return (
            f"Офферы группы товаров успешно созданы "
        )

    def get_error_message(self):
        return (
            f"Не удалось создать офферы группы товаров "
        )


class BulkPublishOffer(BulkOfferAPI):
    method_type = 'POST'
    url_postfix = 'bulk_publish_offer'

    def get_success_message(self):
        return (
            f"Офферы группы товаров успешно опубликованы "
        )

    def get_error_message(self):
        return (
            f"Не удалось опубликовать офферы группы товаров "
        )
