#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2020/1/6
# @time: 17:57
# @doc:
# Copyright © 2020 natloc_developer. All rights reserved.
#
# 用例：$ ./iosIcon.py -i ./icon.png -p ./MyProject
#


import nat.image
import nat.cmdOpt
import nat.path
import nat.string
import nat.log
import nat.json


# MARK:- 配置
__MODE_IPHONE = 0
__MODE_IPAD = 1
__MODE_MARKET = 2

__RESOLUTION_DICT = {
    20: [
         (1, [__MODE_IPAD])
        ,(2, [__MODE_IPHONE, __MODE_IPAD])
        ,(3, [__MODE_IPHONE])
    ],
    29: [
         (1, [__MODE_IPHONE, __MODE_IPAD])
        ,(2, [__MODE_IPHONE, __MODE_IPAD])
        ,(3, [__MODE_IPHONE])
    ],
    40: [
         (1, [__MODE_IPAD])
        ,(2, [__MODE_IPHONE, __MODE_IPAD])
        ,(3, [__MODE_IPHONE])
    ],
    50: [
         (1, [__MODE_IPAD])
        ,(2, [__MODE_IPAD])
    ],
    57: [
         (1, [__MODE_IPHONE])
        ,(2, [__MODE_IPHONE])
    ],
    60: [
         (2, [__MODE_IPHONE])
        ,(3, [__MODE_IPHONE])
    ],
    72: [
         (1, [__MODE_IPAD])
        ,(2, [__MODE_IPAD])
    ],
    76: [
         (1, [__MODE_IPAD])
        ,(2, [__MODE_IPAD])
    ],
    83.5: [
        (2, [__MODE_IPAD])
    ],
    1024: [
        (1, [__MODE_MARKET])
    ]
}

__APP_ICON_SET_DIR_SUFFIX = "Assets.xcassets/AppIcon.appiconset"


# MARK:- 命令行

parser = nat.cmdOpt.createParser()
parser.add_argument("-i", "--icon", help=u"icon 图片路径", type=str, required=True)
parser.add_argument("-p", "--project", help=u"项目路径", type=str, required=True)
args = nat.cmdOpt.genArgs(parser)

__icon = nat.path.getAbsPath(nat.string.trim(args.icon))
__project = nat.path.getAbsPath(nat.string.trim(args.project))
__projectName = nat.string.trim(nat.path.getBasename(__project))

__isIconPng = nat.path.isFilePng(__icon)
__isIconJpg = nat.path.isFileJpg(__icon)

# MARK:- 参数检测
if not __isIconPng and not __isIconJpg:
    nat.log.error(u"icon 图片仅支持 png 和 jpg 格式：%s" %(__icon))
elif not nat.path.isDir(__project):
    nat.log.error(u"项目不存在：%s" %(__project))
elif "" == __projectName:
    nat.log.error(u"项目名为空字符串")


__iconImg = nat.image.NatImage(__icon)
if 1024 != __iconImg.getWidth() or 1024 != __iconImg.getHeight():
    nat.log.error(u"icon 图片大小必须为 1024x1024")

__appIconSetDir = "%s/%s/%s" %(__project, __projectName, __APP_ICON_SET_DIR_SUFFIX)
if not nat.path.isDir(__appIconSetDir):
    nat.log.error(u"应用图标目录不存在：%s" %(__appIconSetDir))


# 清空旧图标
for filename in nat.path.listDir(__appIconSetDir):
    file = nat.path.getAbsPath(nat.path.join(__appIconSetDir, filename))
    nat.path.rmFile(file)


# 构建 Contents.json
__imgJsonList = []
__iconSuffix = "png" if __isIconPng else "jpg"

for px in __RESOLUTION_DICT:
    for (scale, modeList) in __RESOLUTION_DICT[px]:
        for mode in modeList:
            imgJson = {
                "size": ("%.1fx%.1f" if type(px) == float else "%ix%i") % (px, px),
                "scale": "%ix" % (scale),
                "filename": "%i@%ix.%s" % (px, scale, __iconSuffix)
            }

            if __MODE_IPHONE == mode:
                imgJson["idiom"] = "iphone"
            elif __MODE_IPAD == mode:
                imgJson["idiom"] = "ipad"
            else:
                imgJson["idiom"] = "ios-marketing"

            __imgJsonList.append(imgJson)

__contentJson = {
    "info": {"version" : 1, "author" : "xcode"},
    "images": __imgJsonList
}

__contentJsonFile = nat.path.join(__appIconSetDir, "Contents.json")
__contentJsonFp = open(__contentJsonFile, "w")
__contentJsonFp.write(nat.json.json2str(__contentJson))
__contentJsonFp.close()


# 生成图片
for px in sorted(__RESOLUTION_DICT.keys(), reverse = True):
    for (scale, modeList) in __RESOLUTION_DICT[px]:
        __iconImg.setWidth(int(px * scale), True)
        __iconImg.saveWithNewPath(nat.path.join(__appIconSetDir, "%i@%ix.%s" %(px, scale, __iconSuffix)))
