# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bank.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_TabWidget(object):
    def total(self):
        self.u=int(self.spinBox_4.text())*int(self.lineEdit_6.text())
        self.label_9.setText(str(self.u))
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(805, 486)
        TabWidget.setMaximumSize(QtCore.QSize(430000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        TabWidget.setFont(font)
        TabWidget.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:repeat, x1:0.476, y1:0.602045, x2:1, y2:0, stop:0.0837004 rgba(116, 116, 144, 217), stop:1 rgba(255, 255, 255, 255));"))
        TabWidget.setIconSize(QtCore.QSize(30, 16))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 59, 171, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(0, 140, 161, 20))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 50, 231, 41))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 211, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.spinBox_4 = QtGui.QSpinBox(self.tab)
        self.spinBox_4.setGeometry(QtCore.QRect(290, 120, 52, 26))
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 125, 151, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(30, 180, 171, 41))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_6 = QtGui.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 170, 231, 41))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(280, 260, 90, 50))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(310, 350, 181, 41))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.pushButton.clicked.connect(self.total)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setMaximumSize(QtCore.QSize(430000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.tab1.setFont(font)
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.verticalScrollBar = QtGui.QScrollBar(self.tab1)
        self.verticalScrollBar.setGeometry(QtCore.QRect(780, 10, 16, 421))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.lineEdit = QtGui.QLineEdit(self.tab1)
        self.lineEdit.setGeometry(QtCore.QRect(240, 60, 241, 51))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.spinBox = QtGui.QSpinBox(self.tab1)
        self.spinBox.setGeometry(QtCore.QRect(330, 160, 52, 26))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label = QtGui.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(20, 80, 201, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 151, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self.tab1)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 320, 211, 51))

        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab1)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 240, 241, 51))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.label_3 = QtGui.QLabel(self.tab1)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 201, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tableWidget = QtGui.QTableWidget(self.tab_4)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 791, 431))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 170, 127))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        TabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_5)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 390, 96, 26))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.listView = QtGui.QListView(self.tab_5)
        self.listView.setGeometry(QtCore.QRect(410, 20, 371, 341))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.line = QtGui.QFrame(self.tab_5)
        self.line.setGeometry(QtCore.QRect(350, 0, 20, 441))
        self.line.setStyleSheet(_fromUtf8("background-color: rgb(85, 0, 0);"))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalScrollBar_2 = QtGui.QScrollBar(self.tab_5)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(760, 20, 16, 341))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName(_fromUtf8("verticalScrollBar_2"))
        self.label_10 = QtGui.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(480, 20, 201, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.comboBox = QtGui.QComboBox(self.tab_5)
        self.comboBox.setGeometry(QtCore.QRect(40, 80, 251, 26))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_11 = QtGui.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(90, 210, 70, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        TabWidget.addTab(self.tab_5, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.label_4.setText(_translate("TabWidget", "GOODS NAME", None))
        self.label_5.setText(_translate("TabWidget", "TOTAL AMOUNT", None))
        self.label_7.setText(_translate("TabWidget", "QUANTITY", None))
        self.label_8.setText(_translate("TabWidget", "PRICE", None))
        self.label_9.setText(_translate("TabWidget", "", None))
        self.pushButton.setText(_translate("TabWidget", "PURCHASED", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "CREDIT", None))
        self.label.setText(_translate("TabWidget", "GOODS NAME", None))
        self.label_2.setText(_translate("TabWidget", "QUANTITY", None))
        self.pushButton_2.setText(_translate("TabWidget", "UPDATE", None))
        self.label_3.setText(_translate("TabWidget", "PRICE", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "NEW GOODS", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("TabWidget", "1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("TabWidget", "2", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TabWidget", "GOODS NAME", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TabWidget", "PRICE", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TabWidget", "AMOUNT", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TabWidget", "QUANTITY", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("TabWidget", "TIME", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("TabWidget", "DATE", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "DATABASE", None))
        self.pushButton_3.setText(_translate("TabWidget", "LOGOUT", None))
        self.label_10.setText(_translate("TabWidget", "NEW GOOD AND PRICE", None))
        self.label_11.setText(_translate("TabWidget", "TextLabel", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_5), _translate("TabWidget", "GOODS PRICE", None))

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    myapp = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(myapp)
    myapp.show()
    sys.exit(app.exec_())