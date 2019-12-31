""" ROCm-SMI (System Management Interface) Tool

This tool provides a user-friendly interface for manipulating
the ROCK (Radeon Open Compute Kernel) via sysfs files.
Please view the README.md file for more information
"""

import os
import re
import sys
from subprocess import check_output
import collections
import logging

from .exception import NoRocmDeviceError, GenericRocmError, RocmUtilFetchError, RocmMemFetchError

# Version of the JSON output used to save clocks
CLOCK_JSON_VERSION = 1

# Set to 1 if an error occurs
RETCODE = 0

# If we want JSON format output instead
PRINT_JSON = False
JSON_DATA = {}

# SMI version. Can't use git describe since rocm-smi in /opt/rocm won't
# have git in that folder. Increment this as needed.
# Major version - Increment when backwards-compatibility breaks
# Minor version - Increment when adding a new feature, set to 0 when major is incremented
# Patch version - Increment when adding a fix, set to 0 when minor is incremented
__version__ = '1.3.1'


def relaunchAsSudo():
    """ Relaunch the SMI as sudo

    To write to sysfs, the SMI requires root access. Use execvp to relaunch the
    script with sudo privileges
    """
    if os.geteuid() != 0:
        os.execvp('sudo', ['sudo'] + sys.argv)


drmprefix = '/sys/class/drm'
hwmonprefix = '/sys/class/hwmon'
debugprefix = '/sys/kernel/debug/dri'
moduleprefix = '/sys/module'
kfdprefix = '/sys/class/kfd/kfd'

headerString = 'ROCm System Management Interface'
footerString = 'End of ROCm SMI Log'

# 80 characters for string and '=' fillers will be the soft-max
headerSpacer = '=' * int((80 - (len(headerString))) / 2)
footerSpacer = '=' * int((80 - (len(footerString))) / 2)

# If the string has an odd number of digits, pad with a space for symmetry
if len(headerString) % 2:
    headerString += ' '
if len(footerString) % 2:
    footerString += ' '
logSpacer = '=' * 80

# These are the valid clock types that can be returned/modified,
# dcefclk (only supported on Vega10 and later)
# fclk (only supported on Vega20 and later)
# mclk
# pcie (PCIe speed, sometimes referred to as lclk for Link clock
# sclk
# socclk (only supported on Vega10 and later)
validClockNames = ['dcefclk', 'fclk', 'mclk', 'pcie', 'sclk', 'socclk']

# These are the valid memory info types that are currently supported
# vram
# vis_vram (Visible VRAM)
# gtt
validMemTypes = ['vram', 'vis_vram', 'gtt']

# These are the types of supported RAS blocks and their respective enums
validRasBlocks = {'fuse': 1 << 13, 'mp1': 1 << 12, 'mp0': 1 << 11, 'sem': 1 << 10, 'smn': 1 << 9,
                  'df': 1 << 8, 'xgmi_wafl': 1 << 7, 'hdp': 1 << 6, 'pcie_bif': 1 << 5,
                  'athub': 1 << 4, 'mmhub': 1 << 3, 'gfx': 1 << 2, 'sdma': 1 << 1, 'umc': 1 << 0}
# These are the valid input types to a RAS file
validRasActions = ['disable', 'enable', 'inject']
# Right now, these are the only supported memory error types,
# ue - Uncorrectable error; ce - Correctable error
validRasTypes = ['ue', 'ce']

# List of software components that we support printing versioning information
validVersionComponents = ['driver']

# Supported firmware blocks
validFwBlocks = {'vce', 'uvd', 'mc', 'me', 'pfp',
'ce', 'rlc', 'rlc_srlc', 'rlc_srlg', 'rlc_srls',
'mec', 'mec2', 'sos', 'asd', 'ta_ras', 'ta_xgmi',
'smc', 'sdma', 'sdma2', 'vcn', 'dmcu'}

# These are the different Retired Page types defined in the kernel,
# and their respective letter-representation in the sysfs interface
validRetiredType = ['retired', 'pending', 'unreservable', 'all']

valuePaths = {
    'id': {'prefix': drmprefix, 'filepath': 'device', 'needsparse': True},
    'sub_id': {'prefix': drmprefix, 'filepath': 'subsystem_device', 'needsparse': False},
    'vbios': {'prefix': drmprefix, 'filepath': 'vbios_version', 'needsparse': False},
    'perf': {'prefix': drmprefix, 'filepath': 'power_dpm_force_performance_level', 'needsparse': False},
    'sclk_od': {'prefix': drmprefix, 'filepath': 'pp_sclk_od', 'needsparse': False},
    'mclk_od': {'prefix': drmprefix, 'filepath': 'pp_mclk_od', 'needsparse': False},
    'dcefclk': {'prefix': drmprefix, 'filepath': 'pp_dpm_dcefclk', 'needsparse': False},
    'fclk': {'prefix': drmprefix, 'filepath': 'pp_dpm_fclk', 'needsparse': False},
    'mclk': {'prefix': drmprefix, 'filepath': 'pp_dpm_mclk', 'needsparse': False},
    'pcie': {'prefix': drmprefix, 'filepath': 'pp_dpm_pcie', 'needsparse': False},
    'sclk': {'prefix': drmprefix, 'filepath': 'pp_dpm_sclk', 'needsparse': False},
    'socclk': {'prefix': drmprefix, 'filepath': 'pp_dpm_socclk', 'needsparse': False},
    'clk_voltage': {'prefix': drmprefix, 'filepath': 'pp_od_clk_voltage', 'needsparse': False},
    'voltage': {'prefix': hwmonprefix, 'filepath': 'in0_input', 'needsparse': False},
    'profile': {'prefix': drmprefix, 'filepath': 'pp_power_profile_mode', 'needsparse': False},
    'use': {'prefix': drmprefix, 'filepath': 'gpu_busy_percent', 'needsparse': False},
    'use_mem': {'prefix': drmprefix, 'filepath': 'mem_busy_percent', 'needsparse': False},
    'pcie_bw': {'prefix': drmprefix, 'filepath': 'pcie_bw', 'needsparse': False},
    'replay_count': {'prefix': drmprefix, 'filepath': 'pcie_replay_count', 'needsparse': False},
    'unique_id': {'prefix': drmprefix, 'filepath': 'unique_id', 'needsparse': False},
    'serial': {'prefix': drmprefix, 'filepath': 'serial_number', 'needsparse': False},
    'vendor': {'prefix': drmprefix, 'filepath': 'vendor', 'needsparse': False},
    'sub_vendor': {'prefix': drmprefix, 'filepath': 'subsystem_vendor', 'needsparse': False},
    'fan': {'prefix': hwmonprefix, 'filepath': 'pwm1', 'needsparse': False},
    'fanmax': {'prefix': hwmonprefix, 'filepath': 'pwm1_max', 'needsparse': False},
    'fanmode': {'prefix': hwmonprefix, 'filepath': 'pwm1_enable', 'needsparse': False},
    'temp1': {'prefix': hwmonprefix, 'filepath': 'temp1_input', 'needsparse': True},
    'temp1_label': {'prefix': hwmonprefix, 'filepath': 'temp1_label', 'needsparse': False},
    'temp2': {'prefix': hwmonprefix, 'filepath': 'temp2_input', 'needsparse': True},
    'temp2_label': {'prefix': hwmonprefix, 'filepath': 'temp2_label', 'needsparse': False},
    'temp3': {'prefix': hwmonprefix, 'filepath': 'temp3_input', 'needsparse': True},
    'temp3_label': {'prefix': hwmonprefix, 'filepath': 'temp3_label', 'needsparse': False},
    'power': {'prefix': hwmonprefix, 'filepath': 'power1_average', 'needsparse': True},
    'power_cap': {'prefix': hwmonprefix, 'filepath': 'power1_cap', 'needsparse': False},
    'power_cap_max': {'prefix': hwmonprefix, 'filepath': 'power1_cap_max', 'needsparse': False},
    'power_cap_min': {'prefix': hwmonprefix, 'filepath': 'power1_cap_min', 'needsparse': False},
    'dpm_state': {'prefix': drmprefix, 'filepath': 'power_dpm_state', 'needsparse': False},
    'vram_used': {'prefix': drmprefix, 'filepath': 'mem_info_vram_used', 'needsparse': False},
    'vram_total': {'prefix': drmprefix, 'filepath': 'mem_info_vram_total', 'needsparse': False},
    'vis_vram_used': {'prefix': drmprefix, 'filepath': 'mem_info_vis_vram_used', 'needsparse': False},
    'vis_vram_total': {'prefix': drmprefix, 'filepath': 'mem_info_vis_vram_total', 'needsparse': False},
    'vram_vendor': {'prefix': drmprefix, 'filepath': 'mem_info_vram_vendor', 'needsparse': False},
    'gtt_used': {'prefix': drmprefix, 'filepath': 'mem_info_gtt_used', 'needsparse': False},
    'gtt_total': {'prefix': drmprefix, 'filepath': 'mem_info_gtt_total', 'needsparse': False},
    'ras_gfx': {'prefix': drmprefix, 'filepath': 'ras/gfx_err_count', 'needsparse': False},
    'ras_umc': {'prefix': drmprefix, 'filepath': 'ras/umc_err_count', 'needsparse': False},
    'ras_mmhub': {'prefix': drmprefix, 'filepath': 'ras/mmhub_err_count', 'needsparse': False},
    'ras_athub': {'prefix': drmprefix, 'filepath': 'ras/athub_err_count', 'needsparse': False},
    'ras_sdma': {'prefix': drmprefix, 'filepath': 'ras/sdma_err_count', 'needsparse': False},
    'ras_pcie_bif': {'prefix': drmprefix, 'filepath': 'ras/pcie_bif_err_count', 'needsparse': False},
    'ras_hdp': {'prefix': drmprefix, 'filepath': 'ras/hdp_err_count', 'needsparse': False},
    'ras_xgmi_wafl': {'prefix': drmprefix, 'filepath': 'ras/xgmi_wafl_err_count', 'needsparse': False},
    'ras_df': {'prefix': drmprefix, 'filepath': 'ras/df_err_count', 'needsparse': False},
    'ras_smn': {'prefix': drmprefix, 'filepath': 'ras/smn_err_count', 'needsparse': False},
    'ras_sem': {'prefix': drmprefix, 'filepath': 'ras/sem_err_count', 'needsparse': False},
    'ras_mp0': {'prefix': drmprefix, 'filepath': 'ras/mp0_err_count', 'needsparse': False},
    'ras_mp1': {'prefix': drmprefix, 'filepath': 'ras/mp1_err_count', 'needsparse': False},
    'ras_fuse': {'prefix': drmprefix, 'filepath': 'ras/fuse_err_count', 'needsparse': False},

    'xgmi_err': {'prefix': drmprefix, 'filepath': 'xgmi_error', 'needsparse': False},
    'ras_features': {'prefix': drmprefix, 'filepath': 'ras/features', 'needsparse': True},
    'bad_pages': {'prefix': drmprefix, 'filepath': 'ras/gpu_vram_bad_pages', 'needsparse': False},
    'ras_ctrl': {'prefix': debugprefix, 'filepath': 'ras/ras_ctrl', 'needsparse': False},
    'gpu_reset': {'prefix': debugprefix, 'filepath': 'amdgpu_gpu_recover', 'needsparse': False},
    'driver': {'prefix': moduleprefix, 'filepath': 'amdgpu/version', 'needsparse': False}
}

for block in validFwBlocks:
    valuePaths['%s_fw_version' % block] = \
        {'prefix': drmprefix, 'filepath': 'fw_version/%s_fw_version' % block, 'needsparse': False}
# SMC has different formatting for its version
valuePaths['smc_fw_version']['needsparse'] = True


def getFilePath(device, key):
    """ Return the filepath for a specific device and key

    Parameters:
    device -- Device whose filepath will be returned
    key -- [$valuePaths.keys()] The sysfs path to return
    """
    if key not in valuePaths.keys():
        raise NoRocmDeviceError('Cannot get file path for key %s' % key)
        logging.debug('Key %s not present in valuePaths map' % key)
        return None
    pathDict = valuePaths[key]

    if pathDict['prefix'] == hwmonprefix:
        # HW Monitor values have a different path structure
        if not getHwmonFromDevice(device):
            logging.warning('GPU[%s]\t: No corresponding HW Monitor found', parseDeviceName(device))
            return None
        filePath = os.path.join(getHwmonFromDevice(device), pathDict['filepath'])
    elif pathDict['prefix'] == debugprefix:
        # Kernel DebugFS values have a different path structure
        filePath = os.path.join(pathDict['prefix'], parseDeviceName(device), pathDict['filepath'])
    elif pathDict['prefix'] == drmprefix:
        filePath = os.path.join(pathDict['prefix'], device, 'device', pathDict['filepath'])
    else:
        # Otherwise, just join the 2 fields without any parsing
        filePath = os.path.join(pathDict['prefix'], pathDict['filepath'])

    if not os.path.isfile(filePath):
        return None
    return filePath


def getSysfsValue(device, key):
    """ Return the desired SysFS value for a specified device

    Parameters:
    device -- DRM device identifier
    key -- [$valuePaths.keys()] Key referencing desired SysFS file
    """
    filePath = getFilePath(device, key)
    pathDict = valuePaths[key]

    if not filePath:
        return None
    # Use try since some sysfs files like power1_average will throw -EINVAL
    # instead of giving something useful.
    try:
        with open(filePath, 'r') as fileContents:
            fileValue = fileContents.read().rstrip('\n')
    except:
        logging.warning('GPU[%s]\t: Unable to read %s', parseDeviceName(device), filePath)
        return None

    # Some sysfs files aren't a single line of text
    if pathDict['needsparse']:
        fileValue = parseSysfsValue(key, fileValue)

    if fileValue == '':
        logging.debug('GPU[%s]\t: Empty SysFS value: %s', parseDeviceName(device), key)

    return fileValue


def parseSysfsValue(key, value):
    """ Parse the sysfs value string

    Parameters:
    key -- [$valuePaths.keys()] Key referencing desired SysFS file
    value -- SysFS value to parse

    Some SysFS files aren't a single line/string, so we need to parse it
    to get the desired value
    """
    if key == 'id':
        # Strip the 0x prefix
        return value[2:]
    if re.match(r'temp[0-9]+', key):
        # Convert from millidegrees
        return int(value) / 1000
    if key == 'power':
        # power1_average returns the value in microwatts. However, if power is not
        # available, it will return "Invalid Argument"
        if value.isdigit():
            return float(value) / 1000 / 1000
    # ras_reatures has "feature mask: 0x%x" as the first line, so get the bitfield out
    if key == 'ras_features':
        return int((value.split('\n')[0]).split(' ')[-1], 16)
    # The smc_fw_version sysfs file stores the version as a hex value like 0x12345678
    # but is parsed as int(0x12).int(0x34).int(0x56).int(0x78)
    if key == 'smc_fw_version':
        return (str('%02d' % int((value[2:4]), 16)) + '.' + str('%02d' % int((value[4:6]), 16)) + '.' +
                str('%02d' % int((value[6:8]), 16)) + '.' + str('%02d' % int((value[8:10]), 16)))

    return ''


def parseDeviceNumber(deviceNum):
    """ Parse the device number, returning the format of card#

    Parameters:
    deviceNum -- DRM device number to parse
    """
    return 'card' + str(deviceNum)


def parseDeviceName(deviceName):
    """ Parse the device name, which is of the format card#.

    Parameters:
    deviceName -- DRM device name to parse
    """
    return deviceName[4:]


def printErr(device, err):
    """ Print out an error to the SMI log

    Parameters:
    device -- DRM device identifier
    err -- Error string to print
    """
    global PRINT_JSON
    devName = parseDeviceName(device)
    for line in err.split('\n'):
        errstr = 'GPU[%s] \t\t: %s' % (devName, line)
        if not PRINT_JSON:
            logging.error(errstr)
        else:
            logging.debug(errstr)


def formatJson(device, log):
    """ Print out in JSON format

    Parameters:
    device -- DRM device identifier
    log -- String to parse and output into JSON format
    """
    global JSON_DATA
    for line in log.splitlines():
        # If we got some bad input somehow, quietly ignore it
        if ':' not in line:
            return
        logTuple = line.split(': ')
        JSON_DATA[device][logTuple[0]] = logTuple[1]


def printLog(device, log):
    """ Print out to the SMI log.

    Parameters:
    device -- DRM device identifier
    log -- String to print to the log
    """
    global PRINT_JSON
    if PRINT_JSON:
        formatJson(device, log)
        return

    devName = parseDeviceName(device)
    for line in log.split('\n'):
        logstr = 'GPU[%s] \t\t: %s' % (devName, line)
        logging.debug(logstr)
        print(logstr)


def printSysLog(log):
    """ Print out to the SMI log for repeated features
    Parameters:
    log -- String to print to the log
    """
    global PRINT_JSON
    global JSON_DATA
    if PRINT_JSON:
        if "system" not in JSON_DATA:
            JSON_DATA["system"] = {}
        formatJson("system", log)
        return
    print(log)


def printLogSpacer():
    """ A helper function to print out the log spacer

    We use this to prevent unnecessary output when printing out
    JSON data. If we want JSON, do nothing, otherwise print out
    the spacer. To keep Python2 compatibility, we don't just use
    the print(end='') option, so instead we made this helper
    """
    global PRINT_JSON
    if PRINT_JSON:
        return
    print(logSpacer)


def doesDeviceExist(device):
    """ Check whether the specified device exists in sysfs.

    Parameters:
    device -- DRM device identifier
    """
    if os.path.exists(os.path.join(drmprefix, device)) == 0:
        return False
    return True


def getPid(name):
    """ Get the process id of a specific application """
    return check_output(["pidof", name])


def confirmOutOfSpecWarning(autoRespond):
    """ Print the warning for running outside of specification and prompt user to accept the terms.

    Parameters:
    autoRespond -- Response to automatically provide for all prompts
    """

    print('''
          ******WARNING******\n
          Operating your AMD GPU outside of official AMD specifications or outside of
          factory settings, including but not limited to the conducting of overclocking,
          over-volting or under-volting (including use of this interface software,
          even if such software has been directly or indirectly provided by AMD or otherwise
          affiliated in any way with AMD), may cause damage to your AMD GPU, system components
          and/or result in system failure, as well as cause other problems.
          DAMAGES CAUSED BY USE OF YOUR AMD GPU OUTSIDE OF OFFICIAL AMD SPECIFICATIONS OR
          OUTSIDE OF FACTORY SETTINGS ARE NOT COVERED UNDER ANY AMD PRODUCT WARRANTY AND
          MAY NOT BE COVERED BY YOUR BOARD OR SYSTEM MANUFACTURER'S WARRANTY.
          Please use this utility with caution.
          ''')
    if not autoRespond:
        user_input = input('Do you accept these terms? [y/N] ')
    else:
        user_input = autoRespond
    if user_input in ['Yes', 'yes', 'y', 'Y', 'YES']:
        return
    else:
        sys.exit('Confirmation not given. Exiting without setting value')


def isDPMAvailable(device):
    """ Check if DPM is available for a specified device.

    Parameters:
    device -- DRM device identifier
    """
    if not doesDeviceExist(device) or not os.path.isfile(getFilePath(device, 'dpm_state')):
        logging.warning('GPU[%s]\t: DPM is not available', parseDeviceName(device))
        return False
    return True


def isRasControlAvailable(device):
    """ Check if RAS control is available for a specified device.

    Parameters:
    device -- DRM device identifier
    """
    path = getFilePath(device, 'ras_ctrl')
    if not doesDeviceExist(device) or not path or not os.path.isfile(path):
        logging.warning('GPU[%s]\t: RAS control is not available', parseDeviceName(device))
        return False
    return True


def getNumProfileArgs(device):
    """ Get the number of Power Profile fields for a specific device

    Parameters:
    device -- DRM device identifier

    This varies per ASIC, so ensure that we get the right number of arguments
    """

    profile = getSysfsValue(device, 'profile')
    numHiddenFields = 0
    if not profile:
        return 0
    # Get the 1st line (column names)
    fields = profile.splitlines()[0]
    # SMU7 has 2 hidden fields for SclkProfileEnable and MclkProfileEnable
    if 'SCLK_UP_HYST' in fields:
        numHiddenFields = 2
    # If there is a CLOCK_TYPE category, that requires a value as well
    if 'CLOCK_TYPE(NAME)' in fields:
        numHiddenFields = 1
    # Subtract 2 to remove NUM and MODE NAME, since they're not valid Profile fields
    return len(fields.split()) - 2 + numHiddenFields


def getBus(device):
    """ Get the PCIe bus information for a specified device

    Parameters:
    device -- DRM device identifier
    """
    bus = os.readlink(os.path.join(drmprefix, device, 'device'))
    return bus.split('/')[-1]


def getMaxLevel(device, leveltype):
    """ Return the maximum level for a specified device.
    Parameters:
    device -- DRM device identifier
    leveltype -- [$validClockNames] Return the maximum desired clock,
                 or the highest numbered Power Profiles
    """
    global RETCODE
    if leveltype not in validClockNames and leveltype != 'profile':
        printErr(device, 'Unable to get max level')
        logging.error('Invalid level type %s', leveltype)
        RETCODE = 1
        return None

    levels = getSysfsValue(device, leveltype)
    if not levels:
        return None
    # lstrip since there are leading spaces for this sysfs file, but no others
    if leveltype == 'profile':
        for line in levels.splitlines():
            if re.match(r'.*CUSTOM.*', line):
                return int(line.lstrip().split()[0])
    return int(levels.splitlines()[-1][0])


def verifySetProfile(device, profile):
    """ Verify data from user to set as Power Profile.

    Ensure that we can set the profile, with Profiles being supported and
    the profile being passed in being valid

    Parameters:
    device -- DRM device identifier
    """
    global RETCODE
    if not isDPMAvailable(device):
        printErr(device, 'Unable to specify profile')
        RETCODE = 1
        return False

    # If it's 1 number, we're setting the level, not the Custom Profile
    if profile.isdigit():
        maxProfileLevel = getMaxLevel(device, 'profile')
        if maxProfileLevel is None:
            printErr(device, 'Unable to set profile')
            logging.debug('GPU[%s]\t: Unable to get max level when trying to set profile',
                          parseDeviceName(device))
            return False
        if int(profile) > maxProfileLevel:
            printErr(device, 'Unable to set profile to level' + str(profile))
            logging.debug('GPU[%s]\t: %d is an invalid level, maximum level is %d',
                          parseDeviceName(device), profile, maxProfileLevel)
            return False
        return True
    # If we get a string, split it into elements to make it a list
    elif isinstance(profile, str):
        if profile == 'reset':
            printErr(device, 'Reset no longer accepted as a Power Profile')
            return False
        else:
            profileList = profile.strip().split(' ')
    elif isinstance(profile, collections.Iterable):
        profileList = profile
    else:
        printErr(device, 'Unsupported profile argument : ' + str(profile))
        return False
    numProfileArgs = getNumProfileArgs(device)
    if numProfileArgs == 0:
        printErr(device, 'Power Profiles not supported')
        return False
    if len(profileList) != numProfileArgs:
        printErr(device, 'Unable to set profile')
        logging.error('GPU[%s]\t: Profile must contain 1 or %d values',
                      parseDeviceName(device), numProfileArgs)
        RETCODE = 1
        return False

    return True


def getProfile(device):
    """ Get either the current profile level, or the custom profile

    The CUSTOM profile might be set, or a specific profile level may have been selected
    Return either a single digit for a non-CUSTOM profile, or return the CUSTOM profile

    Parameters:
    device -- DRM device identifier
    """
    profiles = getSysfsValue(device, 'profile')
    custom = ''
    asic = ''
    level = ''
    numArgs = getNumProfileArgs(device)
    if numArgs == 0:
        printErr(device, 'Unable to get power profile')
        logging.debug('GPU[%s]\t: Power Profile not supported (file is empty)', parseDeviceName(device))
        return None
    for line in profiles.splitlines():
        if re.match(r'.*SCLK_UP_HYST./*', line):
            asic = 'SMU7'
            continue
        if re.match(r'.*\*.*', line):
            level = line.split()[0]
            if re.match(r'.*CUSTOM.*', line):
                # Ditch the NUM and NAME, which end with a : before the profile values
                # Then put it into single words via split
                custom = line.split(':')[1].split()
            break
    if not custom:
        return level
    # We need some special parsing for SMU7 if it's a CUSTOM profile
    if asic == 'SMU7' and custom:
        sclk = custom[0:3]
        mclk = custom[3:]
        if sclk[0] == '-':
            sclkStr = '0 0 0 0'
        else:
            sclkStr = '1 ' + ' '.join(sclk)
        if mclk[0] == '-':
            mclkStr = '0 0 0 0'
        else:
            mclkStr = '1 ' + ' '.join(mclk)
        customStr = sclkStr + ' ' + mclkStr
    else:
        customStr = ' '.join(custom[-numArgs:])
    return customStr


def writeProfileSysfs(device, value):
    """ Write to the Power Profile sysfs file

    This function is different from a regular sysfs file as it could involve
    parsing of the data first.

    Parameters:
    device -- DRM device identifier
    value -- Value to write to the Profile sysfs file
    """
    if not verifySetProfile(device, value):
        return

    # Perf Level must be set to manual for a Power Profile to be specified
    # This is new compared to previous versions of the Power Profile
    setPerfLevel(device, 'manual')
    profilePath = getFilePath(device, 'profile')
    maxLevel = getMaxLevel(device, 'profile')
    if maxLevel is None:
        printErr(device, 'Unable to set profile')
        logging.debug('GPU[%s]\t: Max profile level could not be obtained', parseDeviceName(device))
        return False
    # If it's a single number, then we're choosing the Power Profile, not setting CUSTOM
    if isinstance(value, str) and len(value) == 1:
        profileString = value
    # Otherwise, we're setting the CUSTOM profile
    elif value.isdigit():
        profileString = str(value)
    elif isinstance(value, str) and len(value) > 1:
        if maxLevel is not None:
            # Prepend the Max Level of Profiles since that will always be the CUSTOM profile
            profileString = str(maxLevel) + value
    else:
        printErr(device, 'Invalid input argument ' + value)
        return False
    if writeToSysfs(profilePath, profileString):
        return True
    return False


def writeToSysfs(fsFile, fsValue):
    """ Write to a sysfs file.

    Parameters:
    fsFile -- Path to the sysfs file to modify
    fsValue -- Value to write to the sysfs file
    """
    global RETCODE
    if not os.path.isfile(fsFile):
        raise NoRocmDeviceError('Unable to write to sysfs file')
        logging.debug('%s does not exist', fsFile)
        return False
    try:
        logging.debug('Writing value \'%s\' to file \'%s\'', fsValue, fsFile)
        with open(fsFile, 'w') as fs:
            fs.write(fsValue + '\n')  # Certain sysfs files require \n at the end
    except (IOError, OSError):
        raise NoRocmDeviceError('Unable to write to sysfs file %s' % fsFile)
        logging.warning('IO or OS error')
        RETCODE = 1
        return False
    return True


def isAmdDevice(device):
    """ Return whether the specified device is an AMD device or not
    Parameters:
    device -- DRM device identifier
    """
    vid = getSysfsValue(device, 'vendor')
    if vid == '0x1002':
        return True
    return False


def setPerfLevel(device, level):
    """ Set the Performance Level for a specified device.
    Parameters:
    device -- DRM device identifier
    level -- Performance Level to set
    """
    global RETCODE
    validLevels = ['auto', 'low', 'high', 'manual']
    perfPath = getFilePath(device, 'perf')

    if level not in validLevels:
        printErr(device, 'Unable to set Performance Level')
        logging.error('Invalid Performance level: %s', level)
        RETCODE = 1
        return False
    if not os.path.isfile(perfPath):
        return False
    writeToSysfs(perfPath, level)
    return True


def listDevices(showall):
    """ Return a list of GPU devices.

    Parameters:
    showall -- [True|False] Show all devices, not just AMD devices
    """

    if not os.path.isdir(drmprefix) or not os.listdir(drmprefix):
        raise NoRocmDeviceError('Unable to get devices, /sys/class/drm is empty or missing')
        return None

    devicelist = [device
                    for device in os.listdir(drmprefix)
                    if re.match(r'^card\d+$', device) and (isAmdDevice(device) or showall)]
    return sorted(devicelist, key=lambda x: int(x.partition('card')[2]))


def listAmdHwMons():
    """Return a list of AMD HW Monitors."""
    hwmons = []

    for mon in os.listdir(hwmonprefix):
        tempname = os.path.join(hwmonprefix, mon, 'name')
        if os.path.isfile(tempname):
            with open(tempname, 'r') as tempmon:
                drivername = tempmon.read().rstrip('\n')
                if drivername in ['radeon', 'amdgpu']:
                    hwmons.append(os.path.join(hwmonprefix, mon))
    return hwmons


def getHwmonFromDevice(device):
    """ Return the corresponding HW Monitor for a specified GPU device.
    Parameters:
    device -- DRM device identifier
    """
    drmdev = os.path.realpath(os.path.join(drmprefix, device, 'device'))
    for hwmon in listAmdHwMons():
        if os.path.realpath(os.path.join(hwmon, 'device')) == drmdev:
            return hwmon
    return None


def getUniqueId(device):
    """ Display Unique ID for a list of devices.

    Parameters:
    deviceList -- List of DRM devices (can be a single-item list)
    """

    return getSysfsValue(device, 'unique_id')


def getGpuUse(device):
    """ Display GPU use for a list of devices.

    Parameters:
    deviceList -- List of DRM devices (can be a single-item list)
    """
    use = getSysfsValue(device, 'use')
    if use is None:
        raise RocmUtilFetchError(device, 'Unable to get GPU use: usage not supported (file is empty).')
    else:
        return float(use) / 100


def getMemInfo(device, memType):
    """ Return the specified memory usage for the specified device

    Parameters:
    device -- DRM device identifier
    type -- [vram|vis_vram|gtt] Memory type to return
    """
    if memType not in validMemTypes:
        raise RocmMemFetchError('Invalid memory type %s', memType)
        return (None, None)
    memUsed = getSysfsValue(device, '%s_used' % memType)
    memTotal = getSysfsValue(device, '%s_total' % memType)
    if memUsed is None:
        raise RocmMemFetchError('Unable to get %s_used' % memType)
    elif memTotal is None:
        raise RocmMemFetchError('Unable to get %s_total' % memType)
    return (memUsed, memTotal)


def getProductName(device):
    """ Show the requested product name for a list of devices

    Parameters:
    deviceList -- List of DRM devices (can be a single-item list)
    """
    fileString = ''
    pciLines = ''
    pciFilePath = '/usr/share/misc/pci.ids'
    # If the pci.ids file is found in share, switch to that path
    if os.path.isfile('/usr/share/pci.ids'):
        pciFilePath = '/usr/share/pci.ids'
    # If the pci.ids file is found in hwdata, switch to that path
    if os.path.isfile('/usr/share/hwdata/pci.ids'):
        pciFilePath = '/usr/share/hwdata/pci.ids'
    try:
        with open(pciFilePath, 'rt') as pciFile:
            fileString = pciFile.read()
        # pciLines stores all AMD GPU names (from 1002 to 1003 in pci.ids file)
        pciLines = fileString.split('\n1002')[1].split('\n1003')[0]
    except:
        raise NoRocmDeviceError('Unable to locate pci.ids file')

    # Fetch required sysfs files for product name and store them
    vendor = getSysfsValue(device, 'vendor')
    if vendor and len(vendor) > 2:
        vendor = vendor[2:]
        # Check if the device vendor is 1002, which is AMD's number in pci.ids
        if vendor == '1002':
            vbios = getSysfsValue(device, 'vbios')
            if not vbios:
                raise GenericRocmError(device, 'Unable to get the SKU')
            device_id = getSysfsValue(device, 'id')
            if not device_id:
                raise GenericRocmError(device, 'Unable to get device id')
            sub_id = getSysfsValue(device, 'sub_id')
            if sub_id:
                sub_id = sub_id[2:]
            else:
                raise GenericRocmError(device, 'Unable to get subsystem_device')
            sub_vendor = getSysfsValue(device, 'sub_vendor')
            if sub_vendor:
                sub_vendor = sub_vendor[2:]
            else:
                raise GenericRocmError(device, 'Unable to get subsystem_vendor')
            if len(pciLines) > 0 and len(fileString) > 0:
                # Check if the device ID exists in pciLines before attempting to print
                if pciLines.find('\n\t%s' % device_id) != -1:
                    # variants gets a sublist of all devices in a specific GPU series
                    variants = re.split(r'\n\t[a-z0-9]',
                                        pciLines.split('\n\t%s' % device_id)[1])[0]
                    if variants.find('%s %s' % (sub_vendor, sub_id)) != -1:
                        return variants.split(sub_id, 1)[1].split('\n', 1)[0].strip()
                    return variants.split('\n', 1)[0].strip()
                else:
                    raise GenericRocmError(device, 'Unable to find device ID in PCI IDs file. \
                                        Run update-pciids and try again')
        else:
            raise GenericRocmError(device, f'PCI device is not an AMD device ({vendor} instead of 1002)')
    else:
        raise GenericRocmError(device, 'Unable to get device vendor')


def getVersion(component):
    """ Show the software version for the specified component
    Parameters:
    component - Component (currently only driver)
    """
    if component == 'driver':
        # Only 1 version, so report it for GPU 0
        driver = getSysfsValue(None, 'driver')
        if driver is None:
            driver = os.uname()[2]
        return driver
    return None
