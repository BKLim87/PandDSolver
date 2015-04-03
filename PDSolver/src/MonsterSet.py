'''
Created on 2015. 4. 3.

@author: bklim
'''
from DamageSet import DamageSet

class MonsterSet(DamageSet):
    '''
    classdocs
    '''
    Set = []
    SecondAttackRatio = 0.1
    TwoWayRatio = 1.5
    ColorAwakePuzzleRatio = 0.04
    ColorAwakeRatio = 0.06
    
    def __init__(self):
        '''
        Constructor
        '''
        DamageSet.__init__(self)
        
    def settings(self, s):
        self.Set = s
        
    def getOneColorAttackStat(self, aColor):
        Dmg = 0
        for amon in self.Set:
            if amon.FirstColor[aColor] == True:
                Dmg = Dmg + amon.Attack
            if amon.SecondColor[aColor] == True:
                Dmg = Dmg + int(amon.Attack * self.SecondAttackRatio)
        return Dmg 
    
    def getOneColorRowAwake(self, aColor):
        ra = 0
        for amon in self.Set:
            ra = ra + amon.RowAwake[aColor]
        return ra
    
    def getOneColorColorAwake(self, aColor):
        ca = 0
        for amon in self.Set:
            ca = ca + amon.ColorAwake[aColor]
        return ca
    
    def getOnePopDmg(self, OPI):
        aColor = OPI.Color
        Dmg = 0
        for amon in self.Set:
            
            if OPI.TwoWay == True:
                TwFactor = amon.TwoWay[aColor]
            else:
                TwFactor = 0
            TwFactor = self.TwoWayRatio**TwFactor
            
            CaFactor = self.getOneColorColorAwake(aColor)
            if OPI.PlusPopN > 0:
                CaFactor = (1+self.ColorAwakePuzzleRatio*OPI.PlusPopN)*(1+self.ColorAwakeRatio*self.getOneColorColorAwake(aColor))
            CaFactor = 1
            
            if amon.FirstColor[aColor] == True:
                Dmg = Dmg + int(amon.Attack * (1+((OPI.PopN-3)*0.25)) * TwFactor * CaFactor)
            if amon.SecondColor[aColor] == True:
                Dmg = Dmg + int(amon.Attack * (1+((OPI.PopN-3)*0.25)) * TwFactor * CaFactor * self.SecondAttackRatio)
                
        return Dmg 
        
        
         