#!/usr/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2020/1/2
# @time: 17:14
# @doc:
# Copyright © 2020 natloc_developer. All rights reserved.
#

from bs4 import BeautifulSoup

import nat.cmd
import nat.log
import nat.datetime


__ACCOUNT_USER = "luxiaolong"
__ACCOUNT_PASSWD = "654321qwerQ"


# 根据 issue code 获取标题
def reqJiraTitle(code):
    jiraUrl = u"http://jira.xiaobangtouzi.com/browse/FQ-%i" %(code)

    cmdStr = u"curl -u %s:%s %s" %(__ACCOUNT_USER, __ACCOUNT_PASSWD, jiraUrl)
    html = nat.cmd.executeRead(cmdStr).read()
    htmlLabelArr = BeautifulSoup(html, "html.parser").select("#summary-val")

    if None != htmlLabelArr and None != htmlLabelArr[0]:
        return htmlLabelArr[0].get_text()
    else:
        return u"FQ-%i" %(code)


# 输出耗时
def printArchiveDuration(startTi):
    __costSeconds = int(nat.datetime.getTi() - startTi)
    __costMinutes = __costSeconds / 60
    __costSeconds = __costSeconds % 60
    nat.log.warn(u"完成打包任务，共耗时：%i 分 %i 秒" % (__costMinutes, __costSeconds))


# 同步数据到 QA 集成平台
def syncQualityQA(appName, version, code, branchName, platform, commitId, mode, submitter, downloadUrl):
    __QUALITY_QA_URL = "https://quality-qa.xiaobangtouzi.com/treasure/api/v1/create"
    __QUALITY_QA_HEADER = "Content-Type:application/json"
    __QUALITY_QA_DATA = """{"name": "%s","version_name": "%s", "version": "%s", "branch": "%s", "platform": "%s", "commit_id": "%s", "type": "%s", "submitter": "%s", "created": "%s", "url": "%s"}"""

    quality_qa_data = __QUALITY_QA_DATA %(appName, version, code, branchName, platform, commitId, mode, submitter, nat.datetime.now(), downloadUrl)
    quality_qa_requrest = "curl '%s' -H '%s' -d '%s'" % (__QUALITY_QA_URL, __QUALITY_QA_HEADER, quality_qa_data)

    nat.cmd.execute(quality_qa_requrest)

