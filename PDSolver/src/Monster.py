'''
Created on 2015. 4. 3.

@author: bklim
'''

class Monster(object):
    '''
    classdocs
    '''
    FirstColor = []
    SecondColor = []
    Attack = 0
    Heal = 0
    TwoWay = []
    RowAwake = []
    ColorAwake = []
    Hp = 0

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def settings(self, fc, sc, at, he, tw, ra, ca, h):
        self.FirstColor = fc
        self.SecondColor = sc
        self.Attack = at
        self.Heal = he
        self.Twoway = tw
        self.RowAwake = ra
        self.ColorAwake = ca
        self.Hp = h
    
    