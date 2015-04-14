'''
Created on 2015. 4. 3.

@author: Administrator
'''
from src.DamageStat import DamageStat

class DamageCalculator(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.OnePopInfoList = []
        self.DamageInfo = DamageStat()
        
    def CalculateDmg(self):
        return self.dummydata()
        
        result = [0,0,0,0,0,0,0,0]
        
        for aPop in self.OnePopInfoList:
            tempresult = self.DamageInfo.getOnePopDmg(aPop)
            for i in range(0,len(result)):
                result[i] = result[i] + tempresult[i]
        
        return result
    
    def dummydata(self):
        return [1,1,1,1,1,1,0,0]