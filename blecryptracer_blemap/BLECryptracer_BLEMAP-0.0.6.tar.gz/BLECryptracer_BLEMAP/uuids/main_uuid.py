from worker_uuid import main as uuidMain
from multiprocessing import Process, JoinableQueue, active_children
import sys
import os
import fnmatch

#APK_FOLDER = "/mnt/sda1/apps_gatt/"
#APK_FOLDER = "../../apks2/"
APK_FOLDER = "/Applications/android-tools/apps/real/"
APK_EXTENSION = "apk"

working_folders = ["working_dir", "violistoutput"]

# Number of (multiprocessing) processes.
NUMBER_OF_PROCESSES = 1

error_output = "crypto_analysis_uuid_error.txt"
fo_err = open(error_output, 'a', 0)


def main():
    # Keep track of the number of processes we create.
    num_processes = 0

    #Check for android.jar file.
    if not os.path.exists("android-8"):
        print "android-8 folder not found in working directory."
        sys.exit(1)
        
    if not os.path.isfile("android-8/android.jar"):
        print "android.jar not found in working directory/android-8."
        sys.exit(1)
        
    #Create required directories.
    for wdir in working_folders:
        if not os.path.exists(wdir):
            os.makedirs(wdir)
            
    # Check whether output file already exists.
    # If it does, then append to existing file.
    # If it doesn't, then create a new file and initialise with headers.
    file_exists = False
    output_file = "crypto_analysis_uuid_output.csv"
    try:
        fo_output_file = open(output_file, 'r')
        fo_output_file.close()
        file_exists = True
    except:
        print "Output file does not yet exist. Creating and initialising with column headers."

    fo_output_file = open(output_file, 'a', 0)
    if file_exists != True:
        fo_output_file.write("FILENAME,"
                             "PACKAGE,"                             
                             "BLUETOOTH_UUIDs_DIRECT,"
                             "BLUETOOTH_UUIDs_CREATED,"
                             "BLUETOOTH_UUIDs_INCORRECT_USE,"
                             "UUID_LIST_DIRECT,"
                             "UUID_LIST_CREATED,"
                             "UUID_LIST_INIT,"
                             "IDENTIFIED_STRINGS,"
                             "UNIDENTIFIED_STRINGS,"
                             "TOTAL_INIT,"
                             "IDENTIFIED_INIT"
                             "CLASSIC_UUIDS,"
                             "CLASSIC_CALLS,"
                             "\n")

    # Enumerate all files in app directory.
    matches = []
    for root, dirnames, filenames in os.walk(APK_FOLDER):
        for filename in fnmatch.filter(filenames, '*' + APK_EXTENSION):
            matches.append(os.path.join(root, filename))

    if matches == []:
        print "No APK files found."
        sys.exit(0)

    # Remove already checked apps from list.
    checked_apks = []
    try:
        checked_file = "crypto_analysis_uuid_checked.txt"
        fo_checked = open(checked_file, 'r')
        checked_apks = fo_checked.read().splitlines()
        fo_checked.close()
    except Exception as e:
        print "No existing list of checked files."

    for checked_apk in checked_apks:
        try:
            matches.remove(checked_apk)
        except Exception as e:
            print "Unable to remove APK from list:", str(e)

    if matches == []:
        print "All APK files checked."
        sys.exit(0)

    length_apk_list = len(matches)/NUMBER_OF_PROCESSES
    length_apk_list = int(length_apk_list)
    print "Total number of APKs:", len(
        matches), "\nApproximate number of APKs per thread:", length_apk_list

    # Free up memory
    checked_apks = None
    initial_matches = None

    # Create two process queues: one for sending data to, and one for receiving data from, worker process.
    process_send_queue = JoinableQueue()
    process_receive_queue = JoinableQueue()

    # List for keeping track of processes.
    process_list = []
    # Create worker processes.
    for i in range(0, NUMBER_OF_PROCESSES):
        worker = Process(target=uuidMain, args=(
            process_send_queue, process_receive_queue, num_processes))
        worker.start()
        process_list.append(worker)
        num_processes += 1

    # Send work to worker process.
    for match in matches:
        process_send_queue.put(str(match))

    fo_checked = open(checked_file, 'a', 0)
    completed_apk_count = 0

    while True:
        # Get information sent by worker process.
        result = process_receive_queue.get()
        process_receive_queue.task_done()
        # Analyse the output string.
        analysed_file = result.split(",")[0]
        fo_checked.write(analysed_file+"\n")
        if "Error" in (result.split(",")[2]):
            write_string = result.split("err_div")[0]
            err_string = result.split("err_div")[1]
            fo_output_file.write(write_string+"\n")
            # Log the error to a separate file.
            fo_err.write(analysed_file+","+err_string)
        else:
            fo_output_file.write(result)
        print "\n  Finished analysing", analysed_file

        # Check if any processes have become zombies.
        if len(active_children()) < NUMBER_OF_PROCESSES:
            for p in process_list:
                if not p.is_alive():
                    process_list.remove(p)
                    # Create a new process in its place.
                    replacement_worker = Process(target=uuidMain, args=(
                        process_send_queue, process_receive_queue, num_processes))
                    replacement_worker.start()
                    process_list.append(replacement_worker)
                    num_processes += 1

        # Check if all APKs have been analysed.
        completed_apk_count += 1
        if completed_apk_count == len(matches):
            break

    print "All done."

    # Tell child processes to stop
    for i in range(NUMBER_OF_PROCESSES):
        process_send_queue.put('STOP')


#=====================================================#
if __name__ == "__main__":
    main()
