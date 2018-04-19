# -*- coding: utf-8 -*-
from PyQt5 import uic
 
fin = open('pyqt_Opencv.ui', 'r')
fout = open('pyqt_Opencv.py', 'w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()