import torch
from PIL import Image
from .utils import inference_imshow


class error_checking():
    """ Needs a lot of brain storming.. Yet incomplete ....
    """
    def __init__(self, opt, filename, dataloader):
        self.opt = opt
        classes = [str(i) for i in range(self.opt.num_classes)]
        worst_pred = {}
        best_pred = {}
        for i in classes:
            worst_pred[i] = []
            best_pred[i] = []

        self.opt.normalize = False
        valset = dataloader(self.opt, train = "valid")
        transforms = valset.test_transformations(opt)
        incorrect_pred = open("incorrect_"+filename.strip().split("/")[3][:-4]+".txt", 'r')
        correct_pred = open("correct_"+filename.strip().split("/")[3][:-4]+".txt", 'r')
        for row in incorrect_pred:
#             print(row)
            list_ = row.strip(" \n").split(", ")
#             print(list_)
            image = Image.open(opt.data_loc + list_[0]).convert('RGB')
            image = transforms(image)
            worst_pred[list_[1]].append((image, list_[2:]))
#             print (worst_pred)
        
        self.worst_pred = worst_pred
        
        for row in correct_pred:
#             print(row)
            list_ = row.strip(" \n").split(", ")
            image = Image.open(opt.data_loc + list_[0]).convert('RGB')
            image = transforms(image)
            best_pred[list_[1]].append((image, list_[2:]))
        
        self.best_pred = best_pred
        
    def worst_prediction(self, label, num=5, imgs_per_row=4):
        '''
        Given a label aka class displays the top incorrect predictions for that class
        '''
        worst_list = self.worst_pred[label]
        if(len(worst_list)<num):
            print('Requested {} but total number of incorrect predictions is {}'.format(num, len(worst_list)))
            num = len(worst_list)
        print("Top {} worst predictions for {}:".format(num,label))
        worst_list = sorted(worst_list, key=itemgetter(1), reverse=True )
        pred_prob = [(p[0],p[1]) for c,p in worst_list[:num]]
        images = torch.stack([image.cpu() for image,_ in worst_list[:num]])
        inference_imshow(images, pred_prob, imgs_per_row = imgs_per_row)
        
    def best_prediction(self, label, num=5, imgs_per_row=4):
        '''
        Given a label aka class displays the top incorrect predictions for that class
        '''
        best_list = self.best_pred[label]
        if(len(best_list)<num):
            print('Requested {} but total number of correct predictions is {}'.format(num, len(best_list)))
            num = len(best_list)
        print("Top {} best predictions for {}:".format(num,label))
        best_list = sorted(best_list, key=itemgetter(1), reverse=True )
        pred_prob = [(p) for c,p in best_list[:num]]
        images = torch.stack([image.cpu() for image,_ in best_list[:num]])
        imshow(images, pred_prob, imgs_per_row = imgs_per_row)
