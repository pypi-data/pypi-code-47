from .order import OrderAPI


class ShippingFulfillmentAPI(OrderAPI):
    required_path_params = ['orderId']
    url_postfix = 'shipping_fulfillment'


class CreateShippingFulfillment(ShippingFulfillmentAPI):
    method_type = 'POST'


class GetShippingFulfillment(ShippingFulfillmentAPI):
    method_type = 'GET'
    required_path_params = ['orderId', 'filfillmentId']


class GetShippingFulfillments(ShippingFulfillmentAPI):
    method_type = 'GET'
