import numpy as np
import cv2 
from scipy.linalg import logm

class Kernel():
    def __init__(self):
#init
        self.Primeval_First_Kernel= np.array([[-1,0,1]])
        self.Primeval_second_Kernel= np.array([[1,-2,1]])
#sabel NEED ROTATION 180
        self.sabelx=np.array([[1,0,-1], [2,0,-2], [1,0,-1]])
        self.sabely=self.sabelx.T
        pass

class CovD(object):
    def __init__(self,rectangle=(500,500),**fx):
        self.fx=fx
        self.rectangle=rectangle

        self.First_order = np.mat([-1,0,1])
        self.second_order= np.mat([1,-2,1])
#sabel NEED ROTATION 180
        self.sabelx=np.array([[1,0,-1], [2,0,-2], [1,0,-1]])
        self.sabely=self.sabelx.T


    def _First_Derivative(self,Gray_img,kernel=None):
        if kernel is None:
            kernel=self.First_order
        dx = cv2.filter2D(Gray_img, cv2.CV_64F, kernel)
        dy = cv2.filter2D(Gray_img, cv2.CV_64F, kernel.T)
        return dx,dy

    def _Second_Derivative(self,Gray_img,kernel=None):
        if kernel is None:
            kernel=self.second_order
        ddx = cv2.filter2D(Gray_img, cv2.CV_64F,kernel)
        ddy = cv2.filter2D(Gray_img, cv2.CV_64F,kernel.T)
        return ddx, ddy

    def get_CovD(self,image,center=None,rectangle=None):
        if rectangle is None:
            rectangle=self.rectangle
        # if fx is None:
        if center is None:
            center=(image.shape[0]//2,image.shape[1]//2)
        rect=[center[0]-rectangle[0]//2,center[0]+rectangle[0]//2,center[1]-rectangle[1]//2,center[1]+rectangle[1]//2 ]
        image=image[rect[0]-1 : rect[1]+1, rect[2]-1 :rect[3]+1 ,:]
        grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        dimension=sum(self.fx.values())#a error will generated when use np.sum
        F=np.zeros((rectangle[0],rectangle[1],dimension))
        dx,dy=self._First_Derivative(grayimage)
        ddx,ddy=self._Second_Derivative(grayimage)
        dx=np.abs(dx)
        dy=np.abs(dy)
        ddx=np.abs(ddx)
        ddy=np.abs(ddy)
        i=0
        for key,value in self.fx.items():
            if key is "I" and value is True:
                F[:,:,i]=grayimage[1:-1,1:-1]
                i=i+1
            if key is "x" and value is True:
                F[:,:,i]=F[:,:,i] * np.arange(rectangle[0]).reshape((-1,1))
                i=i+1
            if key is "y" and value is True:
                F[:,:,i]=F[:,:,i] * np.arange(rectangle[1])
                i=i+1
            if key is "R" and value is True:
                F[:,:,i]=image[1:-1,1:-1,0]
                i=i+1
            if key is "G" and value is True:
                F[:,:,i]=image[1:-1,1:-1,1]
                i=i+1
            if key is "B" and value is True:
                F[:,:,i]=image[1:-1,1:-1,2]
                i=i+1
            if key is "dx" and value is True:
                F[:,:,i]=dx[1:-1,1:-1]
                i=i+1
            if key is "dy" and value is True:
                F[:,:,i]=dy[1:-1,1:-1]
                i=i+1
            if key is "ddx" and value is True:
                F[:,:,i]=ddx[1:-1,1:-1]
                i=i+1
            if key is "ddy" and value is True:
                F[:,:,i]=ddy[1:-1,1:-1]
                i=i+1
        mean=np.sum(F,(0,1))/(rectangle[0]*rectangle[1])
        CovD=np.zeros((dimension,dimension))
        for i in range(rectangle[0]):
            for j in range(rectangle[1]):
                m=np.mat(F[i,j,:]-mean)
                CovD=CovD+m.T @ m
        return CovD/(rectangle[0]*rectangle[1]-1)


    def Gen_Coordiantes_Mat(self,p):
        Matx=np.arange(p)
        Maty=np.arange(p).reshape(-1,1)
        for i in range(p-1):
            Matx=np.vstack((Matx,np.arange(p)))
            Maty=np.hstack((Maty,np.arange(p).reshape(-1,1)))
        return Matx,Maty


    @staticmethod
    def Get_Distance(C1,C2):
        return np.linalg.norm(logm(C1) - logm(C2), ord='fro')




