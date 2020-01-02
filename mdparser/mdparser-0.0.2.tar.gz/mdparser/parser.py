# -*- coding: utf8 -*-
import os
import sys
import logging
import markdown

from . import messages
from . import defaults


logger = logging.getLogger("mdparser").getChild(__name__)


class BlogGroup(object):
    """
    实现博客组对象
    """
    logger = logger.getChild("BlogGroup")

    BlogGroupTypes = ('blog', 'book')
    # 博客组类型
    bg_type = None
    # 博客组名
    bg_name = None
    # 博客组简介
    bg_introduction = None
    # 博客组简介的 md5 值
    bg_introduction_md5 = None

    def __init__(self, project_dirname=defaults.PROJECT_DIRNAME,
                 bg_type=defaults.BLOG_GROUP_TYPE,
                 bg_name='python3-std-lib',
                 bg_introduction=None,
                 bg_introduction_md5=None):
        """

        """
        logger = self.logger.getChild("__init__")

        # 默认当前的 blog-group 是一个合格的 blog-group
        self.is_valide_blog_group = True

        # 检查 bg_type 是否正确
        if bg_type not in self.BlogGroupTypes:
            logger.warning(messages.NOT_SUPPORTED_GLOG_TYPE.format(bg_type))

            # 类型不正确所以把这个设置为不合格
            self.is_valide_blog_group = False

        self.bg_type = bg_type
        self.bg_name = bg_name
        self.bg_introduction = bg_introduction
        self.bg_introduction_md5 = bg_introduction_md5


class Parser(object):
    """
    """
    logger = logger.getLogger("Parser")

    def __init__(self, project_dirname="/tmp/leorgs"):
        """
        """
        logger = self.logger.getChild("__init__")

        # 项目的目录
        if os.path.isdir(project_dirname):

            # 当给定的路径不是一个目录时报错
            logger.error(
                messages.PATH_IS_NOT_A_DERECTORY.format(project_dirname))

            # 退出程序
            sys.exit(1)

        # 如果执行到这里说明，对 project_dirname 的检测通过了
        self.project_dirname = project_dirname

    def _get_blog_groups(self):
        """
        返回博客组 ~/types:blog-group
        """
        logger = self.logger.getChild("_get_blog_groups")

        # 打印当前使用的 project dir 是多少
        logger.debug(messages.PROJECT_DIRECTORY_IS.format(
            self.project_dirname))

        # 迭代出 目录
        # dirs = [item for item in os.listdir(self.project_dirname) if os.path.isdir(
        #    os.path.join(self.project_dirname, item))]
        dirs = []
        for item in os.listdir(self.project_dirname):

            # 拼接出完整的 dir 路径
            dir_full_path = os.path.join(self.project_dirname, item)

    def _get_md_files(self):
        """
        获取项目目录下所有的 md 文件(文件路径)
        """
        # 获取项目目录下所有的 md 文件(文件路径)
        for dirname in os.listdir(self.project_dirname):

            # 迭代出所有的 md 文件
            if not dirname.startswith('.'):

                # 以 . 开头的目录就跳过
                continue

            # 如果可以执行到这里说明，不是 .git 目录

            # 当前要迭代的目录
            current_dirname = os.path.join(self.project_dirname, dirname)
            for md_file in os.listdir(current_dirname):

                # 如果是 md 文件就返回
                if md_file.endswith('.md'):
                    yield os.path.join(current_dirname, md_file)
