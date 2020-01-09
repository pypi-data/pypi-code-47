# -*- coding: utf-8 -*-
# Author: Tiancheng Zhao
# Date: 8/12/17
import os
import glob
import boto3
import uuid


class CloudBucket(object):
    roles = {'full-s3': ('AKIAIRZZT5BICC5NFNOA', 'HB2ixc2F12xaFEuqN1G7HwP4VvfgB+l/kgxNXLFd')}

    def __init__(self):
        s3_key = self.roles['full-s3']
        self._s3 = boto3.resource('s3', aws_access_key_id=s3_key[0], aws_secret_access_key=s3_key[1])

    def upload(self, file, task_id="none"):
        file_name = str(uuid.uuid4())+".pdf"
        try:
            key = '{}/{}/{}'.format("temp", task_id, file_name)
            self._s3.meta.client.upload_file(file, 'soco-knowledge',
                                            key)

            return key
        except Exception as e:
            print(e)
            return None

    def upload_folder(self, files, local_dir, folder_name):
        for f in glob.glob("*.pdf"):
            f = f.split("/")[-1]
            try:
                self._s3.meta.client.upload_file(os.path.join(local_dir, f), 'convmind-images',
                                                 '{}/{}/{}'.format("image_annotation", folder_name, f),
                                                 ExtraArgs={'ACL': 'public-read'})
            except Exception as e:
                print(e)

    def deletes(self, files):
        for file in files:
            self._s3.delete_object(Bucket='soco_parsing_files', Key=file)


if __name__ == "__main__":
    x = CloudBucket()
    task_id = str(uuid.uuid4())
    x.upload("../resources/1906.09308.pdf",task_id)
