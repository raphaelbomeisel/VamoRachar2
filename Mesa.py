# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:16:40 2015

@author: Raphael
"""

class Mesa():
    def __init__ (self,tipomesa,numclientes):
        self.tipomesa=tipomesa
        self.numclientes=numclientes
        self.posicaoclientes=[]        
        
    def DistribuicaoMesa(self,numclientes):
        
        if self.tipomesa=='redonda':
            for i in range(numclientes):
                self.posicaoclientes[i].append((360/numclientes)*i)
                

mesa1=Mesa('redonda',4)

mesa1.DistribuicaoMesa(4)
print(posicaoclientes)