# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:53:51 2015

@author: Raphael
"""

from Cardapio import Menu
from firebase import firebase


FIREBASE_URL="https://vamorachar.firebaseio.com/"

if __name__=="__main__":
    
    fb=firebase.FirebaseApplication(FIREBASE_URL,None)
    
    
    # Escreve dados no Firebase
    fb.put('/',"Toyama gosta",toyamagay)
    
