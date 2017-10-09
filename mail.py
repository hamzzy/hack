# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import QInputDialog

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 110, 131, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.up)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 170, 131, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 240, 131, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 315, 131, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.listView = QtGui.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(310, 50, 321, 391))
        self.listView.setObjectName(_fromUtf8("listView"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "INSERT", None))
        self.pushButton_2.setText(_translate("Dialog", "DLETE", None))
        self.pushButton_3.setText(_translate("Dialog", "UPDATE", None))
        self.pushButton_4.setText(_translate("Dialog", "SERCH", None))

    def up(self):
        text, report_title = QtGui.QInputDialog.getText(self,"New report","Report title:")


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    myapp = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(myapp)
    myapp.show()
    sys.exit(app.exec_())
