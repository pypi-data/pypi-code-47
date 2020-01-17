#  Copyright (c) 2020  Gille PREVOT, Guillaume PREVOT, Anne-Delphine PREVOT

class ICO3Log:

    global ICO3LogParamList
    '''
    Root,Link,Message,Connection,Plugin
    
    '''

    ICO3LogParamList = []

    @staticmethod
    def print(xParam, xMessage):
        IDX = ICO3Log.searchParam("All")
        if IDX < 0:
            pass
        else:
            print(xMessage)
            return
        IDX = ICO3Log.searchParam(xParam)
        if IDX < 0:
            return
        print(xMessage)

    @staticmethod
    def addParam(xParam):
        IDX = ICO3Log.searchParam(xParam)
        if IDX < 0:
            ICO3LogParamList.append(xParam)

        return

    @staticmethod
    def clearParams():
        ICO3LogParamList.clear()

    @staticmethod
    def setupParams(xParamAtt):
        if xParamAtt is None:
            return
        xParamList = xParamAtt.split(",")
        ICO3LogParamList.clear()
        ICO3LogParamList.extend(xParamList)



    @staticmethod
    def removeParam(xParam):
        try:
            ICO3LogParamList.remove(xParam)
        except:
            pass

    @staticmethod
    def searchParam(xParam):
        try:
            return ICO3LogParamList.index(xParam)
        except:
            pass
        return -1

if __name__ == '__main__':
    ICO3Log.setupParams(["Debug","IO","Plugin"])
    ICO3Log.print("Debug", "the debug Err")
    ICO3Log.clearParams()
    ICO3Log.addParam("All")
    ICO3Log.print("xxxx", "the debug Err All")

