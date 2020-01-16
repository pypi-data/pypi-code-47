# This script contains build model for EVE Scripts.
#
# (c) iSYSTEM Labs, 2017

import os
import sys
import subprocess as sp

BUILD_TYPE_DEBUG = 'debug'
BUILD_TYPE_RELEASE = 'release'


class CompilerConfig:
    """
    This class contains configuration for compiler.
    """

    def __init__(self):
        self.ARG_FILE = True  # compiler args are given in file

        self.TOOLS_DIR = '/ISYSTEM_APPS/gcc-arm-none-eabi-4_9-2015q1-20150306/bin'
        self.TOOL = 'arm-none-eabi-g++.exe'

        self.FLAGS = '-pipe -x c++ -std=c++11 -mlittle-endian -g3 {OPT_LEVEL} ' + \
                     '-gdwarf-4 -Wall -march=armv6-m -mthumb -mfloat-abi=soft ' + \
                     '-c -fdata-sections -ffunction-sections -fno-exceptions ' + \
                     '-fno-rtti {DEFINES} {INCLUDES}'

        self.INCLUDE_PATHS = []
        self.DEFINES = []
        self.OBJ_DIR = 'obj'

        # add sources always present with
        self.SRC_DIRS = []      # directory with sources
        self.SRC_INCLUDES = ['.cpp'] # search for files which names end with one of these
                            # strings.
        # add known sources
        self.SOURCES = []

    def doFirst(self, platform, buildType, flavor):
        """
        Called before any changes in model are done by builder. Only data
        defined above is available.
        Parameters:
        platform: for example win32 or x64
        buildType: value of option -t in builder, usually 'debug' or 'release'
        flavor: value of option -f in builder
        """
        pass

    def doLast(self, platform, buildType, flavor):
        """
        Called after all changes to model are applied by builder (for example
        command line args are applied, lists of sources are filled with paths
        to all files to be build, ...), but before compiling takes place.
        All data items have their lowercase counterparts with contents updated
        by the builder. Modify it here if needed.
        """
        if buildType == BUILD_TYPE_RELEASE:
            optLevel = '-O2'
        elif buildType == BUILD_TYPE_DEBUG:
            optLevel = '-Og'
        elif buildType == BUILD_TYPE_CLEAN:
            pass  # nothing to do for clean here
        else:
            raise Exception(("Unsupported build type specified: '{}'\n" +
                             " Should be '{}' or '{}'.").format(buildType,
                                                                BUILD_TYPE_DEBUG,
                                                                BUILD_TYPE_RELEASE))

        incPaths = ''
        if self.include_paths:
            incPaths = '-I' + ' -I'.join(self.include_paths)

        defs = ''
        if self.defines:
            defs = '-D' + ' -D'.join(self.defines)

        self.__cmdLineArgs = self.flags.format(OPT_LEVEL=optLevel,
                                               DEFINES=defs,
                                               INCLUDES=incPaths)


    def getCmdLineArgs(self, objFile, srcFile):

        return self.__cmdLineArgs + ' -o {OBJ_FILE} {SRC_FILE}'.format(OBJ_FILE = objFile,
                                                                       SRC_FILE = srcFile)


class LinkerConfig:
    """
    This class contains configuration for linker.
    """

    def __init__(self):
        self.ARGS_TO_FILE = True   # linker args are given in file

        if sys.platform.startswith('linux'):
            self.TOOLS_DIR = '~/bin/gcc-arm-none-eabi-5_3-2016q1/bin'
            self.TOOL = 'arm-none-eabi-gcc'
        else:
            self.TOOLS_DIR = '/ISYSTEM_APPS/gcc-arm-none-eabi-4_9-2015q1-20150306/bin'
            self.TOOL = 'arm-none-eabi-g++.exe'

        self.OUT_DIR = 'dist'    # elf file is placed here
        self.OUT_FILE = 'sample.elf' # is changed by builder

        self.FLAGS = '-nostartfiles -nodefaultlibs -nostdlib -pipe -mlittle-endian ' + \
                     '-march=armv6-m -mthumb -mfpu=vfp  -g3 -u _vfprintf_float ' + \
                     '-fno-exceptions -fno-rtti ' + \
                     '-Wl,--output={OUT_FILE_PATH},-Map={OUT_FILE_NOEXT}.map,' + \
                     '--script={LINK_SCRIPT},-n,--gc-sections'

        self.LINK_SCRIPT = '../linker/EVE.ind'
        self.LIB_DIRS = [] # dirs added with '-L <libDir>' linker option
        self.LIBS = ['nosys', 'c', 'gcc']  # libraries added with -l<libName> linker option.
                       # This script does not check if these libraries are newer than
                       # output file. See PROJ_LIBS for this functionality.
        self.DEPENDS_ON = []    # files, which modification time is checked against
                       # output file for rebuild - these are usually not std libs,
                       # but libs which we build as part of our project. This list
                       # should contain full paths (abs or rel) to library files,
                       # for example: 'lib/libcomm.a'.
                       # These files are not given to linker, but are used only for
                       # time comparison.


    def postBuild(self, platform, buildType, flavor):
        """
        Creates binary file from elf file.

        Returns abs path to created binary file.
        """
        toolPath = os.path.join(self.tools_dir, 'arm-none-eabi-objcopy.exe')
        args = '-O binary ' + os.path.join(self.out_dir, self.out_file)
        binFName = os.path.splitext(self.out_file)[0] + '.bin'
        binFPath = os.path.join(self.out_dir, binFName)
        args += ' ' + binFPath
        cmdLine = toolPath + ' ' + args
        print('\n---- Binary file:\n    $ ' + cmdLine)

        sp.check_call(cmdLine, shell = True)

        return os.path.abspath(binFPath)


    def getCmdLineArgs(self, outFilePath, linkScript, objFiles):

        outFileNoExt = os.path.split(self.out_file)[0]
        out_file_noext = os.path.split(outFileNoExt)[1]

        args = self.flags.format(OUT_FILE_PATH = outFilePath,
                                 LINK_SCRIPT = linkScript,
                                 OUT_FILE_NOEXT = out_file_noext)

        for libDir in self.lib_dirs:
            args += ' -L ' + libDir

        for objFile in objFiles:
            args += ' ' + objFile

        # Libs must follow obj files, otherwise they are not used by gcc linker!
        for lib in self.libs:
            args += ' -l' + lib

        return args


class BuildModel:
    def __init__(self):
        self.config = [CompilerConfig(), LinkerConfig()]

    def compilerConfig(self):
        return self.config[0]

    def linkerConfig(self):
        return self.config[1]

    def configsList(self):
        return self.config
