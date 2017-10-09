# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'array.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import QInputDialog, QLineEdit

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
        MainWindow.resize(768, 618)
        MainWindow.setWindowOpacity(5.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 134, 100);"))
        MainWindow.setProperty("picture", QtGui.QPixmap(_fromUtf8("raw.jpeg")))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 151, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 0, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.padd)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 220, 151, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.up)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 310, 151, 51))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.dele)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 130, 151, 51))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton.clicked.connect(self.serc)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(420, 50, 311, 381))
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(170, 170, 127))
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuARRAY_MANAGER = QtGui.QMenu(self.menubar)
        self.menuARRAY_MANAGER.setObjectName(_fromUtf8("menuARRAY_MANAGER"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtGui.QToolBar(MainWindow)
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.toolBar_4 = QtGui.QToolBar(MainWindow)
        self.toolBar_4.setObjectName(_fromUtf8("toolBar_4"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_4)
        self.toolBar_5 = QtGui.QToolBar(MainWindow)
        self.toolBar_5.setObjectName(_fromUtf8("toolBar_5"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar_5)
        self.toolBar_6 = QtGui.QToolBar(MainWindow)
        self.toolBar_6.setObjectName(_fromUtf8("toolBar_6"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_6)
        MainWindow.insertToolBarBreak(self.toolBar_6)
        self.toolBar_7 = QtGui.QToolBar(MainWindow)
        self.toolBar_7.setObjectName(_fromUtf8("toolBar_7"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_7)
        self.toolBar_8 = QtGui.QToolBar(MainWindow)
        self.toolBar_8.setObjectName(_fromUtf8("toolBar_8"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_8)
        self.toolBar_9 = QtGui.QToolBar(MainWindow)
        self.toolBar_9.setObjectName(_fromUtf8("toolBar_9"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_9)
        self.toolBar_10 = QtGui.QToolBar(MainWindow)
        self.toolBar_10.setObjectName(_fromUtf8("toolBar_10"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_10)
        self.menubar.addAction(self.menuARRAY_MANAGER.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def padd(self):

        text, ok = QtGui.QInputDialog.getText(self.centralwidget, 'Input Dialog', 'Enter your name:')
        if ok:
            text={}
            self.tableWidget.setItem(0, 1,QtGui.QTableWidgetItem(text))

    def up(self):
        text, we = QtGui.QInputDialog.getText(self.centralwidget, 'Input Dialog', 'Enter your name:')

    def dele(self):
        text=''
        self.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem(text))

    def serc(self):
        text, wo = QtGui.QInputDialog.getText(self.centralwidget, 'Input Dialog', 'Enter your name:')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "INSERT", None))
        self.pushButton_2.setText(_translate("MainWindow", "UPDATE", None))
        self.pushButton_4.setText(_translate("MainWindow", "SEARCH", None))
        self.pushButton_5.setText(_translate("MainWindow", "DELETE", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NO", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAME", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "MATRIC NO", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    myapp = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(myapp)
    myapp.show()
    sys.exit(app.exec_())
