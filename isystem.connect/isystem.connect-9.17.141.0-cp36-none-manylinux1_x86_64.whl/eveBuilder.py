#!python
#
# This script builds EVE Executable. It is not full featured builder, as
# it always compiles all given sources, and does not check dependencies.
# Default dirs are set for compilation from dir EVE/scripts.
#
# Example:
# python -m isystem.eveBuilder -DSoCProbe -v SocProbeDemo.cpp
#
# (c) iSYSTEM Labs d.o.o., 2017

from __future__ import print_function

import os
import re
import sys
import yaml
import shlex
import shutil
import argparse
import subprocess as sp
import importlib
import isystem.buildModel as ibm


# If set to True, more details about each step are printed. Use function
# setVerbose(isVerbose) to modify this value.
__g_verbose = False

# fallback for development only
DEV_TOOLCHAIN_DIR = '/ISYSTEM_APPS/gcc-arm-none-eabi-4_9-2015q1-20150306/bin'
GCC_DIR = 'gcc-arm-none-eabi-4_9-2015q1-20150306/bin'
SCRIPTS_DIR = 'scripts'
LINKER_SCRIPT = 'linker/EVE.ind' # relative to eveDir
EVE_SCRIPT_HEADER = 'EveScript.h'

ST_STATUS_OK = 0         # build succeeded
ST_COMPILE_ERROR = -1    # compilation failed
ST_LINK_ERROR = -2       # linking failed
ST_POST_BUILD_ERROR = -3 # post-build step in model failed

TARGET_PREPARE = 'prepare'
TARGET_BUILD = 'build'
TARGET_CLEAN = 'clean'
TARGET_REBUILD = 'rebuild'
STUB_ENDING = 'Stub.cpp'

LIST_SEPARATOR = ','

EVE_DIR = 'eve'
EVE_STUBS_DIR = 'extPoints/stubs'  # relative to eveDir
EVE_SCRIPT_SHARED_DIR = 'scripts/shared'

EVE_FILE_EXTENSION = '.eve'

# YAML tags in EVE file
EVE_TAG_SOURCES = 'sources'  # user specific sources, abs paths or rel. to curr. dir.
EVE_TAG_INC_PATHS = 'includeDirs'  # user specific inc. dirs
EVE_TAG_EXT_CLASSES = 'extClasses' # deprecated, classes to include are defined in EveScript.h
EVE_TAG_EXT_POINT = 'extPoint'
EVE_TAGS_ALL = [EVE_TAG_SOURCES, EVE_TAG_INC_PATHS, EVE_TAG_EXT_CLASSES]

# standard include paths relative to eveDir
EVE_STD_INC_PATHS = ['EveLib/include', 'extPoints/defs', 'extPoints/stubs', EVE_SCRIPT_SHARED_DIR]

# sources which are always available, relative to eveDir
EVE_STD_SOURCES = ['EveLib/src/EveLog.cpp', 'scripts/shared/EveSys.cpp',
                   '{}/ECLog{}'.format(EVE_STUBS_DIR, STUB_ENDING),
                   '{}/ECHost{}'.format(EVE_STUBS_DIR, STUB_ENDING)]

# IDs of extension points
EXT_POINT_SOC_PROBE = 'SoCProbe'

# Mapping of extension point to classes, which are available at that ext. point
EXT_POINTS_TO_EXT_CLASSES = {
    EXT_POINT_SOC_PROBE: ['ECTargetConnection', 'ECArmSWD', 'ECJTAG']
}

# Build status. 0 means OK, enything else is an error. Use method getStatus()
# to access this value. See constants starting with ST_ from this module
# for possible return values.
__g_retStatus = ST_STATUS_OK

# Error counter used internally in this module.
__g_err_count = 0


def log(txt):
    if __g_verbose:
        print(txt)


def _findFiles(srcDir, extensions):
    """
    Returns the list of files on the given path which have one of the given
    extensions. 'srcDir' is searched recursively. Example:

        findFiles('src', ['.c'])

    may return:

        ['src/main.c', 'src/gui/window.c']

    The '.' in extension is optional

    Parameters:

      srcDir - root directory for searching
      extension - file extension used as a search filter
    """

    listOfFiles = []

    for extension in extensions:
        # add . to extension if not present
        if len(extension) > 0:
            if extension[0] != '.':
                extension = '.' + extension
        else:
            extension = '.'

        for root, dirs, files in os.walk(srcDir):
            for fileName in files:
                if fileName.endswith(extension):
                    listOfFiles.append(os.path.join(root, fileName))

    return listOfFiles


def _prepare(directories):
    """
    Creates directories, if they don't exist.

    Parameters:
      directories - list of directories to create
    """
    log('Prepare dirs:\n    ' + '\n    '.join(directories))

    for directory in directories:
        if not os.path.exists(directory):
            os.mkdir(directory)


# If you'd like to specify obj files in linker files, add line:
#
#     INPUT(@OBJ_FILES@)
#
#   to linker file and call:
#
#     builder.replaceInFile(lnkFile, '@OBJ_FILES@', stringOfNewlineSeparatedObjFiles, newLnkFile)
#
#   and specify the 'newLnkFile' as linker script when calling the linker.
def replaceInFile(fileName, token, replacement, destFileName = None):
    """
    Replaces tokens in file.

    Parameters:
      fileName - name of the file where tokens will be replaced
      token - string to replace
      replacement - new string
      destFileName - destination file. If None, then the input file
                     is also the output file.
    """
    inf = open(fileName, 'r')
    outFName = destFileName
    if destFileName == None:
        outFName = fileName + '.tmp~'

    outf = open(outFName, 'w')
    for line in inf:
        if token in line:
            line = line.replace(token, replacement)
            log(line)

        outf.write(line)

    inf.close()
    outf.close()

    if destFileName == None:
        shutil.move(outFName, fileName)


def replaceRegExInFile(fileName, tokenRegEx, replacement, destFileName = None):
    """
    Replaces regular expressions in file. If 'tokenRegEx' contains
    groups (marked with '()'), they can be referenced in replacement
    with '\\N', where N is a group number, for example r'\\1'. Group
    numbers start with 1.

    Example:

    >>> re.sub("(a)", r"c\1", "abxdas")

    'cabxdcas'

    Parameters:
    fileName - name of the file whre tokens will be replaced
    token - regular expression to replace
    replacement - new string, may contain group references
    destFileName - destination file. If None, then the input file
                   is also the output file.
    """
    inf = open(fileName, 'r')
    outFName = destFileName
    if destFileName == None:
        outFName = fileName + '.tmp~'

    outf = open(outFName, 'w')

    for line in inf:
        line = re.sub(tokenRegEx, replacement, line)

        outf.write(line)

    inf.close()
    outf.close()

    if destFileName == None:
        shutil.move(outFName, fileName)


def isSrcNewer(srcFile, destFile):
    """
    Returns true, if the source file is newer than the dest file.
    If the destination file does not exist, True is returned. The
    source file must exist.

    Parameters:
      srcFile - file name of the source file
      destFile - file name of the destination file
    """

    if not os.path.exists(destFile):
        return True

    srcStat = os.stat(srcFile)
    destStat = os.stat(destFile)

    if srcStat.st_mtime >= destStat.st_mtime:
        return True

    return False


def isSrcNewerList(srcFiles, destFile):
    """
    Returns true, if any of the source files is newer than
    the dest file, or the dest file does not exist. For example,
    if any of object files is newer then output file, True is
    returned.
    """
    if not os.path.exists(destFile):
        return True

    for src in srcFiles:
        if isSrcNewer(src, destFile):
            return True

    return False


def argsToLines(args):
    # replace paths separator, to avoid unwanted escaping
    args = args.replace('\\', '/')
    # use shlex to preserve strings with quotes, eg. 'a "b f"' -> ['a', 'b f']
    lines = shlex.split(args)

    for idx in range(len(lines)):
        lines[idx] += '\n'

    return lines


def compile(compilerCfg):
    """
    This function runs compiler with the given compilerCfg on the given source files.
    It can be used for compiling of C/C++ and assembler sources.

    Parameters:
      compilerCfg - compiler options. See class CompilerConfig in the model
                for an example
    """
    global __g_err_count, __g_retStatus

    print('\n--- Compiling (X - skipped because src is older, + - compiled):')

    compilerPath = os.path.join(compilerCfg.tools_dir, compilerCfg.tool)

    objFiles = []

    for srcFile in compilerCfg.sources:
        try:
            baseFilePath, extension = os.path.splitext(srcFile)
            path, fileNameWOExt = os.path.split(baseFilePath)
            objFileName = os.path.join(compilerCfg.obj_dir, fileNameWOExt + '.o')

            if isSrcNewer(srcFile, objFileName):
                args = compilerCfg.getCmdLineArgs(objFileName, srcFile)

                if compilerCfg.arg_file:
                    argsFileName = os.path.join(compilerCfg.obj_dir, fileNameWOExt + '-args.txt')
                    cmd = compilerPath + ' @' + argsFileName
                    with open(argsFileName, 'wt') as of:
                        of.writelines(argsToLines(args))
                else:
                    cmd = compilerPath + ' ' + args

                print('    +', srcFile)
                log('      $ ' + cmd)
                sys.stdout.flush()
                sp.check_call(cmd, shell = True)
            else:
                print('    X', srcFile)

            objFiles.append(objFileName)
        except sp.CalledProcessError as ex:
            print('Compile Error: ', str(ex), file=sys.stderr)
            __g_retStatus = ST_COMPILE_ERROR
            __g_err_count += 1

    return objFiles


def link(linkerCfg, objFiles):
    """
    This function runs linker with the given linkerCfg on the given object files.

    Parameters:
      linkerCfg - linker configuration. See class LinkerConfig in the main script
                  for an example
      objFiles - list of object files to link
    """
    global __g_err_count, __g_retStatus

    linkerPath = os.path.join(linkerCfg.tools_dir, linkerCfg.tool)

    outFileName = os.path.join(linkerCfg.out_dir, linkerCfg.out_file)
    args = linkerCfg.getCmdLineArgs(outFileName, linkerCfg.link_script, objFiles)

    print('\n--- Linking: {}\n    '.format(outFileName), end='')
    log('\n    '.join(objFiles))

    if hasattr(linkerCfg, 'arg_file') and linkerCfg.arg_file:
        argsFileName = os.path.join(linkerCfg.out_dir, 'args.txt')
        cmdLine = linkerPath + ' @' + argsFileName
        with open(argsFileName, 'wt') as of:
            of.writelines(argsToLines(args))
    else:
        cmdLine = linkerPath + ' ' + args

    try:
        if isSrcNewerList(objFiles, outFileName) or isSrcNewerList(linkerCfg.depends_on,
                                                                   outFileName):
            log('\n    $ ' + cmdLine + '\n')

            sys.stdout.flush()
            sp.check_call(cmdLine, shell = True)
        else:
            print('\n    X ', outFileName, file=sys.stdout)
    except sp.CalledProcessError as ex:
        print('Link Error: ', str(ex), file=sys.stderr)
        __g_retStatus = ST_LINK_ERROR
        __g_err_count += 1


def _cleanDir(dirName):
    """
    Removes all files from the given directory.
    """
    log('Removing dir: ' + dirName)
    if os.path.exists(dirName):
        shutil.rmtree(dirName)


def _statusToStr():
    if __g_retStatus == ST_STATUS_OK:
        return 'OK!'
    elif __g_retStatus == ST_COMPILE_ERROR:
        return str(__g_err_count) + ' COMPILE ERROR(S)!'
    elif __g_retStatus == ST_LINK_ERROR:
        return str(__g_err_count) + ' LINK ERROR(S)!'
    elif __g_retStatus == ST_POST_BUILD_ERROR:
        return str(__g_err_count) + ' POST-BUILD ERROR(S)!'
    else:
        return str(__g_err_count) + ' ERROR(S)!'


def printStatus():
    """
    Prints build status to stdout - this function should be called
    after build to see build result.
    """
    print('\n' + _statusToStr(), file=sys.stdout)


def getBuildStatus():
    """
    Returns build status, which can be one of:
      ST_STATUS_OK
      ST_COMPILE_ERROR
      ST_LINK_ERROR
      ST_POST_BUILD_ERROR
    """
    return __g_retStatus


def setVerbose(isVerbose):
    """
    Sets logging verbosity to True (verbose) or False (only errors).
    """
    global __g_verbose
    __g_verbose = isVerbose


def _target_clean(model):
    _cleanDir(model.compilerConfig().obj_dir)
    _cleanDir(model.linkerConfig().out_dir)


# Targets are defined as functions with the name 'target_' + <target name>
def _target_prepare(model):
    _prepare([model.compilerConfig().obj_dir, model.linkerConfig().out_dir])


def _target_build(model):
    _target_prepare(model)
    objFiles = compile(model.compilerConfig())

    # objFiles += compile(model.assemblerConfig)  TODO: add assembler opts to model

    if getBuildStatus() == ST_STATUS_OK:
        link(model.linkerConfig(), objFiles)


def _target_rebuild(model):
    _target_clean(model)
    _target_build(model)


def _execBuildTargets(model, buildAction):

    if buildAction == TARGET_BUILD:
        _target_build(model)
    elif buildAction == TARGET_REBUILD:
        _target_rebuild(model)


def loadJson(jsonfName):
    with open(jsonfName) as inf:
        return json.load(inf)


def loadYAML(yamlFName):
    """
    Loads the given YAML file and returns mapping.
    Throws yaml.YAMLError in case of an error.
    """
    with open(yamlFName) as inf:
        return yaml.load(inf)


def _determineAction(opts):

    if opts.cleanAction:
        if opts.buildAction or opts.rebuildAction:
            raise Exception("Only one of actions '-c', '-b', or '-r' is allowed!")
        return TARGET_CLEAN

    if opts.buildAction and opts.rebuildAction:
        raise Exception("Only one of actions '-b', or '-r' is allowed!")

    if not opts.inputFiles:
        raise Exception("For build (-b) and rebuild (-r) actions at least one input " +
                        "file must be specified!")

    if opts.buildAction:
        return TARGET_BUILD

    if opts.rebuildAction:
        return TARGET_REBUILD

    # select default action if none is specified
    return TARGET_BUILD


def getEveDir(eveDir):
    """
    Returns dir where Eve sources provided by iSYSTEM are installed,
    as given in cmd line.
    """
    if eveDir:
        if not os.path.exists(EVE_DIR):
            raise Exception("Directory '" + EVE_DIR + "' not found in winIDEA install dir!\n" +
                            'Invalid dir specified in command line: ' + eveDir)
        return eveDir

    raise Exception("Option '-e' is mandatory.")


def _getToolchainDir(toolchainDir):
    """
    Returns dir where winIDEA is installed as given in cmd line or
    relative to Python interpreter. GCC is located there.
    """
    if toolchainDir:
        if not os.path.exists(toolchainDir):
            raise Exception("Directory with toolchain not found!\n" +
                            'Invalid dir specified in command line: ' + toolchainDir)
        return toolchainDir

    # If not specified in cmd line, assume this Python interpreter
    # belongs to winIDEA
    pyPath = os.path.split(sys.executable)
    if len(pyPath) < 2:
        raise Exception('Can not deduce toolchain dir from Python executable!\n' +
                        'Specify toolchain dir in command line, or run this script\n' +
                        'with Python which comes with winIDEA.')

    pyPath = os.path.split(pyPath[0])

    if len(pyPath) < 2:
        raise Exception('Can not deduce toolchain dir from Python executable path!\n' +
                        'Specify toolchain dir in command line, or run this script\n' +
                        'with Python which comes with winIDEA.')

    toolchainDir = os.path.join(pyPath[0], GCC_DIR)
    if not os.path.exists(toolchainDir):

        # fallback used for development
        if os.path.exists(DEV_TOOLCHAIN_DIR):
            return DEV_TOOLCHAIN_DIR

        raise Exception("Can not deduce '" + GCC_DIR + "' dir from Python executable path!\n" +
                        "Dir does not exist:\n" + toolchainDir +
                        '\nSpecify toolchain dir in command line, or run this script\n' +
                        'with Python which comes with winIDEA.')

    return toolchainDir


def _preprocessModel(model, eveDir):
    sources = model.compilerConfig().sources

    for srcDir in model.compilerConfig().src_dirs:

        fileList = _findFiles(srcDir, model.compilerConfig().src_includes)

        log("Scanned dir '{0}' for sources, found {1} files:\n     ".format(srcDir,
                                                                            len(fileList))
            + '\n      '.join(fileList))

        sources.extend(fileList)

    model.compilerConfig().c_sources = sources

    model.linkerConfig().link_script = os.path.join(eveDir, LINKER_SCRIPT)


def _addStdSources(model, eveDir):
    sources = model.compilerConfig().sources

    for stdSrc in EVE_STD_SOURCES:
        sources.append(os.path.join(eveDir, stdSrc))

    for stdInc in EVE_STD_INC_PATHS:
        model.compilerConfig().include_paths.append(os.path.join(eveDir, stdInc))


def _classAttrsToInstanceAttrs(obj):
    """
    All upper case attributes in model are stored to the given object
    with lowercase names. Upper case items should be left const, while
    lower case counterparts are modified by builder and methods in model.
    """
    attrs = dir(obj)
    for attr in attrs:
        if attr[0].isupper():
            setattr(obj, attr.lower(), getattr(obj, attr))


def _doFirst(model, buildType):
    """
    Calls method in model, if exists.
    """
    for config in model.configsList():
        if hasattr(config, 'doFirst'):
            # TODO opts.doFirst(opts.platform, opts.buildType, opts.flavor)
            config.doFirst('', buildType, '')


def _doLast(model, buildType):
    """
    Calls method in model, if exists.
    """
    for config in model.configsList():
        if hasattr(config, 'doLast'):
            config.doLast('', buildType, '')


def _postBuild(model, buildType):
    """
    Calls method in model, if exists.
    Returns abs path to output binary file.
    """
    global __g_retStatus

    for config in model.configsList():
        if hasattr(config, 'postBuild'):
            try:
                return config.postBuild('', buildType, '')
            except Exception as ex:
                print('Post-build error:', ex)
                __g_retStatus = ST_POST_BUILD_ERROR


# Eve specific code
def _extractYAML(line, isInCfgBlock):
## def _extractYAML(line: str, isInCfgBlock: bool) -> typing.Tuple[str, bool]:

    line = line.strip()

    if line.startswith('/*{'):
        isInCfgBlock = True
        line = line[2:]  # strip '/*'

    if isInCfgBlock:
        if line.endswith('}*/'):
            isInCfgBlock = False
            line = line[:-2]  # strip '*/'

        return line, isInCfgBlock

    return None, isInCfgBlock


def _loadCfgFromSourceFile(srcFName):

    cfgStr = ''
    isInCfgBlock = False

    with open(srcFName) as inf:
        for line in inf:
            yamlLine, isInCfgBlock = _extractYAML(line, isInCfgBlock)
            if yamlLine:
                cfgStr += yamlLine

    return cfgStr


def _loadModelFromCpp(inputFile):
    yamlData = _loadCfgFromSourceFile(inputFile)
    yamlMap = yaml.load(yamlData)
    if yamlMap == None:
        yamlMap = {}

    return yamlMap


def _parseEveScriptHeader(eveDir, extPointId):
##def _parseEveScriptHeader(eveDir: str, extPointId: str) -> map:
    """
    Parses EveScript.h and extracts YAML configuration for the given
    ext. point ID.
    """

    eveScriptFPath = os.path.join(eveDir, EVE_SCRIPT_SHARED_DIR, EVE_SCRIPT_HEADER)
    isInIfdef = False
    isExtPointFound = False
    isInYamlBlock = False
    yamlCfg = ''

    with open(eveScriptFPath) as inf:

        # Example: #ifdef EXT_PT_SoCWI  // some comment
        ifdefPattern = re.compile(r'\s*#ifdef\s+' + extPointId + r"\s*($|/.*)")
        # incPattern = re.compile(r'\s*#include\s+"(.*).h"')
        endifPattern = re.compile(r'\s*#endif')

        for line in inf:
            if re.match(ifdefPattern, line):
                isInIfdef = True
                isExtPointFound = True

            if isInIfdef:
                yamlLine, isInYamlBlock = _extractYAML(line, isInYamlBlock)
                if yamlLine:
                    yamlCfg += yamlLine

                if re.match(endifPattern, line):
                    break; # all includes for ext. p. must be in one ifdef block.

    if not isExtPointFound:
        ##raise Exception(f"Missing extension point definition in {EVE_SCRIPT_HEADER}"
        ##                f" or invalid ext. point ID was specified: {extPointId}")
        raise Exception("Missing extension point definition in {}"
                        " or invalid ext. point ID: {}".format(EVE_SCRIPT_HEADER, extPointId))

    yamlMap = yaml.load(yamlCfg)
    if not yamlMap:  # should not be None or empty
        ##raise Exception(f"Missing configuration in {EVE_SCRIPT_HEADER}, ext. point ID: {extPointId}")
        raise Exception("Missing configuration in {}, ext. point ID: {}"
                        .format(EVE_SCRIPT_HEADER, extPointId))

    return yamlMap


def _cmdLineToModel(model, extPointId, toolchainDir, outDir, argFile):
    """
    Modifies the model from buildModel.py according to cmd line opts.
    """

    toolchainDir = _getToolchainDir(toolchainDir)

    model.compilerConfig().defines.append(extPointId)
    model.compilerConfig().tools_dir = toolchainDir

    model.linkerConfig().tools_dir = toolchainDir
    log('Toolchain dir: ' + model.linkerConfig().tools_dir)

    #if opts.callbacks:
    #    callbacks = opts.callbacks.split(LIST_SEPARATOR)
    #    log('Callback sources:')
    #    for cb in callbacks:
    #        cbFName = os.path.join(opts.eveDir, EVE_STUBS_DIR, cb + STUB_ENDING)
    #        model.compilerConfig().sources.append(cbFName)
    #        log('    ' + cbFName)

    if outDir:
        model.linkerConfig().out_dir = outDir

    if argFile:
        cfgList = model.configsList()
        for cfg in cfgList:
            cfg.arg_file = True

    log('Output dir: ' + model.linkerConfig().out_dir)


def _verifyUserCfg(userCfg):
    """ Check that only valid tags are used. """
    for tag in userCfg:
        if not tag in EVE_TAGS_ALL:
            ##raise Exception(f"Unknown tag in EveScript.h, configuration for ext. point '{extPointId}'. Available tags: " +
            ##                str(EVE_TAGS_ALL))
            raise Exception("Unknown tag in EveScript.h, configuration for ext. point '{}'. Available tags: "
                            .format(extPointId) + str(EVE_TAGS_ALL))


def _addInfoToModel(model, eveFilePath, eveDir, userCfg, sourceName):
    if EVE_TAG_SOURCES in userCfg:
        log('Adding sources from configuration in {}.'.format(sourceName))
        for eveSourceFile in userCfg[EVE_TAG_SOURCES]:
            if os.path.isabs(eveSourceFile):
                eveSrcWPath = eveSourceFile
            else:
                eveSrcWPath = os.path.join(eveFilePath, eveSourceFile)
            model.compilerConfig().sources.append(eveSrcWPath)
            log('    ' + eveSrcWPath)

    # EVE_TAG_EXT_POINT = 'extPoint'  # move to start of file
    # if EVE_TAG_EXT_POINT in userCfg:
    #    extPoint = userCfg[EVE_TAG_EXT_POINT]
    #    if extPoint in EXT_POINTS_TO_EXT_CLASSES:
    #        extClasses = EXT_POINTS_TO_EXT_CLASSES[extPoint]
    #    else:
    #        availExtPoints = str(list(EXT_POINTS_TO_EXT_CLASSES.keys()))
    #        raise Exception('Unknown extension point: ' + extPoint +
    #                        '\nAvailable ext. points: ' + availExtPoints)

    if EVE_TAG_EXT_CLASSES in userCfg:
        log('Adding stubs for extension classes from configuration in {}.'
            .format(sourceName))

        for eveExtPoint in userCfg[EVE_TAG_EXT_CLASSES]:
            eveSrcWPath = os.path.join(eveDir, EVE_STUBS_DIR, eveExtPoint + STUB_ENDING)
            model.compilerConfig().sources.append(eveSrcWPath)
            log('    ' + eveSrcWPath)

    if EVE_TAG_INC_PATHS in userCfg:
        log('Adding include paths from configuration in {}.'.format(sourceName))
        for incPath in userCfg[EVE_TAG_INC_PATHS]:
            if os.path.isabs(incPath):
                eveIncPath = incPath
            else:
                eveIncPath = os.path.join(eveFilePath, incPath)
                model.compilerConfig().include_paths.append(eveIncPath)
                log('    ' + eveIncPath)

    log('All include paths:\n    ' + '\n    '.join(model.compilerConfig().include_paths))


def _eveFileToModel(model, eveDir, inputFile, extPointId):

    print("Building '{}' ...".format(inputFile))

    eveFilePath, fNameWOPath = os.path.split(inputFile)

    if inputFile.lower().endswith(EVE_FILE_EXTENSION): # deprecated, replaced by EveScript.h
        userCfg = loadYAML(inputFile)
        if not EVE_TAG_SOURCES in userCfg:
            raise Exception("No script source specified in eve file. "
                            + "Specify it as 'sources: ['<fname>']")
        _verifyUserCfg(userCfg)
        _addInfoToModel(model, eveFilePath, eveDir, userCfg, inputFile)

    # use config from EveScript.h
    userCfg = _parseEveScriptHeader(eveDir, extPointId)
    _verifyUserCfg(userCfg)
    if not EVE_TAG_SOURCES in userCfg: # tag 'sources' is optional
        userCfg[EVE_TAG_SOURCES] = []
    userCfg[EVE_TAG_SOURCES].append(fNameWOPath)
    _addInfoToModel(model, eveFilePath, eveDir, userCfg, EVE_SCRIPT_HEADER)

    # use config from user script (.cpp)
    userCfg = _loadModelFromCpp(inputFile)
    _verifyUserCfg(userCfg)
    _addInfoToModel(model, eveFilePath, eveDir, userCfg, inputFile)

    # define output file name
    inFName = os.path.splitext(inputFile)[0]
    inFNamePath = os.path.split(inFName)
    if len(inFNamePath) != 2:
        raise Exception("Input file name should have name and extension: " + inputFile)
    model.linkerConfig().out_file = inFNamePath[1] + '.elf'
    log('Executable name: ' + model.linkerConfig().out_file)



def _getEveDirFromSrcFilePath(inFile):
    absPath = os.path.abspath(inFile)
    while True:
        absPath, folder = os.path.split(absPath)
        if folder == SCRIPTS_DIR:
            return absPath  # path points to eveDir, which is normally one dir above 'scripts'

        if not folder:
            break

    raise Exception("eveDir is not specified, and script is not located in 'scripts' "
                    "subdirectory of eveDir. Please specify eveDir parameter")


def _parseCmdLineOptions():

    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

    parser.add_argument("--toolchainDir", dest='toolchainDir', action = 'store',
                        default = '',
                        help="Defines dir, where GCC toolchain is located, "
                        "usually the last item is 'bin'. "
                        "If not specified, toolchain is assumed to be in ../'" + GCC_DIR +
                        "' relative to "
                        "location of Python executable running this script.")

    parser.add_argument("-e", "--eveDir", dest="eveDir", action = 'store', default = '',
                        help="Specifies directory where standard sources for eve build "
                        + "are located.\nMandatory option.")

    # disabled, since callbacks can not be implemented by users
    # parser.add_argument("-s", "--callbacks", dest="callbacks", action = 'store',
    #                    default = 'stubs',
    #                    help="Specifies list of paths containing callback implementations.\n" +
    #                         "Paths should be relative to eve dir. File names must be " +
    #                         "without extension.\nExtension '.cpp' is automatically added.")

    parser.add_argument("-d", "--outDir", dest="outDir", action = 'store', default = '',
                        help="Specifies directory for storing Eve executables. " +
                        "default is current dir.")

    parser.add_argument("-t", "--buildType", dest="buildType", action = 'store',
                        default = 'release',
                        help="Selects build type, can be 'release' (default) or 'debug'.")

    parser.add_argument("-v", dest="isVerbose", action = 'store_true', default = False,
                        help="produce more output about build steps.")

    parser.add_argument("-c", dest="cleanAction", action = 'store_true', default = False,
                        help="'clean' target. Output directory is removed.")

    parser.add_argument("-b", dest="buildAction", action = 'store_true', default = False,
                        help="'build' target, compilation and linking is executed. This "
                        "is also the default action if neither -c, -b, or -r are specified.")

    parser.add_argument("-r", dest="rebuildAction", action = 'store_true', default = False,
                        help="'rebuild' target, first performs clean, then build.")

    parser.add_argument("--argfile", dest="argFile", action = 'store_true', default = False,
                        help="If specified, args for tools are written to file, otherwise setting "
                        + "in model is used. By default args are given in cmd line.")

    requiredArgs = parser.add_argument_group('required arguments')
    requiredArgs.add_argument("-D", dest="extPointId", action = 'store', required = True,
                              help="Specifies extension point ID, must be specified.")

    parser.add_argument('inputFiles', metavar = 'inputFiles', type = str, nargs='*',
                        help='list of EVE scripts to build. All scripts are built '
                        + 'with the same set of options. At least one must be '
                        + 'specified for build options (-b or -r).')


    options = parser.parse_args()

    return options


def build(inFile, extPointId,
          buildAction = TARGET_BUILD,
          buildType = ibm.BUILD_TYPE_RELEASE,
          eveDir = '', toolchainDir = '', outDir = '', argFile = False):
    """
    The main entry point when called from other modules.
    Parameters:
        inFile - eve file or script source. Set it to 'None' if buildAction == TARGET_CLEAN
        buildAction - one of TARGET_CLEAN, TARGT_BUILD, or TARGT_REBUILD
        buildType - one of TARGET_CLEAN, TARGET_BUILD, TARGET_REBUILD
        eveDir - directory where EVE lib and extension points are located. If empty,
                 it is assumed that script is located in <eveDir>/scripts or subdir,
                 and eveDir is deduced from this information.
        toolchainDir - directory where GCC is located. If empty string,
                       GCC from winIDEA distribution is used.
        outDir - output directory for compiled script binary. If empty,
                 <eveDir>/dist is used
        argFile - if True, arguments are passed to GCC in text file.

    Returns abs. path to output bin file.

    Usage example:

        import eveBuilder

        eveBuilder.setVerbose(<True | False>)
        buildAction = <eveBuilder.TARGET_CLEAN | eveBuilder.TARGT_BUILD | eveBuilder.TARGET_REBUILD>

        if buildAction == TARGET_CLEAN:
            eveBuilder.build(None, buildAction, buildType, eveDir,
                                toolchainDir, outDir, argFile)
        else:
            eveBuilder.build(srcFile, buildAction, buildType, eveDir,
                                toolchainDir, outDir, argFile)

        eveBuilder.printStatus()
        buildStatus = eveBuilder.getBuildStatus()

    """
    __g_retStatus = ST_STATUS_OK
    __g_err_count = 0

    model = ibm.BuildModel()

    _classAttrsToInstanceAttrs(model.compilerConfig())
    _classAttrsToInstanceAttrs(model.linkerConfig())

    _doFirst(model, buildType)

    if not inFile is None:
        if not eveDir:
            eveDir = _getEveDirFromSrcFilePath(inFile)
        _addStdSources(model, eveDir)
        _eveFileToModel(model, eveDir, inFile, extPointId)

    _cmdLineToModel(model, extPointId, toolchainDir, outDir, argFile)
    _preprocessModel(model, eveDir)

    _doLast(model, buildType)

    if buildAction == TARGET_CLEAN:
        _target_clean(model)
    else:
        _execBuildTargets(model, buildAction)
        if getBuildStatus() == ST_STATUS_OK:
            binFPath = _postBuild(model, buildType)

        if getBuildStatus() != ST_STATUS_OK:
            raise Exception(_statusToStr())

        return binFPath


def main():
    """
    The main entry, when this script is run standalone from command line.
    Provide option -h to see available options.
    """

    # modelModule = importlib.import_module('buildModel')
    opts = _parseCmdLineOptions()

    setVerbose(opts.isVerbose)

    buildAction = _determineAction(opts)

    if buildAction == TARGET_CLEAN:
        build(None, buildAction, opts.buildType, opts.eveDir,
                 opts.toolchainDir, opts.outDir, opts.argFile)

    # each input file defines one executable
    binFilePaths = []
    for inFile in opts.inputFiles:
        binFName = build(inFile, opts.extPointId, buildAction, opts.buildType,
                         opts.eveDir, opts.toolchainDir, opts.outDir, opts.argFile)
        binFilePaths.append(binFName)

    print("Compiled script(s):\n-", "- ".join(binFilePaths))
    printStatus()
    sys.exit(getBuildStatus())


if __name__ == '__main__':
    main()
