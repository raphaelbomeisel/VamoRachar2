# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:18:05 2015

@author: Raphael
"""


class cardapio():
    def __init__(self):
        self.bebidas = dict()
        self.pratos = dict()
        self.sobremesas = dict()
    
    def AdicionaBebida(self,bebida,preco):
        self.bebidas[bebida] = preco
      
        
    def AdicionaPrato(self,prato,preco):
        self.pratos[prato] = preco        
        
    def AdicionaSobremesa(self,sobremesa,preco):
        self.sobremesas[sobremesa] = preco       
        
        
    def __str__(self):
        return 'Bebidas: {0}\nLanches: {1}\nSobremesas: {2}'.format(self.bebidas,self.pratos,self.sobremesas)
    
    

        
menu =cardapio()
menu.AdicionaBebida('suco',3.50)
menu.AdicionaBebida('milkshake',6.00)
menu.AdicionaBebida('cerveja',5.00)

menu.AdicionaPrato('xburger',25.00)
menu.AdicionaPrato('salada caeser', 23.00)
menu.AdicionaPrato('batata-frita', 15.00)

menu.AdicionaSobremesa('sundae', 10.00)
menu.AdicionaSobremesa('sorvete simples',7.00)

print(menu)
