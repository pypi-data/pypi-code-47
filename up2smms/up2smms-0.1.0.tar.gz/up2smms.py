# -*- coding: utf-8 -*-
"""
    up2smms
    ~~~~~~~

    Save uploaded pictures in Sm.ms.

    :copyright: (c) 2020 by staugur.
    :license: BSD 3-Clause, see LICENSE for more details.
"""

__version__ = '0.1.0'
__author__ = 'staugur <staugur@saintic.com>'
__hookname__ = 'up2smms'
__description__ = '将图片保存到sm.ms'

import requests
from flask import g

intpl_hooksetting = u'''
<fieldset class="layui-elem-field">
    <legend>sm.ms（{% if "up2smms" in g.site.upload_includes %}使用中{% else %}未使用{% endif %}）</legend>
    <div class="layui-field-box">
        <div class="layui-form-item">
            <label class="layui-form-label"> sm.ms密钥</label>
            <div class="layui-input-block">
                <input type="text" name="smms_token" value="{{ g.site.smms_token }}" placeholder="Api Secret Token @ sm.ms"
                    autocomplete="off" class="layui-input">
            </div>
        </div>
    </div>
</fieldset>
'''


def upimg_save(**kwargs):
    res = dict(code=1)
    try:
        filename = kwargs["filename"]
        stream = kwargs["stream"]
        if not filename or not stream:
            return ValueError
    except (KeyError, ValueError):
        res.update(msg="Parameter error")
    else:
        token = g.cfg.smms_token
        if not token:
            res.update(msg="The sm.ms parameter error")
        else:
            files = {
                'smfile': (
                    filename, stream, 'image/%s' % filename.split(".")[-1]
                )
            }
            headers = {
                "User-Agent": "picbed-up2smms/%s" % __version__,
                "Authorization": token
            }
            try:
                r = requests.post(
                    "https://sm.ms/api/v2/upload",
                    files=files,
                    headers=headers,
                    timeout=5
                )
            except requests.exceptions.RequestException as e:
                res.update(msg=e.message)
            else:
                result = r.json()
                if result.pop("success", False) is True:
                    data = result["data"]
                    res.update(code=0, src=data.pop("url"))
                    res.update(data)
    return res


def upimg_delete(**kwargs):
    result = kwargs.get("save_result")
    hashId = result.get("hash")
    if hashId:
        requests.get("https://sm.ms/api/v2/delete/%s" % hashId).json()
