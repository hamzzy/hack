# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pos import Ui_TabWidget
import sqlite3
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
    def alert(self,title,message):
        msgbox=QtGui.QMessageBox()
        msgbox.setIcon(QtGui.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgbox.exec_()
    def window(self):
        self.myapp = QtGui.QTabWidget()
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self.myapp)
        my.hide()
        self.myapp.show()
    def login (self):
        passname=self.lineEdit.text()
        passkey=self.lineEdit_2.text()
        connection = sqlite3.connect("pog.db")
        result=connection.execute("SELECT * FROM hello" )
        if (passname=='admin' or passkey=='1234'):
            self.window()
            print"user found"
        else:
         self.alert('warning','passname or passkey not correct')
        connection.close()
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(640, 480)
        Form.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:repeat, x1:0.476, y1:0.602045, x2:1, y2:0, stop:0.0837004 rgba(116, 116, 144, 217), stop:1 rgba(255, 255, 255, 255));"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 120, 261, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 240, 261, 41))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 125, 121, 31))
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 101, 31))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 360, 181, 41))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 0, 0);"))
        self.pushButton.clicked.connect(self.login)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 601, 71))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", " PASS NAME :", None))
        self.label_2.setText(_translate("Form", "PASSKEY :", None))
        self.pushButton.setText(_translate("Form", "LOGIN", None))
        self.label_3.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Symbola\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600;\">saler corner</span></p></body></html>", None))

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    my= QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(my)
    my.show()
    sys.exit(app.exec_())