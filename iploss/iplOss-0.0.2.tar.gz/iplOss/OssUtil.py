# -*- coding:utf-8 -*-
import logging
import os

import oss2

from iplOss.MyOSS import MyOSS
from iplOss.MyOSSException import MyOSSException

handler = logging.FileHandler("/data/data/scripts/oss_logs/oss_log.txt")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.addHandler(handler)

'''
简单文件上传：建议不大于5G的小文件使用该方法
'''


def upload(localdir, accessKey, subPath):
    try:
        bucket, myOss, rawToken = getOssAuthBucket(accessKey, subPath)
        localFilePath = localdir
        fileName = os.path.basename(localFilePath)
        basePath = rawToken['basePath']
        with open(localFilePath, 'rb') as fileobj:
            # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
            fileobj.seek(0, os.SEEK_SET)
            # Tell方法用于返回当前位置。
            # current = fileobj.tell()
            key = basePath + fileName
            result = bucket.put_object(key, fileobj)
            print("简单上传http status：{0}".format(result.status))
            fullBathPath = rawToken['fullBasePath']
            uploadPath = fullBathPath + fileName
            print("简单上传upload full path is:", uploadPath)
            signedUrl = myOss.signURL(uploadPath, 3600)
            print("简单上传signed url is:", signedUrl)

    except MyOSSException as e:
        print("OssException:", str(e))
    except Exception as e:
        print("Unknow Error:", e)


def getOssAuthBucket(accessKey, subPath):
    assert accessKey, "accessKey不能为空"
    assert subPath, "subPath不能为空"
    myOss = MyOSS(accessKey)
    rawToken = myOss.init(subPath, 3600)
    bucket = myOss.getOSSClient()
    return bucket, myOss, rawToken


'''
大文件分片上传：建议上传大小不确定且可能单个文件大于5G使用该方法
'''


def multipart_upload(localdir, accessKey, subPath):
    key = ""
    try:
        bucket, myOss, rawToken = getOssAuthBucket(accessKey, subPath)
        basePath = rawToken['basePath']
        localFilePath = localdir
        fileName = os.path.basename(localFilePath)
        key = basePath + fileName
        total_size = os.path.getsize(localFilePath)
        part_size = oss2.determine_part_size(total_size, preferred_size=1024 * 1024)
        upload_id = bucket.init_multipart_upload(key).upload_id
        parts = []
        with open(localFilePath, 'rb') as fileobj:
            part_number = 1
            offset = 0
            while offset < total_size:
                num_to_upload = min(part_size, total_size - offset)
                result = bucket.upload_part(key, upload_id, part_number,
                                            oss2.SizedFileAdapter(fileobj, num_to_upload))
                parts.append(oss2.models.PartInfo(part_number, result.etag))

                offset += num_to_upload
                part_number += 1
            # 完成分片上传
            bucket.complete_multipart_upload(key, upload_id, parts)
            logger.info("本地文件路径:{} -> 上传oss路径:{},上传成功".format(localdir, key))
            fullBathPath = rawToken['fullBasePath']
            uploadPath = fullBathPath + fileName
            print("分片上传upload full path is:", uploadPath)
            signedUrl = myOss.signURL(uploadPath, 3600)
            print("分片上传signed url is:", signedUrl)

    except Exception as err:
        logger.error("本地文件路径:{} -> 上传oss路径:{} ，oss上传异常：{}\\n".format(localdir, key, err))


'''
下载到本地文件
'''


def download(accessKey, subPath, fileName, localFile):
    assert accessKey, "accessKey不能为空"
    assert subPath, "subPath不能为空"
    assert fileName, "要下载的fileName不能为空"
    myOss = MyOSS(accessKey)
    rawToken = myOss.init(subPath, 3600)
    bucket = myOss.getOSSClient()
    basePath = rawToken['basePath']
    objectName = basePath + fileName
    bucket.get_object_to_file(objectName, localFile)
