'''
Created on 2015. 3. 26.

@author: bklim
'''
from src.OnePopInfo import OnePopInfo

class PopInfo(object):
    '''
    Puzzle Color
    -1 = None, 0 = fire, 1 = water, 2 = grass, 3 = light, 4 = dark, 5 = heart, 6 = block, 7 = poison
    '''
    PopPuzzleDict = {}
    

    def __init__(self):
        '''
        Constructor
        '''        
        for aColor in range(0,8):
            self.PopPuzzleDict[aColor] = []
        pass
    
    def addPopPuzzleDict(self, pd):
        for aColor in pd.keys():
            for alist in pd[aColor]:
                self.PopPuzzleDict[aColor].append(alist)
            
    def setPopPuzzleDict(self, pd):
        self.PopPuzzleDict = pd
        
    def calcPopPuzzle(self):
        PopPuzzleNum = {}
        for aColor in self.PopPuzzleDict.keys():
            PopPuzzleNum[aColor] = []
            for alist in self.PopPuzzleDict[aColor]:
                PopPuzzleNum[aColor].append(self.checkPop(alist))
        return PopPuzzleNum
    
    def checkPop(self, alist):
        return len(alist)
    
    def MakePopInfoList(self, Map):
        PopInfoList = []
        for aColor in self.PopPuzzleDict.keys():
            for aList in self.PopPuzzleDict[aColor]:
                PopInfoList.append(self.MakeOnePopInfo(aColor, aList, Map))
        return PopInfoList
    
    def MakeOnePopInfo(self, aColor, aList, Map):
        tempOnePopInfo = OnePopInfo()
        
        tempPopN = len(aList)
        tempTwoWay = False
        if tempPopN == 4:
            tempTwoWay = True
        
        for nr in range(0,5):
            raflag = True
            for nc in range(0,6):
                if [nr,nc] in aList:
                    pass
                else:
                    reflag = False
            if raflag == True:
                tempRowAwake = True
                break
        
        AwakePopN = 0
        for arc in aList:
            if Map[arc[0]][arc[1]].Power == True:
                AwakePopN = AwakePopN + 1
        
        tempOnePopInfo.settings(aColor, tempPopN, AwakePopN, tempTwoWay, tempRowAwake)
        return tempOnePopInfo
        