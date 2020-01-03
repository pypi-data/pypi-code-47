import os
import random
import pickle
import itertools 
from shutil import copyfile


def __write_to_file(to_write, file_name):
    with open(file_name,'w', encoding='utf-8') as file:
        for item in to_write:
            file.write(item.__str__())
            file.write("\n")

def __run_shell_command(command):
    import subprocess
    output = subprocess.check_output(command, shell=True).decode("ascii")
    return output



def create_training_data_keras(source_path, save_path = None, img_size = 224, percent_to_use = 1, validation_split = 0, grayscale = False, one_hot = True, shuffle = True, numpy_array = True, files_to_exclude = [".DS_Store",""]):
    """
    Creates train ready data for classification from image data
    Takes all the image directories alphabetically in a main directory 

    # Arguments:
        source_path: source path of the images see input format
        save_path (None): save path for clean training data 
        img_size (224): size of the images for resizing
        percent_to_use (1): percentage of data that will be used
        validation_split (0.2): splits validation data with given percentage give 0 if you don't want validation split
        grayscale (False): converts images to grayscale
        one_hot (True): makes one hot encoded y train if True if not uses class indexes as labels
        shuffle (True): shuffle the data
        numpy_array (True): converts list to numpy array if True
        files_to_exclude ([".DS_Store",""]): list of file names to exclude in the image directory (can be hidden files)

    # Returns:
        List or numpy array of train data optionally validation data
        if validation_split is 0 -> x, y
        if validation_split is not 0 -> x, y, x_val, y_val

    # Save:
        Saves x train and y train optionally validation x and y 
        Save format is .pkl (pickle data)
        If you want you can prevent saveing the file by passing None as save_path

    # Input format:
        source_path = some_dir
        
        /some_dir
        ├──/class1
            ├──img1.jpg
            ├──img2.jpg
        ├──/class2
            ├──img1.jpg

    # Output format:
        save_path = save/food_data

        save/food_data_x_train.pkl
        save/food_data_y_train.pkl   
        save/food_data_x_validation.pkl
        save/food_data_y_validation.pkl   
        
    # Example:
        ``python
            source_path = "C:\\Users\\can\\datasets\\deep_learning\\food-101\\only3"
            save_path = "C:\\Users\\can\\Desktop\\food10class1000sampleeach"
            create_training_data_keras(source_path, save_path, img_size = 299, validation_split=0.1, percent_to_use=0.1, grayscale = True, files_to_exclude=["excludemoe","hi.txt"])
        ``                      
    """

    import numpy as np
    import cv2

    x = []
    y = [] 
    x_val = []
    y_val = []

    CATEGORIES = os.listdir(source_path)  # get all file names from main dir
    CATEGORIES.sort()                     # sort the directories

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in CATEGORIES: 
            CATEGORIES.remove(exclude)
    

    # loop in the main directory
    for category_index, category in enumerate(CATEGORIES):

        path = os.path.join(source_path, category)
        number_of_categories = len(CATEGORIES)
        index_of_category = CATEGORIES.index(category)
        images = os.listdir(path)


        # fix possible percentage errors
        if(validation_split < 0 or validation_split > 1):
            print("Enter a possible validation_split between 0 and 1")
            return

        if(percent_to_use <= 0 or percent_to_use > 1):
            print("Enter a possible percentage between 0 and 1")
            return
        elif(int(percent_to_use * len(images)) == 0):
            print("Percentage is too small for this set")
            return
        else:
            stop_index = int(len(images)*percent_to_use)


        # loop inside each category folder with itertools for stoping on a percentage
        for image_index, img in enumerate(itertools.islice(images , 0, stop_index)):

            # print percent info
            print("File name: {} - {}/{}  Image:{}/{}".format(category, index_of_category+1, number_of_categories, image_index+1, stop_index), end="\r")
            
            # there can be broken images
            try:
                # convert grayscale
                if(grayscale):
                    temp_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                else:
                    temp_array = cv2.imread(os.path.join(path, img)) 

                # resize image
                img_array = cv2.resize(temp_array, (img_size, img_size))   

                # one hot encoding
                if(one_hot):  
                    temp_y = []
                    for i in range(len(CATEGORIES)):
                        if(i == category_index):
                            temp_y.append(1)
                        else:
                            temp_y.append(0)
                    y.append(temp_y)
                # if one hot is not selected use index of the file as label
                else:
                    y.append(index_of_category)  

                x.append(img_array)
            except:
                pass

        print("")


    if(shuffle):
        xy = list(zip(x,y))
        random.shuffle(xy)
        x, y = list(zip(*xy))
    

    # validation split
    if(validation_split != 0):
        if(int(validation_split * len(images)) == 0):
            print("Validation split is too small for this set")
            return

        # split
        train_percent = int(len(x) - (validation_split * len(x)))
        x_val = x[train_percent:]
        y_val = y[train_percent:]
        x = x[:train_percent]
        y = y[:train_percent]

        print("\nvalidation x: {0} validation y: {1}".format(len(x_val),len(y_val)))

    print("train x: {0} train y: {1}\n".format(len(x),len(y)))

    # array conversion
    if(numpy_array):
        if(grayscale):
            third_dimension = 1
        else:
            third_dimension = 3
    
        x = np.array(x).reshape(-1, img_size, img_size, third_dimension)
        y = np.array(y)

        print("shape of train x: {0}\nshape of train y: {1}".format(x.shape,y.shape))

        if(validation_split != 0):
            x_val = np.array(x_val).reshape(-1, img_size, img_size, third_dimension)
            y_val = np.array(y_val)    
            print("shape of validation x: {0}\nshape of validation y: {1}".format(x_val.shape,y_val.shape))
    

    # save
    if(save_path != None):
        with open(save_path + "_x_train.pkl", "wb") as file:
            pickle.dump(x, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("\nfile saved -> {0}{1}".format(save_path,"_x_train.pkl"))

        with open(save_path + "_y_train.pkl", "wb") as file:
            pickle.dump(y, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("file saved -> {0}{1}".format(save_path,"_y_train.pkl"))
        
        if(validation_split != 0):
            with open(save_path + "_x_validation.pkl", "wb") as file:
                pickle.dump(x_val, file, protocol=pickle.HIGHEST_PROTOCOL)
                print("file saved -> {0}{1}".format(save_path,"_x_validation.pkl"))

            with open(save_path + "_y_validation.pkl", "wb") as file:
                pickle.dump(y_val, file, protocol=pickle.HIGHEST_PROTOCOL)
                print("file saved -> {0}{1}\n".format(save_path,"_y_validation.pkl"))
        
    if(validation_split):
        return x, y, x_val, y_val
    else:
        return x, y

# bunun adini degistirdim karıistirma
def create_training_data_yolo(source_path, percent_to_use = 1, validation_split = 0.2, auto_label_by_center = False, train_machine_path_sep = "/", shuffle = True, files_to_exclude = [".DS_Store","train.txt","test.txt","obj.names","obj.data"]):
    """
    Creates required training files for yolo 

    # Arguments:
        source_path: source path of the images see input format
        percent_to_use (1): percentage of data that will be used
        validation_split (0.2): splits validation data with given percentage give 0 if you don't want validation split
        auto_label_by_center (False): creates label txt files for all images labels images by their center automatically (use it if all of your datasets images are centered)
        train_machine_path_sep ("/"): if you are going to use a windows machine for training change this  
        shuffle (True): shuffle the paths
        files_to_exclude ([".DS_Store","train.txt","test.txt","obj.names","obj.data"]): list of file names to exclude in the image directory (can be hidden files)

    # Save:
        Creates train.txt and test.txt files

    # Input format:
        source_path = some_dir
        
        /some_dir
        ├──/class1
            ├──img1.jpg
            ├──img2.jpg
        ├──/class2
            ├──img3.jpg

    # Output format:
        /some_dir
        train.txt --> data/obj/class1/img1.jpg
        test.txt   
        obj.data
        obj.names                
    """


    # get all file names from main dir and sort the directories
    CATEGORIES = os.listdir(source_path)  
    CATEGORIES.sort()           

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in CATEGORIES: 
            CATEGORIES.remove(exclude)
    
    # change path seperator if needed
    save_path = "data/obj/".replace("/",train_machine_path_sep)

    # prepare obj.data
    objdata = []
    objdata.append("classes = {0}".format(len(CATEGORIES)))
    objdata.append("train  = data/train.txt".replace("/",train_machine_path_sep))
    objdata.append("valid  = data/test.txt".replace("/",train_machine_path_sep))
    objdata.append("names = data/obj.names".replace("/",train_machine_path_sep))
    objdata.append("backup = backup")


    total_image_count = 0
    image_names = []
    # loop in the main directory
    for category_index, category in enumerate(CATEGORIES):

        path = os.path.join(source_path, category)
        number_of_categories = len(CATEGORIES)
        index_of_category = CATEGORIES.index(category)
        images = os.listdir(path)

        # fix possible percentage error
        if(percent_to_use <= 0 or percent_to_use > 1):
            print("Enter a possible percentage between 0 and 1")
            return
        elif(int(percent_to_use * len(images)) == 0):
            print("Percentage is too small for this set")
            return
        else:
            stop_index = int(len(images)*percent_to_use)


        # loop inside each category folder   itertools for stoping on a percentage
        for image_index, img in enumerate(itertools.islice(images , 0, stop_index)):

            # percent info
            print("File name: {} - {}/{}  Image:{}/{}".format(category, index_of_category+1, number_of_categories, image_index+1, stop_index), end="\r")


            # if auto_label_by_center is True create label files and label images by the image center
            if(auto_label_by_center):
                yolo_labels = "{0} {1} {2} {3} {4}".format(category_index, 0.5, 0.5, 1, 1)
                
                basename, extension = os.path.splitext(img)
                txtname = basename + ".txt"
                abs_save_path = os.path.join(path, txtname)
        
                __write_to_file([yolo_labels], file_name = abs_save_path)

            # using save_path's last character (data/obj/ or data\\obj\\) to separete inner paths so if operating system is different inner paths will be matches 
            img_and_path = save_path + category + save_path[-1] + img
            image_names.append(img_and_path)
            
            # count images for dividing validation later
            total_image_count += 1
        
        print("")


    # shuffle and divide train and test sets
    if(shuffle):
        random.shuffle(image_names)
    image_names_train = []
    image_names_test = []
    train_percent = int((validation_split * total_image_count))
    image_names_train += image_names[train_percent:]
    image_names_test += image_names[:train_percent]


    # create files
    __write_to_file(image_names_train, file_name = os.path.join(source_path, "train.txt"))
    __write_to_file(image_names_test, file_name = os.path.join(source_path, "test.txt"))

    __write_to_file(CATEGORIES, file_name = os.path.join(source_path, "obj.names"))
    __write_to_file(objdata, file_name = os.path.join(source_path, "obj.data"))

    print("\nfile saved -> {0}\nfile saved -> {1}\nfile saved -> {2}\nfile saved -> {3}".format("train.txt", "test.txt","obj.names","obj.data"))


def make_prediction_from_directory_keras(images_path, keras_model_path, image_size = 224, print_output=True, model_summary=True, show_images=False, grayscale = False, files_to_exclude = [".DS_Store",""]):
    """
    Reads test data from directory resizes it and makes prediction with using a keras model

    # Arguments:
        images_path: source path of the test images see input format
        keras_model_path: path of the keras model 
        img_size (224): size of the images for resizing
        print_output (True): prints output
        model_summary (True): shows keras model summary 
        show_images (False): shows the predicted image
        grayscale (False): converts images to grayscale
        files_to_exclude ([".DS_Store",""]): list of file names to exclude in the image directory (can be hidden files)

    # Returns:
        Prediction results in a list
    
    # Input format:
        images_path = some_dir
        
        /some_dir
            ├──img1.jpg
            ├──img2.jpg
    """

    import warnings
    warnings.filterwarnings("ignore")

    import matplotlib.pyplot as plt
    import numpy as np
    import keras
    import cv2

    test_images = []
    test_image_names = []

    images = os.listdir(images_path)
    images.sort()

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in images: 
            images.remove(exclude)

    # load model
    model = keras.models.load_model(keras_model_path)

    # get all images
    for image in images:
        abs_path = os.path.join(images_path, image)

        try:
            if(grayscale):
                third_dimension = 1
                img_array = cv2.imread(abs_path, cv2.IMREAD_GRAYSCALE)
            else:
                third_dimension = 3
                img_array = cv2.imread(abs_path)

            new_array = cv2.resize(img_array, (image_size, image_size))
            test_images.append(new_array.reshape(-1, image_size, image_size, third_dimension))    
            test_image_names.append(image)
        except:
            pass
    
    # show model summary
    if(model_summary):
        model.summary()

    predictions = []

    for image, name in zip(test_images,test_image_names):
        prediction = model.predict(image)
        prediction_class = np.argmax(prediction)
        predictions.append(prediction_class)
        if(print_output):
            print("{0} : {1}".format(name,prediction_class))

        if(show_images):
            abs_path = os.path.join(images_path, name)
            img = cv2.imread(abs_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgplot = plt.imshow(img)
            plt.show()

    return predictions


def make_prediction_from_array_keras(test_x, keras_model_path, print_output=True, model_summary=True, show_images=False):
    """
    makes prediction with using a keras model

    # Arguments:
        test_x: numpy array of images
        keras_model_path: path of the keras model
        print_output (True): prints output
        model_summary (True): shows keras model summary 
        show_images (False): shows the predicted image
        grayscale (False): converts images to grayscale
        files_to_exclude ([".DS_Store",""]): list of file names to exclude in the image directory (can be hidden files)

    # Returns:
        Prediction results in a list
    """

    import warnings
    warnings.filterwarnings("ignore")

    import matplotlib.pyplot as plt
    import numpy as np
    import keras
    import cv2

    # load model
    model = keras.models.load_model(keras_model_path)

    # show model summary
    if(model_summary):
        model.summary()

    predictions = []

    for index, image in enumerate(test_x):

        # add an extra dimension to array since we are iterating over the array the first dimension is disapeares
        new_image = np.expand_dims(image, axis=0)
        prediction = model.predict(new_image)
        prediction_class = np.argmax(prediction)
        predictions.append(prediction_class)
        if(print_output):
            print("{0} : {1}".format(index, prediction_class))

        if(show_images):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            imgplot = plt.imshow(image)
            plt.show()

    return predictions


def make_prediction_from_directory_yolo(images_path, darknet_path, darknet_command = "./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights {0} -i 0 -thresh 0.2 -dont_show", save_path = "detection_results", handle_shell_exceptions = True, files_to_exclude = [".DS_Store",""]):
    """
    
    """

    save_path = os.path.join(darknet_path, save_path)

    # make the dir
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    images = os.listdir(images_path)
    images.sort()

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in images: 
            images.remove(exclude)

    image_count = len(images)
    for index, image in enumerate(images):
        abs_path = os.path.join(images_path, image)

        if(handle_shell_exceptions):
            try:
                __run_shell_command("cd {0} && {1}".format(darknet_path,darknet_command.format(abs_path)))
            except:
                pass
        else:
            __run_shell_command("cd {0} && {1}".format(darknet_path,darknet_command.format(abs_path)))

        copyfile(os.path.join(darknet_path, "predictions.jpg"), os.path.join(save_path, "predictions{0}.jpg".format(index)))
        
        print("File name: {0} - {1}/{2}".format(image, index+1, image_count), end="\r")

    print("\nAll images saved to {0}".format(save_path))


def train_test_split(train_x, train_y, test_size=0.2, save_path=None):
    """
    Splits train and test sets from numpy array

    # Arguments:
        train_x: taining data
        train_y: labels of the training data
        test_size (0.2): size of the test set to split
        save_path (None): save path for for seperated data

    # Returns 
        splitted train and test data
        train_x, train_y, test_x, test_y
    """

    new_train_x = []
    new_train_y = []
    
    test_x = []
    test_y = []

    if(len(train_x) != len(train_y)):
        print("x and y sizes does not match")
        return
    
    data_count = len(train_x)
    train_percent = int((data_count * test_size))

    new_train_x = train_x[train_percent:]
    new_train_y = train_y[train_percent:]
    
    test_x = train_x[:train_percent]
    test_y = train_y[:train_percent]

    print("\ntest x: {0} test y: {1}".format(len(test_x),len(test_x)))
    print("train x: {0} train y: {1}".format(len(new_train_x),len(new_train_y)))

    # save
    if(save_path != None):
        with open(save_path + "_x_train.pkl", "wb") as file:
            pickle.dump(new_train_x, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("\nfile saved -> {0}{1}".format(save_path,"_x_train.pkl"))

        with open(save_path + "_y_train.pkl", "wb") as file:
            pickle.dump(new_train_y, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("file saved -> {0}{1}".format(save_path,"_y_train.pkl"))
        
        with open(save_path + "_x_test.pkl", "wb") as file:
            pickle.dump(test_x, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("file saved -> {0}{1}".format(save_path,"_x_test.pkl"))

        with open(save_path + "_y_test.pkl", "wb") as file:
            pickle.dump(test_y, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("file saved -> {0}{1}\n".format(save_path,"_y_test.pkl"))
        
    return new_train_x, new_train_y, test_x, test_y


def create_confusion_matrix(predictions, actual_values, class_names=None, one_hot=False, normalize=False):
    """ 
    Creates a confusion matrix

    # Arguments:
        predictions: list of predicted numerical class labels of each sample ex:[1,2,5,3,1]
        actual_values: list of actual numerical class labels of each sample ex:[1,2,5,3,1] or onehot encoded [[0,0,1],[1,0,0],[0,1,0]]
        class_names (None): names of classes that will be drawn, if you want only the array and not the plot pass None (matplotlib required)
        one_hot (False): if labels are one hot formatted use this
        normalize (False): normalizes the values of the matrix

    # Retruns:
        A numpy array of confusion matrix 
    """
    from sklearn.metrics import confusion_matrix
    import numpy as np

    # decode one hot
    if(one_hot):
        labels = []
        for one_hot_value in actual_values:
            for index,value in enumerate(one_hot_value):
                if(value == 1):
                    labels.append(index)
        actual_values = labels

    # create confusion matrix
    cnf_matrix = confusion_matrix(actual_values, predictions)

    if(normalize):
        cnf_matrix = cnf_matrix.astype('float') / cnf_matrix.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Not Normalized confusion matrix')
    
    print("xlabel: True label\nylabel: predicted label")
    print(cnf_matrix)

    # plot the matrix
    if(class_names):
        import matplotlib.pyplot as plt

        title='Confusion matrix'
        cmap=plt.cm.Blues

        plt.imshow(cnf_matrix, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(class_names))
        plt.xticks(tick_marks, class_names, rotation=45)
        plt.yticks(tick_marks, class_names)

        
        thresh = cnf_matrix.max() / 2.
        for i, j in itertools.product(range(cnf_matrix.shape[0]), range(cnf_matrix.shape[1])):
            plt.text(j, i, cnf_matrix[i, j],horizontalalignment="center",color="white" if cnf_matrix[i, j] > thresh else "black")
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()

    return cnf_matrix









# decrypted
def __create_training_data_yolo(source_path, save_path = "data/obj/", percent_to_use = 1, validation_split = 0.2, rename_duplicates = False, shuffle = True, files_to_exclude = [".DS_Store","data","train.txt","test.txt","obj.names","obj.data"]):
    """
    Creates train ready data for yolo, labels all the images by center automatically
    (This is not the optimal way of labeling but if you need a lot of data fast this is an option)

    # Arguments:
        source_path: source path of the images see input format
        save_path (data/obj/): this path will be added at the begining of every image name in the train.txt and test.txt files
        percent_to_use (1): percentage of data that will be used
        validation_split (0.2): splits validation data with given percentage give 0 if you don't want validation split
        rename_duplicates (False): renames duplicates while copying images but it slows down the process if you don't have any duplicates in your set don't use it
        shuffle (True): shuffle the paths
        files_to_exclude ([".DS_Store","data,"train.txt","test.txt","obj.names","obj.data"]): list of file names to exclude in the image directory (can be hidden files)

    # Save:
        Copies all images in to save_path directory and creates txt files for each image see output format

    # Input format:
        (if there are duplicates you can use rename duplicates)
        source_path = some_dir
        
        /some_dir
        ├──/class1
            ├──img1.jpg
            ├──img2.jpg
            ├──img3.jpg
        ├──/class2
            ├──img3.jpg

    # Output format:
        (if rename duplicates is on it renames images)
        source_path = some_dir
        save_path = "data/obj/"
        
        /some_dir
        train.txt
        test.txt
        ├──data/obj/
            ├──img1.jpg
            ├──img1.txt
            ├──img2.jpg
            ├──img2.txt
            ├──img3.jpg
            ├──img3.txt
            ├──img3(1).jpg
            ├──img3(1).txt                  
    """

    image_names = [] 
    
    CATEGORIES = os.listdir(source_path)  # get all file names from main dir
    CATEGORIES.sort()                     # sort the directories

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in CATEGORIES: 
            CATEGORIES.remove(exclude)
    
    # make the dir
    if not os.path.exists(os.path.join(source_path, save_path)):
        os.makedirs(os.path.join(source_path, save_path))
    
    total_image_count = 0

    # loop in the main directory
    for category_index, category in enumerate(CATEGORIES):


        path = os.path.join(source_path, category)
        number_of_categories = len(CATEGORIES)
        index_of_category = CATEGORIES.index(category)
        images = os.listdir(path)

        # fix possible percentage error
        if(percent_to_use <= 0 or percent_to_use > 1):
            print("Enter a possible percentage between 0 and 1")
            return
        elif(int(percent_to_use * len(images)) == 0):
            print("Percentage is too small for this set")
            return
        else:
            stop_index = int(len(images)*percent_to_use)

              

        # loop inside each category folder   itertools for stoping on a percentage
        for image_index, img in enumerate(itertools.islice(images , 0, stop_index)):

            # percent info
            print("File name: {} - {}/{}  Image:{}/{}".format(category, index_of_category+1, number_of_categories, image_index+1, stop_index), end="\r")

        
            # yolo label format
            # <object-class> <x_center> <y_center> <width> <height>
            # class 0.5 0.5 1 1 

            yolo_labels = "{0} {1} {2} {3} {4}".format(category_index, 0.5, 0.5, 1, 1)
            
            absolute_save_path = os.path.join(source_path, save_path)
            img_and_path = save_path + img

            # if rename duplicates enabled name can be changed but original name is needed to copy the file 
            img_new_name = img

            # rename duplicates if enabled
            if(rename_duplicates):
                duplicate_number = 1
                while(True):
                    if(img_and_path in image_names):

                        # reset the image name tor prevet something like this img(1)(2).jpg
                        img_and_path = save_path + img 

                        # change the image name in the train or test file
                        basename, extension = os.path.splitext(img_and_path)
                        img_and_path = "{0}{1}{2}{3}{4}".format(basename, "(", duplicate_number, ")", extension)
                        
                        # change real image name
                        basename, extension = os.path.splitext(img)
                        img_new_name = "{0}{1}{2}{3}{4}".format(basename, "(", duplicate_number, ")", extension)
                        duplicate_number += 1
                    else:
                        break
            

            basename, _ = os.path.splitext(img_new_name)
            text_name = basename + ".txt"
            path_for_txt_file = os.path.join(absolute_save_path, text_name)
 
            __write_to_file([yolo_labels], path_for_txt_file)


            # copy_files_to_new_path
            new_path_img = os.path.join(absolute_save_path, img_new_name)            
            copyfile(os.path.join(path, img), new_path_img)

            image_names.append(img_and_path)

            # count images for dividing validation later
            total_image_count += 1
        
        print("")

    # shuffle and divide train and test sets
    if(shuffle):
        random.shuffle(image_names)
    image_names_train = []
    image_names_test = []

    train_percent = int((validation_split * total_image_count))
    image_names_train += image_names[train_percent:]
    image_names_test += image_names[:train_percent]

    # prepare obj.data
    objdata = []
    objdata.append("classes = {0}".format(len(CATEGORIES)))
    objdata.append("train  = data/train.txt")
    objdata.append("valid  = data/test.txt")
    objdata.append("names = data/obj.names")
    objdata.append("backup = backup")

    # save to file
    __write_to_file(image_names_train, file_name = os.path.join(source_path, "train.txt"))
    __write_to_file(image_names_test, file_name = os.path.join(source_path, "test.txt"))

    __write_to_file(CATEGORIES, file_name = os.path.join(source_path, "obj.names"))
    __write_to_file(objdata, file_name = os.path.join(source_path, "obj.data"))

    print("\nfile saved -> {0}\nfile saved -> {1}\nfile saved -> {2}\nfile saved -> {3}".format("train.txt", "test.txt","obj.names","obj.data"))






