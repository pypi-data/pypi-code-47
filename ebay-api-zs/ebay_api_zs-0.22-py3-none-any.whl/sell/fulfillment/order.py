import re

from .base import FulfillmentAPI


class OrderAPI(FulfillmentAPI):
    resource = 'order'


class GetOrder(OrderAPI):
    method_type = 'GET'
    required_path_params = ['orderId']


class GetOrders(OrderAPI):
    method_type = 'GET'
    allowed_query_params = ['orderIds', 'filter', 'offset', 'limit']

    def clean_offset(self, offset):
        return super().clean_offset(offset, max_num=999)

    def clean_limit(self, limit):
        return super().clean_limit(limit, max_num=1000)

    def clean_orderIds(self, orderIds_string):
        is_valid = True
        message = ''
        order_ids = [order_id.strip() for order_id in orderIds_string.split(',')]
        if not (1 <= len(order_ids) <= 50):
            message = f'Количество ID заказов должно лежать в диапазоне [1:50].'
            message += f'Передано ID заказов: {len(order_ids)}'
        elif len(order_ids) != len(set(order_ids)):
            message = f'Среди ID заказов есть повторяющиеся.\nСписок ID: {orderIds_string}'
        else:
            for order_id in order_ids:
                for part in order_id.split('-'):
                    if not part.isdigit():
                        message += f'Недопустимый ID заказа: {order_id}.\n'
        if message:
            is_valid = False
        return is_valid, ','.join(order_ids), message

    def clean_filter(self, filter_string):
        # doc: https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrders#h2-input
        def _percent_encode(string):
            string = string.replace('[', '%5B')
            string = string.replace(']', '%5D')
            string = string.replace('{', '%7B')
            string = string.replace('}', '%7D')
            string = string.replace('|', '%7C')
            return string

        def _is_datetime(strings):
            # TODO: проверить на соответствие шаблону 2016-03-21T08:25:43.511Z
            # doc: https://www.journaldev.com/23365/python-string-to-datetime-strptime
            # for string in strings:
            #     if string:
            #         try:
            #             datetime.datetime.strptime(string, '%Y-%m-%d')
            #         except ValueError:
            #             return False
            return True

        is_valid = True
        message = ''
        allowed_filters = ['creationdate', 'lastmodifieddate', 'orderfulfillmentstatus']
        allowed_orderfulfillmentstatuses = ['{NOT_STARTED|IN_PROGRESS}', '{FULFILLED|IN_PROGRESS}']
        for pair in filter_string.split(','):
            key, value = pair.split(':')
            if key == 'orderfulfillmentstatus':
                if value.strip() not in allowed_orderfulfillmentstatuses:
                    message += f'Недопустимое значение фильтра {key}: {value}.\n'
                    message += f'Допустимые значения: {allowed_orderfulfillmentstatuses}.\n'
            elif key in ['creationdate', 'lastmodifieddate']:
                if (not re.match('^[.+\.\..+]$', value.strip())) or (not _is_datetime(value.split('..'))):  # noqa: W605
                    message += f'Недопустимое значение фильтра {key}: {value}.\n'
                    message += f'Значение должно соответствовать шаблону: [<datetime>..<datetime or empty string>]'
            else:
                message += f'Недопустимый фильтр: {key}.\n'
                message += f'Допустимые фильтры: {allowed_filters}.\n'

        if message:
            is_valid = False
        else:
            filter_string = ','.join([
                _percent_encode(filter_pair.strip())
                for filter_pair in filter_string.split(',')
            ])
        return is_valid, filter_string, message


class IssueRefund(OrderAPI):
    method_type = 'POST'
    required_path_params = ['orderId']
    url_postfix = 'issue_refund'
