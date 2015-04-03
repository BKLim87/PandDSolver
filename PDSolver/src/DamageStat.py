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
    def getOnePopDmg(self, OPI):
        pass