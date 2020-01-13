#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import shutil

try:
    from tools import *
    from component import *
    from occ import *
    from log import logger
    from solution import *
except:
    from yoctools.tools import *
    from yoctools.component import *
    from yoctools.occ import *
    from yoctools.log import logger
    from yoctools.solution import *


class YoC:
    def __init__(self):
        self.occ = None
        self.occ_components = None
        self.yoc_path = ''
        self.yoc_version_base = 'v7.2'
        self.yoc_version_id = 0

        # scanning .yoc file directory
        v = current_pwd()
        while v != '/':
            f = os.path.join(v, '.yoc')
            if os.path.exists(f):
                conf = yaml_load(f)
                if 'yoc_version' in conf:
                    self.yoc_version_base = conf['yoc_version']
                if 'commit' in conf:
                    self.yoc_version_id = int(conf['commit'])

                self.yoc_path = v
                break
            v = os.path.dirname(v)

        if self.yoc_path == '':
            self.yoc_path = current_pwd()
            v = os.path.join(self.yoc_path, '.yoc')
            write_file('yoc_version: v7.2\ncommit: 0\n', v)

        self.components = ComponentGroup()

        def scan_directory(path):
            filename = os.path.join(path, 'package.yaml')
            if os.path.isfile(filename):
                pack = Component(filename)

                if pack.version == '':
                    pack.version = self.yoc_version_base + '.%d' % self.yoc_version_id

                if pack.type in ['solution']:
                    if pack.path != current_pwd():
                        return

                if not self.components.add(pack):
                    pre_component = self.components.get(pack.name)
                    logger.error('component `%s` is multiple (%s : %s)' % (pack.name, pre_component.path, pack.path))
                    exit(0)

        # scanning yoc all components
        for path in ['components', 'boards']:
            walk_path = os.path.join(self.yoc_path, path)
            for dirpath, sub_path, _ in os.walk(walk_path):
                for name in sub_path:
                    scan_directory(os.path.join(dirpath, name))
        scan_directory(current_pwd())


    def check_depend(self, component):
        component.load_package()
        for name in component.depends:
            c = self.components.get(name)
            if c:
                c.depends_on.append(component)
                self.check_depend(c)


    def getSolution(self):
        for _, component in self.components.items():
            if component.path == current_pwd():
                self.check_depend(component)
                solution = Solution()
                solution.set_solution(self.components)

                return solution



    def add_component(self, name):
        self.occ_update()
        if self.components.get(name) == None:
            component = self.occ_components.get(name)
            if component:
                for dep in component.depends:
                    self.add_component(dep['name'])
                self.components.add(component)

            return component


    def remove_component(self, name):
        component = self.components.get(name)
        if component:
            if not component.depends_on:                     # 如果没有组件依赖它
                for dep in component.depends:
                    p = self.components.get(dep)
                    if p:
                        if name in p.depends_on:
                            del p.depends_on[name]
                        self.remove_component(dep)

                shutil.rmtree(component.path)
                self.components.remove(component)
                self.components.calc_depend()
                return True
            else:
                logger.info("remove fail, %s depends on:" % component.name)
                for dep in component.depends_on:
                    logger.info('  ' + dep.name)
                return False


    def save_version(self):
        pass
        # v = os.path.join(self.yoc_path, '.yoc')
        # self.yoc_version_id += 1
        # write_file('yoc_version: v7.2\ncommit: %d\n' % self.yoc_version_id, v)


    def upload(self, name):
        component = self.components.get(name)
        if component:
            if not os.path.isdir(os.path.join(component.path, '.git')):
                if self.occ == None:
                    self.occ = OCC()
                self.occ.login()
                zip_file = component.zip(self.yoc_path)
                if self.occ.upload(component.version, component.type, zip_file) == 0:
                    print("component upload success: " + component.name)
                else:
                    print("component upload fail: " + component.name)
                # self.save_version()


    def uploadall(self):
        if self.occ == None:
            self.occ = OCC()
        self.occ.login()
        for _, component in self.components.items():
            zip_file = component.zip(self.yoc_path)
            # self.occ.upload(version_inc(component.version, 1), component.type, zip_file)
            if self.occ.upload(component.version, component.type, zip_file) == 0:
                print("component upload success: " + component.name)
            else:
                print("component upload fail: " + component.name)


    def update(self):
        for _, component in self.components.items():
            component.download(self.yoc_path)
        for _, component in self.components.items():
            if component.type == 'solution':
                genSConstruct(self.components, component.path)


    def occ_update(self):
        if self.occ == None:
            self.occ = OCC()
            self.occ_components = self.occ.yocComponentList('614193542956318720')
            for _, component in self.occ_components.items():
                component.path = os.path.join(self.yoc_path, component.path)


    def list(self):
        for _, component in self.components.items():
            component.load_package()
            component.show()
            # print(component.name)
            # if component.depends:
            #     print('  ', 'depends:')
            #     for v in component.depends:
            #         print('    -', v)
            # if component.depends_on:
            #     print('  ', 'depends_on:')
            #     for p in component.depends_on:
            #         print('    -', p.name)


if __name__ == "__main__":
    yoc = YoC()
    yoc.list()
    # solution = yoc.getSolution()
    # solution.show()
    # for c in solution.components:
    #     c.show()
    #     c.info(4)
