#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, hamming_loss
from sklearn import tree
import numpy as np
import pandas as pd

class ML3RC():
   
    def __init__(self):
        self.classifiers=[]
        self.labels = []
        self.numColonnes = 0
        
    def recurse(self,tree_,node, depth,columns):
        dependencies = []
        val = tree_.feature[node]
        len_x = self.numColonnes - len(self.labels)
        if  val != tree._tree.TREE_UNDEFINED:
            if val >= len_x :
                name = columns[val]
                dependencies.append({'class':name,'depth':depth})
            dependencies = dependencies + self.recurse(tree_,tree_.children_left[node], depth + 1,columns)
            dependencies = dependencies + self.recurse(tree_,tree_.children_right[node], depth + 1,columns)
        return dependencies
    
    def fitdata(self,all_data,y):
        self.classifiers=[]
        self.labels = y.columns
        self.numColonnes = len(all_data.columns)
        x_train, x_test, y_train, y_test = train_test_split(all_data, y, test_size=0.20)
        x_train_ = x_train.drop(self.labels, axis=1)
        x_test_ = x_test.drop(self.labels, axis=1)
        print('1- creating initials classifiers')
        for l in self.labels:
            arbre_dependencies=[]
            x_train_l = x_train.drop([l], axis=1)
            x_test_l = x_test.drop([l], axis=1)
            y_train_l =  y_train[l]
            y_test_l = y_test[l]
            H_l = DecisionTreeClassifier()
            H_l_prime = DecisionTreeClassifier()
            H_l.fit(x_train_, y_train_l)
            H_l_prime.fit(x_train_l, y_train_l)
            y_pred_l = H_l.predict(x_test_)
            y_pred_l_prime = H_l_prime.predict(x_test_l)    
            Acc_H_l = accuracy_score(y_test_l, y_pred_l)
            Acc_H_l_prime = accuracy_score(y_test_l, y_pred_l_prime)
            if Acc_H_l_prime > Acc_H_l :
                H = H_l_prime
                typeclassifier = 1
                acc=Acc_H_l_prime
                report=classification_report(y_test_l,y_pred_l_prime,output_dict=True)
                arbre_dependencies=self.recurse(H.tree_,0, 1,x_train_l.columns)
                hloss=hamming_loss(y_test_l,y_pred_l_prime)
            else:
                H = H_l
                typeclassifier = 0
                acc=Acc_H_l
                report=classification_report(y_test_l,y_pred_l,output_dict=True)
                hloss=hamming_loss(y_test_l,y_pred_l)

            classifier = {'TypeClassifier':typeclassifier,'Label':l,'Classifier':H,'Din':arbre_dependencies,'report':report,'hamming-loss':hloss,'accuracy':acc,'Pout':0,'Pin':0} 
            #print(classification_report(y_test_amazed_suprized, y_pred_amazed_suprized_prime))
            self.classifiers.append(classifier)
        print('2- Start calculating Pin and Pout for S measure')
        self.Pin_Pout()
        print('3- Eliminating cycles')
        self.Eliminate_cycles(x_train,x_test,y_train,y_test)
        self.sortClassifiers()
        self.report()

    def get_classifier_accuracy(self,the_label):
        return list(filter(lambda x: the_label in x['Label'], self.classifiers))[0]['accuracy']
    def get_classifier_by_label(self,the_label):
        return [(idx, the_c) for idx, the_c in enumerate(self.classifiers) if the_c['Label'] == the_label]
    def Pin_Pout(self):
        for classifier in self.classifiers:
            if(classifier['TypeClassifier']==0):
                PJI = 0
            else:
                PJI=0
                the_depth = classifier['Classifier'].get_depth()
                for c in classifier['Din']:
                    index=self.get_classifier_by_label(c['class'])[0][0]
                    v=(1-(c['depth']/the_depth))* self.classifiers[index]['accuracy']
                    PJI += v
                    self.classifiers[index]['Pout']+=v
                    #print(self.classifiers[index]['Label'], " : " ,v ," : ",self.classifiers[index]['Pout'])
            classifier['Pin']=-PJI
            
    def S(self,the_classifier):
        return the_classifier['Pin']+the_classifier['Pout']   
    
    def getSMeasure(self):
        for classifier in self.classifiers:
            print(classifier['Label'],' ---- Pin : ',classifier['Pin'],' | PoutS : ',classifier['Pout'],' | S : ',self.S(classifier))
            
    def Eliminate_cycles(self,x_train,x_test,y_train,y_test):
        for classifier in self.classifiers:
            classifier['Relearn']=False
            for c in classifier['Din']:
                index=self.get_classifier_by_label(c['class'])[0][0]
                j_classifier = self.classifiers[index]
                if self.S(classifier)>self.S(j_classifier):
                    classifier['Relearn']=True
                    classifier['Din']=[x for x in classifier['Din'] if (self.classifiers[index]['Label'] != x.get('class'))]
            if classifier['Relearn']==True: #relearn the classifier
                din_labels = [l.get('class') for l in classifier['Din']]
                delete_labels=[l for l in self.labels if l not in din_labels]
                x_train_for_relearn = x_train.drop(delete_labels, axis=1)
                x_test_for_relearn = x_test.drop(delete_labels, axis=1)
                y_train_for_relearn =  y_train[classifier['Label']]
                y_test_for_relearn = y_test[classifier['Label']]
                H_final = DecisionTreeClassifier()
                H_final.fit(x_train_for_relearn, y_train_for_relearn)
                y_pred= H_final.predict(x_test_for_relearn)
                Acc_H_final = accuracy_score(y_test_for_relearn, y_pred)
                report=classification_report(y_test_for_relearn,y_pred,output_dict=True)
                classifier['TypeClassifier']=2
                classifier['final_accuracy']=Acc_H_final
                classifier['Classifier']=H_final
                classifier['report']=report
    def report(self):
        print("********************** Report for training:")
        acc = 0
        precision=0
        recall=0
        f1score=0
        hloss=0
        numClassifier=len(self.classifiers)
        for classifier in self.classifiers:
            r=classifier['report']
            acc+=classifier['accuracy']
            precision+=r['weighted avg']['precision']
            recall+=r['weighted avg']['recall']
            f1score+=r['weighted avg']['f1-score']
            hloss+=classifier['hamming-loss']
        acc/=numClassifier
        precision/=numClassifier
        recall/=numClassifier
        f1score/=numClassifier
        hloss/=numClassifier
        final_report={'hamming-loss':hloss,'accuracy':acc,'precision':precision,'recall':recall,'f1-score':f1score}
        print(final_report)

    def sortClassifiers(self):
        self.classifiers = sorted(self.classifiers, key=lambda c: self.S(c),reverse=True)
    
    def createPrediction(self,count):
        d={}
        for l in self.labels:
            d[l]=np.zeros(count)
        return d
    def createDataInputsForClassifier(self,classifier,data,predictions):
        data_for_label=data
        for c in classifier['Din']:
            data_for_label=pd.concat([data_for_label,predictions[c['class']]],axis=1)
        return data_for_label
    def Predict(self,data):
        if self.numColonnes-len(self.labels) != len(data.columns):
            print('Test data must be the same dimensions as train data')
            return
        Data = self.createPrediction(data.count()[1])
        predictions = pd.DataFrame (Data, columns = self.labels)
        for classifier in self.classifiers:
            if classifier['TypeClassifier']==0:
                x_test_l=data
            if classifier['TypeClassifier']==1:
                x_test_l=pd.concat([data,predictions.drop([classifier['Label']], axis=1)],axis=1)
            if classifier['TypeClassifier']==2:
                x_test_l = self.createDataInputsForClassifier(classifier,data,predictions)
            
            y_pred_l = classifier['Classifier'].predict(x_test_l)
            predictions[classifier['Label']]=y_pred_l
        return predictions
    def accuracyScore(self,y_test,y_pred):
        scores = []
        for label in y_pred:
            scores.append(accuracy_score(y_test[label],y_pred[label]))
        return scores

