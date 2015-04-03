'''
Created on 2015. 3. 26.

@author: bklim
'''

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
    
        