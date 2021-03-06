# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:16:40 2015

@author: Raphael
"""



from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Mesa():
    def __init__ (self,tipomesa,numclientes):
        self.tipomesa=tipomesa
        self.numclientes=numclientes
        self.posicaoclientes=[]        
        
    def DistribuicaoMesa(self,numclientes):
        
        if self.tipomesa=='redonda':
            for i in range(0, numclientes):
                self.posicaoclientes.append((360/numclientes)*i)
                
        



class Ui_LugaresMesa(Mesa):
    
    def __init__(self,tipomesa,numclientes):
        
        Mesa.__init__(self,tipomesa, numclientes)
        
    
    def setupUi(self, LugaresMesa):
        LugaresMesa.setObjectName(_fromUtf8("LugaresMesa"))
        LugaresMesa.resize(476, 363)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LugaresMesa.setWindowIcon(icon)

        for i in range(self.numclientes):       
        
            self.Cliente = QtGui.QPushButton(LugaresMesa)
            self.Cliente.setGeometry(QtCore.QRect(100*i, 170, 75, 23))
            self.Cliente.setObjectName(_fromUtf8("Cliente %i" %i))

        self.retranslateUi(LugaresMesa)
        QtCore.QMetaObject.connectSlotsByName(LugaresMesa)

    def retranslateUi(self, LugaresMesa):
        LugaresMesa.setWindowTitle(_translate("LugaresMesa", "Vamo Rachar? Lugares", None))
        self.Cliente.setText(_translate("LugaresMesa", "Cliente", None))

mesa=Ui_LugaresMesa("redonda",4)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LugaresMesa = QtGui.QWidget()
    ui = Ui_LugaresMesa()
    ui.setupUi(LugaresMesa)
    LugaresMesa.show()
    sys.exit(app.exec_())




