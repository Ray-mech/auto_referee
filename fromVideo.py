# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#import os.path
#import time
import datetime
import copy
#import math
import cv2
#from numpy import *

from pyqt_Opencv import Ui_Qt_CV_MainWindow


class DesignerMainWindow(QtWidgets.QMainWindow,Ui_Qt_CV_MainWindow):
    log = ""
    
    
    def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
        self.ui = Ui_Qt_CV_MainWindow()
        self.setupUi(self)
        
        """初期実行メソッド"""
        self.logging("System started")
        videopath = 0 #'./videofile.mp4'
        self.cap = cv2.VideoCapture(videopath)
        self.cap.set(3,1280)
        self.cap.set(4,416)
        self.startLoop()
        """------------"""
        
    def logging(self, string):
        now = datetime.datetime.now()
        timestmp = '{0:%H}:{0:%M}:{0:%S}'.format(now)
        newStr = timestmp + "\t" + string
        self.log = newStr + "\n" + self.log
        self.note_browser.setPlainText(self.log)

    def startLoop(self):
        fps = 30
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.captureVideo)
        self.timer.start(1000/fps)
        self.logging("Loop started")
        
    def captureVideo(self):
        ret, frame = self.cap.read()
        
        if ret == False:
            frame = cv2.imread("nocam.png")
            img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(img)
            self.cam_View1.setPixmap(pix)
            self.cam_View2.setPixmap(pix)
            return
        ##previewOriginal##
        oframe = cv2.resize(frame,(480,270))
        oframe = cv2.cvtColor(oframe, cv2.COLOR_BGR2RGB)
        oimg = QtGui.QImage(oframe, oframe.shape[1], oframe.shape[0], QtGui.QImage.Format_RGB888)
        opix = QtGui.QPixmap.fromImage(oimg)
        self.cam_View1.setPixmap(opix)
        
        ##CALC##
        result = calcImage(frame)
        
        
        ##previewCalcd##
        result = cv2.resize(result,(896,504))
        #result = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)
        img = QtGui.QImage(result, result.shape[1], result.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.cam_View2.setPixmap(pix)


def calcImage(frame):
    original = copy.deepcopy(frame)
    mask = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = mask
    result = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)
    return result #RGBで返すこと！

            
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   dmw = DesignerMainWindow()
   dmw.show()
	#dmw.showFullScreen()
   sys.exit(app.exec_())