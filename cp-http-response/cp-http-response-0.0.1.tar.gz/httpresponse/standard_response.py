# coding=utf-8
__author__ = 'peter gra'
__date__ = '2019-12-16 11:35'
from enum import IntEnum, unique
import datetime


@unique
class ServiceCode(IntEnum):
    '''
    服务器返回的code
    '''
    ###********** 通用 code **********###
    # 未知错误
    unkonw_failure = -1,
    # 成功请求
    success = 0,

    ###********** 控制类 code **********###
    control_pass = 881,
    control_review = 882,
    control_old_version = 883,

    ###********** 请求预处理错误 code **********###
    # http method 错误(不是POST)
    http_method_error = 991,
    # 参数格式不正确
    param_format_checking_error = 992,
    # 参数解密不通过
    param_decryption_checking_error = 994,
    # 参数被篡改
    param_signature_checking_error = 995,
    # 操作待支持
    param_waiting_support = 996,

    ###********** 用户 code **********###
    # 用户匹配失败
    user_matching_failure = 10001,
    # 用户不存在
    user_not_exist = 10002,
    # 用户被封禁
    user_status_banned = 10003,
    # jwt_token token不合法 & 失效
    jwt_token_invalid = 10004,
    # 标记删除
    user_is_delete = 10005,
    # 用户存在并登陆
    user_already_exist_confirm = 10106,
    # 用户存在 信息不匹配
    user_already_exist_failure = 10107,
    # 第三方账号重复绑定
    user_open_repeat_bound = 10110,
    # 账号重复绑定
    user_account_already_bound = 10111,
    # 第三方信息拉取失败
    user_open_info_error = 10112,

    ###********** 资源 code **********###
    # 资源存在, 资源访问时间过期
    resouce_overdue = 20001,
    # 资源不存在
    resouce_not_exist = 20002,
    # 脏数据 拒绝访问
    resouce_multiple_objects = 20003,
    # 没有权限访问
    resouce_not_permissions = 20004,
    # 资源该状态不允许修改
    resouce_initial_state_illegal = 20005,
    # 正在处理
    resouce_working = 20006,
    # 资源不足
    resouce_lack = 20007,
    # 资源没有更新
    resouce_version_is_latest = 20008,

    ###********** 操作 code **********###
    # 没有操作权限 | 操作权限不足
    operation_not_permissions = 30001,
    # 不支持该操作
    operation_not_support = 30002,
    # 不在合法的下单时间内
    operation_not_in_create_order_range = 30003,
    # 不在合法的兑换时间内
    operation_not_in_exchange_order_range = 30004,
    # 操作过快 超过频率限制
    operation_too_fast = 30005,
    # 重复操作
    operation_repeat = 30006,
    # 不在合法的时间内
    operation_not_in_legal_date_range = 30007,
    # 操作校检错误
    operation_donot_match = 30008,
    # 模块关闭
    operation_module_close = 30009,
    # 操作已达上限
    operation_trigger_maximize = 30010,


'''
服务器code对应描述文字
'''
ServiceCodeDesc = {
    ###********** 通用 code **********###
    ServiceCode.unkonw_failure: 'Unkonw Failure',
    ServiceCode.success: 'Success',

    ###********** 控制类 code **********###
    ServiceCode.control_pass: 'Pass',
    ServiceCode.control_review: 'Review',
    ServiceCode.control_old_version: 'Version is too old',

    ###********** 请求预处理错误 code **********###
    ServiceCode.http_method_error: 'Http method error',
    ServiceCode.jwt_token_invalid: 'Identity is overdue',
    ServiceCode.param_format_checking_error: 'Parameter format error',
    ServiceCode.param_decryption_checking_error: 'Parameters of decryption error',
    ServiceCode.param_signature_checking_error: 'Parameters signature error',
    ServiceCode.param_waiting_support: 'Operation is not yet supported',

    ###********** 用户 code **********###
    ServiceCode.user_matching_failure: 'The user matching error',
    ServiceCode.user_not_exist: 'The user does not exist',
    ServiceCode.user_already_exist_confirm: 'The user has been registered and login',
    ServiceCode.user_already_exist_failure: 'The user has already been registered',
    ServiceCode.user_status_banned: 'User is currently is banned',
    ServiceCode.user_open_repeat_bound: 'The third party account repeat binding',
    ServiceCode.user_account_already_bound: 'The repeat binding account',
    ServiceCode.user_open_info_error: 'Third party information acquisition fail',
    ServiceCode.user_is_delete: 'The user is deleted logic',

    ###********** 资源 code **********###
    ServiceCode.resouce_overdue: 'Resources overdue',
    ServiceCode.resouce_not_exist: 'Resources do not exist',
    ServiceCode.resouce_multiple_objects: "Resources has multiple objects",
    ServiceCode.resouce_not_permissions: "There is no access to resources",
    ServiceCode.resouce_initial_state_illegal: "Resources in the state is not allowed to change",
    ServiceCode.resouce_working: "Resources are being processing",
    ServiceCode.resouce_lack: "Resources of lack",
    ServiceCode.resouce_version_is_latest: "The version number is the latest of resources",

    ###********** 操作 code **********###
    ServiceCode.operation_not_permissions: 'Operating access is not enough',
    ServiceCode.operation_not_support: 'Operation is not supported',
    ServiceCode.operation_not_in_create_order_range: 'The current time within the stipulated time',
    ServiceCode.operation_not_in_exchange_order_range: 'The current time within the stipulated time',
    ServiceCode.operation_too_fast: 'Operating frequency more than',
    ServiceCode.operation_repeat: 'Repeatable operation process',
    ServiceCode.operation_not_in_legal_date_range: 'Is not in the legal date',
    ServiceCode.operation_donot_match: "Don't match",
    ServiceCode.operation_module_close: "Module close",
    ServiceCode.operation_trigger_maximize: "Have reached the maximum value",
}


class StandardResponse(object):
    def __init__(self, code=ServiceCode.success, data=None, extra=None):
        self._code = code.value
        self._desc = ServiceCodeDesc[code]
        self._date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._data = data
        self._extra = extra

    def data(self):
        res_dict = {
            'code': self._code,
            'desc': self._desc,
            'date': self._date,
        }
        if self._data:
            res_dict['data'] = self._data
        if self._extra:
            res_dict['extra'] = self._extra
        return res_dict
