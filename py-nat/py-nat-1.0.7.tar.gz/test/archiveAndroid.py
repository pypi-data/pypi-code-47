#!/usr/bin/python
# -*- coding: utf8 -*-


import argparse
import sys
import os
import time

import nat.coding
import nat.datetime
import nat.log

nat.coding.setDefaultUTF8()



# ----- 开始时间

def __timestamp():
	return int(nat.datetime.getTi())

__scriptStartTimestamp = __timestamp()


# ----- 根据项目修改的常量


from nat_lib.global_ import nat_global

__APP_NAME = nat_global.getStr("APP_NAME")
__APP_LOGO_FILE = nat_global.getStr("APP_LOGO_FILE")
__PLATFORM = nat_global.getStr("PLATFORM")
__PROJECT_GIT_URL = nat_global.getStr("PROJECT_GIT_URL")
_TEAM_ID = nat_global.getStr("TEAM_ID")
_BUNDLE_ID = nat_global.getStr("BUNDLE_ID")

_ITC_API_KEY = nat_global.getStr("ITC_API_KEY")
_ITC_ISSUER_ID = nat_global.getStr("ITC_ISSUER_ID")

_CERTIFICATE_INFO_ADHOC = nat_global.get("CERTIFICATE_INFO_ADHOC")   # 财商：正式
_EXTRA_ADHOC_BUNDLEID_PROVISION_LIST = nat_global.get("EXTRA_ADHOC_BUNDLEID_PROVISION_LIST")
_CERTIFICATE_INFO_APPSTORE = nat_global.get("CERTIFICATE_INFO_APPSTORE")   # 财商：正式
_EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST = nat_global.get("EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST")

__QIYE_WECHAT_WEBHOOK = nat_global.getStr("QIYE_WECHAT_WEBHOOK")

__QRCODE_BG_PNG_PATH = nat_global.getStr("QRCODE_BG_PNG_PATH")
__QRCODE_BG_STANDBY_PNG_PATH = nat_global.getStr("QRCODE_BG_STANDBY_PNG_PATH")

__GIT_BRANCH_MODE = nat_global.getStr("GIT_BRANCH_MODE")
__POD_UPDATE_FQ_RESOURCE = nat_global.getBool("POD_UPDATE_FQ_RESOURCE")

__APK_SCRIPT_PATH = nat_global.getStr("APK_SCRIPT_PATH")


# ----- 不常修改的常量
__PROJECT_DIR_PREFIX = "/Users/xb/Documents/"

_ACCOUNT_USER = "luxiaolong"
_ACCOUNT_PASSWD = "654321qwerQ"

__SERVER_HOST_IP = "10.20.22.224"
_DOWNLOAD_IPA_URL_DOMAIN = "http://%s" %(__SERVER_HOST_IP)
_MINI_HTTPS_DIR = "/Library/WebServer/Documents/http"

__DEFAULT_GITEE = "https://gitee.com/natloc/xb.git"
__DEFAULT_GITEE_RAW = "https://gitee.com/natloc/xb/raw/master"

_CODE_FILENAME = ".code"



import datetime

from nat_lib.archive import nat_path
from nat_lib.archive import nat_file
from nat_lib.archive import nat_plist
from nat_lib.log import nat_console
from nat_lib.var_type import nat_string
from nat_lib.system import nat_cmd
from nat_lib.vcs import nat_git
from nat_lib.media import nat_image
from nat_lib.var_type import nat_version

from nat_lib.thd.ios import nat_ipa
from nat_lib.thd.wechat import nat_group_robot
from nat_lib.thd.qrcode import nat_qrcode

from bs4 import BeautifulSoup
import qrcode
from PIL import Image



# ----- 解析命令行
_parser = argparse.ArgumentParser()


_group = _parser.add_mutually_exclusive_group(required=False)
_group.add_argument("-p", "--projectDirectory", help=u"项目目录", type=str)

_parser.add_argument("-v", "--version", help=u"迭代版本号，如：1.13", type=str, required=True)
_parser.add_argument("--vsn", help=u"版本号；如：1.0.0", type=str, required=False)
_parser.add_argument("--silence", help=u"不发消息到企业微信群", action="store_true")

_groupMode = _parser.add_mutually_exclusive_group(required=False)
_groupMode.add_argument("--release", help=u"开启 Release 模式", action="store_true")
_groupMode.add_argument("--staging", help=u"开启 Staging 模式", action="store_true")
_groupMode.add_argument("--debug", help=u"开启 Debug 模式", action="store_true")
_groupMode.add_argument("--appstore", help=u"上传到 appstore", action="store_true")

_parser.add_argument("--releaseNote", help=u"更新日志", type=str)

# android 特有选项
_parser.add_argument("--args", help=u"android 参数列表；以空格为分隔符", type=str)
_parser.add_argument("--commitInfo", help=u"android 提交信息", type=str)


_args = _parser.parse_args()


_version = nat_string.trim(_args.version)
_versionName = nat_string.trim(_args.vsn)
_projectDir = nat_path.getAbsPath(nat_string.trim(_args.projectDirectory))

_isSilence = _args.silence

_isModeRelease = _args.release
_isModeStaging = _args.staging
_isModeAppStore = _args.appstore

_androidArgs = _args.args
_releaseNote = _args.releaseNote
if None == _releaseNote:
	_releaseNote = u""

_commitInfo = _args.commitInfo
if None == _commitInfo:
	commitInfo = u""


# =====自定义：
if _isModeAppStore:
	_mode = "appstore"
elif _isModeStaging:
	_mode = "staging"
elif _isModeRelease:
	_mode = "release"
else:
	_mode = "debug"


_projectName = os.path.basename(__PROJECT_GIT_URL).split(".")[0]
_platform = __PLATFORM
_projectDir = "%s/%s/%s/v%s" %(__PROJECT_DIR_PREFIX, _platform, _projectName, _version)   # 如：/Users/xb/Documents/ios/fq/v1.13   # 之后将变成 /Users/xb/Documents/ios/fq/v1.13/fq
_isIOS = "ios" == __PLATFORM
__projectInfoPlistPath = "%s/%s/%s/Info.plist" %(_projectDir, _projectName, _projectName)



# 根据 issue code 获取标题
def _reqJiraTitle(code):
	jiraUrl = u"http://jira.xiaobangtouzi.com/browse/FQ-%i" %(code)

	cmdStr = u"curl -u %s:%s %s" %(_ACCOUNT_USER, _ACCOUNT_PASSWD, jiraUrl)
	html = os.popen(cmdStr).read()
	htmlLabelArr = BeautifulSoup(html, "html.parser").select("#summary-val")
	if None != htmlLabelArr and None != htmlLabelArr[0]:
		return htmlLabelArr[0].get_text()
	else:
		return u"FQ-%i" %(code)

# 解析更新内容行为 md 字符串
def _parseUpdateLines(contentLineArr):
	content = u""

	for contentLine in contentLineArr:
		contentLine = contentLine.strip()

		if "" == contentLine:
			continue

		# info 类别：任务
		elif contentLine.startswith("+"):
			try:
				jiraCode = int(contentLine)
				jiraIssueTitle = _reqJiraTitle(jiraCode)
				content += u"- **<font color=\"info\">[任务]</font>** [%s](http://jira.xiaobangtouzi.com/browse/FQ-%i)\n" %(jiraIssueTitle, jiraCode)
			except:
				contentLine = contentLine[1:].strip()
				content += u"- **<font color=\"info\">[任务]</font>** %s\n" %(contentLine)

		# warning 类别：bug
		elif contentLine.startswith("-"):
			contentLine = contentLine[1:].strip()
			try:
				jiraCode = int(contentLine)
				jiraIssueTitle = _reqJiraTitle(jiraCode)
				content += u"- **<font color=\"warning\">[bug]</font>** [%s](http://jira.xiaobangtouzi.com/browse/FQ-%i)\n" %(jiraIssueTitle, jiraCode)
			except:
				nat_console.exit(u"- 类别必须填写 jira 的单号数字，当前内容错误：%s" %(contentLine))

		# comment 类别：
		elif contentLine.startswith("*"):
			contentLine = contentLine[1:].strip()
			content += u"- **<font color=\"comment\">[备注]</font>** %s\n" %(contentLine)

		# 引用 类别：
		elif contentLine.startswith(">"):
			content += u"%s\n" %(contentLine)

		else:
			content += u"- %s\n" %(contentLine)

	return content


# ----- 检测参数
if "" == _version:
	nat.log.exit(u"请输入迭代号；如：1.13 迭代")
elif not nat_path.isDir(_MINI_HTTPS_DIR):
	nat.log.exit(u"mini 服务器的 https 目录不存在：%s" %(_MINI_HTTPS_DIR))


# ----- 小帮 android 打包类
class XbAndroidArchive:

	__projectDirPath = ""
	_projectName = ""

	_datetime = ""   # 年月日时分；如：201805051259

	_argApkPath = ""
	_argVersionName = ""
	_argBuildType = ""
	_argPartnerNo = ""
	_argCommitName = ""
	_argCommitId = ""
	_argCommitBranch = ""

	def __init__(self, projectDirPath):
		# 项目路径、项目名
		projectPath = nat_path.getAbsPath(nat_string.trim(projectDirPath))
		if not nat_path.isDir(projectPath) and not nat_path.mkDirRecursive(projectPath):
			nat_console.exit(u"初始化失败：项目目录不存在，项目名：%s，目录：%s" %(_projectName, projectPath))

		projectName = nat_path.getBasename(projectDirPath)
		if "" == projectName:
			nat_console.exit(u"初始化失败：项目名为空，%s" %(_projectName))

		self.__projectDirPath = projectPath
		_projectDir = projectPath
		self._projectName = projectName

		# 解析参数
		argsArr = _androidArgs.split(" ")
		if len(argsArr) >= 4:
			self._argApkPath = argsArr[0]
			self._argVersionName = argsArr[1]
			self._argBuildType = argsArr[2]
			self._argPartnerNo = argsArr[3]

		# 解析提交信息
		argsArr = _commitInfo.split(" ")
		if len(argsArr) >= 3:
			self._argCommitName = argsArr[0]
			self._argCommitId = argsArr[1]
			self._argCommitBranch = argsArr[2]

		# 检测参数
		if not nat_path.isDir(self._argApkPath):
			nat_console.exit(u"初始化失败：http 目录不存在，%s" %(_projectName))
		elif not self._argApkPath.startswith(_MINI_HTTPS_DIR):
			nat_console.exit(u"初始化失败：apk 路径不是 Http 目录，%s" %(_projectName))

		# 时间
		self._datetime = time.strftime("%Y%m%d%H%M", time.localtime())



	def getCode(self):
		codePath = self.getCodePath()
		if not nat_path.isFile(codePath):
			codeDirPath = os.path.dirname(codePath)
			if not nat_path.mkDirRecursive(codeDirPath) or not nat_file.createEmptyFile(codePath, "1"):
				nat_console.exit(u"创建 %s 文件失败" %(codePath))

		codeInt = int(nat_string.trim(nat_file.read(codePath)))
		return "%02d" %(codeInt)

	def getCodePath(self):
		exportDirPath = self._getAvailExportedDirPath()
		exportBasename = "export-%s/%s" %(_version, self._getIsReleaseModeStr().lower())
		exportDir = nat_path.join(exportDirPath, exportBasename)

		return nat_path.join(exportDir, _CODE_FILENAME)


	def _getIsReleaseMode(self):
		return _isModeRelease

	def _getIsStagingMode(self):
		return _isModeStaging

	def _getIsReleaseModeStr(self):
		if self._getIsStagingMode():
			return u"Staging"
		elif self._getIsReleaseMode():
			return u"Release"
		else:
			return u"Debug"

	def _mkReleaseTag(self):
		if self._getIsStagingMode():
			return u"Staging"
		elif self._getIsReleaseMode():
			return u"正式"
		else:
			return u"QA"


	def _getAvailExportedDirPath(self):
		return _projectDir


	# 生成 apk 的 basename
	def _mkApkBasename(self):
		return "xiaobangguihua_%s_%s_%s_%s" %(_version, self._getIsReleaseModeStr().lower(), self._argPartnerNo, self._datetime)

	def _mkApkFilename(self):
		return "%s.apk" %(self._mkApkBasename())

	def _mkApkHttpPath(self):
		return nat_path.join(self._argApkPath, "%s/%s" %(self._datetime, self._mkApkFilename()))

	# 生成下载链接
	def _mkApkDownloadUrl(self):
		httpPath = self._argApkPath[len(_MINI_HTTPS_DIR):]
		httpPath = nat_path.join(httpPath, "%s/%s" %(self._datetime, self._mkApkFilename()))
		return "%s%s" %(_DOWNLOAD_IPA_URL_DOMAIN, httpPath)


	# 生成迭代号；如：1.3
	def _mkDiedai(self):
		valueArr = _version.split(".")
		if len(valueArr) >= 2:
			return "%s.%s" %(valueArr[0], valueArr[1])
		else:
			valueArr = self._argVersionName.split(".")
			if len(valueArr) >= 2:
				return "%s.%s" %(valueArr[0], valueArr[1])
			else:
				return self._argVersionName


	# 发布日志
	def getUpdateMdContent(self):
		content = u"### 【提测-%s】\n#### 【android-%s迭代-%s】\n" %(self._mkReleaseTag(), self._mkDiedai(), _code)
		content += _parseUpdateLines(_releaseNote.split("\\n"))

		return content



# ----- 实例化对象
archive = XbAndroidArchive(_projectDir)

_code = archive.getCode()
__vsnCode = "v%s/%s" %(_version, _code)   # 如：v1.13/03
__vsnModeCode = "v%s/%s/%s" %(_version, _mode, _code)   # 如：v1.13/debug/03
__projectPlatformVsn = "%s/%s/v%s" %(archive._projectName, _platform, _version)   # 如：fq/ios/v1.13
__projectPlatformVsnMode = "%s/%s" %(__projectPlatformVsn, _mode)   # 如：fq/ios/v1.13/debug
__projectPlatformVsnModeCode = "%s/%s/%s" %(__projectPlatformVsn, _mode, _code)   # 如：fq/ios/v1.13/debug/03
__versionCode = "%s%s" %(nat_version.toCodeStr(_versionName), _code)   # 如：01010104
__miniDirPath = "%s/%s" %(_MINI_HTTPS_DIR, __projectPlatformVsnModeCode)   # 如：/...web.../fq/ios/v1.13/release/03/
__manifestDownloadUrl = "%s/%s.plist" %(__DEFAULT_GITEE_RAW, __projectPlatformVsnModeCode)


# ----- android 打包
cmdStr = "%s %s %s" %(__APK_SCRIPT_PATH, _androidArgs, archive._datetime)
if not nat_cmd.cmd(cmdStr):
	nat.log.exit(u"执行 android 打包脚本失败：执行命令失败：%s" %(cmdStr))

# 检测打包结果
apkHttpPath = archive._mkApkHttpPath()
if not nat_path.isFile(apkHttpPath):
	nat.log.exit(u"执行 android 打包脚本失败：没有生成 apk 文件：%s" %(apkHttpPath))


# ----- 通知企业微信群
if not _isSilence:
	nat.log.warn(u"开始通知企业微信群")

	# md
	msgMd = nat_group_robot.MarkdownMessage(__QIYE_WECHAT_WEBHOOK)
	msgMd.append(archive.getUpdateMdContent())
	msgMd.append("\n\n")
	msgMd.append(msgMd.mkLink(u"点击安装 APK (%s)" %(archive._mkApkFilename()), archive._mkApkDownloadUrl()))

	# text
	msgText = nat_group_robot.TextMessage(__QIYE_WECHAT_WEBHOOK)
	msgText.setMentionedAll()

	# 发送消息
	msgMd.send()
	msgText.send()


# 推送到自动化建设 - app 包管理
nat.log.warn(u"开始推送到集成平台")
__QUALITY_QA_URL = "https://quality-qa.xiaobangtouzi.com/treasure/api/v1/create"
__QUALITY_QA_HEADER = "Content-Type:application/json"
__QUALITY_QA_DATA = """{"name": "%s","version_name": "%s", "version": "%s", "branch": "%s", "platform": "%s", "commit_id": "%s", "type": "%s", "submitter": "%s", "created": "%s", "url": "%s"}"""

commit_id = archive._argCommitId
submitter = archive._argCommitName
targetBranchName = archive._argCommitBranch
quality_qa_download_url = archive._mkApkDownloadUrl()

quality_qa_data = __QUALITY_QA_DATA %(__APP_NAME, _version, _code, targetBranchName, _platform, commit_id, _mode, submitter, datetime.datetime.now(), quality_qa_download_url)
quality_qa_requrest = "curl '%s' -H '%s' -d '%s'" %(__QUALITY_QA_URL, __QUALITY_QA_HEADER, quality_qa_data)
nat_cmd.cmd(quality_qa_requrest)


# ----- 递增迭代 code 号
_code = int(_code) + 1
nat_cmd.cmd("echo %d > %s" %(_code, archive.getCodePath()))


# ----- 完成打包
__costSeconds = __timestamp() - __scriptStartTimestamp
__costMinutes = __costSeconds / 60
__costSeconds = __costSeconds % 60
nat.log.warn(u"完成打包任务，共耗时：%i 分 %i 秒" %(__costMinutes, __costSeconds))

















