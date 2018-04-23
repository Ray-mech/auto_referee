# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_Opencv.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qt_CV_MainWindow(object):
    def setupUi(self, Qt_CV_MainWindow):
        Qt_CV_MainWindow.setObjectName("Qt_CV_MainWindow")
        Qt_CV_MainWindow.resize(940, 834)
        Qt_CV_MainWindow.setStyleSheet("background-color: rgb(16, 16, 16);\n"
"border-color: rgb(0, 255, 59);\n"
"color: rgb(192, 255, 253);")
        self.centralwidget = QtWidgets.QWidget(Qt_CV_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.note_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.note_browser.setGeometry(QtCore.QRect(510, 170, 411, 111))
        self.note_browser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.note_browser.setObjectName("note_browser")
        self.cam_View1 = QtWidgets.QLabel(self.centralwidget)
        self.cam_View1.setGeometry(QtCore.QRect(20, 10, 482, 272))
        self.cam_View1.setFrameShape(QtWidgets.QFrame.Box)
        self.cam_View1.setObjectName("cam_View1")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.cam_View2 = QtWidgets.QLabel(self.centralwidget)
        self.cam_View2.setGeometry(QtCore.QRect(20, 310, 898, 506))
        self.cam_View2.setFrameShape(QtWidgets.QFrame.Box)
        self.cam_View2.setObjectName("cam_View2")
        self.scoreLcd1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.scoreLcd1.setGeometry(QtCore.QRect(520, 80, 111, 81))
        self.scoreLcd1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scoreLcd1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scoreLcd1.setSmallDecimalPoint(False)
        self.scoreLcd1.setDigitCount(2)
        self.scoreLcd1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.scoreLcd1.setProperty("value", 0.0)
        self.scoreLcd1.setObjectName("scoreLcd1")
        self.scoreLcd2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.scoreLcd2.setGeometry(QtCore.QRect(800, 80, 111, 81))
        self.scoreLcd2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scoreLcd2.setSmallDecimalPoint(False)
        self.scoreLcd2.setDigitCount(2)
        self.scoreLcd2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.scoreLcd2.setProperty("value", 0.0)
        self.scoreLcd2.setObjectName("scoreLcd2")
        self.twentyfourLcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.twentyfourLcd.setGeometry(QtCore.QRect(670, 80, 91, 51))
        self.twentyfourLcd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.twentyfourLcd.setSmallDecimalPoint(False)
        self.twentyfourLcd.setDigitCount(2)
        self.twentyfourLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.twentyfourLcd.setProperty("value", 24.0)
        self.twentyfourLcd.setProperty("intValue", 24)
        self.twentyfourLcd.setObjectName("twentyfourLcd")
        self.time_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.time_browser.setGeometry(QtCore.QRect(510, 10, 411, 61))
        self.time_browser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.time_browser.setObjectName("time_browser")
        Qt_CV_MainWindow.setCentralWidget(self.centralwidget)
        self.actionQuit = QtWidgets.QAction(Qt_CV_MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(Qt_CV_MainWindow)
        self.actionQuit.triggered.connect(Qt_CV_MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(Qt_CV_MainWindow)

    def retranslateUi(self, Qt_CV_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Qt_CV_MainWindow.setWindowTitle(_translate("Qt_CV_MainWindow", "Automatic Referee System"))
        self.cam_View1.setText(_translate("Qt_CV_MainWindow", "cam"))
        self.label_9.setText(_translate("Qt_CV_MainWindow", "PREVIEW"))
        self.cam_View2.setText(_translate("Qt_CV_MainWindow", "cam"))
        self.actionQuit.setText(_translate("Qt_CV_MainWindow", "Quit"))

