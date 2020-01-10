"""
Name : InsightFace.py
Author  : Cash
Contact : tkggpdc2007@163.com
Time    : 2020-01-08 10:52
Desc:
"""

import numpy as np
import insightface
from sklearn.cluster import DBSCAN
from ..libs.common import singleton

__all__ = ['InsightFace']


@singleton
class InsightFace:
    def __init__(self,
                 det_name='retinaface_r50_v1',
                 rec_name='arcface_r100_v1',
                 ga_name=None,  # 'genderage_v1'
                 ctx_id=-1):
        self.model = insightface.app.FaceAnalysis(det_name, rec_name, ga_name)
        self.model.prepare(ctx_id=ctx_id, nms=0.4)

    def batch_encodings(self, images):
        """
        批量获取人脸编码信息
        :param images: a list of images
        :return: a list of encodings
        """
        encodings = list(np.empty((len(images), 512)))
        for i in range(len(images) - 1, -1, -1):
            face = self.model.get(images[i])
            if len(face):
                encodings[i] = face[0].normed_embedding
            else:
                del (images[i])
                del (encodings[i])
        return encodings

    def face_locations(self, image):
        """
        获取人脸位置信息
        :param image: a image with face
        :return: a list of box: [(x1,y1,x2,y2)]
        """
        face = self.model.get(image)
        return [face[i].bbox for i in range(len(face))]

    @staticmethod
    def face_distance(encoding1, encoding2):
        """
        获取人脸编码的欧式距离
        :param encoding1: an encoding
        :param encoding2: an encoding to check
        :return: distance
        """
        return np.linalg.norm(encoding1 - encoding2)

    @staticmethod
    def face_cluster(encodings, min_distance=1.0):
        """
        获取人脸聚类信息，哪些人脸属于同一人脸
        :param encodings: a list of encodings
        :param min_distance: cluster distance
        :return: a list of labels, the number of clusters
        """
        number = len(encodings)
        if number <= 0:
            return [], 0
        matrix = [[np.linalg.norm(encodings[i] - encodings[j]) for j in range(number)] for i in range(number)]

        db = DBSCAN(eps=min_distance, min_samples=1, metric='precomputed')
        db.fit(matrix)
        labels = db.labels_
        num_clusters = len(set(labels)) - (1 if -1 in labels else 0)

        return labels, num_clusters
