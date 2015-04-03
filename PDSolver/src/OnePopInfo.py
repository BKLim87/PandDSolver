'''
Created on 2015. 4. 3.

@author: bklim
'''

class OnePopInfo(object):
    '''
    classdocs
    '''
    Color = -1
    PopN = 0
    PlusPopN = 0
    TwoWay = False
    RowAwake = False

    def __init__(self):
        '''
        Constructor
        '''
    def settings(self, c, pn, ppn, tw, ra):
        self.Color = c
        self.PopN = pn
        self.PlusPopN = ppn
        self.TwoWay = tw
        self.RowAwake = ra