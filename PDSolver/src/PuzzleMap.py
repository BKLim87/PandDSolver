'''
Created on 2-115. 3. 2-1.

@author: bklim
'''

class PuzzleMap(object):
    '''
    -1 = None, 0 = fire, 1 = water, 2 = grass, 3 = light, 4 = dark, 5 = heart, 6 = block, 7 = poison
    '''
    Map = None
    
    

    def __init__(self):
        '''
        Constructor
        '''
        self.clear()
    
    def clear(self):
        self.Map = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]
        
    def setPuzzle(self, rowcol, puzzle):
        self.Map[rowcol[0]][rowcol[1]] = puzzle
    
    def getPuzzle(self, rowcol):
        return self.Map[rowcol[0]][rowcol[1]]    
    
    def run(self):
        for rown in range(0,5):
            for col in range(0,6):
                break
            break
        return
    
    def findPop(self, rowcol):
        Color = self.getPuzzle(rowcol)
        TempBoolMap = [[False]*6,[False]*6,[False]*6,[False]*6,[False]*6]
        
        for rown in range(0,5):
            for coln in range(0,6):
                if self.Map[rown][coln] == Color:
                    TempBoolMap[rown][coln] == True
                    
    def findGlueSet(self, BoolMap):
        for rown in range(0,5):
            for coln in range(0,6):
                if BoolMap[rown][coln] == True:
                    NearSame = self.findNearSamePuzzleRowNCol(BoolMap, [rown, coln])
                    return        
        return
    
    def findNearSamePuzzles(self, Map, rowcol):
        NearSame = self.findNearSamePuzzleRowNCol(Map, rowcol)        
        if NearSame != []:
            return NearSame
        else:
            for xy in NearSame:
                self.findNearSamePuzzles(Map, xy)
                
                asdfijasdfijasdfijsodfij
                asdoifjoasdifjosdifjoasdijf
                
            return NearSame 
        
    def findNearSamePuzzleRowNCol(self, Map, rowcol):
        rown = rowcol[0]
        coln = rowcol[1]        
            
        NearRowNCol = [[rown+1, coln], [rown-1, coln], [rown, coln+1], [rown, coln-1]]
        NearSameRowNCol = []
        
        for [x,y] in NearRowNCol:
            if Map[rown][coln] == Map[x][y] and x>=0 and x<=4 and y>=0 and y<=5:
                NearSameRowNCol.append([x,y])
                
        return NearSameRowNCol