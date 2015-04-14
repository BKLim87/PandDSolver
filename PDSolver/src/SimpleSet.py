'''
Created on 2015. 4. 3.

@author: Administrator
'''
from src.DamageStat import DamageStat

class SimpleSet(DamageStat):
    '''
    classdocs
    '''
    ColorDamage = []
    RowAwake = []
    ColorAwake = []
    TwoWayDamage = []
    Hp = 10000

    def __init__(self):
        '''
        Constructor
        '''
        DamageStat.__init__(self)
        self.ColorDamage = [0,0,0,0,0,0,0,0]
        self.TwoWayDamage = [0,0,0,0,0,0,0,0]
        
    def settings(self, cd, ra, ca, tw):
        self.ColorDamage = cd
        self.RowAwake = ra
        self.ColorAwake = ca
        self.TwoWayDamage = tw
        
    def getOneColorRowAwake(self, aColor):
        return self.RowAwake
    
    def getOneColorColorAwake(self, aColor):
        return self.ColorAwake
    
    def getOnePopDmg(self, OPI):
        aColor = OPI.Color
        Dmg = 0
        
        CaFactor = self.getOneColorColorAwake(aColor)
        if OPI.PlusPopN > 0:
            CaFactor = (1 + self.ColorAwakePuzzleRatio * OPI.PlusPopN) * (1 + self.ColorAwakeRatio * self.getOneColorColorAwake(aColor))
        else:
            CaFactor = 1
        
        if aColor == 7:
            Dmg = -1*int(self.Hp*(0.25+0.05*(OPI.PopN-3)))
        
        if OPI.Twoway == True:
            Dmg = self.TwoWayDamage[aColor] * CaFactor
        else:
            Dmg = self.ColorDamage[aColor] * (1 + ((OPI.PopN - 3) * 0.25)) * CaFactor 
        
        return self.DamageToList(aColor, Dmg)