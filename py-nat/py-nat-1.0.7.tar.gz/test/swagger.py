#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/24
# @time: 15:57
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import os
import json
import sys
import argparse
import shutil
import random

import nat.coding
import nat.log
import thd.wechat.group_robot
import nat.file
import nat.path
import nat.git
import nat.cmd

nat.coding.setDefaultUTF8()


# --- 常量

__METIS_SERVER_URL = "http://swagger.xiaobangtouzi.com/swagger/metis-server-qa.json"
__USER_CENTER_URL = "http://swagger.xiaobangtouzi.com/swagger/user-center-server-qa.json"

# 完整的链接由 __METIS_QUICK_LINK_PREVIOUS/TagStr/OperationIdStr 组成
__METIS_QUICK_LINK_PREVIOUS = "http://swagger.xiaobangtouzi.com/swagger/?urls.primaryName=metis-server-qa#"

# 财商 ios
__GIT_IOS_BRANCHNAME = "master"
__GIT_POD_NAME = "fq-resource"
__POD_INDEX_NAME = "xiaobangtouzi-ios-spec"
__GIT_SWIFT_URL = "https://luxiaolong:654321qwerQ@code.xiaobangtouzi.com/ios/%s.git" %(__GIT_POD_NAME)
__GIT_SPEC_URL = "https://luxiaolong:654321qwerQ@code.xiaobangtouzi.com/ios/spec.git"

# 财商 android
__GIT_KOTLIN_BRANCHNAME = "developer"
__GIT_KOTLIN_URL = "https://luxiaolong:654321qwerQ@code.xiaobangtouzi.com/android/android-vo.git"


_projectDir = os.path.dirname(sys.path[0])
_modelDir = os.path.join(_projectDir, "src/course/model")

#__ROBOT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=55309ab8-adb4-45f6-ae96-7689ad088590"
__ROBOT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=49e78e2a-02a6-4f60-8949-45c026174d21"   # 测试



# --- 命令行选项

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help=u"修改 swagger 的用户名", type=str)

group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("--ios", help=u"平台类型：iOS", action="store_true")
group.add_argument("--android", help=u"平台类型：Android", action="store_true")
group.add_argument("--h5", help=u"平台类型：h5", action="store_true")

args = parser.parse_args()


# --- 内部变量

# __outputDir = os.path.abspath(args.output)
# if not os.path.isdir(__outputDir):
# 	__exit(u"生成文件的输出目录不存在：%s" %(__outputDir))

# 用户名
__usernameDict = {
	"changyuan":	u"常远",
	"zhanghaotian":	u"皓天",
	"yanglijuan":	u"丽娟",
	"houchangchun":	u"长春",
	"zhourongyu":	u"山荣"
}
__username = __usernameDict.get(args.username, "")



__genSwift = args.ios
__genKotlin = args.android
__genH5 = args.h5


if not __genSwift and not __genKotlin and not __genH5:
	__genSwift = True
	__genKotlin = True
	__genH5 = True


# key-ModelNameStr; value-[PathStr, ...]
__modelNamePathDict = {}
# key-PathStr; value-(SummaryStr, TagStr, OperationIdStr)
__pathInfoDict = {}

__modelAdded = []
__modelModified = []
__modelDeleted = []
__modelRenamed = []




class MetaClass:
	_name = ""
	_fieldArr = []


class MetaField:
	_name = ""
	_typeName = ""   # 如：string/integer/number/boolean/object
	_subtypeName = ""   # 如：int64/int32/float/double
	_isList = False
	_comment = ""



# --- 内部方法

def __reqSwaggerJson(url):
	cmd = "curl %s" %(url)
	respStr = os.popen(cmd).read()
	return json.loads(respStr)

def __parsePath(swaggerJson):
	paths = swaggerJson["paths"]

	for path in paths:
		jsonData = paths[path].get("get", None)
		if None == jsonData:
			jsonData = paths[path].get("post", None)

		if None != jsonData:
			summaryStr = jsonData.get("summary", "")
			tagStr = jsonData["tags"][0]
			operationIdStr = jsonData["operationId"]
			__pathInfoDict[path] = (summaryStr, tagStr, operationIdStr)

			paramsArr = jsonData.get("parameters", [])
			for param in paramsArr:
				schemaJson = param.get("schema", {})
				__parsePathSchemaJson(path, schemaJson)

			resp200SchemaJson = jsonData.get("responses", {}).get("200", {}).get("schema", {})
			__parsePathSchemaJson(path, resp200SchemaJson)

def __parsePathSchemaJson(path, schemaJson):
	if None != schemaJson:
		refStr = schemaJson.get("$ref", "")
		modelName = refStr.split("/")[-1]
		if "" != modelName and modelName != refStr:
			modelPathArr = __modelNamePathDict.get(modelName, None)
			if None == modelPathArr:
				modelPathArr = []

			modelPathArr.append(path)
			__modelNamePathDict[modelName] = modelPathArr

def __parseModel(swaggerJson):
	models = swaggerJson["definitions"]
	clsArr = []

	for clsName in models:
		# 过滤 《...》 类型
		if "" == clsName or clsName.find("«") >= 0:
			continue


		metaCls = MetaClass()
		metaCls._name = clsName

		# 解析单个 model
		metaFieldArr = []
		fields = models[clsName].get("properties", "")
		if "" != fields:
			for fieldName in fields:
				if "" == fieldName:
					continue

				metaField = MetaField()
				metaField._name = fieldName

				field = fields[fieldName]
				# 解析字段
				fieldType = field.get("type", "")
				fieldRef = field.get("$ref", "")
				lastSepIndex = fieldRef.rfind("/")

				# 关联字段
				if lastSepIndex > 0:
					metaField._typeName = fieldRef[lastSepIndex+1:]

				# 数组字段
				elif "array" == fieldType:
					metaField._isList = True
					metaField._comment = field.get("description", "")

					# 引用类型数组
					fieldRef = field["items"].get("$ref")

					if None != fieldRef:
						lastSepIndex = fieldRef.rfind("/")

						if lastSepIndex < 0:
							nat.log.exit("解析数组字段失败，字段名:%s" %(fieldName))

						else:
							metaField._typeName = fieldRef[lastSepIndex+1:]

					# 基础类型数组
					else:
						metaField._typeName = field["items"]["type"]


				# 普通字段
				else:
					metaField._typeName = fieldType
					metaField._subtypeName = field.get("format", "")
					metaField._comment = field.get("description", "")

				metaFieldArr.append(metaField)


		metaCls._fieldArr = metaFieldArr
		clsArr.append(metaCls)

	return clsArr


# 生成关联链接
def __mkModelLineStr(modelNameArr, title):
	filesChangedStr = u""

	if len(modelNameArr) > 0:
		filesChangedStr += u"\n\n##### %s：" %(title)

		for modelName in modelNameArr:
			filesChangedStr += u"\n- %s" %(modelName)

			pathArr = __modelNamePathDict.get(modelName, None)
			if None != pathArr:
				for path in pathArr:
					(summaryStr, tagStr, operationIdStr) = __pathInfoDict[path]
					filesChangedStr += u"\n    - [%s - %s](%s/%s/%s)" %(path, summaryStr, __METIS_QUICK_LINK_PREVIOUS, tagStr, operationIdStr)

	return filesChangedStr


# 移除旧文件
def __removeOldFiles(outputDir, suffix, firstLine):
	for filename in os.listdir(outputDir):
		(basename, suffixWithDot) = os.path.splitext(filename)
		if ".%s" %(suffix) == suffixWithDot:
			file = nat.path.join(outputDir, filename)
			fp = open(file, "r")
			firstLineStr = fp.readline().strip()
			fp.close()

			# 判定为自动生成的文件，则删除
			if firstLineStr == firstLine:
				os.remove(file)

def __gitClone(gitUrl, branchName):
	nat.git.clone(gitUrl)

	projectName = os.path.splitext(os.path.basename(gitUrl))[0]
	projectDir = nat.path.join(os.getcwd(), projectName)

	# 切换分支
	if "master" != branchName:
		nat.path.changeCwd(projectDir)
		os.system("git checkout -b %s origin/%s" %(branchName, branchName))
		nat.git.push(branchName=branchName)

	# 创建 model 目录
	outputDir = nat.path.join(projectDir, "Classes/swagger_model")
	if not nat.path.isDir(outputDir):
		os.makedirs(outputDir)

	return (projectDir, outputDir)

# return: hasChanged :: bool
def __gitPush(projectDir, isIOS = False, branchName = "master"):
	cwd = nat.path.cwd()

	nat.path.changeCwd(projectDir)
	nat.git.add()

	hasChanged = False
	if nat.git.status_isDirty():
		# 更新 pod 索引
		if isIOS:
			nat.git.clone(__GIT_SPEC_URL)
			specDir = nat.path.join(projectDir, "spec")
			nat.path.changeCwd(specDir)

			podspecFile = nat.path.join(specDir, "%s/0.0.1/%s.podspec" %(__GIT_POD_NAME, __GIT_POD_NAME))
			if nat.path.isFile(podspecFile):
				os.system("echo \" \" >> %s" %(podspecFile))
				nat.git.addAndCommit("[Fix]")
				nat.git.push()

			nat.path.changeCwd(projectDir)
			nat.path.rmDirRecursive(specDir)


		# 解析变更的文件：仅在解析 swift 时进行处理
		if isIOS:
			nat.log.warn(u"开始检测文件变更")
			lines = nat.cmd.executeRead("git status").read().split("\n")
			for line in lines:
				splitArr = line.strip().split(" ")
				if len(splitArr) >= 4:
					(basename, suffix) = os.path.splitext(os.path.basename(splitArr[-1]))
					if ".swift" == suffix and "" != basename:
						if "modified:" == splitArr[0]:
							__modelModified.append(basename)
						elif "new" == splitArr[0] and "file:" == splitArr[1]:
							__modelAdded.append(basename)
						elif "deleted" == splitArr[0]:
							__modelDeleted.append(basename)
						elif "renamed:" == splitArr[0]:
							if "->" == splitArr[-2] and len(splitArr) >= 4:
								__modelRenamed.append(u"%s 已改名为 %s" %(splitArr[-3], splitArr[-1]))
							else:
								__modelRenamed.append(basename)

		# 提交
		nat.git.commit("【自动生成】")
		nat.git.push(branchName=branchName)
		hasChanged = True

	nat.path.changeCwd(cwd)
	nat.path.rmDirRecursive(projectDir)

	return hasChanged


# --- swift 部分

__SWIFT_FIRST_LINE = u"// 自动生成，请勿手动修改"

def __genSwiftCode(clsArr, outputDir):
	for cls in clsArr:

		# 文件头
		modelContent = __SWIFT_FIRST_LINE
		modelContent += u"\nimport Foundation"
		modelContent += u"\nimport HandyJSON"
		modelContent += u"\n\nopen class %s: HandyJSON{" %(cls._name)
		modelContent += u"\n\tpublic required init(){}\n"

		# 字段
		for field in cls._fieldArr:
			line = ""

			# 注释行
			comment = field._comment.strip()
			if "" != comment:
				line = u"\n\t/// %s" %(comment)

			# 字段行
			fieldType = __fmtSwiftFieldType(field)
			if "" == fieldType:
				nat.log.exit("格式化字段类型出错，字段名：%s，字段类型：%s，子类型：%s" %(field._name, field._typeName, field._subtypeName))

			# 列表类型
			if field._isList:
				fieldType = "[%s]" %(fieldType)

			line += u"\n\topen var %s: %s?" %(field._name, fieldType)

			modelContent += line

		# 文件尾
		modelContent += u"\n\n}"

		# 写入文件
		filePath = "%s.swift" %(nat.path.join(outputDir, cls._name))
		nat.file.createEmptyFile(filePath, modelContent)

def __fmtSwiftFieldType(field):
	typeName = field._typeName
	subTypeName = field._subtypeName

	if "string" == typeName:
		return "String"

	elif "integer" == typeName:
		if "int64" == subTypeName:
			return "Int64"
		elif "int32" == subTypeName:
			return "Int"
		else:
			nat.log.exit(u"未知整型：%s，子类型：%s，字段名：%s" %(typeName, subTypeName, field._name))

	elif "number" == typeName:
		if "float" == subTypeName:
			return "Float"
		elif "double" == subTypeName:
			return "Double"
		elif "" == subTypeName:
			return "Float"
		else:
			nat.log.exit(u"未知数值类型：%s，子类型：%s，字段名：%s" %(typeName, subTypeName, field._name))

	elif "boolean" == typeName:
		return "Bool"

	elif "object" == typeName:
		return "Dictionary<String, Any>"

	else:
		return typeName



# --- kotlin 部分

__KOTLIN_FIRST_LINE = u"// 自动生成，请勿手动修改"

def __genKotlinCode(clsArr, outputDir):
	for cls in clsArr:

		# 文件头
		modelContent = __SWIFT_FIRST_LINE
		modelContent += u"\npackage com.xiaobang.fq.model"
		modelContent += u"\n\ndata class %s @JvmOverloads constructor(" %(cls._name)

		# 字段
		for field in cls._fieldArr:
			line = ""

			# 注释行
			comment = field._comment.strip()
			if "" != comment:
				line = u"\n\t// %s" %(comment)

			# 字段行
			(fieldType, isNullable, defValue) = __fmtKotlinFieldType(field)
			if "" == fieldType:
				nat.log.exit("格式化字段类型出错，字段名：%s，字段类型：%s，子类型：%s" %(field._name, field._typeName, field._subtypeName))

			# 列表类型
			if field._isList:
				fieldType = "List<%s>" %(fieldType)
				isNullable = True


			nullableStr = ""
			if isNullable:
				nullableStr = "?"

			line += u"\n\tvar %s: %s%s = %s," %(field._name, fieldType, nullableStr, defValue)

			modelContent += line

		# 文件尾
		if "," == modelContent[-1]:
			modelContent = modelContent[:-1]

		modelContent += u"\n\n)"

		# 写入文件
		filePath = "%s.kt" %(nat.path.join(outputDir, cls._name))
		nat.file.createEmptyFile(filePath, modelContent)

def __fmtKotlinFieldType(field):
	typeName = field._typeName
	subTypeName = field._subtypeName

	if "string" == typeName:
		return ("String", True, "null")

	elif "integer" == typeName:
		if "int64" == subTypeName:
			return ("Long", False, "0L")
		elif "int32" == subTypeName:
			return ("Int", False, "0")
		else:
			nat.log.exit(u"未知整型：%s，子类型：%s，字段名：%s" %(typeName, subTypeName, field._name))

	elif "number" == typeName:
		if "double" == subTypeName:
			return ("Double", False, "0.0")
		elif "" == subTypeName or "float" == subTypeName:
			return ("Float", False, "0F")
		else:
			nat.log.exit(u"未知数值类型：%s，子类型：%s，字段名：%s" %(typeName, subTypeName, field._name))

	elif "boolean" == typeName:
		return ("Boolean", False, "false")

	elif "object" == typeName:
		return ("Map<String, Any>", True, "null")

	else:
		return (typeName, True, "null")



# --- 入口

def main():
	global __username

	# 网络请求
	json = __reqSwaggerJson(__METIS_SERVER_URL)

	# 解析
	__parsePath(json)
	clsArr = __parseModel(json)

	hasChanged = False

	# 生成
	if __genSwift:
		nat.log.warn(u"开始生成 swift 文件")
		(projectDir, __outputDir) = __gitClone(__GIT_SWIFT_URL, __GIT_IOS_BRANCHNAME)

		__removeOldFiles(__outputDir, "swift", __SWIFT_FIRST_LINE)
		__genSwiftCode(clsArr, __outputDir)

		if __gitPush(projectDir, True, __GIT_IOS_BRANCHNAME):
			hasChanged = True
			nat.log.warn(u"推送 swift 文件成功")
		else:
			nat.log.warn(u"swift 无变更")

	if __genKotlin:
		nat.log.warn(u"开始生成 kotlin 文件")
		(projectDir, __outputDir) = __gitClone(__GIT_KOTLIN_URL, __GIT_KOTLIN_BRANCHNAME)

		__removeOldFiles(__outputDir, "kt", __KOTLIN_FIRST_LINE)
		__genKotlinCode(clsArr, __outputDir)

		if __gitPush(projectDir, branchName = __GIT_KOTLIN_BRANCHNAME):
			nat.log.warn(u"推送 kotlin 成功")
		else:
			nat.log.warn(u"kotlin 无变更")

	# 通知到企业微信群
	if hasChanged or True:
		nat.log.warn(u"开始通知企业微信群")

		filesChangedStr = u""
		filesChangedStr += __mkModelLineStr(__modelAdded, u"新增")
		filesChangedStr += __mkModelLineStr(__modelModified, u"修改")
		filesChangedStr += __mkModelLineStr(__modelRenamed, u"重命名")
		filesChangedStr += __mkModelLineStr(__modelDeleted, u"删除")

		nat.log.warn(u"开始发送消息")
		msg = thd.wechat.group_robot.MarkdownMessage(__ROBOT_WEBHOOK)

		msg.append(u"【%s 更新了 swagger】" %(msg.mkColorOrange(__username)), fragmentCount=3, shouldAppendNewLine=True)
		msg.append(filesChangedStr)

		msg.send()

		nat.log.warn(u"生成接口文件成功")


main()

