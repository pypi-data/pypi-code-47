# Serena Bonaretti, 2019

"""
Module with functions to analyze the zib images

"""

import multiprocessing
import numpy as np
import os
import pkg_resources
import platform
import re
import SimpleITK as sitk
import sitk_functions as sitkf
import time

def folder_divider():

    """
    Based on the OS determines if file path strings contain "\" or "/"

    """

    # determine the system to define the folder divider ("\" or "/")
    sys = platform.system()
    if sys == "Linux":
        folder_div = "/"
    elif sys == "Darwin":
        folder_div = "/"
    elif sys == "Windows":
        folder_div = "\\"

    return folder_div



# ---------------------------------------------------------------------------------------------------------------------------
# READ INPUT FILE FOR PREPROCESSING OF ZIB MASKS ----------------------------------------------------------------------------
# function modified from load_image_data_preprocessing in pykneer_io.py -----------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

def load_image_data_preprocessing_metafile(input_file_name):

    """
    Parses the input file of preprocessing.ipynb
    """
    
    folder_div = folder_divider()

    # ----------------------------------------------------------------------------------------------------------------------
    # check if input file exists
    if not os.path.exists(input_file_name):
        print("----------------------------------------------------------------------------------------")
        print("ERROR: The file  %s does not exist" % (input_file_name) )
        print("----------------------------------------------------------------------------------------")
        return {}

    # ----------------------------------------------------------------------------------------------------------------------
    # get input_file_name content
    file_content=[]
    for line in open(input_file_name):
        file_content.append(line.rstrip("\n"))

    # clear empty spaces at the end of strings (if human enters spaces by mistake)
    for i in range(0,len(file_content)):
        file_content[i] = file_content[i].rstrip()

    # ----------------------------------------------------------------------------------------------------------------------
    # folders

    # line 1 is the original folder of acquired dcm
    # add slash or back slash at the end
    original_folder = file_content[0]
    if not original_folder.endswith(folder_div):
        original_folder = original_folder + folder_div
    # make sure the last folder is called "original"
    temp = os.path.basename(os.path.normpath(original_folder))
    if temp != "original":
        print("----------------------------------------------------------------------------------------")
        print("""ERROR: Put your dicoms in a parent folder called "original" """)
        print("----------------------------------------------------------------------------------------")
        return {}
    # make sure that the path exists
    if not os.path.isdir(original_folder):
        print("----------------------------------------------------------------------------------------")
        print("ERROR: The original folder %s does not exist" % (original_folder) )
        print("----------------------------------------------------------------------------------------")
        return {}

    # create the preprocessed folder
    preprocessed_folder = os.path.split(original_folder)[0]     # remove the slash or backslash
    preprocessed_folder = os.path.split(preprocessed_folder)[0] # remove "original"
    preprocessed_folder = preprocessed_folder + folder_div + "preprocessed" + folder_div
    if not os.path.isdir(preprocessed_folder):
        os.mkdir(preprocessed_folder)
        print("-> preprocessed_folder %s created" % (preprocessed_folder) )

    # ----------------------------------------------------------------------------------------------------------------------
    # get images and create a dictionary for each of them
    all_image_data = []
    for i in range(1,len(file_content),2):

        # current image folder name
        image_file_name = file_content[i]

        # if there are empty lines at the end of the file skip them
        if len(image_file_name) != 0:

            # make sure the file exists
            if not os.path.isfile(original_folder + image_file_name):
                print("----------------------------------------------------------------------------------------")
                print("ERROR: The file %s does not exist" % (image_file_name) )
                print("----------------------------------------------------------------------------------------")
                return {}

            # make sure the files is a metafile
            if image_file_name.endswith(".mha") or image_file_name.endswith(".mhd"):
                a = 1 #print(original_folder + image_file_name)
            else:
                print("----------------------------------------------------------------------------------------")
                print("ERROR: The file %s is not a metafile" % (original_folder + image_file_name) )
                print("----------------------------------------------------------------------------------------")
                return {}

            # knee laterality
            laterality = file_content[i+1]
            if laterality != "right" and laterality != "Right" and laterality != "left" and laterality != "left":
                print("----------------------------------------------------------------------------------------")
                print("ERROR: Knee laterality must be 'right' or 'left'")
                print("----------------------------------------------------------------------------------------")
                return {}

            # create the dictionary
            image_data = {}
            # add inputs
            image_data["original_folder"]        = original_folder
            image_data["preprocessed_folder"]    = preprocessed_folder
            image_data["image_file_name"] = image_file_name
            image_data["laterality"]             = laterality
            # add outputs
            image_name_root, image_name_ext = os.path.splitext(image_file_name)
            image_data["image_name_root"]        = image_name_root
            image_data["temp_file_name"]         = preprocessed_folder + image_data["image_name_root"] + "_temp.mha"
            image_data["original_file_name"]     = preprocessed_folder + image_data["image_name_root"] + "_orig.mha"
            image_data["preprocessed_file_name"] = preprocessed_folder + image_data["image_name_root"] + "_prep.mha"
            image_data["info_file_name"]         = preprocessed_folder + image_data["image_name_root"] + "_orig.txt"

            # print current file name
            print (image_data["image_name_root"])

            # send to the data list
            all_image_data.append(image_data)

    print ("-> information loaded for " + str(len(all_image_data)) + " subjects")

    # return the dictionary
    return all_image_data



# ---------------------------------------------------------------------------------------------------------------------------
# READ IMAGES IN PREPROCESSING OF ZIB MASKS ---------------------------------------------------------------------------------
# function modified from sitk_functions.py ----------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------


def read_metafile_images_s(image_data):

    # read dicom stack and put it in a 3D matrix
    img = sitk.ReadImage(image_data["original_folder"] + image_data["image_file_name"]) # ReadImage is the only function changed 
    
    # print out image information
    print("-> " + image_data["image_name_root"])
    sitkf.print_image_info(img)

    # save image to temp
    sitk.WriteImage(img, image_data["temp_file_name"])

def read_metafile_images(all_image_data, n_of_processes):

    start_time = time.time()
    pool = multiprocessing.Pool(processes=n_of_processes)
    pool.map(read_metafile_images_s, all_image_data)
    print ("-> Metafile images read")
    print ("-> The total time was %.2f seconds (about %d min)" % ((time.time() - start_time), (time.time() - start_time)/60))


def cast_to_int(all_image_data):
    # Make sure that all images are in Int
    
    for i in range(0, len(all_image_data)):
        
        mask_name = all_image_data[i]["original_folder"] + all_image_data[i]["image_file_name"]
        
        # read mask
        mask = sitk.ReadImage(mask_name)
        
        # cast mask
        mask = sitk.Cast(mask,sitk.sitkInt16)
        
        # save mask
        sitk.WriteImage(mask, mask_name)