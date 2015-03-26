'''
Created on 2015. 3. 26.

@author: bklim
'''

class PopInfo(object):
    '''
    Puzzle Color
    -1 = None, 0 = fire, 1 = water, 2 = grass, 3 = light, 4 = dark, 5 = heart, 6 = block, 7 = poison
    '''
    PopPuzzleDict = None
    

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def addPopPuzzleDict(self, pd):
        for aColor in pd.keys():
            if aColor in self.PopPuzzleDict.keys():
                self.PopPuzzleDict[aColor].expand(pd[aColor])
            else:
                self.PopPuzzleDict[aColor] = pd[aColor]
    
    def setPopPuzzleDict(self, pd):
        self.PopPuzzleDict = pd
        
    def calcPopPuzzle(self):
        PopPuzzleNum = {}
        for aColor in self.PopPuzzleDict.keys():
            for alist in self.PopPuzzleDict[aColor]:
                PopPuzzleNum[aColor] = len(alist)
        return PopPuzzleNum
    
        