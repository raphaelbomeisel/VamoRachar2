# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSituacao.ui'
#
# Created: Sun Jun 21 15:26:57 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import sys
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(601, 457)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(490, 0, 111, 21))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 261, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 0, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(320, 30, 251, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 189))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.listView = QtGui.QListView(self.scrollAreaWidgetContents)
        self.listView.setGeometry(QtCore.QRect(0, 0, 256, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 111, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 170, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
               
          
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 310, 221, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.listView_2 = QtGui.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(320, 330, 261, 71))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.btn)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTEST = QtGui.QMenu(self.menubar)
        self.menuTEST.setObjectName(_fromUtf8("menuTEST"))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
       
        MainWindow.setStatusBar(self.statusbar)
        self.actionCLIENTE = QtGui.QAction(MainWindow)
        self.actionCLIENTE.setObjectName(_fromUtf8("actionCLIENTE"))
        self.actionMesa = QtGui.QAction(MainWindow)
        self.actionMesa.setObjectName(_fromUtf8("actionMesa"))
        self.actionCard_pio = QtGui.QAction(MainWindow)
        self.actionCard_pio.setObjectName(_fromUtf8("actionCard_pio"))
        self.actionProgresso_Cozinha = QtGui.QAction(MainWindow)
        self.actionProgresso_Cozinha.setObjectName(_fromUtf8("actionProgresso_Cozinha"))
        self.actionSitua_o_Mesas = QtGui.QAction(MainWindow)
        self.actionSitua_o_Mesas.setObjectName(_fromUtf8("actionSitua_o_Mesas"))
        self.actionFila_Clientes = QtGui.QAction(MainWindow)
        self.actionFila_Clientes.setObjectName(_fromUtf8("actionFila_Clientes"))
        self.menuTEST.addAction(self.actionProgresso_Cozinha)
        self.menuTEST.addAction(self.actionSitua_o_Mesas)
        self.menuTEST.addAction(self.actionFila_Clientes)
        self.menubar.addAction(self.menuTEST.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Vamo Rachar?", None))
        self.label.setText(_translate("MainWindow", "Escolha sua mesa", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Mesa1", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mesa2", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Mesa3", None))
        self.label_2.setText(_translate("MainWindow", "Pedidos", None))
        self.label_3.setText(_translate("MainWindow", "Status do pedido", None))
        self.label_4.setText(_translate("MainWindow", "TextLabel", None))
        self.label_5.setText(_translate("MainWindow", "Tempo para entrega", None))
        self.label_6.setText(_translate("MainWindow", "Situação de outras mesas", None))
        self.pushButton.setText(_translate("MainWindow", "Finalizar Mesa", None))
        self.menuTEST.setTitle(_translate("MainWindow", "Opções", None))
        self.actionCLIENTE.setText(_translate("MainWindow", "Anotar pedido", None))
        self.actionMesa.setText(_translate("MainWindow", "Mesa", None))
        self.actionCard_pio.setText(_translate("MainWindow", "Cardápio", None))
        self.actionProgresso_Cozinha.setText(_translate("MainWindow", "Progresso Cozinha", None))
        self.actionSitua_o_Mesas.setText(_translate("MainWindow", "Situação Mesas", None))
        self.actionFila_Clientes.setText(_translate("MainWindow", "Fila Clientes", None))


    def tempoentrega(self):
        self.completed=0
        
        while self.completed<100:
            self.completed += 0.001
            self.progress.setValue(self.completed)
    
    def btn(self):
        
        MainWindow.close()
            

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

