# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from argparse import RawTextHelpFormatter
from jdcloud_cli.cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class PartnerController(BaseController):
    class Meta:
        label = 'partner'
        help = '渠道合作伙伴管理平台API'
        description = '''
        partner cli 子命令，欢迎使用京东云渠道合作伙伴 API 服务。 本文档提供的 API 可供渠道合作伙伴使用请求调用的方式来管理客户。渠道合作伙伴 API全新发布，提供更加规范和全面的 API 接口文档，统一的参数风格和公共错误码，统一的 SDK/CLI 版本与 API 文档严格一致，给您带来简单快捷的使用体验；支持全地域就近接入让您更快连接京东云产品。。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) NA """, dest='regionId',  required=False)),
            (['--customer-pin'], dict(help="""(string) 客户pin """, dest='customerPin',  required=False)),
            (['--alias-name'], dict(help="""(string) 客户昵称 """, dest='aliasName',  required=False)),
            (['--login-name'], dict(help="""(string) 帐户名 """, dest='loginName',  required=False)),
            (['--start-rel-time'], dict(help="""(string) 关联开始时间（格式：yyyy-MM-dd HH:mm:ss） """, dest='startRelTime',  required=False)),
            (['--end-rel-time'], dict(help="""(string) 关联结束时间（格式：yyyy-MM-dd HH:mm:ss） """, dest='endRelTime',  required=False)),
            (['--page-index'], dict(help="""(int) 当前页序号 """, dest='pageIndex', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 当前条数 """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询客户信息 ''',
        description='''
            查询客户信息。

            示例: jdc partner query-my-customer-list 
        ''',
    )
    def query_my_customer_list(self):
        client_factory = ClientFactory('partner')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.partner.apis.QueryMyCustomerListRequest import QueryMyCustomerListRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = QueryMyCustomerListRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) NA """, dest='regionId',  required=False)),
            (['--start-time'], dict(help="""(string) 按月查询开始时间（yyyy/MM/dd） """, dest='startTime',  required=True)),
            (['--end-time'], dict(help="""(string) 按月查询结束时间（yyyy/MM/dd） """, dest='endTime',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询服务商相关的总消费数据 ''',
        description='''
            查询服务商相关的总消费数据。

            示例: jdc partner get-total-consumption  --start-time xxx --end-time xxx
        ''',
    )
    def get_total_consumption(self):
        client_factory = ClientFactory('partner')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.partner.apis.GetTotalConsumptionRequest import GetTotalConsumptionRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetTotalConsumptionRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) NA """, dest='regionId',  required=False)),
            (['--start-time'], dict(help="""(string) 按月查询开始时间（yyyy/MM/dd） """, dest='startTime',  required=True)),
            (['--end-time'], dict(help="""(string) 按月查询结束时间（yyyy/MM/dd） """, dest='endTime',  required=True)),
            (['--pin'], dict(help="""(string) pin """, dest='pin',  required=False)),
            (['--page-size'], dict(help="""(int) 每页条数 """, dest='pageSize', type=int, required=True)),
            (['--page-index'], dict(help="""(int) 第几页 """, dest='pageIndex', type=int, required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询服务商下每个客户总消费数据 ''',
        description='''
            查询服务商下每个客户总消费数据。

            示例: jdc partner get-each-consumption  --start-time xxx --end-time xxx --page-size 0 --page-index 0
        ''',
    )
    def get_each_consumption(self):
        client_factory = ClientFactory('partner')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.partner.apis.GetEachConsumptionRequest import GetEachConsumptionRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetEachConsumptionRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) NA """, dest='regionId',  required=False)),
            (['--pin'], dict(help="""(string) pin """, dest='pin',  required=False)),
            (['--start-time'], dict(help="""(string) 按月查询开始时间（yyyy-MM-dd）,不可跨月 """, dest='startTime',  required=True)),
            (['--end-time'], dict(help="""(string) 按月查询结束时间（yyyy-MM-dd）,不可跨月 """, dest='endTime',  required=True)),
            (['--page-size'], dict(help="""(int) 每页条数,不超过100 """, dest='pageSize', type=int, required=True)),
            (['--page-index'], dict(help="""(int) 第几页 """, dest='pageIndex', type=int, required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询服务商相关pin下每个产品的消费数据 ''',
        description='''
            查询服务商相关pin下每个产品的消费数据。

            示例: jdc partner describe-customer-bill-by-product  --start-time xxx --end-time xxx --page-size 0 --page-index 0
        ''',
    )
    def describe_customer_bill_by_product(self):
        client_factory = ClientFactory('partner')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.partner.apis.DescribeCustomerBillByProductRequest import DescribeCustomerBillByProductRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeCustomerBillByProductRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['query-my-customer-list','get-total-consumption','get-each-consumption','describe-customer-bill-by-product',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('partner', self.app.pargs.api)
        skeleton.show()
