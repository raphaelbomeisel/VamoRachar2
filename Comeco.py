# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Começo.ui'
#
# Created: Sun Jun 21 18:22:09 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.ListaPedido = QtGui.QTextBrowser(Form)
        self.ListaPedido.setGeometry(QtCore.QRect(140, 30, 251, 51))
        self.ListaPedido.setObjectName(_fromUtf8("ListaPedido"))
        self.AnotaPedido = QtGui.QTextEdit(Form)
        self.AnotaPedido.setGeometry(QtCore.QRect(0, 160, 191, 21))
        self.AnotaPedido.setObjectName(_fromUtf8("AnotaPedido"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 210, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.retranslateUi(Form)
        
        #apertar botao
        
        self.pushButton.clicked.connect(self.Pedidos)
        
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))
    
        
    def Pedidos(self):
        
        self.AnotaPedido.QTextEdit("wsdfa")
                
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

