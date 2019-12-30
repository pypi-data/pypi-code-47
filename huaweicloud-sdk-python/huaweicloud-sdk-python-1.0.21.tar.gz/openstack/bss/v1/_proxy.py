# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack import proxy2
from openstack.bss.v1 import period_resourse as _period_resourse
from openstack.bss.v1 import bill as _bill
from openstack.bss.v1 import period_order as _period_order
from openstack.bss.v1 import enquiry as _enquiry
from openstack.bss.v1 import customer_management as _customer_management
from openstack.bss.v1 import utilities as _utilities
from openstack.bss.v1 import pay_per_use_resource as _pay_per_use_resources
from openstack.bss.v1 import realname_auth as _realname_auth


class Proxy(proxy2.BaseProxy):

    def query_customer_resource(self, domain_id, **kwargs):
        '''
        A customer can query its pay-per-use resources on the partner sales platform.
        The on-demand resource data has a latency, and the latency for each cloud service data varies.
        The data obtained using this API is for reference only.
        This API can be invoked using the partner AK/SK or token only.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_pay_per_use_resources.QueryCustomerResource, domain_id=domain_id, **kwargs)

    def query_partner_monthly_bills(self, domain_id, **kwargs):
        '''
        This API is used to query monthly bills.
        This API can be invoked only by the partner account AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._get(_bill.query_partner_monthly_bills, domain_id=domain_id, requires_id=False, **kwargs)

    def enable_auto_renew(self, domain_id, resource_id, action_id, **kwargs):
        '''
        A customer can use this API to enable automatic subscription renewal for its long-term yearly/monthly resources to prevent the resources from being deleted when they are expired.
        This API can be invoked using the customer token only.
        :param action_id:
        :param domain_id:
        :param resource_id:
        :param kwargs:
        :return:
        '''
        return self._create(_period_resourse.AutoRenew, domain_id=domain_id, resource_id=resource_id, action_id=action_id, **kwargs)

    def disable_auto_renew(self, domain_id, resource_id, action_id, **kwargs):
        '''
        A customer can disable automatic subscription renewal when needed. After disabling this function, the customer needs to manually renew the subscription to the resources before they expire.
        This API can be invoked using the customer token only.
        :param domain_id:
        :param resource_id:
        :param action_id:
        :return:
        '''
        return self._delete(_period_resourse.AutoRenew, domain_id=domain_id, resource_id=resource_id, action_id=action_id, **kwargs)

    def renew_subscription_by_resourceId(self, domain_id, **kwargs):
        '''
        When subscription to yearly/monthly resources of a customer is about to expire, the customer can renew the subscription to the resources.
        This API can be invoked using the customer token only.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_period_resourse.OrderRenewByResourceid, domain_id=domain_id, **kwargs)

    def unsubscribe_by_resourceId(self, domain_id, **kwargs):
        '''
        If a customer has subscribed to a yearly/monthly resource, the customer can use this API to unsubscribe from the resource, including the renewed part and currently used part.
        The customer cannot use the resources after unsubscription.
        This API can be invoked using the customer token only.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_period_resourse.OrderDeleteByResourceid, domain_id=domain_id, **kwargs)

    def pay_period_order(self, domain_id, **kwargs):
        '''
        A customer can invoke this API to pay yearly-monthly product orders in the pending payment status.
        This API can be invoked using the customer token only.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_period_order.PayPeriodOrder, domain_id=domain_id, **kwargs)

    def unsubscribe_period_order(self, domain_id, **kwargs):
        '''
        A customer can invoke this API to unsubscribe from early-monthly product orders in the subscribed, changing, or failed to be provisioned status.
        This API can be invoked using the customer token only.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._delete(_period_order.UnsubscribePeriodOrder, domain_id=domain_id, requires_id=False, **kwargs)

    def cancel_order(self, domain_id, **kwargs):
        '''
        A customer can invoke this API to cancel orders in the pending payment status.
        This API can be invoked using the customer token only.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_period_order.CancelOrder, domain_id=domain_id, **kwargs)

    def query_customer_period_resources_list(self, domain_id, **kwargs):
        '''
        A customer can query one or all yearly/monthly resources on the customer platform.
        This API can be invoked only by the customer AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._get(_period_resourse.QueryCustomerPeriodResourcesList, domain_id=domain_id, requires_id=False, **kwargs)

    def query_order_detail(self, domain_id, **kwargs):
        '''
        A customer can query resource details and provisioning status of an order on the partner sales platform.
        This API can be invoked using the customer token only.

        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._get(_period_order.QueryOrderDetail, domain_id=domain_id, requires_id=False, **kwargs)

    def query_order_list(self, domain_id, **kwargs):
        '''
        After a customer purchases yearly/monthly resources, it can query the orders in different statuses,
         such as in the pending approval, processing, canceled, completed, and pending payment statuses.
        This API can be invoked using the customer AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._get(_period_order.QueryOrderList, domain_id=domain_id, requires_id=False, **kwargs)

    def query_rating(self, domain_id, **kwargs):
        '''
        The partner sales platform obtains the product prices on the HUAWEI CLOUD official website based on the product catalog.
        This API can be invoked using the customer token, or the partner's AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_enquiry.QueryRating, domain_id=domain_id, **kwargs)

    def create_customer(self, domain_id, **kwargs):
        '''
        This API is used to create a HUAWEI CLOUD account for a customer when the customer creates an account on your sales platform, and bind the customer account
        on the partner sales platform to the HUAWEI CLOUD account.
        In addition, the HUAWEI CLOUD account is bound to the partner account.
        This API can be invoked only by the partner AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_customer_management.CreateCustomer, domain_id=domain_id, **kwargs)

    def check_customer_register_info(self, domain_id, **kwargs):
        '''
        This API is used to check whether the account name, and mobile number or email address entered by the customer can be used for registration.
        This API can be invoked only by the partner AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_customer_management.CheckCustomerRegisterInfo, domain_id=domain_id, **kwargs)

    def query_customer_list(self, domain_id, **kwargs):
        '''
        This API is used to query your customers.
        This API can be invoked only by the partner account AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_customer_management.QueryCustomerList, domain_id=domain_id, **kwargs)

    def send_verification_code(self, domain_id, **kwargs):
        '''
        If customers enter email addresses for registration, this API is used to send a registration verification code to the email addresses to verify the registration information.
        This API can be invoked only by the partner AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_utilities.SendVerificationcode, domain_id=domain_id, **kwargs)

    def individual_realname_auth(self, domain_id, **kwargs):
        '''
        This API can be used to submit an individual real-name authentication application.
        This API can be invoked only by the partner account AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_realname_auth.IndividualRealnameAuth, domain_id=domain_id, **kwargs)

    def enterprise_realname_auth(self, domain_id, **kwargs):
        '''
        This API can be used to submit an enterprise real-name authentication application.
        This API can be invoked only by the partner account AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_realname_auth.EnterpriseRealnameAuth, domain_id=domain_id, **kwargs)

    def change_enterprise_realname_auth(self, domain_id, **kwargs):
        '''
        This API can be used to submit a real-name authentication change application.
        This API can be invoked only by the partner account AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._create(_realname_auth.EnterpriseRealnameAuthChange, domain_id=domain_id, **kwargs)

    def query_realname_auth(self, domain_id, **kwargs):
        '''
        If the response to a real-name authentication application or real-name authentication change application indicates that manual review is required,
        this API can be used to query the review result.
        This API can be invoked only by the partner account AK/SK or token.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._get(_realname_auth.QueryRealnameAuth, domain_id=domain_id, **kwargs)

    def query_resource_status_by_orderId(self, domain_id, order_id, **kwargs):
        '''
         A customer can query resource details and provisioning status of an order on the partner sales platform.
        This API can be invoked using the customer token only.
        :param domain_id:
        :param order_id:
        :param kwargs:
        :return:
        '''
        return self._get(_period_order.QueryOrderResource, domain_id=domain_id, order_id=order_id, **kwargs)

    def query_refund_order_amount(self, domain_id, order_id, **kwargs):
        '''
        A customer can query the resources and original orders of the unsubscription amount for an unsubscription order or degrade order.
        This API can be invoked using the AK/SK or token of the partner or the token of the partner's customer.
        :param domain_id:
        :param order_id:
        :param kwargs:
        :return:
        '''
        return self._get(_period_order.QueryRefundOrder, domain_id=domain_id, order_id=order_id, **kwargs)

    def query_resource_usage_details(self, domain_id, **kwargs):
        '''
        his API can be used to query usage details of each resource for a customer on the customer platform. The resource details have a latency (a maximum of 24 hours).
        This API can be invoked using the customer AK/SK or token only.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._get(_bill.QueryBillResRecords, domain_id=domain_id, **kwargs)

    def query_resource_usage_record(self, domain_id, **kwargs):
        '''
        This API can be used to query the usage details of each resource for a customer on the customer platform.
        This API can be invoked using the customer AK/SK or token only.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._get(_bill.QueryResFeeRecords, domain_id=domain_id, **kwargs)

    def query_monthly_expenditure_summary(self, domain_id, **kwargs):
        '''
        * This API can be used to query the expenditure summary bills of a customer on the customer platform. The bills summarize the summary data by month. The data of the previous day is updated once a day.
        * This API can be invoked using the customer AK/SK or token only.
        :param domain_id:
        :param kwargs:
        :return:
        '''
        return self._get(_bill.QueryBillMonthlySum, domain_id=domain_id, **kwargs)
