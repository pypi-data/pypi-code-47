from imagepreprocessing import create_training_data_keras,create_training_data_yolo, make_prediction_from_directory, make_prediction_from_array, create_confusion_matrix, train_test_split

source_path = "C:\\Users\\can\\ProjectDependencies\\datasets\\deep_learning\\food-101\\only3"
save_path = "C:\\Users\\can\\Desktop\\food"

images_path = "C:\\Users\\can\\PROJECTS\\PythonProjects\\deep_learning\\test_images\\food2"
model_path = "C:\\Users\\can\\PROJECTS\\PythonProjects\\deep_learning\\saved_models\\a.h5"

class_names = ["elma","ayva","armut"]



# create_training_data_yolo(source_path, percent_to_use=0.1,rename_duplicates=True, validation_split = 0.2)

# create_training_data_yolo(source_path, percent_to_use=1,validation_split = 0.2, auto_label_by_center = False)

create_training_data_yolo(source_path, train_machine_path_sep = "\\", percent_to_use = 1, validation_split = 0.2, auto_label_by_center = False)



# x, y, x_val, y_val = create_training_data_keras(source_path, save_path = None, validation_split=0.2, percent_to_use=0.1)

# x, y, test_x, test_y =  train_test_split(x,y, save_path=None)


# predictions = make_prediction_from_array(test_x, model_path, print_output=False)

# create_confusion_matrix(predictions,test_y,class_names=class_names, one_hot=True)




# class_names = ["elma","ayva","armut"]
# classes =     [0,0,0, 1,1,1, 2,2,2]
# predictions = [0,0,0, 0,1,1, 2,1,2]

# pred = make_prediction_from_directory(images_path, model_path, print_output=False)

# create_confusion_matrix(predictions,classes,class_names=class_names)














# # BUNU YAP BI ARA
# import keras
# import numpy as np
# model = keras.models.load_model(model_path)
# score = model.evaluate(test_x, test_y, verbose=0)
# print('Test loss:', score[0])
# print('Test accuracy:', score[1])
# print(score)


