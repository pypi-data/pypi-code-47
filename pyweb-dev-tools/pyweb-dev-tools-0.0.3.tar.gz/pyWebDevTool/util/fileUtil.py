#!/usr/bin/env python
# coding=utf8

# 当前文件的路径
import os
import shutil
import sys


def getRootPath():
    pwd = sys.argv[0]
    return getAbsPath(pwd)


def getAbsPath(path):
    if os.path.isfile(path):
        pwd = os.path.abspath(getDirname(path))
        return pwd
    return path


def getDirname(path):
    return os.path.dirname(path)


def getParentPath(path=None):
    if path is None:
        path = getRootPath()
    return os.path.abspath(os.path.dirname(getAbsPath(path)) + os.path.sep + ".")


def getGraderParentPath(path=None):
    if path is None:
        path = getRootPath()
    return os.path.abspath(os.path.dirname(getAbsPath(path)) + os.path.sep + "..")


def listFile(rootDir):
    files = []
    if not os.path.exists(rootDir):
        return files
    __listDir(rootDir, files)
    return files


def __listDir(rootDir, files):
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        files.append(pathname)
        if not os.path.isfile(pathname):
            __listDir(pathname, files)


def delFile(filePath):
    """文件被占用无法使用os.remove删除"""
    cmd = "del /f/q  \"%s\"" % filePath
    os.system(cmd)


def copyFile(src, dest):
    if os.path.exists(dest):
        delFile(dest)
    return shutil.copyfile(src, dest)


def copyFolder(src, dest, override=False, ignore=None):
    if os.path.exists(dest) and not override:
        delDir(dest)
    return copytree(src, dest, ignore=ignore)


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        return True
    else:
        return False


def delDir(path, excluedFile=None, is_del_root=True):
    if not os.path.exists(path):
        return
    filelist = os.listdir(path)  # 列出该目录下的所有文件名
    for f in filelist:
        if excluedFile is not None and f == os.path.basename(excluedFile):
            continue
        filepath = os.path.join(path, f)  # 将文件名映射成绝对路劲
        if os.path.isfile(filepath):  # 判断该文件是否为文件或者文件夹
            os.remove(filepath)  # 若为文件，则直接删除
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)  # 若为文件夹，则删除该文件夹及文件夹内所有文件
    if is_del_root:
        shutil.rmtree(path, True)  # 最后删除总文件夹


def forceMove(sourcePath, targetPath, excluedFiles=None):
    """移动目录下所有文件（夹）到目标目录 文件存在则覆盖"""
    files = listFile(sourcePath)
    for f in files:
        exclude_flag = False
        if excluedFiles is not None:
            for e in excluedFiles:
                if os.path.abspath(f).startswith(os.path.abspath(e)):
                    from pyWebDevTool.util.loggerFactory import Logger
                    logger = Logger()
                    logger.debug("排除的文件：{}".format(f))
                    exclude_flag = True
                    continue
        if not exclude_flag:
            t = targetPath + f.replace(sourcePath, "")
            move(f, t)


def move(sourceFile, targetFile):
    if not os.path.exists(sourceFile):
        raise OSError("源文件不存在：" + sourceFile)
    from pyWebDevTool.util.loggerFactory import Logger
    logger = Logger()
    logger.info("移动覆盖文件（夹）：{}到：{}".format(sourceFile, targetFile))
    if os.path.exists(targetFile):
        if os.path.isfile(sourceFile):
            os.remove(targetFile)
            os.rename(sourceFile, targetFile)
    else:
        if os.path.isfile(sourceFile):
            if not os.path.exists(os.path.dirname(targetFile)):
                os.makedirs(os.path.dirname(targetFile))
            os.rename(sourceFile, targetFile)
        else:
            os.makedirs(targetFile)


def copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2,
             ignore_dangling_symlinks=False):
    """Recursively copy a directory tree.

    The destination directory must not already exist.
    If exception(s) occur, an Error is raised with a list of reasons.

    If the optional symlinks flag is true, symbolic links in the
    source tree result in symbolic links in the destination tree; if
    it is false, the contents of the files pointed to by symbolic
    links are copied. If the file pointed by the symlink doesn't
    exist, an exception will be added in the list of errors raised in
    an Error exception at the end of the copy process.

    You can set the optional ignore_dangling_symlinks flag to true if you
    want to silence this exception. Notice that this has no effect on
    platforms that don't support os.symlink.

    The optional ignore argument is a callable. If given, it
    is called with the `src` parameter, which is the directory
    being visited by copytree(), and `names` which is the list of
    `src` contents, as returned by os.listdir():

        callable(src, names) -> ignored_names

    Since copytree() is called recursively, the callable will be
    called once for each directory that is copied. It returns a
    list of names relative to the `src` directory that should
    not be copied.

    The optional copy_function argument is a callable that will be used
    to copy each file. It will be called with the source path and the
    destination path as arguments. By default, copy2() is used, but any
    function that supports the same signature (like copy()) can be used.

    """
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    os.makedirs(dst, exist_ok=True)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.islink(srcname):
                linkto = os.readlink(srcname)
                if symlinks:
                    # We can't just leave it to `copy_function` because legacy
                    # code with a custom `copy_function` may rely on copytree
                    # doing the right thing.
                    os.symlink(linkto, dstname)
                    shutil.copystat(srcname, dstname, follow_symlinks=not symlinks)
                else:
                    # ignore dangling symlink if the flag is on
                    if not os.path.exists(linkto) and ignore_dangling_symlinks:
                        continue
                    # otherwise let the copy occurs. copy2 will raise an error
                    if os.path.isdir(srcname):
                        copytree(srcname, dstname, symlinks, ignore,
                                 copy_function)
                    else:
                        copy_function(srcname, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks, ignore, copy_function)
            else:
                # Will raise a SpecialFileError for unsupported file types
                copy_function(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except shutil.Error as err:
            errors.extend(err.args[0])
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
    try:
        shutil.copystat(src, dst)
    except OSError as why:
        # Copying file access times may fail on Windows
        if getattr(why, 'winerror', None) is None:
            errors.append((src, dst, str(why)))
    if errors:
        raise shutil.Error(errors)
    return dst


def create_file(filename,default_content=None):
    """
    创建文件
    :param filename:
    :param default_content:
    :return:
    """
    path = filename[0:filename.rfind("/")]
    if not os.path.isdir(path):  # 无文件夹时创建
        os.makedirs(path)
    if not os.path.isfile(filename):  # 无文件时创建
        with open(filename, mode="w", encoding="utf-8") as f:
            if default_content is not None:
                f.write(default_content)
    else:
        pass
