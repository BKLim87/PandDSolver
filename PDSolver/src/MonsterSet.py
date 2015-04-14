'''
Created on 2015. 4. 3.

@author: bklim
'''
from src.DamageStat import DamageStat

class MonsterSet(DamageStat):
    '''
    classdocs
    '''
    Set = []
    SecondAttackRatio = 0.1
    TwoWayRatio = 1.5
    ColorAwakePuzzleRatio = 0.04
    ColorAwakeRatio = 0.06
    TotalHp = 0
    
    def __init__(self):
        '''
        Constructor
        '''
        DamageStat.__init__(self)
        for aMon in self.Set:
            self.TotalHp = self.TotalHp + aMon.Hp
                    
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
            if aColor == 5:
                Dmg = Dmg + amon.Heal
                
            if aColor == 7:
                Dmg = Dmg - int(amon.Hp*(0.25+0.05*(OPI.PopN-3)))
                
            else:
                if OPI.TwoWay == True:
                    TwFactor = amon.TwoWay[aColor]
                else:
                    TwFactor = 0
                TwFactor = self.TwoWayRatio ** TwFactor
                
                CaFactor = self.getOneColorColorAwake(aColor)
                if OPI.PlusPopN > 0:
                    CaFactor = (1 + self.ColorAwakePuzzleRatio * OPI.PlusPopN) * (1 + self.ColorAwakeRatio * self.getOneColorColorAwake(aColor))
                else:
                    CaFactor = 1
                
                if amon.FirstColor[aColor] == True:
                    Dmg = Dmg + int(amon.Attack * (1 + ((OPI.PopN - 3) * 0.25)) * TwFactor * CaFactor)
                if amon.SecondColor[aColor] == True:
                    Dmg = Dmg + int(amon.Attack * (1 + ((OPI.PopN - 3) * 0.25)) * TwFactor * CaFactor * self.SecondAttackRatio)
                
        return self.DamageToList(aColor, Dmg)