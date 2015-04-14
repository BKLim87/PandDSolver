'''
Created on 2015. 4. 3.

@author: bklim
'''
from abc import ABCMeta, abstractmethod


class DamageStat(metaclass=ABCMeta):
    '''
    classdocs
    '''
    SecondAttackRatio = 0.1
    TwoWayRatio = 1.5
    ColorAwakePuzzleRatio = 0.04
    ColorAwakeRatio = 0.06

    def __init__(self):
        '''
        Constructor
        '''
    @abstractmethod()
    def getOneColorRowAwake(self, aColor):
        pass
    @abstractmethod()
    def getOneColorColorAwake(self, aColor):
        pass
    @abstractmethod()
    def getOnePopDmg(self, OPI):
        pass
    
    def DamageToList(self, aColor, Dmg):
        DmgList = [0,0,0,0,0,0,0,0]
        DmgList[aColor] = Dmg
        return DmgList
    
    def ListAdd(self, aList, bList):
        if len(aList) == len(bList):
            reList = []
            for i in range(len(aList)):
                reList.append(aList[i] + bList[i])
            return reList
        else:
            return None
        
    def ListMultiple(self, aList, bList):
        if len(aList) == len(bList):
            reList = []
            for i in range(len(aList)):
                reList.append(aList[i] * bList[i])
            return reList
        else:
            return None