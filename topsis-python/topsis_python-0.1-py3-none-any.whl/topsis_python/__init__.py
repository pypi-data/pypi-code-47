# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:01:53 2020

@author: LENOVO
"""
import pandas as pd
import numpy as np
import warnings
class topsis:
	a=None #Matrix
	w=None #Weight matrix
	r=None #Normalisation matrix 
	m=None #Number of rows
	n=None #Number of columns
	aw=[] #worst alternative
	ab=[] #best alternative
	diw=None
	dib=None
	siw=None
	sib=None	
	def __init__(self,a,w,j):
		self.a=a
		self.m=len(a)
		self.n=len(a[0])
		self.w=w
		self.j=j

	#Step 2
	def step2(self):
		self.r=self.a.astype(float)
		for i in range(self.n):
			nm=sum(self.a[:,i]**2)**0.5
			for j in range(self.m):
				self.r[j,i]=self.r[j,i]/nm
	#Step 3
	def step3(self):
		self.t=self.r*self.w
#Step 4
	def step4(self):
		for i in range(self.n):
			if self.j[i]=="+":
				self.aw.append(min(self.t[:,i]))
				self.ab.append(max(self.t[:,i]))
			else:
				self.aw.append(max(self.t[:,i]))
				self.ab.append(min(self.t[:,i]))
	#Step 5			
	def step5(self):
		self.diw=(self.t-self.aw)**2
		self.dib=(self.t-self.ab)**2
		self.dw=[]
		self.db=[]
		for j in range(self.m):
			self.dw.append(sum(self.diw[j,:])**0.5)
			self.db.append(sum(self.dib[j,:])**0.5)
		self.dw=np.array(self.dw)
		self.db=np.array(self.db)
	#Step 6
	def step6(self):
		np.seterr(all='ignore')
		self.siw=self.dw/(self.dw+self.db)
		x=0
		m=0
		for i in range(self.m):
			if self.siw[i]>m:
				m=self.siw[i]
				x=i
		print ('Choice',x+1,'is the best')
	
	def calc(self):
		self.step2()
		self.step3()
		self.step4()
		self.step5()
		self.step6()
file=input("enter file name:")
file1=pd.read_csv(file)
a=file1.iloc[0:,1:].values
w1=input("weights to be associated with every column separated with commas:")
w2=list(w1.split(","))
w2=list(map(float,w2))
w3=[]
for i in range(len(a)):
    w3.append(w2)
w=np.array(w3)
j=input("enter + or - to max or min columns separated with commas:")
j1=list(j.split(","))        
p1=topsis(a,w,j1)
p1.calc()