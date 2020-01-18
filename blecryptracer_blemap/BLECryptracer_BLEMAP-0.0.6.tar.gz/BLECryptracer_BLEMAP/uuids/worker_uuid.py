import os
import sys
import fnmatch
import re
import collections
import timeit
import shutil
from time import sleep
from multiprocessing import JoinableQueue
from subprocess import *
from threading import Timer
from androguard.misc import *
from androguard.core import *
from androguard import session
from common.constants import FILENAME, PACKAGE, TAG_BLE_UUIDS, TAG_CLASSIC_UUIDS, KIND, LOCATION_IN_APK, KIND_CLASSIC, KIND_CREATED, KIND_DIRECT, KIND_HIGH_PROBABILITY, KIND_INCORRECT_USE, KIND_LONGLONG, KIND_MEDIUM_PROBABILITY

working_dir_base = "working_dir/"
error_dir = "error/"
extension = "apk"

MAX_RUNTIME = 1800
THREAD_WORKING_DIR =""

#variables/arrays for storing UUIDs.
CLASSIC_CALLS = False
UUID_CANDIDATES = []
CLASSIC_UUIDS = []
BLE_UUIDs = []
BLE_CREATED_UUIDS = []
BLE_INCORRECT_UUIDS = []
UUID_LIST_HIGH = []
UUID_LIST_MED = []
LONGLONG_UUIDS = []
RESERVED_BLE_UUIDS = []
RESERVED_CLASSIC_UUIDS = []
IDENTIFIED_STRINGS = 0
UNIDENTIFIED_STRINGS = 0
TOTAL_INIT = 0
IDENTIFIED_INIT = 0

def main(filename):
    """ Initialise analysis.
    
    Gets APK files, execute Violist and AnalyzeAPK, and start analysis procedure.
    Returns output to calling process as comma-separated string.
    """    
    file_with_extension = os.path.basename(filename)
    process_id = '{0}_dir'.format(file_with_extension)
    try:
        createViolistWorkingDir(process_id)
    except Exception as e:
        print("FATAL ERROR: Could not create working directory!\n", str(e))
        sys.exit(1)    
    try:
        populateReservedUuidList()   
    except Exception as e:
        print("FATAL ERROR: Could not populate UUID list!\n", str(e))
        sys.exit(1)

    # Get APK from main process.
    filepath = filename
    
    resetValues()
    try:
    #Run violist analysis to get high-certainty UUIDs.
        violist_output = startViolistAnalysis(filepath)
        if (violist_output[0] != ""):
            sleep(0.1)
            return {}  
            
        #Run Androguard analysis to get remaining (created) UUIDs.
        androguard_output = startAndroguardAnalysis(filepath)   
        #If an error occurred, the first element of the output array
        # will be a non-empty string.
        if (androguard_output[0]) != "":           
            sleep(0.1)
            return {}  
        #Get final list of UUIDs.
        ble_uuids_to_save = {}
        for uuid in BLE_UUIDs:
            ble_uuids_to_save[uuid[0]] = {KIND: KIND_DIRECT,LOCATION_IN_APK:uuid[1]}
        for uuid in BLE_CREATED_UUIDS:
            ble_uuids_to_save[uuid[0]] = {KIND: KIND_CREATED,LOCATION_IN_APK:uuid[1]}
        for uuid in BLE_INCORRECT_UUIDS:
            ble_uuids_to_save[uuid[0]] = {KIND: KIND_INCORRECT_USE,LOCATION_IN_APK:uuid[1]}
        for uuid in UUID_LIST_HIGH:
            ble_uuids_to_save[uuid[0]] = {KIND: KIND_HIGH_PROBABILITY,LOCATION_IN_APK:uuid[1]}
        for uuid in UUID_LIST_MED:
            ble_uuids_to_save[uuid[0]] = {KIND: KIND_MEDIUM_PROBABILITY,LOCATION_IN_APK:uuid[1]}
        for uuid in LONGLONG_UUIDS:
            ble_uuids_to_save[uuid[0]] = {KIND: KIND_LONGLONG,LOCATION_IN_APK:uuid[1]}
        classic_uuids_to_save = {}
        for uuid in CLASSIC_UUIDS:
            classic_uuids_to_save[uuid[0]] = {KIND:KIND_CLASSIC,LOCATION_IN_APK:uuid[1]}
        output = {FILENAME:filepath,PACKAGE:androguard_output[1],TAG_BLE_UUIDS:ble_uuids_to_save,TAG_CLASSIC_UUIDS: classic_uuids_to_save}
        return output
    except Exception as e:
        print("Unhandled error: ", str(e))
        sleep(0.1)
        return {}   
        

def createViolistWorkingDir(process_id):
    """ Create working directory for violist.
    
    Keyword arguments:
    process_id -- Process ID for this worker thread.
    """
    
    global THREAD_WORKING_DIR
    
    working_dir = working_dir_base + str(process_id) + "/"
    THREAD_WORKING_DIR = working_dir
    if not os.path.exists(working_dir):
        os.makedirs(working_dir)

def resetValues():
    """ Reset global variables."""
    
    global CLASSIC_CALLS
    global UUID_CANDIDATES
    global CLASSIC_UUIDS
    global BLE_UUIDs
    global BLE_CREATED_UUIDS
    global BLE_INCORRECT_UUIDS
    global UUID_LIST_HIGH
    global UUID_LIST_MED
    global LONGLONG_UUIDS
    
    # Reset values for each new APK.
    CLASSIC_CALLS = False
    UUID_CANDIDATES = []
    CLASSIC_UUIDS = []
    BLE_UUIDs = []
    BLE_CREATED_UUIDS = []
    BLE_INCORRECT_UUIDS = []
    UUID_LIST_HIGH = []
    UUID_LIST_MED = []
    LONGLONG_UUIDS = []

def startViolistAnalysis(filepath):
    """ Get high certainty UUIDs via Violist."""
    
    output = ["",""]
    outfileExists = False
    split_path = os.path.split(filepath)
    filename = split_path[1]
    split_filename = filename.split(".")
    sha256 = split_filename[0]
    
    #Copy apk to working folder.
    target_working_file = os.path.join(THREAD_WORKING_DIR, filename)
    try:
        shutil.copy(filepath, target_working_file)

    except Exception as e:
        output[0] = "Error"
        output[1] = "APK copy error: " + str(e)
        print('1 '+output)
        return output
    
    #Create config file.
    config_file_location = os.path.join(THREAD_WORKING_DIR, "config.txt")
    #Write to new config file.
    fo_config = open(config_file_location, "w")
    
    #Hack to get the 1 (loopUnraveledTime) to not have Carriage-Return.    
    config_string1 = ("androidJarPath=./uuids/android-8/\n"
                    "parentFolderOfApk=" + THREAD_WORKING_DIR +"\n"
                    "apkName=" + filename + "\n"
                    "loopUnraveledTime=1\n" + 
                    "<java.util.UUID: java.util.UUID fromString(java.lang.String)>@1\n" +
                    "<android.os.ParcelUuid: android.os.ParcelUuid fromString(java.lang.String)>@1\n")
   
    fo_config.write(config_string1)
    fo_config.close()
    
    #Execute Violist.
    args = ['uuids/Violist.jar', config_file_location]
    result = jarWrapper(args)
    result_file = os.path.join(THREAD_WORKING_DIR,"result.txt")
    if result == "Error":
        #If the result file exists, then ignore the error.
        if not os.path.exists(result_file):
            try:
                os.remove(target_working_file)
                #shutil.rmtree(os.path.join(THREAD_WORKING_DIR,"MethodSummary"), False)
            except Exception:
                pass
            output[0] = "Error"
            output[1] = "Results file doesn't exist."
            return output
        else:
            outfileExists = True
    #If there was no error, but also no result file.
    if not os.path.exists(result_file):
        try:
            os.remove(target_working_file)
            #shutil.rmtree(os.path.join(THREAD_WORKING_DIR,"MethodSummary"), False)
        except Exception:
            pass
        output[0] = "Error"
        output[1] = "Results file doesn't exist."
        return output
    else:
        outfileExists = True
        
    #Let Violist complete all functions, so that we can delete the files.
    sleep(0.1)
    #Get the result file and copy it out to the final output folder and delete all other files.        
    dest_result_file = sha256 + ".txt"
    if (outfileExists):
        try:
            shutil.copy(result_file, dest_result_file)
            os.remove(result_file)
        except Exception as e:
            print('Error moving and deleting results file')
            try:
                os.remove(target_working_file)
                #shutil.rmtree(os.path.join(THREAD_WORKING_DIR,"MethodSummary"), False)
            except Exception:
                pass
            output[0] = "Error"
            output[1] = "Could not copy result file: " + str(e)
            return output
       
    #Delete the directory to save space.
    try:
        shutil.rmtree(os.path.join(THREAD_WORKING_DIR,"MethodSummary"), False)
    except Exception as e:
        if not os.path.exists(os.path.join(THREAD_WORKING_DIR,"MethodSummary")):
            pass
        else:
            output[0] = "Error"
            output[1] = "Could not delete MethodSummary folder: " + str(e)
            return output
        
    #Delete the APK from the working directory as well.
    try:
        os.remove(target_working_file)
    except:
        output[0] = "Error"
        output[1] = "Could not delete working file" + str(target_working_file)
        return output
        
    string_values = []
    #Try to read and parse output file.
    if (outfileExists):
        try:
            fo_file_out = open(dest_result_file,'r')
            file_contents = fo_file_out.read()
            split_by_mname = file_contents.split("Method Name:")

            num_strings = len(split_by_mname)
            if num_strings >= 1:
                for i in range(1,num_strings):
                    split_by_newline = split_by_mname[i].split("\n")
                    string_location_raw = split_by_newline[0].strip()
                    string_location = (((string_location_raw.split(":"))[0]).split("<"))[1].strip()
                    split_by_value = split_by_mname[i].split("Value:")
                    
                    if len(split_by_value) < 2:
                        continue
                    splitvalue_by_newline = split_by_value[1].split("\n")
                    string_value = splitvalue_by_newline[0].strip()

                    if (re.match("[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", string_value)):
                        string_values.append([string_value, string_location])
                
        except Exception as e:
            output[0] = "Error"
            output[1] = "Analysis error" + str(e)
            return output
    #Remove working dir and final result file.
    if os.path.exists(working_dir_base):
        shutil.rmtree(working_dir_base)
        os.remove(dest_result_file)

    if string_values != []:
        sortViolistUUIDs(string_values)  
        
    return output

def sortViolistUUIDs(string_values):
    global CLASSIC_UUIDS
    global BLE_UUIDs
    global BLE_INCORRECT_UUIDS
    global UUID_LIST_HIGH
    
    for uuid_candidate_group in string_values:
        uuid_candidate = uuid_candidate_group[0]
        # Look for exact pattern matches.
        if((len(uuid_candidate) == 36) and 
               (re.match("[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", uuid_candidate))):
            #UUIDs that are derived from the Bluetooth Base UUID.
            if ((uuid_candidate[0:4] == "0000") and 
                    (uuid_candidate[8:] == "-0000-1000-8000-00805f9b34fb")):
                if((uuid_candidate[4:8] in RESERVED_CLASSIC_UUIDS) and 
                       (uuid_candidate_group not in CLASSIC_UUIDS)):
                    CLASSIC_UUIDS.append(uuid_candidate_group)
                elif((uuid_candidate[4:8] in RESERVED_BLE_UUIDS) and 
                         (uuid_candidate_group not in BLE_UUIDs)):
                    BLE_UUIDs.append(uuid_candidate_group)
                elif((uuid_candidate[4:8] != "0000") and 
                         (uuid_candidate[4:8] not in RESERVED_BLE_UUIDS) and 
                         (uuid_candidate_group not in BLE_INCORRECT_UUIDS)):
                    BLE_INCORRECT_UUIDS.append(uuid_candidate_group)
            elif (uuid_candidate_group not in UUID_LIST_HIGH):
                UUID_LIST_HIGH.append(uuid_candidate_group)
                
def startAndroguardAnalysis(filepath):
    #Initialise output.
    output = ["",""]
    
    # Get default session.
    sess = get_default_session()
    
    # Try Androguard's AnalyzeAPK() against the APK.
    # If it fails, then we cannot proceed with this APK,
    # so move on to next.
    try:
        a, d, dx = AnalyzeAPK(filepath, session=sess)
    except Exception as e:
        output[0] = "Error"
        output[1] = str(e)
        # Reset the session for the next analysis.
        # Otherwise, memory consumption builds up over time
        # (Androguard 3.1.0).
        sess.reset()
        return output
        
    if a == None or d == None or dx == None:
        output[0] = "Error"
        output[1] = "a, d or dx is null"
        sess.reset()
        return output
        
    apk_package = a.get_package()
    
    # If AnalyzeAPK succeeded, and none of the analysis file are None,
    #  then proceed.
    try:
        startAnalysis(a, d, dx)
    except Exception as e:
        output[0] = apk_package
        output[1] = str(e)
        sess.reset()
        return output
     
    sess.reset()
    output[1] = apk_package
    return output
       

def startAnalysis(a, d, dx):
    """ Schedule analysis tasks.
    
    Keyword arguments:
    a   -- Androguard APK object.
    d   -- Androguard array of DalvikVMFormat objects.
    dx  -- Androguard Analysis object.
    """
    
    global UUID_LIST_MED
    
    checkForClassicCalls(a, d, dx)
    generateCandidateList(a, d, dx)
    getRemainingUuids()
    getLongLongUuids(a, d, dx)


def checkForClassicCalls(a, d, dx):
    """ Check for calls to Classic Bluetooth APIS.
    
    Keyword arguments:
    a   -- Androguard APK object.
    d   -- Androguard array of DalvikVMFormat objects.
    dx  -- Androguard Analysis object.
    """

    global CLASSIC_CALLS

    ext_methods = []
    ext_methods.extend(dx.find_methods(
        "Landroid/bluetooth/BluetoothAdapter;", "startDiscovery", "."))
    ext_methods.extend(dx.find_methods(
        "Landroid/bluetooth/BluetoothSocket;", ".", "."))
    ext_methods.extend(dx.find_methods(
        "Landroid/bluetooth/BluetoothServerSocket;", ".", "."))
    classic_methods = []
    for ext_method in ext_methods:
        for element in ext_method.get_xref_from():
            if element[1] not in classic_methods:
                classic_methods.append(element[1])

    if classic_methods == []:
        CLASSIC_CALLS = False
    else:
        CLASSIC_CALLS = True


def generateCandidateList(a, d, dx):
    """ Generate a list of candidate UUIDs.
    
    Keyword arguments:
    a   -- Androguard APK object.
    d   -- Androguard array of DalvikVMFormat objects.
    dx  -- Androguard Analysis object.
    
    Identify all strings within the APK that match certain criteria.
    The strings have to contain only printable characters, 
     they must be 36 characters or less,
     and they must be within a method that makes reference to UUIDs.
    """
    
    global UUID_CANDIDATES

    # First get all strings.
    all_string_analysis_objects_in_apk = dx.get_strings()

    for string_analysis_object in all_string_analysis_objects_in_apk:
        string_value = string_analysis_object.get_value()
        string_xref_from = string_analysis_object.get_xref_from()
        for element in string_xref_from:
            calling_method = element[1]
            is_method_uuid = isMethodUuid(calling_method)
            if not (is_method_uuid):
                continue
            calling_method_class = calling_method.get_class_name()
            method_location_identifier = (calling_method_class[1:]).replace("/",".")
            # Prune out the non-printable and unsuitably long characters first.
            if((re.match("[ -~]", string_value)) and 
                   (len(string_value) <= 36) and 
                   ([string_value.lower(),method_location_identifier] not in UUID_CANDIDATES)):
                # Append string after converting to lowercase
                UUID_CANDIDATES.append([string_value.lower(),method_location_identifier])
    return


"""
This function returns true if the provided method makes some reference to UUIDs.
"""


def isMethodUuid(method):
    """ Identify if a method makes reference to UUIDs.
    
    Keyword arguments:
    method -- the method of interest.
    """
    
    list_instructions = list(method.get_instructions())
    for instruction in list_instructions:
        if (("Ljava/util/UUID;" in instruction.get_output()) or 
                ("Landroid/os/ParcelUuid;" in instruction.get_output())):
            return True
    return False


def getRemainingUuids():
    """ Get UUIDs that do not follow strict UUID pattern.
    
    Identify strings with format specifiers and see if any 
     combinations make UUIDs.
    """
    
    global UUID_CANDIDATES
    global UUID_LIST_HIGH
    global UUID_LIST_MED
    global BLE_UUIDs
    global BLE_INCORRECT_UUIDS
    global UNIDENTIFIED_STRINGS

    for uuid_candidate_group in UUID_CANDIDATES:
        uuid_candidate = uuid_candidate_group[0]
        # To include formatting functions,
        #  but exclude those strings that have already been taken to be UUIDs.
        if not ((re.match("^[A-Za-z0-9-%]+$", uuid_candidate)) and 
                    (uuid_candidate_group not in UUID_LIST_HIGH) and 
                    (uuid_candidate_group not in UUID_LIST_MED) and 
                    (uuid_candidate_group not in BLE_UUIDs) and 
                    (uuid_candidate_group not in BLE_INCORRECT_UUIDS) and 
                    (uuid_candidate_group not in CLASSIC_UUIDS)):
            continue

        # String contains format specifier.
        if("%s" in uuid_candidate) or ("%4s" in uuid_candidate):
            # If the string without format specifier isn't at least 28 characters long, ignore.
            # It's unlikely that a UUID would be created by piecing together more than 2 strings?
            string_without_format_specifier = uuid_candidate.replace(
                "%s", "").replace("%4s", "")
            if len(string_without_format_specifier) < 28:
                continue

            # String without specifier contains only hex characters.
            if (re.match("^[A-Fa-f0-9-]+$", string_without_format_specifier)):
                formatRemainingUuids(uuid_candidate_group)
        elif("%" in uuid_candidate):
            print("FOUND %, ", uuid_candidate)
            if ((re.match("^[A-Za-z0-9]+$", uuid_candidate.replace("%",""))) and
                    (len(uuid_candidate) > 30) and 
                    (len(uuid_candidate) < 36)):
                UNIDENTIFIED_STRINGS = UNIDENTIFIED_STRINGS + 1

def formatRemainingUuids(uuid_group):
    global UUID_CANDIDATES
    global UUID_LIST_HIGH
    global UUID_LIST_MED
    global BLE_UUIDs

    string_with_format_specifier = uuid_group[0]
    string_location = uuid_group[1]
    
    uuid_prefix_list = []
    uuid_suffix_list = []
    for uuid_high_group in UUID_LIST_HIGH:
        uuid_high = uuid_high_group[0]
        if (uuid_high[:6] not in uuid_prefix_list):
            uuid_prefix_list.append(uuid_high[:6])
        if (uuid_high[-28:] not in uuid_suffix_list):
            uuid_suffix_list.append(uuid_high[-28:])

    FORMAT_STRINGS = []

    string_without_format_specifier = string_with_format_specifier.replace(
        "%s", "").replace("%4s", "")
    len_string_without_format_specifier = len(string_without_format_specifier)
    len_remaining_string = 36 - len_string_without_format_specifier

    for uuid_candidate_group in UUID_CANDIDATES:
        uuid_candidate = uuid_candidate_group[0]
        if ((len(uuid_candidate) == len_remaining_string) and 
                (re.match("^[A-Fa-f0-9]+$", uuid_candidate)) and 
                (uuid_candidate not in FORMAT_STRINGS)):
            FORMAT_STRINGS.append(uuid_candidate)

    FORMAT_STRINGS.sort(key=lambda string: string[0])

    for format_string in FORMAT_STRINGS:
        formatted_string = ""
        # Replace the %s or %4s with other characters.
        if ("%s" in string_with_format_specifier):
            formatted_string = string_with_format_specifier.replace(
                "%s", format_string)
        elif ("%4s" in string_with_format_specifier):
            formatted_string = string_with_format_specifier.replace(
                "%4s", format_string)
        elif ("%04s" in string_with_format_specifier):
            formatted_string = string_with_format_specifier.replace(
                "%04s", format_string)

        # Make sure the resultant string matches the expected format
        if not (re.match("[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", formatted_string)):
            continue
        # Try and weed out false positives.
        # Most characteristic UUIDs within a service differ only by the 8th hex character (1-indexed).
        if ((formatted_string[:6] in uuid_prefix_list) and 
                (formatted_string[-28:] in uuid_suffix_list) and 
                ([formatted_string,string_location] not in BLE_UUIDs) and 
                ([formatted_string,string_location] not in BLE_CREATED_UUIDS) and 
                ([formatted_string,string_location] not in UUID_LIST_HIGH) and 
                ([formatted_string,string_location] not in UUID_LIST_MED)):
            UUID_LIST_MED.append([formatted_string,string_location])
        # Check for reserved.
        elif ((formatted_string[-28:] == "-0000-1000-8000-00805f9b34fb") and 
                  (formatted_string[:4] == "0000") and 
                  (formatted_string[4:8] in RESERVED_BLE_UUIDS) and 
                  ([formatted_string,string_location] not in BLE_UUIDs) and 
                  ([formatted_string,string_location] not in BLE_CREATED_UUIDS) and 
                  ([formatted_string,string_location] not in UUID_LIST_HIGH) and 
                  ([formatted_string,string_location] not in UUID_LIST_MED)):
            BLE_CREATED_UUIDS.append([formatted_string,string_location])


def getLongLongUuids(a, d, dx):
    global TOTAL_INIT
    
    ext_methods = dx.find_methods("Ljava/util/UUID;", "<init>", ".")
    uuid_methods = []
    for ext_method in ext_methods:
        for element in ext_method.get_xref_from():
            if element[1] not in uuid_methods:                
                uuid_methods.append(element[1])

    if uuid_methods == []:
        return

    init_calls = []
    for path_idx, method in enumerate(uuid_methods):
        instructions = method.get_instructions()
        for ins_idx, instruction in enumerate(instructions):
            if "Ljava/util/UUID;-><init>" in instruction.get_output():
                instr_operands = instruction.get_operands(0)
                init_calls.append(
                    [method, ins_idx, instr_operands[1], instr_operands[3]])

    TOTAL_INIT = len(init_calls)
    
    for init_call in init_calls:
        traceLongLong(init_call)


def traceLongLong(init_call):
    global IDENTIFIED_INIT
    
    method = init_call[0]
    method_location_raw = method.get_class_name()
    method_location_identifier = method_location_raw[1:].replace("/",",")
    instruction_id = init_call[1]
    operand1 = init_call[2]
    operand2 = init_call[3]

    instructions = method.get_instructions()
    list_instructions = list(instructions)
    num_instructions = len(list_instructions)
    reversed_instructions = reversed(list_instructions)
    starting_index = num_instructions - instruction_id
    operand_part1 = ""
    operand_part2 = ""
    intermediate_operand = ""
    final_operand = ""

    # Go through all instructions in the method,
    #  looking for the component parts (i.e., the <long,long>)
    for idx, instruction in enumerate(reversed_instructions):
        if idx < starting_index:
            continue

        operands = instruction.get_operands(0)
        instr_op_value = instruction.get_op_value()

        # Standard, straightforward case.
        # const-wide and register match
        if ((instr_op_value == 0x18) and 
                (((operands[0] == operand1) and 
                 (operand_part1 == "")) or 
                 ((operands[0] == operand2) and 
                 (operand_part2 == "")))):
            operand_value = operands[1][1]
            hex_value = (hex(operand_value)).replace("0x", "")
            string_operand_value = str(hex_value)
            if string_operand_value[0] != "-":
                component_operand = string_operand_value
            else:
                component_operand = convertSignedToUnsigned(operand_value)

            if (operands[0] == operand1):
                operand_part1 = component_operand
            elif (operands[0] == operand2):
                operand_part2 = component_operand
            else:
                pass

        # If both parts have been identified, stop processing further instructions.
        if (operand_part1 != "") and (operand_part2 != ""):
            break

    if (operand_part1 != "") and (operand_part2 != ""):
        if ((len(operand_part1) + len(operand_part2)) == 32):
            intermediate_operand = operand_part1 + operand_part2
        elif ((len(operand_part1) + len(operand_part2)) < 32):
            padding_len = 32 - (len(operand_part1) + len(operand_part2))
            intermediate_operand = "0" * padding_len
            intermediate_operand = intermediate_operand + operand_part1 + operand_part2
        else:
            pass
        if intermediate_operand != "":
            final_operand = intermediate_operand[0:8] + "-" + intermediate_operand[8:12] + "-" + \
                intermediate_operand[12:16] + "-" + \
                intermediate_operand[16:20] + "-" + intermediate_operand[20:]
            IDENTIFIED_INIT = IDENTIFIED_INIT + 1
            if [final_operand,method_location_identifier] not in LONGLONG_UUIDS:
                LONGLONG_UUIDS.append([final_operand,method_location_identifier])


def convertSignedToUnsigned(negative_component_value):
    """ Generate Two's complement of negative UUID components.
    
    Keyword arguments:
    negative_component_value -- the UUID component that needs to be converted.
    
    Returns:
    hex_value -- unsigned hex.
    """
    string_bin_value = format(abs(negative_component_value), '064b')
    inverted_bin_value = ''.join(
        '1' if x == '0' else '0' for x in string_bin_value)
    add_one = int(inverted_bin_value, 2) + int("1", 2)
    hex_value = (hex(add_one).replace("0x", "")).replace("L", "")
    return hex_value


def jarWrapper(args):
    isError = None
    kill = lambda process: process.kill()
    command = ['java', '-jar']
    command.extend(args)
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    my_timer = Timer(MAX_RUNTIME, kill, [process])
    
    try:
        my_timer.start()
        stdout, stderr = process.communicate()
        # if stderr != '':            
            # error_file = error_dir + sha256 + ".txt"
            # fo_error = open(error_file,'a',0)
            # fo_error.write(str(stderr))
            # fo_error.close()
        
    except Exception as e:
        isError = "Error"
        print('Error launching violist '+str(e))
    finally:
        my_timer.cancel()
    
    return isError

    
def convertUuidListToString():
    """ Convert all lists of UUIDs to a single string. """
    
    global UUID_LIST_HIGH
    global UUID_LIST_MED
    global BLE_UUIDs
    global BLE_CREATED_UUIDS
    global BLE_INCORRECT_UUIDS
    global IDENTIFIED_STRINGS
    uuid_string = ""
    reserved_uuid_list = ""
    incorrect_use_list = ""
    
    # Add the BLE UUIDs (that are defined fully).
    bluetooth_uuid_string = ""
    for uuid in BLE_UUIDs:
        if bluetooth_uuid_string == "":
            bluetooth_uuid_string = bluetooth_uuid_string + uuid[0] + " [" + uuid[1] + "]"
        else:
            bluetooth_uuid_string = bluetooth_uuid_string + ";" + uuid[0] + " [" + uuid[1] + "]"
    uuid_string = uuid_string + bluetooth_uuid_string

    # Add the BLE UUIDs that were pieced together.
    uuid_string = uuid_string + ","
    pieced_bluetooth_string = ""
    for uuid in BLE_CREATED_UUIDS:
        if pieced_bluetooth_string == "":
            pieced_bluetooth_string = pieced_bluetooth_string + uuid[0] + " [" + uuid[1] + "]"
        else:
            pieced_bluetooth_string = pieced_bluetooth_string + ";" + uuid[0] + " [" + uuid[1] + "]"
    uuid_string = uuid_string + pieced_bluetooth_string

    # Add the BLE UUIDs that may be incorrectly used.
    uuid_string = uuid_string + ","
    incorrect_uuid_string = ""
    for uuid in BLE_INCORRECT_UUIDS:
        if incorrect_uuid_string == "":
            incorrect_uuid_string = incorrect_uuid_string + uuid[0] + " [" + uuid[1] + "]"
        else:
            incorrect_uuid_string = incorrect_uuid_string + ";" + uuid[0] + " [" + uuid[1] + "]"
    uuid_string = uuid_string + incorrect_uuid_string

    # Add the UUIDs that have high probability.
    uuid_string = uuid_string + ","
    high_certainty_string = ""
    for uuid in UUID_LIST_HIGH:
        if high_certainty_string == "":
            high_certainty_string = high_certainty_string + uuid[0] + " [" + uuid[1] + "]"
        else:
            high_certainty_string = high_certainty_string + ";" + uuid[0] + " [" + uuid[1] + "]"
    uuid_string = uuid_string + high_certainty_string

    # Add the UUIDs that have medium probability after a comma.
    uuid_string = uuid_string + ","
    medium_certainty_string = ""
    for uuid in UUID_LIST_MED:
        if medium_certainty_string == "":
            medium_certainty_string = medium_certainty_string + uuid[0] + " [" + uuid[1] + "]"
        else:
            medium_certainty_string = medium_certainty_string + ";" + uuid[0] + " [" + uuid[1] + "]"
    uuid_string = uuid_string + medium_certainty_string

    # Add the <long,long> UUIDs.
    uuid_string = uuid_string + ","
    longlong_string = ""
    for uuid in LONGLONG_UUIDS:
        if longlong_string == "":
            longlong_string = longlong_string + uuid[0] + " [" + uuid[1] + "]"
        else:
            longlong_string = longlong_string + ";" + uuid[0] + " [" + uuid[1] + "]"
    uuid_string = uuid_string + longlong_string

    # Add statistical info.
    uuid_string = uuid_string + ","
    IDENTIFIED_STRINGS = (len(BLE_UUIDs) 
                              + len(BLE_CREATED_UUIDS) 
                              + len(BLE_INCORRECT_UUIDS) 
                              + len(UUID_LIST_HIGH) 
                              + len(UUID_LIST_MED))
    uuid_string = uuid_string + str(IDENTIFIED_STRINGS) + "," + str(UNIDENTIFIED_STRINGS)
    uuid_string = uuid_string + "," + str(TOTAL_INIT) + "," + str(IDENTIFIED_INIT)
    
    # Add the Classic Bluetooth UUIDs (that are defined fully).
    uuid_string = uuid_string + ","
    classic_uuid_string = ""
    for uuid in CLASSIC_UUIDS:
        if classic_uuid_string == "":
            classic_uuid_string = classic_uuid_string + uuid[0] + " [" + uuid[1] + "]"
        else:
            classic_uuid_string = classic_uuid_string + ";" + uuid[0] + " [" + uuid[1] + "]"
    uuid_string = uuid_string + classic_uuid_string
    
    return uuid_string


def populateReservedUuidList():
    """ Populate the global list of reserved UUIDs.
    
    Populate lists of adopted Bluetooth UUIDs (Classic and LE)
     from hardcoded arrays.
    """
    global RESERVED_CLASSIC_UUIDS
    global RESERVED_BLE_UUIDS

    classic_uuids = ["0000",
                     "0001",
                     "0002",
                     "0003",
                     "0004",
                     "0005",
                     "0006",
                     "0007",
                     "0008",
                     "0009",
                     "0010",
                     "0011",
                     "0012",
                     "0014",
                     "0016",
                     "0017",
                     "0019",
                     "0100",
                     "0200",
                     "0201",
                     "0202",
                     "0203",
                     "0204",
                     "0205",
                     "0206",
                     "0207",
                     "0208",
                     "0209",
                     "0300",
                     "0301",
                     "0302",
                     "0303",
                     "0304",
                     "0305",
                     "0306",
                     "0307",
                     "0308",
                     "0309",
                     "0310",
                     "0311",
                     "0312",
                     "0313",
                     "0314",
                     "0315",
                     "0316",
                     "0317",
                     "0350",
                     "0352",
                     "0354",
                     "0356",
                     "0358",
                     "0360",
                     "0362",
                     "0364",
                     "0366",
                     "0368",
                     "0370",
                     "0372",
                     "0374",
                     "0376",
                     "0378",
                     "1000",
                     "1001",
                     "1002",
                     "1101",
                     "1102",
                     "1103",
                     "1104",
                     "1105",
                     "1106",
                     "1107",
                     "1108",
                     "1109",
                     "1110",
                     "1111",
                     "1112",
                     "1113",
                     "1114",
                     "1115",
                     "1116",
                     "1117",
                     "1118",
                     "1119",
                     "1120",
                     "1121",
                     "1122",
                     "1123",
                     "1124",
                     "1125",
                     "1126",
                     "1127",
                     "1128",
                     "1130",
                     "1131",
                     "1132",
                     "1133",
                     "1134",
                     "1135",
                     "1136",
                     "1200",
                     "1201",
                     "1202",
                     "1203",
                     "1204",
                     "1205",
                     "1206",
                     "1300",
                     "1301",
                     "1302",
                     "1303",
                     "1304",
                     "1305",
                     "1400",
                     "1401",
                     "1402",
                     "0200",
                     "020F",
                     "0210",
                     "0317",
                     "1138",
                     "113A",
                     "113B",
                     "113C",
                     "113D",
                     "113E",
                     "000A",
                     "000B",
                     "000C",
                     "000D",
                     "000E",
                     "000F",
                     "001B",
                     "001E",
                     "001F",
                     "020A",
                     "020B",
                     "020C",
                     "020D",
                     "020E",
                     "0302",
                     "030A",
                     "030B",
                     "030C",
                     "030D",
                     "030E",
                     "035A",
                     "035C",
                     "035E",
                     "037A",
                     "110A",
                     "110B",
                     "110C",
                     "110D",
                     "110E",
                     "110F",
                     "111A",
                     "111B",
                     "111C",
                     "111D",
                     "111E",
                     "111F",
                     "112D",
                     "112E",
                     "112F",
                     "1137",
                     "1139"]

    for classic_uuid in classic_uuids:
        lowercase_uuid = classic_uuid.lower().strip()
        RESERVED_CLASSIC_UUIDS.append(lowercase_uuid)

    reserved_uuids = ["1800",
                      "1801",
                      "1802",
                      "1803",
                      "1804",
                      "1805",
                      "1806",
                      "1807",
                      "1808",
                      "1809",
                      "180A",
                      "180D",
                      "180E",
                      "180F",
                      "1810",
                      "1811",
                      "1812",
                      "1813",
                      "1814",
                      "1815",
                      "1816",
                      "1818",
                      "1819",
                      "181A",
                      "181B",
                      "181C",
                      "181D",
                      "181E",
                      "181F",
                      "1820",
                      "1821",
                      "1822",
                      "1823",
                      "1824",
                      "1825",
                      "1826",
                      "1827",
                      "1828",
                      "1829",
                      "183A",
                      "2800",
                      "2801",
                      "2802",
                      "2803",
                      "2900",
                      "2901",
                      "2902",
                      "2903",
                      "2904",
                      "2905",
                      "2906",
                      "2907",
                      "2908",
                      "2909",
                      "290A",
                      "290B",
                      "290C",
                      "290D",
                      "290E",
                      "2A00",
                      "2A01",
                      "2A02",
                      "2A03",
                      "2A04",
                      "2A05",
                      "2A06",
                      "2A07",
                      "2A08",
                      "2A09",
                      "2A0A",
                      "2A0B",
                      "2A0C",
                      "2A0D",
                      "2A0E",
                      "2A0F",
                      "2A10",
                      "2A11",
                      "2A12",
                      "2A13",
                      "2A14",
                      "2A15",
                      "2A16",
                      "2A17",
                      "2A18",
                      "2A19",
                      "2A1A",
                      "2A1B",
                      "2A1C",
                      "2A1D",
                      "2A1E",
                      "2A1F",
                      "2A20",
                      "2A21",
                      "2A22",
                      "2A23",
                      "2A24",
                      "2A25",
                      "2A26",
                      "2A27",
                      "2A28",
                      "2A29",
                      "2A2A",
                      "2A2B",
                      "2A2C",
                      "2A2F",
                      "2A30",
                      "2A31",
                      "2A32",
                      "2A33",
                      "2A34",
                      "2A35",
                      "2A36",
                      "2A37",
                      "2A38",
                      "2A39",
                      "2A3A",
                      "2A3B",
                      "2A3C",
                      "2A3D",
                      "2A3E",
                      "2A3F",
                      "2A40",
                      "2A41",
                      "2A42",
                      "2A43",
                      "2A44",
                      "2A45",
                      "2A46",
                      "2A47",
                      "2A48",
                      "2A49",
                      "2A4A",
                      "2A4B",
                      "2A4C",
                      "2A4D",
                      "2A4E",
                      "2A4F",
                      "2A50",
                      "2A51",
                      "2A52",
                      "2A53",
                      "2A54",
                      "2A55",
                      "2A56",
                      "2A57",
                      "2A58",
                      "2A59",
                      "2A5A",
                      "2A5B",
                      "2A5C",
                      "2A5D",
                      "2A5E",
                      "2A5F",
                      "2A60",
                      "2A62",
                      "2A63",
                      "2A64",
                      "2A65",
                      "2A66",
                      "2A67",
                      "2A68",
                      "2A69",
                      "2A6A",
                      "2A6B",
                      "2A6C",
                      "2A6D",
                      "2A6E",
                      "2A6F",
                      "2A70",
                      "2A71",
                      "2A72",
                      "2A73",
                      "2A74",
                      "2A75",
                      "2A76",
                      "2A77",
                      "2A78",
                      "2A79",
                      "2A7A",
                      "2A7B",
                      "2A7D",
                      "2A7E",
                      "2A7F",
                      "2A80",
                      "2A81",
                      "2A82",
                      "2A83",
                      "2A84",
                      "2A85",
                      "2A86",
                      "2A87",
                      "2A88",
                      "2A89",
                      "2A8A",
                      "2A8B",
                      "2A8C",
                      "2A8D",
                      "2A8E",
                      "2A8F",
                      "2A90",
                      "2A91",
                      "2A92",
                      "2A93",
                      "2A94",
                      "2A95",
                      "2A96",
                      "2A97",
                      "2A98",
                      "2A99",
                      "2A9A",
                      "2A9B",
                      "2A9C",
                      "2A9D",
                      "2A9E",
                      "2A9F",
                      "2AA0",
                      "2AA1",
                      "2AA2",
                      "2AA3",
                      "2AA4",
                      "2AA5",
                      "2AA6",
                      "2AA7",
                      "2AA8",
                      "2AA9",
                      "2AAA",
                      "2AAB",
                      "2AAC",
                      "2AAD",
                      "2AAE",
                      "2AAF",
                      "2AB0",
                      "2AB1",
                      "2AB2",
                      "2AB3",
                      "2AB4",
                      "2AB5",
                      "2AB6",
                      "2AB7",
                      "2AB8",
                      "2AB9",
                      "2ABA",
                      "2ABB",
                      "2ABC",
                      "2ABD",
                      "2ABE",
                      "2ABF",
                      "2AC0",
                      "2AC1",
                      "2AC2",
                      "2AC3",
                      "2AC4",
                      "2AC5",
                      "2AC6",
                      "2AC7",
                      "2AC8",
                      "2AC9",
                      "2ACC",
                      "2ACD",
                      "2ACE",
                      "2ACF",
                      "2AD0",
                      "2AD1",
                      "2AD2",
                      "2AD3",
                      "2AD4",
                      "2AD5",
                      "2AD6",
                      "2AD7",
                      "2AD8",
                      "2AD9",
                      "2ADA",
                      "2AED",
                      "2B1D",
                      "2B1E",
                      "2B1F",
                      "2B20",
                      "2B21",
                      "2B22",
                      "2B23",
                      "2B24",
                      "2B25",
                      "2B26",
                      "2B27",
                      "2B28",
                      "FDCA",
                      "FDCB",
                      "FDCC",
                      "FDCD",
                      "FDCE",
                      "FDCF",
                      "FDD0",
                      "FDD1",
                      "FDD2",
                      "FDD3",
                      "FDD4",
                      "FDD5",
                      "FDD6",
                      "FDD7",
                      "FDD8",
                      "FDD9",
                      "FDDA",
                      "FDDB",
                      "FDDC",
                      "FDDD",
                      "FDDE",
                      "FDDF",
                      "FDE0",
                      "FDE1",
                      "FDE2",
                      "FDE3",
                      "FDE4",
                      "FDE5",
                      "FDE6",
                      "FDE7",
                      "FDE8",
                      "FDE9",
                      "FDEA",
                      "FDEB",
                      "FDEC",
                      "FDED",
                      "FDEE",
                      "FDEF",
                      "FDF0",
                      "FDF1",
                      "FDF2",
                      "FDF3",
                      "FDF4",
                      "FDF5",
                      "FDF6",
                      "FDF7",
                      "FDF8",
                      "FDF9",
                      "FDFA",
                      "FDFB",
                      "FDFC",
                      "FDFD",
                      "FDFE",
                      "FDFF",
                      "FE00",
                      "FE01",
                      "FE02",
                      "FE03",
                      "FE04",
                      "FE05",
                      "FE06",
                      "FE07",
                      "FE08",
                      "FE09",
                      "FE0A",
                      "FE0B",
                      "FE0C",
                      "FE0D",
                      "FE0E",
                      "FE0F",
                      "FE10",
                      "FE11",
                      "FE12",
                      "FE13",
                      "FE14",
                      "FE15",
                      "FE16",
                      "FE17",
                      "FE18",
                      "FE19",
                      "FE1A",
                      "FE1B",
                      "FE1C",
                      "FE1D",
                      "FE1E",
                      "FE1F",
                      "FE20",
                      "FE21",
                      "FE22",
                      "FE23",
                      "FE24",
                      "FE25",
                      "FE26",
                      "FE27",
                      "FE28",
                      "FE29",
                      "FE2A",
                      "FE2B",
                      "FE2C",
                      "FE2D",
                      "FE2E",
                      "FE2F",
                      "FE30",
                      "FE31",
                      "FE32",
                      "FE33",
                      "FE34",
                      "FE35",
                      "FE36",
                      "FE37",
                      "FE38",
                      "FE39",
                      "FE3A",
                      "FE3B",
                      "FE3C",
                      "FE3D",
                      "FE3E",
                      "FE3F",
                      "FE40",
                      "FE41",
                      "FE42",
                      "FE43",
                      "FE44",
                      "FE45",
                      "FE46",
                      "FE47",
                      "FE48",
                      "FE49",
                      "FE4A",
                      "FE4B",
                      "FE4C",
                      "FE4D",
                      "FE4E",
                      "FE4F",
                      "FE50",
                      "FE51",
                      "FE52",
                      "FE53",
                      "FE54",
                      "FE55",
                      "FE56",
                      "FE57",
                      "FE58",
                      "FE59",
                      "FE5A",
                      "FE5B",
                      "FE5C",
                      "FE5D",
                      "FE5E",
                      "FE5F",
                      "FE60",
                      "FE61",
                      "FE62",
                      "FE63",
                      "FE64",
                      "FE65",
                      "FE66",
                      "FE67",
                      "FE68",
                      "FE69",
                      "FE6A",
                      "FE6B",
                      "FE6C",
                      "FE6D",
                      "FE6E",
                      "FE6F",
                      "FE70",
                      "FE71",
                      "FE72",
                      "FE73",
                      "FE74",
                      "FE75",
                      "FE76",
                      "FE77",
                      "FE78",
                      "FE79",
                      "FE7A",
                      "FE7B",
                      "FE7C",
                      "FE7D",
                      "FE7E",
                      "FE7F",
                      "FE80",
                      "FE81",
                      "FE82",
                      "FE83",
                      "FE84",
                      "FE85",
                      "FE86",
                      "FE87",
                      "FE88",
                      "FE89",
                      "FE8A",
                      "FE8B",
                      "FE8C",
                      "FE8D",
                      "FE8E",
                      "FE8F",
                      "FE90",
                      "FE91",
                      "FE92",
                      "FE93",
                      "FE94",
                      "FE95",
                      "FE96",
                      "FE97",
                      "FE98",
                      "FE99",
                      "FE9A",
                      "FE9B",
                      "FE9C",
                      "FE9D",
                      "FE9E",
                      "FE9F",
                      "FEA0",
                      "FEA1",
                      "FEA2",
                      "FEA3",
                      "FEA4",
                      "FEA5",
                      "FEA6",
                      "FEA7",
                      "FEA8",
                      "FEA9",
                      "FEAA",
                      "FEAB",
                      "FEAC",
                      "FEAD",
                      "FEAE",
                      "FEAF",
                      "FEB0",
                      "FEB1",
                      "FEB2",
                      "FEB3",
                      "FEB4",
                      "FEB5",
                      "FEB6",
                      "FEB7",
                      "FEB8",
                      "FEB9",
                      "FEBA",
                      "FEBB",
                      "FEBC",
                      "FEBD",
                      "FEBE",
                      "FEBF",
                      "FEC0",
                      "FEC1",
                      "FEC2",
                      "FEC3",
                      "FEC4",
                      "FEC5",
                      "FEC6",
                      "FEC7",
                      "FEC8",
                      "FEC9",
                      "FECA",
                      "FECB",
                      "FECC",
                      "FECD",
                      "FECE",
                      "FECF",
                      "FED0",
                      "FED1",
                      "FED2",
                      "FED3",
                      "FED4",
                      "FED5",
                      "FED6",
                      "FED7",
                      "FED8",
                      "FED9",
                      "FEDA",
                      "FEDB",
                      "FEDC",
                      "FEDD",
                      "FEDE",
                      "FEDF",
                      "FEE0",
                      "FEE1",
                      "FEE2",
                      "FEE3",
                      "FEE4",
                      "FEE5",
                      "FEE6",
                      "FEE7",
                      "FEE8",
                      "FEE9",
                      "FEEA",
                      "FEEB",
                      "FEEC",
                      "FEED",
                      "FEEE",
                      "FEEF",
                      "FEF0",
                      "FEF1",
                      "FEF2",
                      "FEF3",
                      "FEF4",
                      "FEF5",
                      "FEF6",
                      "FEF7",
                      "FEF8",
                      "FEF9",
                      "FEFA",
                      "FEFB",
                      "FEFC",
                      "FEFD",
                      "FEFE",
                      "FEFF",
                      "FFFC",
                      "FFFD",
                      "FFFE"]


    for reserved_uuid in reserved_uuids:
        lowercase_uuid = reserved_uuid.lower().strip()
        RESERVED_BLE_UUIDS.append(lowercase_uuid)

#=====================================================#
if __name__ == "__main__":
    main()
