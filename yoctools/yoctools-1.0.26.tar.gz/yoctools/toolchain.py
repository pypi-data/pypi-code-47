#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from .tools import *
import tarfile
import subprocess
import platform
import urllib

if hasattr(urllib, "urlretrieve"):
    urlretrieve = urllib.urlretrieve
else:
    import urllib.request
    urlretrieve = urllib.request.urlretrieve


toolchain_url_64 = "https://cop-image-prod.oss-cn-hangzhou.aliyuncs.com/resource/420257228264570880/1574927493455/csky-elfabiv2-tools-x86_64-minilibc-20191122.tar.gz"
toolchain_url_32 = "https://cop-image-prod.oss-cn-hangzhou.aliyuncs.com/resource/420257228264570880/1574927450819/csky-elfabiv2-tools-i386-minilibc-20191122.tar.gz"

rsicv_url_64 = 'https://cop-image-prod.oss-cn-hangzhou.aliyuncs.com/resource/420262990181302272/1577083328051/riscv64-elf-x86_64-20191111.tar.gz'
rsicv_url_32 = 'https://cop-image-prod.oss-cn-hangzhou.aliyuncs.com/resource/420262990181302272/1577082864564/riscv64-elf-i386-20191111.tar.gz'

all_toolchain_url = {
    'csky-abiv2-elf': [toolchain_url_32, toolchain_url_64],
    'riscv64-unknown-elf': [rsicv_url_32, rsicv_url_64]
}

start_time = time.time()


def Schedule(blocknum, blocksize, totalsize):
    speed = (blocknum * blocksize) / (time.time() - start_time)
    # speed_str = " Speed: %.2f" % speed
    speed_str = " Speed: %sB/S         " % format_size(speed)
    recv_size = blocknum * blocksize

    # 设置下载进度条
    f = sys.stdout
    pervent = recv_size / totalsize
    percent_str = "%.2f%%" % (pervent * 100)
    n = round(pervent * 50)
    s = ('#' * n).ljust(50, '-')
    f.write(percent_str.ljust(8, ' ') + '[' + s + ']' + speed_str)
    f.flush()
    f.write('\r')


def format_size(bytes):
    bytes = float(bytes)
    kb = bytes / 1024
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.3fG" % (G)
        else:
            return "%.3fM" % (M)
    else:
        return "%.3fK" % (kb)


class ToolchainInstall:
    def download(self, arch):
        global start_time
        start_time = time.time()
        toolchain_path = home_path('.thead/' + arch)

        if os.path.exists(toolchain_path):
            return

        architecture = platform.architecture()
        if architecture[0] == '64bit':
            toolchain_url = all_toolchain_url[arch][1]
        else:
            toolchain_url = all_toolchain_url[arch][0]

        tar_path = '/tmp/' + os.path.basename(toolchain_url)
        urlretrieve(toolchain_url, tar_path, Schedule)
        print("")
        with tarfile.open(tar_path, 'r:gz') as tar:
            tar.extractall(toolchain_path)

        os.remove(tar_path)

    def fix_env(self, arch):
        toolchain_path = '$HOME/.thead/%s/bin' % arch
        shell = os.getenv('SHELL')
        shell = os.path.basename(shell)

        if shell == 'zsh':
            rc = home_path('.zshrc')

        elif shell == 'bash':
            rc = home_path('.bashrc')

        with open(rc, 'r') as f:
            contents = f.readlines()

        export_path = ''
        for i in range(len(contents)):
            c = contents[i]
            idx = c.find(' PATH')
            if idx > 0:
                idx = c.find('=')
                if idx >= 0:
                    export_path = c[idx + 1:]

                    if export_path.find(toolchain_path) < 0:
                        export_path = 'export PATH=' + toolchain_path + ':' + export_path
                        contents[i] = export_path

        if not export_path:
            contents.insert(0, 'export PATH=' + toolchain_path + ':$PATH\n\n')

        with open(rc, 'w') as f:
            contents = f.writelines(contents)

    def check_toolchain(self, arch='csky-abiv2-elf'):
        gcc = subprocess.Popen(arch + '-gcc --version', shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        lines = gcc.stdout.readlines()
        for text in lines:
            text = text.decode().strip()
            if text.find('command not found') >= 0:
                self.download(arch)
        self.fix_env(arch)
