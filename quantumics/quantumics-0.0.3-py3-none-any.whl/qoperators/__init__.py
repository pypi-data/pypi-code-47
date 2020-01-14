from .qoperators import QOperator, QOperatorMetrics, QMetric;




def get_model():
	return CPUQProcessor();




def UBASE(*args, **kwargs):
	return get_model().processor.UBase(*args, **kwargs);





def U0(*args, **kwargs):
	return get_model().processor.U0(*args, **kwargs);





def U1(*args, **kwargs):
	return get_model().processor.U1(*args, **kwargs);





def U2(*args, **kwargs):
	return get_model().processor.U2(*args, **kwargs);





def U3(*args, **kwargs):
	return get_model().processor.U3(*args, **kwargs);





def MEASURE(*args, **kwargs):
	return get_model().processor.Measure(*args, **kwargs);




def MIN(*args, **kwargs):
	return get_model().processor.Min(*args, **kwargs);




def MAX(*args, **kwargs):
	return get_model().processor.Max(*args, **kwargs);




def SUM(*args, **kwargs):
	return get_model().processor.Sum(*args, **kwargs);




def A(*args, **kwargs):
	return get_model().processor.A(*args, **kwargs);




def At(*args, **kwargs):
	return get_model().processor.At(*args, **kwargs);




def EXP(*args, **kwargs):
	return get_model().processor.Exp(*args, **kwargs)




def LOG(*args, **kwargs):
	return get_model().processor.Log(*args, **kwargs)




def POW(*args, **kwargs):
	return get_model().processor.Pow(*args, **kwargs)




def FFT(*args, **kwargs):
	return get_model().processor.Fft(*args, **kwargs)




def SVD(*args, **kwargs):
	return get_model().processor.Svd(*args, **kwargs)




def PCA(*args, **kwargs):
	return get_model().processor.Pca(*args, **kwargs);




def SIGMOID(*args, **kwargs):
	return get_model().processor.Sigmoid(*args, **kwargs)




def LOGIT(*args, **kwargs):
	return get_model().processor.Logit(*args, **kwargs);




def GRAD(*args, **kwargs):
	return get_model().processor.Grad(*args, **kwargs);




def HESSIAN(*args, **kwargs):
	return get_model().processor.Hessian(*args, **kwargs);




def I(*args, **kwargs):
	return get_model().processor.Identity(*args, **kwargs);




def H(*args, **kwargs):
	return get_model().processor.Hadamard(*args, **kwargs);




def R(*args, **kwargs):
	return get_model().processor.Rot(*args, **kwargs);




def RX(theta, *args, **kwargs):
	return get_model().processor.RotX(*args, **kwargs);




def RY(theta, *args, **kwargs):
	return get_model().processor.RotY(*args, **kwargs);




def RZ(theta, *args, **kwargs):
	return get_model().processor.RotZ(*args, **kwargs);




def RZZ(theta, *args, **kwargs):
	return get_model().processor.RotZZ(*args, **kwargs);




def Z(*args, **kwargs):
	return get_model().processor.Z(*args, **kwargs);




def PauliX(*args, **kwargs):
	return get_model().processor.PauliX(*args, **kwargs);



def PauliY(*args, **kwargs):
	return get_model().processor.PauliY(*args, **kwargs);



def PauliZ(*args, **kwargs):
	return get_model().processor.PauliZ(*args, **kwargs)




def S(*args, **kwargs):
	return get_model().processor.S(*args, **kwargs);




def SDG(*args, **kwargs):
	return get_model().processor.SDG(*args, **kwargs);




def CNOT(*args, **kwargs):
	return get_model().processor.CNot(*args, **kwargs);



def CX(*args, **kwargs):
	return get_model().processor.CX(*args, **kwargs);




def CY(*args, **kwargs):
	return get_model().processor.CY(*args, **kwargs);




def CZ(*args, **kwargs):
	return get_model().processor.CZ(*args, **kwargs);




def TOFFOLI(*args, **kwargs):
	return get_model().processor.Toffoli(*args, **kwargs);




def T(*args, **kwargs):
	return get_model().processor.T(*args, **kwargs);




def TDG(*args, **kwargs):
	return get_model().processor.TDG(*args, **kwargs);




def SWAP(*args, **kwargs):
	return get_model().processor.Swap(*args, **kwargs);





def AND(*args, **kwargs):
	return get_model().processor.Qand(*args, **kwargs);




def OR(*args, **kwargs):
	return get_model().processor.Qor(*args, **kwargs);





