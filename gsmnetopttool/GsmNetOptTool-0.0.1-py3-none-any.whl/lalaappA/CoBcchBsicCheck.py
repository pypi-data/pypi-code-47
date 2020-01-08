# CoBcchBsicCheck.py
# GSM 通信网络小区同主频同BSIC小区检查

from math import radians, cos, sin, asin, sqrt


class CellLongLat(object):
	cellLong = 0
	cellLat = 0
	def __init__(self, cellLong, cellLat):
		self.cellLong = cellLong
		self.cellLat = cellLat


def geoDistance(lng1, lat1, lng2, lat2):
	'''
	返回两经纬度间的距离，单位：米，三位小数
	#distT = geoDistance(120.12802999999997,30.28708,115.86572000000001,28.7427) # 446.721 千米
	'''
	# 断言：保证为正数
	assert lng1 >= 0, "Longi must be non-negative!"
	lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)]) # 经纬度转换成弧度
	dlon = lng2 - lng1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 
	distance = 2*asin(sqrt(a))*6371*1000 # 地球平均半径，6371km
	distance = round(distance, 3)
	return distance


def getCellLocation(sSitedataFilename):
	dictCL = {}
	try:
		with open(sSitedataFilename, "r") as of:
			for eachrow in of:
				lst = eachrow.split("\t")
				if len(lst) >= 4:
					sCellname = lst[0]
					cellLong = lst[2] 
					cellLat = lst[3]
					if sCellname not in dictCL:
						dictCL[sCellname] = CellLongLat(cellLong, cellLat)
	except IOError as err: # No such file or directory:
		pass
	except:
		pass
	finally: #无论有无异常产生，都会执行！
		return dictCL


def getCoBcchBsicCelllist(sCarrierFilename):
	'''
	功能：从Mcom_Carrier文件中读取 BCCH 、BSIC和小区名称
	sCarrierFilename：Mcom_Carrier文件
	返回字典 key:Value 为 BCCH_BSIC:[CELLA, CELLB]
	'''
	dictTmp = {}
	try:
		with open(sCarrierFilename, "r") as of:
			for eachrow in of:
				lst = eachrow.split("\t")
				if len(lst) >= 6:
					sBcch_Bsic = lst[4] + "_" + lst[5]
					sCellname = lst[0]
					if sBcch_Bsic not in dictTmp:
						dictTmp[sBcch_Bsic] = [sCellname]
					else:
						dictTmp[sBcch_Bsic].append(sCellname)
	except FileNotFoundError as err: # No such file or directory:
		print(err)
	except:
		pass
	finally: #无论有无异常产生，都会执行！
		#print("Try Finally Part!")
		return dictTmp


def checkCoBcchBsicPair(dictBcchBsic, dictCellLoc, distSet = 1000):
	lstResult = ["BCCH_BSIC,CELLA,CELLB,距离(米)"]
	for key in dictBcchBsic: # 字典循环
		if len(dictBcchBsic[key]) >= 2: # BCCH_BSIC对下有两个及以上小区
			lstTmp = dictBcchBsic[key] # 小区列表
			for i in range(0, len(lstTmp)):
				for j in range(i+1, len(lstTmp)): # 小区以下配对
					sCellA = lstTmp[i] 
					sCellB = lstTmp[j]
					if sCellA in dictCellLoc and sCellB in dictCellLoc: # 两小区均有经纬度信息
						distanceAB = geoDistance(float(dictCellLoc[sCellA].cellLong),float(dictCellLoc[sCellA].cellLat)
							,float(dictCellLoc[sCellB].cellLong),float(dictCellLoc[sCellB].cellLat)) # 获取两点距离
						if distanceAB <= distSet: # 距离达标
							lstResult.append(key + "," + sCellA + "," + sCellB + "," + str(distanceAB))
	return lstResult


def writeListToFile(lstToWrite, sFilename):
	with open(sFilename,"w") as wf:
		for eachitem in lstToWrite:
			wf.write(eachitem + "\n")

if __name__ == '__main__':
	sSite = "Mcomsite_20191217.txt" # McomSitedata文件
	sCarrier = "McomCarrier_20191217.txt"
	dictCarrier = getCoBcchBsicCelllist(sCarrier)
	dictSite = getCellLocation(sSite)
	lst = checkCoBcchBsicPair(dictCarrier, dictSite, 500)
	writeListToFile(lst, "CoBcchBsicCheck.txt")
	iPair = len(lst)-1
	print("检查完成！同频同BSIC小区对有 {0} 对!".format(iPair)) # str.format()方法进行字符串格式化
