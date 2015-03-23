'''
Created on 2-115. 3. 2-1.

@author: bklim
'''
from Puzzle import Puzzle 
import itertools
import types





class PuzzleMap(object):
    '''
    Puzzle Color
    -1 = None, 0 = fire, 1 = water, 2 = grass, 3 = light, 4 = dark, 5 = heart, 6 = block, 7 = poison
    '''
    Map = []
    
    

    def __init__(self):
        '''
        Constructor
        '''
        self.clear()
        
    def setPuzzle(self, rowcol, puzzle):
        self.Map[rowcol[0]][rowcol[1]] = puzzle
        
    def setPuzzlesbyNumber(self, numbers):
        for i in range(0,30):
            row = i//6
            col = i%6
            Color = int(numbers[i])
            self.setPuzzle([row, col], Puzzle(Color, False))
    
    def clear(self):
        self.Map = []
        for x in range(0,5):
            temprow = []
            for y in range(0,6):
                temprow.append(Puzzle(-1, False))
            self.Map.append(temprow)
    
    def getPuzzle(self, rowcol):
        return self.Map[rowcol[0]][rowcol[1]]    
    
    def run(self):
        onestepPops = self.findPops()
        print(onestepPops)
        
        pass
    
    def removePops(self, onestepPops):
        
    
        pass    
    
    def findPops(self):
        [HorMap, VerMap] = self.ThreeRowHorVerMap()
        willPopDic = {}
        for Color in range(1, 8):
            willPopDic[Color] = []
            ColorHorMap = self.ValueCopy(HorMap)
            ColorVerMap = self.ValueCopy(VerMap)
            
            for x in range(0,5):
                for y in range(0,4):
                    if ColorHorMap[x][y] != Color:
                        ColorHorMap[x][y] = -1
            
            for x in range(0,3):
                for y in range(0,6):
                    if ColorVerMap[x][y] != Color:
                        ColorVerMap[x][y] = -1
                        
            willPoPRowCol = self.getRowColfromHorVerMap(ColorHorMap, ColorVerMap)
            stacks = self.getStacks(willPoPRowCol)
            willPopDic[Color] = willPopDic[Color] + stacks.copy()
        
        return willPopDic
            
    def getStacks(self, rclist):
        if len(rclist) == 0:
            return []
        
        temprclist = self.ValueCopy(rclist)
        stacks = []
        stacks.append([temprclist.pop()])
        while len(temprclist)>0:
            temprc = temprclist.pop()
            
            for x in range(0,len(stacks)):
                for rc in stacks[x]:
                    if self.isNearRowCol(rc, temprc):
                        stacks[x].append(temprc)
                        break
                        break
            stacks.append([temprc])
        mergeFlag = True
        while mergeFlag:
            mergeFlag = False
            for [x,y] in itertools.product(range(len(stacks)), range(len(stacks))):
                if x != y:
                    if self.isNearStack(stacks[x], stacks[y]):
                        mergeFlag = True
                        stacks[x] = stacks[x] + stacks[y]
                        stacks.remove(stacks[y])
                        break
        
        return stacks
    
    def isNearStack(self, stack1, stack2):
        for rc1 in stack1:
            for rc2 in stack2:
                if self.isNearRowCol(rc1, rc2):
                    return True
        return False
                
    def getRowColfromHorVerMap(self, HorMap, VerMap):
        RClist = []
        for x in range(0,5):
            for y in range(0,4):
                if HorMap[x][y] >=0:
                    RClist.append([x,y])
                    RClist.append([x,y+1])
                    RClist.append([x,y+2])
        
        for x in range(0,3):
            for y in range(0,6):
                if VerMap[x][y] >=0:
                    RClist.append([x,y])
                    RClist.append([x+1,y])
                    RClist.append([x+2,y])
        
        uniqueRClist = []
        
        if len(RClist) > 0:
            RClist.sort()
            uniqueRClist.append(RClist[0])
            olderrc = RClist[0]
            for rc in RClist:
                if olderrc != rc:
                    olderrc = rc
                    uniqueRClist.append(rc)
            
        return uniqueRClist
                        
    def isNearRowCol(self, rowcol1, rowcol2):
        disRow = rowcol1[0] - rowcol2[0]
        disCol = rowcol1[1] - rowcol2[1]
        dis = disRow*disRow + disCol*disCol
        if dis == 1:
            return True
        else:
            return False
    
    def ThreeRowHorVerMap(self):
        HorMap = [[-1]*4, [-1]*4, [-1]*4, [-1]*4, [-1]*4]
        VerMap = [[-1]*6, [-1]*6, [-1]*6]
        
        for rown in range(0,5):
            for coln in range(0,4):
                targetColor = self.getPuzzle([rown, coln]).Color
                Flag = True
                for x in range(1,3):
                    if targetColor != self.getPuzzle([rown, coln+x]).Color:
                        Flag = False
                if Flag == True:
                    HorMap[rown][coln] = targetColor
        
        for rown in range(0,3):
            for coln in range(0,6):
                targetColor = self.getPuzzle([rown, coln]).Color
                Flag = True
                for x in range(1,3):
                    if targetColor != self.getPuzzle([rown+x, coln]).Color:
                        Flag = False
                if Flag == True:
                    VerMap[rown][coln] = targetColor
        
        return [HorMap, VerMap]

    def ValueCopy(self, array):
        result = []
        
        if type(array) == list:
            for a in array:
                result.append(self.ValueCopy(a))
            pass
        else:
            result = array
            pass
        
        return result

if __name__ == "__main__":
    PM = PuzzleMap()
    PM.setPuzzlesbyNumber('111111122222133333444444555555')
    PM.run()
    pass    