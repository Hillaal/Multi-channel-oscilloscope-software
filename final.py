from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QLabel
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import time
import datetime
import matplotlib.pyplot as plot
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from scipy import signal
from PyQt5.QtGui import QIcon, QPixmap
import tempfile
import shutil

from spectWindow1 import Ui_spectWindow1
from spectWindow2 import Ui_spectWindow2
from spectWindow3 import Ui_spectWindow3

class Ui_mainwindow(QtGui.QMainWindow):
    
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.setEnabled(True)
        mainwindow.resize(1450, 897)
        font = QtGui.QFont()
        font.setPointSize(6)
        mainwindow.setFont(font)
        mainwindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        mainwindow.setStyleSheet("QMainWindow{\n"

"\n"
"\n"
"\n"
"}\n"
"\n"

"QWidget\n"
"{\n"
"background-color:  #d4d5dd;"
"}\n"
"\n"

"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar\n"
"{\n"
"    background-color: #34373f;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transparent;\n"

"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: #f0f5f3;\n"
"    color: #34373f;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: #dcdcdf;\n"
"    border: 1px solid #000;\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #dcdcdf;\n"
"    border: 1px solid;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu QWidget{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #34373f;\n"
"    color: #ffffff;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    min-width : 150px;\n"
"    padding: 3px 20px 3px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #34373f;\n"
"    color: #f0f5f3;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #262626;\n"
"\n"
"}\n"
"\n"

"QPushButton{\n"
"    color:#34373f;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-bottom-color: rgb(150,150,150);\n"
"    border-right-color: rgb(165,165,165);\n"
"    border-left-color: rgb(165,165,165);\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    color:#0b0c0e;\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color:#34373f;\n"
"    border-right-color:#34373f;\n"
"    border-left-color:  #34373f;\n"
"    border-bottom-color: #34373f;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c7cad1, stop:1 #b9bdc6);\n"
"}\n"
"QPushButton:default{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: rgb(68, 72, 81);\n"
"    border-left-color:  rgb(68, 72, 81);\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: rgb(68, 72, 81);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"    border-top-color: rgba(255,150,60,200);\n"
"    border-right-color: rgb(68, 72, 81);\n"
"    border-left-color: rgb(68, 72, 81);\n"
"    border-bottom-color: rgba(200,70,20,200);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(24)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.show_ch1 = QtWidgets.QCheckBox(self.centralwidget)
        self.show_ch1.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.show_ch1.setFont(font)
        self.show_ch1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_ch1.setCheckable(True)
        self.show_ch1.setChecked(True)
        self.show_ch1.setTristate(False)
        self.show_ch1.setObjectName("show_ch1")
        self.horizontalLayout_4.addWidget(self.show_ch1)
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_4.addWidget(self.graphicsView)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.up1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up1.sizePolicy().hasHeightForWidth())
        self.up1.setSizePolicy(sizePolicy)
        self.up1.setMinimumSize(QtCore.QSize(35, 35))
        self.up1.setMaximumSize(QtCore.QSize(35, 35))
        self.up1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.up1.setText("")
        self.up1.setObjectName("up1")
        self.verticalLayout.addWidget(self.up1, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.left1 = QtWidgets.QPushButton(self.centralwidget)
        self.left1.setMinimumSize(QtCore.QSize(35, 35))
        self.left1.setMaximumSize(QtCore.QSize(35, 35))
        self.left1.setText("")
        self.left1.setObjectName("left1")
        self.horizontalLayout_7.addWidget(self.left1)
        self.right1 = QtWidgets.QPushButton(self.centralwidget)
        self.right1.setMinimumSize(QtCore.QSize(35, 35))
        self.right1.setMaximumSize(QtCore.QSize(35, 35))
        self.right1.setText("")
        self.right1.setObjectName("right1")
        self.horizontalLayout_7.addWidget(self.right1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.down1 = QtWidgets.QPushButton(self.centralwidget)
        self.down1.setMinimumSize(QtCore.QSize(35, 35))
        self.down1.setMaximumSize(QtCore.QSize(35, 35))
        self.down1.setText("")
        self.down1.setObjectName("down1")
        self.verticalLayout.addWidget(self.down1, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 7, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zoomin1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin1.setMinimumSize(QtCore.QSize(35, 35))
        self.zoomin1.setMaximumSize(QtCore.QSize(35, 35))
        self.zoomin1.setText("")
        self.zoomin1.setObjectName("zoomin1")
        self.horizontalLayout.addWidget(self.zoomin1)
        self.zoomout1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout1.setMinimumSize(QtCore.QSize(35, 35))
        self.zoomout1.setMaximumSize(QtCore.QSize(35, 35))
        self.zoomout1.setText("")
        self.zoomout1.setObjectName("zoomout1")
        self.horizontalLayout.addWidget(self.zoomout1)
        self.resume1 = QtWidgets.QPushButton(self.centralwidget)
        self.resume1.setMinimumSize(QtCore.QSize(35, 35))
        self.resume1.setMaximumSize(QtCore.QSize(35, 35))
        self.resume1.setText("")
        self.resume1.setObjectName("resume1")
        self.horizontalLayout.addWidget(self.resume1)
        self.pause1 = QtWidgets.QPushButton(self.centralwidget)
        self.pause1.setMinimumSize(QtCore.QSize(35, 35))
        self.pause1.setMaximumSize(QtCore.QSize(35, 35))
        self.pause1.setText("")
        self.pause1.setObjectName("pause1")
        self.horizontalLayout.addWidget(self.pause1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.spectro1 = QtWidgets.QPushButton(self.centralwidget)
        self.spectro1.setMinimumSize(QtCore.QSize(92, 34))
        self.spectro1.setMaximumSize(QtCore.QSize(92, 34))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.spectro1.setFont(font)
        self.spectro1.setObjectName("spectro1")
        self.horizontalLayout_10.addWidget(self.spectro1)
        self.clear1 = QtWidgets.QPushButton(self.centralwidget)
        self.clear1.setMinimumSize(QtCore.QSize(92, 34))
        self.clear1.setMaximumSize(QtCore.QSize(92, 34))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.clear1.setFont(font)
        self.clear1.setObjectName("clear1")
        self.horizontalLayout_10.addWidget(self.clear1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12.addLayout(self.verticalLayout_7)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(24)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.show_ch2 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.show_ch2.setFont(font)
        self.show_ch2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_ch2.setChecked(True)
        self.show_ch2.setObjectName("show_ch2")
        self.horizontalLayout_5.addWidget(self.show_ch2)
        self.graphicsView_2 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_5.addWidget(self.graphicsView_2)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.up2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up2.sizePolicy().hasHeightForWidth())
        self.up2.setSizePolicy(sizePolicy)
        self.up2.setMinimumSize(QtCore.QSize(0, 35))
        self.up2.setMaximumSize(QtCore.QSize(35, 35))
        self.up2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.up2.setText("")
        self.up2.setObjectName("up2")
        self.verticalLayout_2.addWidget(self.up2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.left2 = QtWidgets.QPushButton(self.centralwidget)
        self.left2.setMinimumSize(QtCore.QSize(0, 35))
        self.left2.setMaximumSize(QtCore.QSize(35, 35))
        self.left2.setText("")
        self.left2.setObjectName("left2")
        self.horizontalLayout_8.addWidget(self.left2)
        self.right2 = QtWidgets.QPushButton(self.centralwidget)
        self.right2.setMinimumSize(QtCore.QSize(0, 35))
        self.right2.setMaximumSize(QtCore.QSize(35, 35))
        self.right2.setText("")
        self.right2.setObjectName("right2")
        self.horizontalLayout_8.addWidget(self.right2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.down2 = QtWidgets.QPushButton(self.centralwidget)
        self.down2.setMinimumSize(QtCore.QSize(0, 35))
        self.down2.setMaximumSize(QtCore.QSize(35, 35))
        self.down2.setText("")
        self.down2.setObjectName("down2")
        self.verticalLayout_2.addWidget(self.down2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 7, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.zoomin2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin2.setMinimumSize(QtCore.QSize(35, 35))
        self.zoomin2.setMaximumSize(QtCore.QSize(35, 35))
        self.zoomin2.setText("")
        self.zoomin2.setObjectName("zoomin2")
        self.horizontalLayout_2.addWidget(self.zoomin2)
        self.zoomout2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout2.setMinimumSize(QtCore.QSize(35, 35))
        self.zoomout2.setMaximumSize(QtCore.QSize(35, 35))
        self.zoomout2.setText("")
        self.zoomout2.setObjectName("zoomout2")
        self.horizontalLayout_2.addWidget(self.zoomout2)
        self.resume2 = QtWidgets.QPushButton(self.centralwidget)
        self.resume2.setMinimumSize(QtCore.QSize(35, 35))
        self.resume2.setMaximumSize(QtCore.QSize(35, 35))
        self.resume2.setText("")
        self.resume2.setObjectName("resume2")
        self.horizontalLayout_2.addWidget(self.resume2)
        self.pause2 = QtWidgets.QPushButton(self.centralwidget)
        self.pause2.setMinimumSize(QtCore.QSize(35, 35))
        self.pause2.setMaximumSize(QtCore.QSize(35, 35))
        self.pause2.setText("")
        self.pause2.setObjectName("pause2")
        self.horizontalLayout_2.addWidget(self.pause2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.spectro2 = QtWidgets.QPushButton(self.centralwidget)
        self.spectro2.setMinimumSize(QtCore.QSize(92, 34))
        self.spectro2.setMaximumSize(QtCore.QSize(92, 34))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.spectro2.setFont(font)
        self.spectro2.setObjectName("spectro2")
        self.horizontalLayout_11.addWidget(self.spectro2)
        self.clear2 = QtWidgets.QPushButton(self.centralwidget)
        self.clear2.setMinimumSize(QtCore.QSize(92, 34))
        self.clear2.setMaximumSize(QtCore.QSize(92, 34))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.clear2.setFont(font)
        self.clear2.setObjectName("clear2")
        self.horizontalLayout_11.addWidget(self.clear2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(24)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.show_ch3 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.show_ch3.setFont(font)
        self.show_ch3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_ch3.setChecked(True)
        self.show_ch3.setObjectName("show_ch3")
        self.horizontalLayout_6.addWidget(self.show_ch3)
        self.graphicsView_3 =pg.PlotWidget(self.centralwidget)
        self.graphicsView_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_6.addWidget(self.graphicsView_3)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.up3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up3.sizePolicy().hasHeightForWidth())
        self.up3.setSizePolicy(sizePolicy)
        self.up3.setMinimumSize(QtCore.QSize(0, 35))
        self.up3.setMaximumSize(QtCore.QSize(35, 35))
        self.up3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.up3.setText("")
        self.up3.setObjectName("up3")
        self.verticalLayout_3.addWidget(self.up3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.left3 = QtWidgets.QPushButton(self.centralwidget)
        self.left3.setMinimumSize(QtCore.QSize(0, 35))
        self.left3.setMaximumSize(QtCore.QSize(35, 35))
        self.left3.setText("")
        self.left3.setObjectName("left3")
        self.horizontalLayout_9.addWidget(self.left3)
        self.right3 = QtWidgets.QPushButton(self.centralwidget)
        self.right3.setMinimumSize(QtCore.QSize(0, 35))
        self.right3.setMaximumSize(QtCore.QSize(35, 35))
        self.right3.setText("")
        self.right3.setObjectName("right3")
        self.horizontalLayout_9.addWidget(self.right3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.down3 = QtWidgets.QPushButton(self.centralwidget)
        self.down3.setMinimumSize(QtCore.QSize(0, 35))
        self.down3.setMaximumSize(QtCore.QSize(35, 35))
        self.down3.setText("")
        self.down3.setObjectName("down3")
        self.verticalLayout_3.addWidget(self.down3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 7, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.zoomin3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin3.setMinimumSize(QtCore.QSize(35, 35))
        self.zoomin3.setMaximumSize(QtCore.QSize(35, 35))
        self.zoomin3.setText("")
        self.zoomin3.setObjectName("zoomin3")
        self.horizontalLayout_3.addWidget(self.zoomin3)
        self.zoomout3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout3.setMinimumSize(QtCore.QSize(35, 35))
        self.zoomout3.setMaximumSize(QtCore.QSize(35, 35))
        self.zoomout3.setText("")
        self.zoomout3.setObjectName("zoomout3")
        self.horizontalLayout_3.addWidget(self.zoomout3)
        self.resume3 = QtWidgets.QPushButton(self.centralwidget)
        self.resume3.setMinimumSize(QtCore.QSize(35, 35))
        self.resume3.setMaximumSize(QtCore.QSize(35, 35))
        self.resume3.setText("")
        self.resume3.setObjectName("resume3")
        self.horizontalLayout_3.addWidget(self.resume3)
        self.pause3 = QtWidgets.QPushButton(self.centralwidget)
        self.pause3.setMinimumSize(QtCore.QSize(35, 35))
        self.pause3.setMaximumSize(QtCore.QSize(35, 35))
        self.pause3.setText("")
        self.pause3.setObjectName("pause3")
        self.horizontalLayout_3.addWidget(self.pause3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.spectro3 = QtWidgets.QPushButton(self.centralwidget)
        self.spectro3.setMinimumSize(QtCore.QSize(92, 34))
        self.spectro3.setMaximumSize(QtCore.QSize(92, 34))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.spectro3.setFont(font)
        self.spectro3.setObjectName("spectro3")
        self.horizontalLayout_15.addWidget(self.spectro3)
        self.clear3 = QtWidgets.QPushButton(self.centralwidget)
        self.clear3.setMinimumSize(QtCore.QSize(92, 34))
        self.clear3.setMaximumSize(QtCore.QSize(92, 34))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.clear3.setFont(font)
        self.clear3.setObjectName("clear3")
        self.horizontalLayout_15.addWidget(self.clear3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setBaseSize(QtCore.QSize(4, 8))
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1347, 26))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menusignal_processing = QtWidgets.QMenu(self.menubar)
        self.menusignal_processing.setBaseSize(QtCore.QSize(7, 7))
        self.menusignal_processing.setObjectName("menusignal_processing")
        self.ch1 = QtWidgets.QMenu(self.menubar)
        self.ch1.setObjectName("ch1")
        self.ch2 = QtWidgets.QMenu(self.menubar)
        self.ch2.setObjectName("ch2")
        self.ch3 = QtWidgets.QMenu(self.menubar)
        self.ch3.setObjectName("ch3")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        mainwindow.setMenuBar(self.menubar)
        self.actionhelp = QtWidgets.QAction(mainwindow)
        self.actionhelp.setObjectName("actionhelp")
        self.close = QtWidgets.QAction(mainwindow)
        self.close.setObjectName("close")
        self.actionhelp_2 = QtWidgets.QAction(mainwindow)
        self.actionhelp_2.setObjectName("actionhelp_2")
        self.open_ch1 = QtWidgets.QAction(mainwindow)
        self.open_ch1.setObjectName("open_ch1")
        self.open_ch2 = QtWidgets.QAction(mainwindow)
        self.open_ch2.setObjectName("open_ch2")
        self.open_ch3 = QtWidgets.QAction(mainwindow)
        self.open_ch3.setObjectName("open_ch3")
        self.about = QtWidgets.QAction(mainwindow)
        self.about.setObjectName("about")
        self.savePDF = QtWidgets.QAction(mainwindow)
        self.savePDF.setObjectName("savePDF")
        self.menusignal_processing.addAction(self.savePDF)
        self.menusignal_processing.addAction(self.close)
        self.ch1.addAction(self.open_ch1)
        self.ch2.addAction(self.open_ch2)
        self.ch3.addAction(self.open_ch3)
        self.help.addAction(self.about)
        self.menubar.addAction(self.menusignal_processing.menuAction())
        self.menubar.addAction(self.ch1.menuAction())
        self.menubar.addAction(self.ch2.menuAction())
        self.menubar.addAction(self.ch3.menuAction())
        self.menubar.addAction(self.help.menuAction())
    
        self.b1=0
        self.c1=1
        
        self.b2=0
        self.c2=1
        
        self.b3=0
        self.c3=1
        
        self.sc_x1=0
        self.sc_x2=0
        self.sc_x3=0
        self.sc_y1=0
        self.sc_y2=0
        self.sc_y3=0

        self.retranslateUi(mainwindow)


    ################ Timer for qt ##################
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer3 = QtCore.QTimer()



    ############################### UI and Events #################################

    def retranslateUi(self, mainwindow):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Signal Viewer"))
        self.show_ch1.setText(_translate("mainwindow", "Channel 1"))
        self.spectro1.setText(_translate("mainwindow", "Spectrogram"))
        self.clear1.setText(_translate("mainwindow", "Clear"))
        self.show_ch2.setText(_translate("mainwindow", "Channel 2"))
        self.spectro2.setText(_translate("mainwindow", "SPECTROGRAM"))
        self.clear2.setText(_translate("mainwindow", "Clear"))
        self.show_ch3.setText(_translate("mainwindow", "Channel 3"))
        self.spectro3.setText(_translate("mainwindow", "Spectrogram"))
        self.clear3.setText(_translate("mainwindow", "Clear"))
        self.menusignal_processing.setTitle(_translate("mainwindow", "File"))
        self.ch1.setTitle(_translate("mainwindow", "Channel 1"))
        self.ch2.setTitle(_translate("mainwindow", "Channel 2"))
        self.ch3.setTitle(_translate("mainwindow", "Channel 3"))
        self.help.setTitle(_translate("mainwindow", "Help"))
        self.actionhelp.setText(_translate("mainwindow", "help"))
        self.close.setText(_translate("mainwindow", "Close "))
        self.actionhelp_2.setText(_translate("mainwindow", "help "))
        self.open_ch1.setText(_translate("mainwindow", "Load Signal"))
        self.open_ch2.setText(_translate("mainwindow", "Load Signal"))
        self.open_ch3.setText(_translate("mainwindow", "Load Signal"))
        self.about.setText(_translate("mainwindow", "About"))
        self.savePDF.setText(_translate("mainwindow", "Save PDF"))
        
        
        
        ######################## Icons ###############################

        self.resume1.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/play.png")))
        self.resume2.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/play.png")))
        self.resume3.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/play.png")))
        self.pause1.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/pause.png")))
        self.pause2.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/pause.png")))
        self.pause3.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/pause.png")))

        self.zoomin1.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/in.png")))
        self.zoomout1.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/out.png")))
        self.zoomin2.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/in.png")))
        self.zoomout2.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/out.png")))
        self.zoomin3.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/in.png")))
        self.zoomout3.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/out.png")))

        self.up1.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/up.png")))
        self.down1.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/down.png")))
        self.left1.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/left.png")))
        self.right1.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/right.png")))

        self.up2.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/up.png")))
        self.down2.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/down.png")))
        self.left2.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/left.png")))
        self.right2.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/right.png")))
        
        self.up3.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/up.png")))
        self.down3.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/down.png")))
        self.left3.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/left.png")))
        self.right3.setIcon(QIcon(os.path.join(THIS_FOLDER,"icons/right.png")))


        ############# Resume buttons Actions ##################

        self.resume1.clicked.connect(lambda :self.timer1.start())
        self.resume2.clicked.connect(lambda :self.timer2.start())
        self.resume3.clicked.connect(lambda :self.timer3.start())

        self.pause1.clicked.connect(lambda :self.timer1.stop())
        self.pause2.clicked.connect(lambda :self.timer2.stop())
        self.pause3.clicked.connect(lambda :self.timer3.stop())

        self.zoomin1.clicked.connect(lambda :self.zi_1())
        self.zoomin2.clicked.connect(lambda :self.zi_2())
        self.zoomin3.clicked.connect(lambda :self.zi_3())
        self.zoomout1.clicked.connect(lambda :self.zo_1())
        self.zoomout2.clicked.connect(lambda :self.zo_2())
        self.zoomout3.clicked.connect(lambda :self.zo_3())
        
        ##################### Shortcuts ##################
        self.show_ch1.setShortcut(_translate("MAINWINDOW", "Ctrl+h"))
        self.show_ch2.setShortcut(_translate("MAINWINDOW", "shift+h"))
        self.show_ch3.setShortcut(_translate("MAINWINDOW", "alt+h"))
        

        self.zoomout1.setShortcut(_translate("MAINWINDOW", "Ctrl+-"))
        self.zoomout2.setShortcut(_translate("MainWindow", "shift+-"))
        self.zoomout3.setShortcut(_translate("MainWindow", "alt+-"))
        
        self.zoomin1.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.zoomin2.setShortcut(_translate("MainWindow", "shift++"))
        self.zoomin3.setShortcut(_translate("MainWindow", "alt++"))
 
        self.resume1.setShortcut(_translate("MainWindow", "Ctrl+r"))
        self.resume2.setShortcut(_translate("MainWindow", "shift+r"))
        self.resume3.setShortcut(_translate("MainWindow", "alt+r"))
        
        self.pause1.setShortcut(_translate("MainWindow", "Ctrl+p"))
        self.pause2.setShortcut(_translate("MAINWINDOW", "shift+p"))
        self.pause3.setShortcut(_translate("MainWindow", "alt+p"))
        
        self.savePDF.setShortcut(_translate("MainWindow", "Ctrl+s"))
        
        self.open_ch1.setShortcut(_translate("MAinWindow", "ctrl+o"))
        self.open_ch2.setShortcut(_translate("MAinWindow", "shift+o"))        
        self.open_ch3.setShortcut(_translate("MAinWindow", "alt+o"))
        
        self.right1.setShortcut(_translate("MAinWindow", "ctrl+6"))
        self.right2.setShortcut(_translate("MAinWindow", "ctrl+alt+6"))        
        self.right3.setShortcut(_translate("MAinWindow", "alt+6"))
        
        self.left1.setShortcut(_translate("MAinWindow", "ctrl+4"))
        self.left2.setShortcut(_translate("MAinWindow", "ctrl+alt+4"))        
        self.left3.setShortcut(_translate("MAinWindow", "alt+4"))
        
        self.down1.setShortcut(_translate("MAinWindow", "ctrl+2"))
        self.down2.setShortcut(_translate("MAinWindow", "ctrl+alt+2"))        
        self.down3.setShortcut(_translate("MAinWindow", "alt+2"))
        
        self.up1.setShortcut(_translate("MAinWindow", "ctrl+8"))
        self.up2.setShortcut(_translate("MAinWindow", "ctrl+alt+8"))        
        self.up3.setShortcut(_translate("MAinWindow", "alt+8"))
        
        self.clear1.setShortcut(_translate("MAinWindow", "ctrl+c"))
        self.clear2.setShortcut(_translate("MAinWindow", "shift+c"))        
        self.clear3.setShortcut(_translate("MAinWindow", "alt+c"))
        
        self.spectro1.setShortcut(_translate("MAinWindow", "ctrl+m"))
        self.spectro2.setShortcut(_translate("MAinWindow", "shift+m"))        
        self.spectro3.setShortcut(_translate("MAinWindow", "alt+m"))
        
        self.about.setShortcut(_translate("MAinWindow", "ctrl+a"))
        
        ##################### Save pdf ######################
        
        self.savePDF.triggered.connect(lambda:self.savepdf())
       
        
       
        ################### Scrolling buttons ###################

        self.right1.clicked.connect(lambda :self.scrollR(1))
        self.right2.clicked.connect(lambda :self.scrollR(2))
        self.right3.clicked.connect(lambda :self.scrollR(3))
        self.left1.clicked.connect(lambda :self.scrollL(1))
        self.left2.clicked.connect(lambda :self.scrollL(2))
        self.left3.clicked.connect(lambda :self.scrollL(3))
        self.up1.clicked.connect(lambda :self.scrollU(1))
        self.up2.clicked.connect(lambda :self.scrollU(2))
        self.up3.clicked.connect(lambda :self.scrollU(3))
        self.down1.clicked.connect(lambda :self.scrollD(1))
        self.down2.clicked.connect(lambda :self.scrollD(2))
        self.down3.clicked.connect(lambda :self.scrollD(3))

        ################## Clear ######################

        self.clear1.clicked.connect(lambda:self.delete(1))
        self.clear2.clicked.connect(lambda:self.delete(2))
        self.clear3.clicked.connect(lambda:self.delete(3))



        ################# Loading Data ################

        self.close.triggered.connect(sys.exit)
        self.about.triggered.connect(self.showDialog)
        self.open_ch1.triggered.connect(lambda: self.play1())
        self.open_ch2.triggered.connect(lambda: self.play2())
        self.open_ch3.triggered.connect(lambda: self.play3())

        ################# Hide Channels ################

        self.show_ch1.stateChanged.connect(lambda: self.hide1(self.show_ch1,self.graphicsView))
        self.show_ch2.stateChanged.connect(lambda: self.hide2(self.show_ch2,self.graphicsView_2))
        self.show_ch3.stateChanged.connect(lambda: self.hide3(self.show_ch3,self.graphicsView_3))

        ################# Show Spectrogram ################

        self.spectro1.clicked.connect(lambda: self.showwindow(1))
        self.spectro2.clicked.connect(lambda: self.showwindow(2))
        self.spectro3.clicked.connect(lambda: self.showwindow(3))



#########################################functions###################

    ################# reading dataaa ###############

    def read_data(self,ch):
        loadSignal= QtGui.QFileDialog.getOpenFileName( self, 'Open only CSV ', os.getenv('HOME') ,"csv(*.csv)")
        path=loadSignal[0]  
        data=np.genfromtxt(path,delimiter = ' ')
        x1=data[: , 0]
        if ch==1:
            self.y1_array =data[: , 1]
            self.x1= list(x1[:])
            self.y1= list(self.y1_array [:])
            self.ch1=1
            self.spectro(1,data)
        if ch==2:
            self.y2_array =data[: , 1]
            self.x2= list(x1[:])
            self.y2= list(self.y2_array [:])
            self.ch2=1
            self.spectro(2,data)
        if ch==3:
            self.y3_array =data[: , 1]
            self.x3= list(x1[:])
            self.y3= list(self.y3_array [:])
            self.ch3=1
            self.spectro(3,data)


    ########### Function in qt timer to update the data ###########

    def update1(self):
        if self.st_x1>len(self.x1):
            self.st_x1=10
        x=self.x1[:self.st_x1]
        y=self.y1[:self.st_x1]
        self.st_x1+=10
        self.graphicsView.plot(x,y,pen=pg.mkPen('b', width=1))
        if  self.x1[self.st_x1] >1:
            self.graphicsView.setLimits(xMin =min(x ), xMax=max(x)) 
            self.c1=self.x1[self.st_x1]
        if max(self.x1)>0.5:    
            self.graphicsView.plotItem.setXRange(max(x)-0.5 , max(x))
    def update2(self):
        if self.st_x2>len(self.x2):
            self.st_x2=10
        x=self.x2[:self.st_x2]
        y=self.y2[:self.st_x2]
        self.st_x2+=10
        self.graphicsView_2.plot(x,y,pen=pg.mkPen('r', width=2))
        if  self.x2[self.st_x2] >0.9:
            self.c2=self.x2[self.st_x2]
            self.graphicsView_2.setLimits(xMin =min(x ), xMax=max(x)) 
        if max(self.x2)>0.5:    
            self.graphicsView_2.plotItem.setXRange(max(x)-0.5 , max(x))
    def update3(self):
       if self.st_x3>len(self.x3):
            self.st_x1=10
       x=self.x3[:self.st_x3]
       y=self.y3[:self.st_x3]
       self.st_x3+=10
       self.graphicsView_3.plot(x,y,pen=pg.mkPen('g', width=3))
       if  self.x3[self.st_x3] >0.9:
           self.c3=self.x3[self.st_x3] 
           self.graphicsView_3.setLimits(xMin =min(x ), xMax=max(x)) 
       if max(self.x3)>0.5:    
            self.graphicsView_3.plotItem.setXRange(max(x)-0.5 , max(x))
            
                                       
    ############## Playing data on adding the file ##########

    def play1(self):
        self.read_data(1)
        self.timer1.start()
        self.st_x1=10
        self.timer1.setInterval(50)
        self.e_x1=0
        self.graphicsView.setMouseEnabled(x=None)
        self.graphicsView.setXRange(0,1)
        
        self.timer1.timeout.connect(self.update1)
        self.timer1.start()
        
    def play2(self):
        self.read_data(2)
        self.st_x2=10
        self.timer2.setInterval(100)
        self.e_x2=0
        self.graphicsView_2.setMouseEnabled(x=None)
        
        self.graphicsView_2.setXRange(-.5,1)
        
        self.graphicsView_2.setYRange(0,1)
        self.timer2.timeout.connect(self.update2)
        self.timer2.start()

    def play3(self):
        self.read_data(3)
        self.st_x3=10
        self.timer3.setInterval(100)
        self.e_x3=0
        self.graphicsView_3.setXRange(0,1)
        self.timer3.timeout.connect(self.update3)
        self.timer3.start()


    ############ Zooming #############

    def zi_1(self):
        if(self.b1 < 3):
            self.c1-=0.2
            self.graphicsView.setXRange(self.x1[self.e_x1],self.c1)
            self.b1+=1
        
    def zi_2(self):
        if(self.b2 < 3):
            self.c2-=0.2
            self.graphicsView_2.setXRange(self.x2[self.e_x2],self.c2)
            self.b2+=1


    def zi_3(self):
        if(self.b3 < 3):
            self.c3-=0.2
            self.graphicsView_3.setXRange(self.x3[self.e_x3],self.c3)
            self.b3+=1

    def zo_1(self):
        if(self.b1 >0):
            self.c1+=0.2
            self.graphicsView.setXRange(self.x1[self.e_x1],self.c1)
            self.b1-=1
    def zo_2(self):
        if(self.b2 >0):
            self.c2+=0.2
            self.graphicsView_2.setXRange(self.x2[self.e_x2],self.c2)
            self.b2-=1


    def zo_3(self):
        if(self.b3 >0):
            self.c3 +=0.2
            self.b3-=1
        self.graphicsView_3.setXRange(self.x3[self.e_x3],self.c3)


    ############# Saving data #############

    def savepdf(self) :
         fig=plot.figure()
         if self.ch1==1:
             plot.subplot(2, 3, 1)
             plot.plot(self.x1,self.y1,color="red", linewidth=2,scalex=True)
             plot.subplot(2, 3, 4)
             Pxx, freqs, bins, im = plot.specgram(self.y1_array,Fs=1/self.x1[1])
         if self.ch2==1:
             plot.subplot(2, 3, 2)
             plot.plot(self.x2,self.y2,color="blue", linewidth=2,scalex=True)
             plot.subplot(2, 3, 5)
             Pxx, freqs, bins, im = plot.specgram(self.y2_array,Fs=1/self.x2[1])
         if self.ch3==1:
             plot.subplot(2, 3, 3)
             plot.plot(self.x3,self.y3,color="black", linewidth=2,scalex=True)
             plot.subplot(2, 3, 6)
             Pxx, freqs, bins, im = plot.specgram(self.y3_array,Fs=1/self.x3[1])
            
         plot.subplots_adjust(bottom=0.1, right=0.9999999,left=0.1 ,top=1.0)    
         plot.show()
         fig.savefig("SIGNAL_PLOT.pdf")

    ############### Clear data ##############

    def delete(self,c):

        if 1==c:
            self.graphicsView.clear()
            self.timer1.stop()
            self.ch1=0
            self.ui1.spectView1.clear()

        elif 2==c:
            self.graphicsView_2.clear()
            self.timer2.stop()
            self.ch2=0
            self.ui2.spectView2.clear()


        elif 3==c:
            self.graphicsView_3.clear()
            self.timer3.stop()
            self.ch3=0
            self.ui3.spectView3.clear()
        
  ################## About message ############################
  ############### Hide Channels function ######################

        #resume buttoms actions
        self.resume1.clicked.connect(lambda :self.timer1.start())
        self.resume2.clicked.connect(lambda :self.timer2.start())
        self.resume3.clicked.connect(lambda :self.timer3.start())

        self.pause1.clicked.connect(lambda :self.timer1.stop())
        self.pause2.clicked.connect(lambda :self.timer2.stop())
        self.pause3.clicked.connect(lambda :self.timer3.stop())

        self.zoomin1.clicked.connect(lambda :self.zi_1())
        self.zoomin2.clicked.connect(lambda :self.zi_2())
        self.zoomin3.clicked.connect(lambda :self.zi_3())
        self.zoomout1.clicked.connect(lambda :self.zo_1())
        self.zoomout2.clicked.connect(lambda :self.zo_2())
        self.zoomout3.clicked.connect(lambda :self.zo_3())
        
        #####################shortcuts
       
        #aaahoooooooooooooooooooooo save pdf ******************
        
        self.savePDF.triggered.connect(lambda:self.savepdf())
       
        
       
        #***********************scrolling button**************
        self.right1.clicked.connect(lambda :self.scrollR(1))
        self.right2.clicked.connect(lambda :self.scrollR(2))
        self.right3.clicked.connect(lambda :self.scrollR(3))
        self.left1.clicked.connect(lambda :self.scrollL(1))
        self.left2.clicked.connect(lambda :self.scrollL(2))
        self.left3.clicked.connect(lambda :self.scrollL(3))
        self.up1.clicked.connect(lambda :self.scrollU(1))
        self.up2.clicked.connect(lambda :self.scrollU(2))
        self.up3.clicked.connect(lambda :self.scrollU(3))
        self.down1.clicked.connect(lambda :self.scrollD(1))
        self.down2.clicked.connect(lambda :self.scrollD(2))
        self.down3.clicked.connect(lambda :self.scrollD(3))
        #clear event
        self.clear1.clicked.connect(lambda:self.delete(1))
        self.clear2.clicked.connect(lambda:self.delete(2))
        self.clear3.clicked.connect(lambda:self.delete(3))



            ############## Hilal Events #############
        self.close.triggered.connect(sys.exit)
        self.about.triggered.connect(self.showDialog)
        self.open_ch1.triggered.connect(lambda: self.play1())
        self.open_ch2.triggered.connect(lambda: self.play2())
        self.open_ch3.triggered.connect(lambda: self.play3())

        self.show_ch1.stateChanged.connect(lambda: self.hide1(self.show_ch1,self.graphicsView))
        self.show_ch2.stateChanged.connect(lambda: self.hide2(self.show_ch2,self.graphicsView_2))
        self.show_ch3.stateChanged.connect(lambda: self.hide3(self.show_ch3,self.graphicsView_3))
        #self.show_spect.stateChanged.connect(lambda: self.hide(self.show_spect,self.tabWidget))

        self.spectro1.clicked.connect(lambda: self.showwindow(1))
        self.spectro2.clicked.connect(lambda: self.showwindow(2))
        self.spectro3.clicked.connect(lambda: self.showwindow(3))
     
     ##########About message################

    def showDialog(self):
          QMessageBox.information(self,"About","""Signal Viewer is a software for visualizing signals \n (c) 2021 SBME Cairo University\n some shortcuts
for channels 
1:ctrl+
2:shift+
3:alt+
\nfor shortcuts
zoomout:-
zoomin:+
\nresume:r
pause1:p
\nsavePDF:s
\nup:8
down::2
left:4
right:6
\nspectrogram: m
clear:c
about:a
""")


    def hide1 (self,channel,graphicsView):
        if (channel.isChecked()):
            graphicsView.show()
            self.pause1.show()
            self.resume1.show()
            self.zoomin1.show()
            self.zoomout1.show()
            self.up1.show()
            self.down1.show()
            self.left1.show()
            self.right1.show()
            self.clear1.show()
            self.spectro1.show()
        else:
            graphicsView.hide()
            self.pause1.hide()
            self.resume1.hide()
            self.zoomin1.hide()
            self.zoomout1.hide()
            self.up1.hide()
            self.down1.hide()
            self.left1.hide()
            self.right1.hide()
            self.clear1.hide()
            self.spectro1.hide()

    def hide2 (self,channel,graphicsView):
        if (channel.isChecked()):
            graphicsView.show()
            self.pause2.show()
            self.resume2.show()
            self.zoomin2.show()
            self.zoomout2.show()
            self.up2.show()
            self.down2.show()
            self.left2.show()
            self.right2.show()
            self.clear2.show()
            self.spectro2.show()

            
        else:
            graphicsView.hide()
            self.pause2.hide()
            self.resume2.hide()
            self.zoomin2.hide()
            self.zoomout2.hide()
            self.up2.hide()
            self.down2.hide()
            self.left2.hide()
            self.right2.hide()
            self.clear2.hide()
            self.spectro2.hide()

    def hide3 (self,channel,graphicsView):
        if (channel.isChecked()):
            graphicsView.show()
            self.pause3.show()
            self.resume3.show()
            self.zoomin3.show()
            self.zoomout3.show()
            self.up3.show()
            self.down3.show()
            self.left3.show()
            self.right3.show()
            self.clear3.show()
            self.spectro3.show()

        else:
            graphicsView.hide()
            self.pause3.hide()
            self.resume3.hide()
            self.zoomin3.hide()
            self.zoomout3.hide()
            self.up3.hide()
            self.down3.hide()
            self.left3.hide()
            self.right3.hide()
            self.clear3.hide()
            self.spectro3.hide()

    def hide (self,channel,graphicsView):
        if (channel.isChecked()):
            graphicsView.show()
        else:
            graphicsView.hide()


    #################### Spectrogram ###########################

    def showwindow(self,ch):
        if 1 == ch:
            self.window1.show()
        elif 2 == ch:
            self.window2.show()
        elif 3 == ch:
            self.window3.show()


    def spectro (self,ch,d):   #ch for channel  and  d for Data
       
        dirpath = tempfile.mkdtemp()
        


        if ch ==1:
            
            plot.specgram(self.y1,Fs=1/self.x1[1])
            plot.savefig(os.path.join(dirpath,"plot1.png"))
            plot1 = QPixmap(os.path.join(dirpath,"plot1.png"))
            self.window1=QtWidgets.QWidget()
            self.ui1=Ui_spectWindow1()
            self.ui1.setupUi(self.window1)
            self.ui1.spectView1.setPixmap(plot1)



        elif ch ==2:
            
            plot.specgram(self.y2,Fs=1/self.x2[1])

            plot.savefig(os.path.join(dirpath,"plot2.png"))
            plot2= QPixmap(os.path.join(dirpath,"plot2.png"))
            self.window2=QtWidgets.QWidget()
            self.ui2=Ui_spectWindow2()
            self.ui2.setupUi(self.window2)
            self.ui2.spectView2.setPixmap(plot2)
            



        elif ch ==3:
            
            plot.specgram(self.y3,Fs=1/self.x3[0])
            plot.savefig(os.path.join(dirpath,"plot3.png"))
            plot3 = QPixmap(os.path.join(dirpath,"plot3.png"))
            self.window3=QtWidgets.QWidget()
            self.ui3=Ui_spectWindow3()
            self.ui3.setupUi(self.window3)
            self.ui3.spectView3.setPixmap(plot3)


        shutil.rmtree(dirpath)

    ########################### Scrolling on x axis ##############################

    def scrollR(self,ch):
        if ch==1:
            self.sc_x1 +=0.1
            self.graphicsView.setXRange(self.sc_x1,self.sc_x1 +1)
             
        if ch==2:
             self.sc_x2 +=0.1
             self.graphicsView_2.setXRange(self.sc_x2,self.sc_x2 +1)
             
        if ch==3:
              self.sc_x3 +=0.1
              self.graphicsView_3.setXRange(self.sc_x3,self.sc_x3 +1)


    def scrollL(self,ch):
        if ch==1:
            self.sc_x1 -=0.1
            self.graphicsView.setXRange(self.sc_x1,self.sc_x1 +1)
             
        if ch==2:
             self.sc_x2 -=0.1
             self.graphicsView_2.setXRange(self.sc_x2,self.sc_x2 +1)
             
        if ch==3:
             self.sc_x3 -=0.1
             self.graphicsView_3.setXRange(self.sc_x3,self.sc_x3 +1)

    ########################## Scrollling on y axis ######################
    
    def scrollU(self,ch):
        if ch==1:
            self.sc_y1 +=0.1
            self.graphicsView.setYRange(self.sc_y1,self.sc_y1 +1)
             
        if ch==2:
             self.sc_y2 +=0.1
             self.graphicsView_2.setYRange(self.sc_y2,self.sc_y2 +1)
             
        if ch==3:
              self.sc_y3 +=0.1
              self.graphicsView_3.setYRange(self.sc_y3,self.sc_y3 +1)


    def scrollD(self,ch):
        if ch==1:
            self.sc_y1 -=0.1
            self.graphicsView.setYRange(self.sc_y1,self.sc_y1 +1)
             
        if ch==2:
             self.sc_y2 -=0.1
             self.graphicsView_2.setYRange(self.sc_y2,self.sc_y2 +1)
             
        if ch==3:
             self.sc_y3 -=0.1
             self.graphicsView_3.setYRange(self.sc_y3,self.sc_y3 +1)













if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
