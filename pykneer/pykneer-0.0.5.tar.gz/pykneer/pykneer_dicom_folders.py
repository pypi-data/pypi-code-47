# Serena Bonaretti, 2019

"""
Module with functions to organize dicom images in separate folders based on the dicome tag for echo time: tag = "0018|0081"

We consider two possibilities of parent_folder structure:   
    
1. Input contains list of subject folders, which contain list of dicom images with different TE:  
    
   parent
   |___ subject1 (one acquisition)
        |... dicom images with different TE
   |___ subject2 (one acquisition)
        |... dicom images with different TE

   Becomes:
       
   parent
   |___ subject1 (one acquisition)
        |___ subfolder1
             |... dicom images with same TE
        |___ subfolderN
             |... dicom images with same TE        
   |___ subject2 (one acquisition)
        |___ subfolder1
             |... dicom images with same TE
        |___ subfolderN
             |... dicom images with same TE        
    
2. Input contains list of subject folders, which contain different acquisition folders, which contain list of dicom images with different TE: 
    
   parent
   |___ subject1 
        |___ acquistion1
             |... dicom images with different TE
        |___ acquistionM
             |... dicom images with different TE
   |___ subject2 
        |___ acquistion1
             |... dicom images with different TE
        |___ acquistionM
             |... dicom images with different TE
   
   Becomes:
   
   parent
   |___ subject1 
        |___ acquistion1
             |___ subfolder1
                  |... dicom images with same TE
             |___ subfolderN
                  |... dicom images with same TE
        |___ acquistionM
             |___ subfolder1
                  |... dicom images with same TE
             |___ subfolderN
                  |... dicom images with same TE
   |___ subject2 
        |___ acquistion1
             |___ subfolder1
                  |... dicom images with same TE
             |___ subfolderN
                  |... dicom images with same TE
        |___ acquistionM
             |___ subfolder1
                  |... dicom images with same TE
             |___ subfolderN
                  |... dicom images with same TE
                  
"""


import SimpleITK as sitk
import os

# pyKNEER imports 
# ugly way to use relative vs. absolute imports when developing vs. when using package - cannot find a better way
if __package__ is None or __package__ == '':
    # uses current directory visibility
    import pykneer_io  as io
else:
    # uses current package visibility
    from . import pykneer_io  as io


def dicom_to_folders(dicom_folder, output_folder, tag, viz):    
    """
    Separates the dicome folders in subfolder according to the parameter tag in the dicom header of each image (i.e. slice)
    """
    
    folder_div = io.folder_divider()
        
    
    # get file names of dicom in dicom_folder
    series_IDs        = sitk.ImageSeriesReader.GetGDCMSeriesIDs(dicom_folder)
    if len (series_IDs) == 0:
        print ("There are no dicom files in the folder " + dicom_folder)
        return {}
    else: 
        # get all file names
        series_file_names = []
        for i in range(0, len(series_IDs)):
            series_file_names.extend(list(sitk.ImageSeriesReader.GetGDCMSeriesFileNames(dicom_folder, series_IDs[i])))
        
        # prepare the header reader
        reader = sitk.ImageFileReader()
        
        # get TE value from each header
        TE = []
        for i in range(0,len(series_file_names)):
            reader.SetFileName(series_file_names[i])
            img = reader.Execute()
            
            # get metaDataKeys and metaData
            metaDataKeys = img.GetMetaDataKeys()
            metaData     = []
            for k in range (0,len(metaDataKeys)):
                metaData.append(img.GetMetaData( img.GetMetaDataKeys()[k]))
            
            # get TE
            if tag in metaDataKeys:
                index = metaDataKeys.index(tag)
                TE.append(metaData[index])
        
        # find unique values in TE (using sets)
        TE_set    = set(TE)
        unique_TE = list(TE_set)
                
        # sort TE values - sort the strings because TE values are strings in header - conversion to number can cause bugs due to spaces, ect.
        # convert to int to get the indeces to sort the strings in unique_TE
        unique_TE_num = []
        for i in range(0,len(unique_TE)): 
            unique_TE_num.append( float(unique_TE[i]))
        # get the indeces for the sorting
        indeces = sorted(range(len(unique_TE_num)),key=unique_TE_num.__getitem__)
        # sort the strings in unique_TE in ascending order - lower TEs have better contrast than higher TEs
        unique_TE = [unique_TE[i] for i in indeces]
        
        
        # create subdirectories 
        subdir_names = []
        for i in range (0,len(unique_TE)): 
            # subdirectory name
            subdir_name = output_folder + "0" + str(i+1)  + folder_div # considering that there will not be more than 9 echos
            # append to list of subdirectory names
            subdir_names.append(subdir_name)
            # create subdirectory
            if not os.path.isdir(subdir_name):
                os.mkdir(subdir_name)
        
        # print current child directory 
        # get child directory name
        dicom_folder_name = output_folder.rsplit('/', 2)[1]
        # case 1:
        if viz == 1:
              
            print ("____ " + dicom_folder_name + " - " + str(len(series_file_names)) + " images")
        # case 2:
        elif viz == 2:
            print ("    |____ " + dicom_folder_name + " - " + str(len(series_file_names)) + " images")

        
#        # copy files to subdirectories
#        # for each TE
#        for a in range (0,len(unique_TE)):
#            
#            # get index of dicoms with current TE  
#            index = []
#            for i, j in enumerate (TE):
#                if j == str(unique_TE[a]):
#                    index.append(i)
#                 
#            # for each dicom with current TE       
#            for i in index:
#                # define current and next file names
#                image_file_name = series_file_names[i].rsplit('/', 1)[1]
#                name_input  = series_file_names[i]
#                name_output = subdir_names[a] + image_file_name
#                # move the file
#                os.rename(name_input, name_output)   
#           
#            # case 1:
#            if viz == 1:
#                # print current grandchilder directory 
#                dicom_folder_name = subdir_names[a].rsplit('/', 2)[1]
#                print ("    |____ " + dicom_folder_name + " - " + str(len(index)) + " images - TE: " + str(unique_TE[a]))
#            # case 2:
#            elif viz == 2:
#                print ("        |____ " + dicom_folder_name + " - " + str(len(index)) + " images - TE: " + str(unique_TE[a]))
          
        
def organize_folders (parent_folder):  
    
    """
    Reads content of parent folder and determines if it is case 1 or 2
    Creates the output folder "original" 
    """
    
    # dicom tag for echo time 
    tag = "0020|0013"# TE-tag: "0018|0081" # InstanceNumber (0020,0013)
    
    # check whether parent_folder exists
    if not os.path.isdir(parent_folder):
        print("----------------------------------------------------------------------------------------")
        print("ERROR: The folder %s does not exist" % (parent_folder) )
        print("----------------------------------------------------------------------------------------")
        return {}
        
    # make sure there is a backslash at the end of parent_folder
    folder_div = io.folder_divider()
    if not parent_folder.endswith(folder_div):
        parent_folder = parent_folder + folder_div
    
    # get child content
    parent_content = os.listdir(parent_folder)
    
    # create the output_folder "original" if it does not exist already 
    original_folder = parent_folder + "original" + folder_div
    if not os.path.isdir(original_folder):
        os.mkdir(original_folder)

    
    for b in range(0,len(parent_content)):
        subject_folder = parent_folder + parent_content[b]
        
        # if subject_folder is a folder 
        if os.path.isdir(subject_folder) and parent_content[b] != "original":
        
            # make sure there is a backslash at the end of dicom_folder
            if not subject_folder.endswith(folder_div):
                subject_folder = subject_folder + folder_div
            
            # check if subject_folder exists 
            if not os.path.isdir(subject_folder):
                print("----------------------------------------------------------------------------------------")
                print("ERROR: The folder %s does not exist" % (subject_folder) )
                print("----------------------------------------------------------------------------------------")
                return {}
            
            # check that subject_folder is not empty 
            if len(os.listdir(subject_folder)) == 0:
                print("----------------------------------------------------------------------------------------")
                print("ERROR: The folder %s is empty" % (subject_folder) )
                print("----------------------------------------------------------------------------------------")
                return {}
                    
            
            # check if there are acquisition_folders in subject_folder
            # not checking if there are dicoms because sitk.ImageSeriesReader.GetGDCMSeriesIDs returns a warning that compromises the print out of the folder structure
            subject_content = os.listdir(subject_folder)  
            acquisition_folders = []
            for c in range(0,len(subject_content)):
                current_content = subject_folder + subject_content[c]  
                # add current_content to acquisition_folders
                if os.path.isdir(current_content):
                    # make sure there is a backslash at the end of current_content
                    if not current_content.endswith(folder_div):
                        current_content = current_content + folder_div
                    acquisition_folders.append(current_content)
            
            # case 1: file_content are dicom files
            if len(acquisition_folders) == 0:
                # define output_folder to pass to dicom_to_folders
                output_folder = original_folder + parent_content[b] + folder_div
                if not os.path.isdir(output_folder):
                    os.mkdir(output_folder)
                print("-> case 1")
                print(output_folder)
                # separete dicoms in subfolders
                dicom_to_folders(subject_folder, output_folder, tag, 1)
            
            # case 2: file_content are acquisition folders  
            else: 
                # visualize subject_folder 
                folder_file_name = subject_folder.rsplit('/', 2)[1]
                print ("|____ " + folder_file_name)

                print ("\nAcquisition folders")
                print (acquisition_folders)
                
                print (" ")
                # for each acquisition_folders
                for d in range(0, len(acquisition_folders)):
                    
                    # define output_folder to pass to dicom_to_folders
#                    acquisition_folder = original_folder + parent_content[b] + folder_div + os.path.basename(os.path.normpath(acquisition_folders[d])) + folder_div
#                    print ("parent_content[b]:")
#                    print (parent_content[b])
#                    print ("acquisition_folders[d]:")
#                    print (acquisition_folders[d])
#                    print ("os.path.basename(acquisition_folders[d]):")
#                    print (os.path.basename(os.path.normpath(acquisition_folders[d])))
                    
                    # make subject folder
                    output_subject_folder = original_folder + parent_content[b] + folder_div
                    if not os.path.isdir(output_subject_folder):
                        os.mkdir(output_subject_folder)
                    
                    # make acquistion folder 
                    output_acquisition_folder = original_folder + parent_content[b] + folder_div + os.path.basename(os.path.normpath(acquisition_folders[d])) + folder_div
                    if not os.path.isdir(output_acquisition_folder):
                        os.mkdir(output_acquisition_folder)
                    print("-> case 2")
                    print(output_acquisition_folder)
                
                    # separete dicoms in subfolders
                    dicom_to_folders(acquisition_folders[d], output_acquisition_folder, tag, 2)
                    
    print ("--> Done")
