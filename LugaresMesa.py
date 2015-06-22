# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Começo.ui'
#
# Created: Sun Jun 21 18:59:30 2015
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

class Ui_LugaresMesa(object):
    def setupUi(self, LugaresMesa):
        LugaresMesa.setObjectName(_fromUtf8("LugaresMesa"))
        LugaresMesa.resize(476, 363)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LugaresMesa.setWindowIcon(icon)
        self.Cliente = QtGui.QPushButton(LugaresMesa)
        self.Cliente.setGeometry(QtCore.QRect(200, 170, 75, 23))
        self.Cliente.setObjectName(_fromUtf8("Cliente"))

        self.retranslateUi(LugaresMesa)
        QtCore.QMetaObject.connectSlotsByName(LugaresMesa)

    def retranslateUi(self, LugaresMesa):
        LugaresMesa.setWindowTitle(_translate("LugaresMesa", "Vamo Rachar? Lugares", None))
        self.Cliente.setText(_translate("LugaresMesa", "Cliente", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LugaresMesa = QtGui.QWidget()
    ui = Ui_LugaresMesa()
    ui.setupUi(LugaresMesa)
    LugaresMesa.show()
    sys.exit(app.exec_())

