# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#import os.path
#import time
import datetime
#import copy
#import math
import cv2
import numpy as np

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
        self.slider1.valueChanged.connect(self.showRange)
        self.slider2.valueChanged.connect(self.showRange)

        
    def logging(self, string):
        now = datetime.datetime.now()
        timestmp = '{0:%H}:{0:%M}:{0:%S}'.format(now)
        newStr = timestmp + "\t" + string
        self.log = newStr + "\n" + self.log
        self.note_browser.setPlainText(self.log)
    def showRange(self):
        string = "H:" + str(self.slider1.value()) + " - " + str(self.slider2.value())
        self.logging(string)
        
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
        result = self.calcImage(frame)
        
        
        ##previewCalcd##
        result = cv2.resize(result,(480,270))
        #result = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)
        img = QtGui.QImage(result, result.shape[1], result.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.cam_View2.setPixmap(pix)
        
        ##show fieldstate##
        self.field_View.setPixmap(QtGui.QPixmap("./img/halfcourt.png"))
        


    def calcImage(self,frame):
        mask, result = self.getBall(frame)
        #return cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
        return cv2.cvtColor(result, cv2.COLOR_BGR2RGB) #RGBで返すこと！
        
    def getBall(self,frame):    
        h1 = self.slider1.value()
        h2 = self.slider2.value()
        g_min = np.array([h1,60,20])
        g_max = np.array([h2,255,255])
        
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsvFrame, g_min, g_max)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
        mask = cv2.medianBlur(mask,3) 
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        #"""Hough (circle)
        ball = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 20, param1=15, param2=15, minRadius=1000, maxRadius=0)
        #ball = np.uint16(np.around(ball))
    
        if ball != None:
            ball = ball[0]
            maxBallsize = -1;
            maxBall = [0,0,0]
            for i in range(len(ball)):
                if ball[i][2] > maxBallsize:
                    maxBall = ball[i]
                    maxBallsize = ball[i][2]
                
            cv2.circle(frame,(maxBall[0],maxBall[1]),maxBallsize,(0,255,0),2)
            cv2.circle(frame,(maxBall[0],maxBall[1]),8,(0,0,255),3)
        #"""
            
        """
        for i in ball[0,:]:
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
        """
        
        result = cv2.bitwise_and(frame,frame,mask=mask)
        return mask, result

            
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   dmw = DesignerMainWindow()
   dmw.show()
	#dmw.showFullScreen()
   sys.exit(app.exec_())