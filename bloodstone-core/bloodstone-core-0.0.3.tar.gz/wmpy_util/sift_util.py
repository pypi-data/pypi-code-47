#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : WeiWang Zhang
@Time    : 2019-09-20 12:09
@File    : sift_util.py
@Software: PyCharm
@Desc    : 基于SIFT相似度算法，将'训练图片'仿射变换为'查询图片'的大小
"""
from wmpy_util.time_util import *
from wmpy_util import img_util as iu
from wmpy_util import file_util as fu
import numpy as np
import os
import cv2
import time


class SiftException(Exception):
    def __init__(self, err='sift error!'):
        Exception.__init__(self, err)


feature_cache = dict()


class LocateCard:
    def __init__(self, save_debug=False, save_path=None, speed_up=False):
        self.save_debug = save_debug
        if save_debug:
            fu.check_dir(save_path, True)
        self.save_path = save_path
        self.sift = cv2.xfeatures2d.SIFT_create()
        self.MIN_MATCH_COUNT = 10
        self.KNN_MATCH_SUPPRESS = 0.8  # KNN匹配的极大值抑制比例，该值越小则符合要求的匹配越少
        self.speed_up = speed_up

    def locate(self, query_img, query_feature, train_img, train_mask=None):
        """
        寻找图像中的身份证并进行图像矫正（透视变换）
        :param query_img: 用于查询的图片(如，标准身份证图片)
        :param query_feature:查询图片的sift特征，如果传递该参数将不重复计算query_img的sift特征
        :param train_img: 为需要识别的图像
        :param train_mask: 训练图片掩膜，用于计算sift特征
        :return:
        """
        qh, qw = query_img.shape[:2]
        if self.speed_up:
            query_pts, train_pts = self.find_match_with_sift_fast(query_img, train_img, train_mask)
        else:
            query_pts, train_pts = self.find_match_with_sift(query_img, train_img, train_mask)
        # 用HomoGraphy计算图像与图像之间映射关系, M为转换矩阵
        q2t_mat, _ = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        # 计算模板在目标图片上的轮廓
        query_edge = np.float32([[0, 0], [0, qh - 1], [qw - 1, qh - 1], [qw - 1, 0]]).reshape(-1, 1, 2)
        query_dege_on_train = cv2.perspectiveTransform(query_edge, q2t_mat)
        # 根据模板尺寸和需求宽度，计算所需图片整体尺寸
        t2q_mat = np.mat(q2t_mat).I
        result_img = cv2.warpPerspective(train_img, t2q_mat, (qw, qh), borderValue=[255, 255, 255],
                                         borderMode=cv2.BORDER_REPLICATE)
        # -----------存储中间图片，正式环境不需要------------
        if self.save_debug:
            train_copy = train_img.copy()
            # 存储原图
            iu.save_result(train_copy, self.save_path, "origin.jpg")
            # 组合图的上面两张，反应sift匹配情况
            cv2.polylines(train_copy, [np.int32(query_dege_on_train)], True, [0, 255, 0], 2,
                          cv2.LINE_AA)  # 画出识别到的卡片边框
            img_combine = iu.img_joint_with_colorgap((train_copy, result_img),
                                                     axis=1, align=0, gap=2,
                                                     gap_color=[255, 0, 0])  # 组合图的下面两张，分别为带识别框的原图/变换后的图片
            # 画出sift全过程图片
            iu.save_result(img_combine, self.save_path, "origin_vs_transform.jpg")
        # -----------对结果做出检查，如果离谱则报错，不返回结果------------
        if len(query_pts) <= self.MIN_MATCH_COUNT:
            raise SiftException("模板匹配度不足 - %d/%d" % (len(query_pts), self.MIN_MATCH_COUNT))
        # TODO计算原图上圈出的身份证面积，并以此判断是否是一个有效的识别（比如面积占比必须大于1/8）
        self.check_area_size(train_img.shape, query_dege_on_train)
        # im_r图像矫正结果  M_r对应的透视变换矩阵
        return result_img, t2q_mat

    # @timer(batch=10)
    def find_match_with_sift(self, query_img, train_img, train_mask=None):
        """
        找到两张图片的匹配点对
        :param query_img:
        :param train_img:
        :param train_mask:
        :return:
        """
        if callable(train_mask):
            train_mask = train_mask(query_img)
        query_kp, query_des = self.get_x_feature(query_img, mask=None, cache=self.speed_up)
        train_kp, train_des = self.get_x_feature(train_img, mask=train_mask)
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=10)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(query_des, train_des, k=2)
        # 两个最佳匹配之间距离之比要小于0.7, 比例过大说明最佳匹配的两点非常接近，很可能是噪声点
        good = []
        for m, n in matches:
            if m.distance < self.KNN_MATCH_SUPPRESS * n.distance:
                good.append(m)
        if self.save_debug:
            # flag = cv2.DRAW_MATCHES_FLAGS_DEFAULT
            flag = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
            tmp = cv2.drawMatches(query_img, query_kp, train_img, train_kp, good, outImg=None,
                                  flags=flag)
            pic_name = "sift_match.jpg"
            cv2.imwrite(os.path.join(self.save_path, pic_name), tmp)
            cv2.imwrite(os.path.join(self.save_path, "train_mask.jpg"), train_mask)
        # reshape为(x,y)数组
        query_pts = np.float32([query_kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        train_pts = np.float32([train_kp[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        return query_pts, train_pts

    @timer(batch=10)
    def find_match_with_sift_fast(self, query_img, train_img, train_mask=None):
        """
        找到两张图片的匹配点对
        :param query_img:
        :param train_img:
        :param train_mask:
        :return:
        """
        # 计算sift特征前将图片缩放到指定大小
        x_feature_width = 600
        query_small, query_scall = iu.img_resize_longer_size(query_img, x_feature_width)
        train_small, train_scall = iu.img_resize_longer_size(train_img, x_feature_width)
        query_pts, train_pts = self.find_match_with_sift(query_small, train_small, train_mask=train_mask)
        query_pts = query_pts / query_scall
        train_pts = train_pts / train_scall
        return query_pts, train_pts

    def get_x_feature(self, img, mask=None, cache=False):
        """
        获取图像sift特征
        :param img:
        :param mask:
        :param cache: 是否使用缓存
        :return:
        """
        if cache:
            h, w = img.shape[:2]
            mid = int(w / 2)
            # 取图片中间宽度为10的条带像素和作为缓存key，在图片数量不是特别多的时候足够区分图片(此处尽量仅缓存模板)
            img_key = np.sum(img[:, mid - 5:mid + 5, :])
            x_feature = feature_cache.get(img_key, None)
            if x_feature is None:
                x_feature = self.sift.detectAndCompute(img, mask=mask)
                feature_cache[img_key] = x_feature
        else:
            x_feature = self.sift.detectAndCompute(img, mask=mask)
        # 此处拆分方便理解
        kp, des = x_feature
        return kp, des

    def check_area_size(self, shape, dst):
        """
        检测识别到的身份证区域是否有效
        :param shape: 图片尺寸 [h,w]
        :param dst:  标记身份证区域的多边形顶点
        :return:
        """
        # 计算原图面积
        ori_area = shape[0] * shape[1]
        card_area = cv2.contourArea(dst)
        # 如果识别到的卡片面积过大或者过小则不予判断
        if card_area < (ori_area / 8) or card_area > (ori_area * 1.5):
            raise SiftException("识别到的卡片面积异常 识别/实际 = %.2f" % (card_area / ori_area))
        max_cor = np.max(dst, axis=0)
        min_cor = np.min(dst, axis=0)
        [[width, height]] = max_cor - min_cor
        # 如果识别到的卡片高宽过大或者过小则不予判断
        if width < (shape[1] / 4) or width > (shape[1] * 1.5):
            raise SiftException("识别到的卡片宽度异常 识别/实际 = %.2f" % (width / shape[1]))
        if height < (shape[0] / 5) or height > (shape[0] * 1.5):
            raise SiftException("识别到的卡片高度异常 识别/实际 = %.2f" % (height / shape[0]))

    @staticmethod
    def mask_idcard(img):
        """
        对身份证的蓝色区域作出mask
        :param img:
        :return:
        """
        shape = img.shape
        if len(shape) < 3:
            return None
        img = np.intp(img)
        blue, green, red = cv2.split(img)
        # target = blue * 2 - green - red
        # target = blue+green - red *2
        target = blue - red
        target = np.uint8((np.abs(target) + target) / 2)
        # binary = cv2.adaptiveThreshold(target, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 151, 2)
        th, binary = cv2.threshold(target, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # 膨胀和腐蚀操作的核函数
        dilate_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (35, 35))
        # 1. 膨胀一次，让轮廓突出
        dilation = cv2.dilate(binary, dilate_rect, iterations=1)
        # if self.save_debug:
        #     combine = iu.img_joint((img, target, binary, dilation))
        #     iu.save_result(combine, self.save_path, file_name="blue-red.jpg")
        return dilation



if __name__ == '__main__':
    pass
