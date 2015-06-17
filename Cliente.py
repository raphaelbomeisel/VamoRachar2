# -*- coding: utf-8 -*-
"""
Created on Thu May 28 09:27:37 2015

@author: Raphael
"""

from Cardapio import cardapio



class Cliente():
    def __init__(self):
        
        self.PerfilCliente=dict()
        self.contatotal=0
        
   
    def ContaCliente(self,bebida,sobremesa,prato,preco):
        
        self.cliente[prato]=preco
        self.contatotal+=preco
        
    def Historico(self,cpf,nome,observacoes):
        
        self.PerfilCliente[cpf]=[nome,observacoes]     
      
    def __str__(self):
        return 'PerfilCliente:{0}'.format(self.PerfilCliente)
     
cliente1=Cliente()
cliente2=Cliente()
cliente1.Historico('43390089010','João da Silva','não gosta de pimenta')
cliente2.Historico('45533378906', 'Pedro Cunha', 'mal passado. suco sem açucar')
print(cliente2.PerfilCliente['45533378906'])
