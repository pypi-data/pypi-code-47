# -*- coding:utf-8 -*-
import re

import click

from src.local import http_server, pc_info
from src.ming import config
from src.server import server_config


def validate_ip_type(ctx, param, value):
    compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    err_msg = '{}不符合ip格式!请检查后输入'.format(value)
    try:
        if compile_ip.match(value):
            return value
        else:
            raise click.BadParameter(err_msg)
    except ValueError:
        raise click.BadParameter(err_msg)


def print_version(ctx, param, value):
    """
    输出工具版本
    :param ctx:   click上下文
    :param param: 参数
    :param value:  值
    :return:
    """
    if not value or ctx.resilient_parsing:
        return

    version_info = """
    仅适用linux 其他平台部分功能异常 
    jiuming-tools Version {}""".format(config.version)
    click.echo(version_info)
    ctx.exit()


def update_version(ctx, param, value):
    click.echo("更新jiuming-tools。。。")


@click.group()
@click.option('--version', '-v', help='工具版本', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def cli():
    pass


# ---------------------- server tools ----------------------------------------------------------------------------------
@cli.group(help='远程服务器管理')
def server():
    pass


@server.command("list", help='显示所有服务器配置')
def server_list():
    server_config.server_list()


@server.command("add", help='添加服务器配置')
@click.option('--name', '-n', prompt='请输入服务器名称')
@click.option('--host', '-h', prompt='请输入服务器地址', callback=validate_ip_type)
@click.option('--port', '-p', prompt='请输入服务器ssh端口,默认为22', default=22)
@click.option('--username', '-u', prompt='请输入服务器用户名')
@click.option('--password', '-pwd', prompt='请输入密码')
def server_add(name, host, port, username, password):
    server_config.server_add(name, host, port, username, password)


@server.command("remove", help='根据名称删除服务器配置')
@click.option('--name', '-n', type=str, prompt='请输入服务器名称', help='服务器名称')
def server_remove(name):
    server_config.server_remove(name)


@server.command('edit', help='使用vi编辑服务器配置')
def server_edit():
    server_config.server_edit()


@server.command('sync-config', help='同步配置')
@click.option('--model', '-m')
def server_sync_config():
    click.echo("同步server配置")


@server.command('connect', help='🔗连接服务器')
@click.option('--name', '-n', type=str, prompt='请输入服务器名称', help='服务器名称')
def server_connect(name):
    server_config.server_connect(name)


# ----------------------------------- local tools ----------------------------------------------------------------------

@cli.group(help='本机使用的工具')
def local():
    pass


@local.command('pc-info', help='电脑配置')
def local_pc_info():
    pc_info.echo_pc_info()


@local.command('http', help='根据指定文件夹开启临时http服务器')
@click.option('--d', '-d', type=click.Path(exists=True), default='.', nargs=1, help='指定静态文件目录,默认为.')
@click.option('--port', '-p', default=80, type=int, nargs=1, help='指定服务端口,默认为80')
@click.option('--host', '-h', default='0.0.0.0', callback=validate_ip_type, type=str, nargs=1,
              help='指定服务监听地址,默认为0.0.0.0')
def local_tmp_http(d, port, host):
    http_server.http_server(d, port, host)


# ming 函数
if __name__ == '__main__':
    cli()
