'''
Created on 2015. 3. 20.

@author: Administrator
'''

class Puzzle(object):
    '''
    classdocs
    -1 = None, 0 = fire, 1 = water, 2 = grass, 3 = light, 4 = dark, 5 = heart, 6 = block, 7 = poison
    
    '''
    Color = None
    Power = False
    def __init__(self, co, po):
        '''
        Constructor
        '''
        self.Color = co
        self.Power = po
        
    def getColor(self):
        return self.Color
    def setColor(self, co):
        self.Color = co
    def getPower(self):
        return self.Power
    def setPower(self, po):
        self.Power = po