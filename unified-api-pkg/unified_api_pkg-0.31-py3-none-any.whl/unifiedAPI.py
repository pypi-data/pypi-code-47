#Provide Unified API in here
from .qrcode import sale,voidSale,refund,retrieval

#Dictonary for transData,List for printOut
def SaleQR(payment_type, qr_code, ecr_ref, amount, additional_amount,payment_option,criteria_cardbin,transData,printOut):
	printOut.clear()
	result = sale(qr_code,ecr_ref,amount,transData,printOut)
	return result

def Void(payment_type,invoice,transData,printOut):
	printOut.clear()
	if payment_type is "QR":
		result = voidSale(invoice,transData,printOut)
		return result
	else:
		return -1;
		
def Refund(payment_type,ecr_ref,amount,originalTransRef,transData,printOut):
	printOut.clear()
	if payment_type is "QR":
		result = refund(ecr_ref,amount,originalTransRef,transData,printOut)
		return result
	else:
		return -1;

def Retrieval(payment_type, invoice,ecr_ref,transData,printOut):
	printOut.clear()
	if payment_type is "QR":
		result = retrieval(invoice,ecr_ref,transData,printOut)
		return result
	else:
		return -1;