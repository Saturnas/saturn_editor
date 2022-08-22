from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PIL import Image
import pilgram
import pilgram.css
import pilgram.css.blending
import os
import pyautogui

import cv2
import numpy as np

###########size constraint that program would not become bigger than screen
width, height = pyautogui.size()
###########################################################################


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 846)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("background-color: rgb(35,38,45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(9, 9, 9, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
        self.header.setMaximumSize(QtCore.QSize(width, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.header.setPalette(palette)
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_left_side_frame = QtWidgets.QFrame(self.header)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)

        #################################Names for pictures
        self.image = QPixmap()
        self.image2 = ''
        self.give_name = ''


        self.header_left_side_frame.setPalette(palette)
        self.header_left_side_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_left_side_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_left_side_frame.setObjectName("header_left_side_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.header_left_side_frame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(774, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 2, 1, 1)
        self.tools_labe = QtWidgets.QLabel(self.header_left_side_frame)
        self.tools_labe.setStyleSheet("color: rgb(255, 255, 255);")
        self.tools_labe.setAlignment(QtCore.Qt.AlignCenter)
        self.tools_labe.setObjectName("tools_labe")
        self.gridLayout_4.addWidget(self.tools_labe, 1, 0, 1, 1)
        self.tools = QtWidgets.QPushButton(self.header_left_side_frame)
        self.tools.setMinimumSize(QtCore.QSize(30, 33))
        self.tools.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tools.setIcon(icon)
        self.tools.setIconSize(QtCore.QSize(45, 35))
        self.tools.setCheckable(True)
        self.tools.setFlat(True)
        self.tools.setObjectName("tools")
        self.gridLayout_4.addWidget(self.tools, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.header_left_side_frame)
        self.header_right_side_frame = QtWidgets.QFrame(self.header)
        self.header_right_side_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_right_side_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_right_side_frame.setObjectName("header_right_side_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.header_right_side_frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.open_file = QtWidgets.QPushButton(self.header_right_side_frame,  clicked= lambda: self.openImage())
        self.open_file.setMinimumSize(QtCore.QSize(30, 30))
        self.open_file.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/4682752.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file.setIcon(icon1)
        self.open_file.setIconSize(QtCore.QSize(42, 48))
        self.open_file.setFlat(True)
        self.open_file.setObjectName("open_file")
        self.gridLayout.addWidget(self.open_file, 0, 0, 1, 1)
        self.save_file = QtWidgets.QPushButton(self.header_right_side_frame, clicked= lambda: self.saveImage())
        self.save_file.setMinimumSize(QtCore.QSize(30, 30))
        self.save_file.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.save_file.setIcon(icon2)
        self.save_file.setIconSize(QtCore.QSize(42, 38))
        self.save_file.setFlat(True)
        self.save_file.setObjectName("save_file")
        self.gridLayout.addWidget(self.save_file, 0, 1, 1, 1)
        self.openfile_label = QtWidgets.QLabel(self.header_right_side_frame)
        self.openfile_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.openfile_label.setAlignment(QtCore.Qt.AlignCenter)
        self.openfile_label.setObjectName("openfile_label")
        self.gridLayout.addWidget(self.openfile_label, 1, 0, 1, 1)
        self.print = QtWidgets.QPushButton(self.header_right_side_frame, clicked= lambda: self.printImage())
        self.print.setMinimumSize(QtCore.QSize(38, 38))
        self.print.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/print2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.print.setIcon(icon3)
        self.print.setIconSize(QtCore.QSize(48, 38))
        self.print.setFlat(True)
        self.print.setObjectName("print")
        self.gridLayout.addWidget(self.print, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.header_right_side_frame)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.save_file_label = QtWidgets.QLabel(self.header_right_side_frame)
        self.save_file_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.save_file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.save_file_label.setObjectName("save_file_label")
        self.gridLayout.addWidget(self.save_file_label, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.header_right_side_frame)
        self.verticalLayout.addWidget(self.header)
        self.body_frame = QtWidgets.QFrame(self.centralwidget)
        self.body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_frame.setObjectName("body_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tools_frame = QtWidgets.QFrame(self.body_frame)
        self.tools_frame.setMaximumSize(QtCore.QSize(500, height))
        self.tools_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tools_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tools_frame.setObjectName("tools_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tools_frame)
        self.horizontalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.filters_frame = QtWidgets.QFrame(self.tools_frame)
        self.filters_frame.setMinimumSize(QtCore.QSize(60, 0))
        self.filters_frame.setMaximumSize(QtCore.QSize(50, height))
        self.filters_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filters_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filters_frame.setObjectName("filters_frame")
        #######################Tool frame invisible
        self.filters_frame.setVisible(False)
        #######################################
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.filters_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.filters_label = QtWidgets.QLabel(self.filters_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.filters_label.setFont(font)
        self.filters_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.filters_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filters_label.setObjectName("filters_label")
        self.verticalLayout_5.addWidget(self.filters_label)
        self.line_2 = QtWidgets.QFrame(self.filters_frame)
        self.line_2.setLineWidth(5)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.instagram_filter = QtWidgets.QPushButton(self.filters_frame)
        self.instagram_filter.setMinimumSize(QtCore.QSize(40, 40))
        self.instagram_filter.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/insta2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.instagram_filter.setIcon(icon4)
        self.instagram_filter.setIconSize(QtCore.QSize(40, 40))
        self.instagram_filter.setCheckable(True)
        self.instagram_filter.setFlat(True)
        self.instagram_filter.setObjectName("instagram_filter")
        self.verticalLayout_5.addWidget(self.instagram_filter)
        self.instagram_label = QtWidgets.QLabel(self.filters_frame)
        self.instagram_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.instagram_label.setAlignment(QtCore.Qt.AlignCenter)
        self.instagram_label.setObjectName("instagram_label")
        self.verticalLayout_5.addWidget(self.instagram_label)
        self.css_filter = QtWidgets.QPushButton(self.filters_frame)
        self.css_filter.setMinimumSize(QtCore.QSize(40, 40))
        self.css_filter.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/css.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.css_filter.setIcon(icon5)
        self.css_filter.setIconSize(QtCore.QSize(40, 40))
        self.css_filter.setCheckable(True)
        self.css_filter.setFlat(True)
        self.css_filter.setObjectName("css_filter")
        self.verticalLayout_5.addWidget(self.css_filter)
        self.css_label = QtWidgets.QLabel(self.filters_frame)
        self.css_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.css_label.setAlignment(QtCore.Qt.AlignCenter)
        self.css_label.setObjectName("css_label")
        self.verticalLayout_5.addWidget(self.css_label)
        self.blender_filter = QtWidgets.QPushButton(self.filters_frame)
        self.blender_filter.setMinimumSize(QtCore.QSize(40, 40))
        self.blender_filter.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/blender.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.blender_filter.setIcon(icon6)
        self.blender_filter.setIconSize(QtCore.QSize(60, 50))
        self.blender_filter.setCheckable(True)
        self.blender_filter.setFlat(True)
        self.blender_filter.setObjectName("blender_filter")
        self.verticalLayout_5.addWidget(self.blender_filter)
        self.blender_label = QtWidgets.QLabel(self.filters_frame)
        self.blender_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.blender_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blender_label.setObjectName("blender_label")
        self.verticalLayout_5.addWidget(self.blender_label)
        self.line = QtWidgets.QFrame(self.filters_frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.edit_image = QtWidgets.QPushButton(self.filters_frame)
        self.edit_image.setMinimumSize(QtCore.QSize(40, 40))
        self.edit_image.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.edit_image.setIcon(icon7)
        self.edit_image.setIconSize(QtCore.QSize(40, 40))
        self.edit_image.setCheckable(True)
        self.edit_image.setFlat(True)
        self.edit_image.setObjectName("edit_image")
        self.verticalLayout_5.addWidget(self.edit_image)
        self.edit_image_label = QtWidgets.QLabel(self.filters_frame)
        self.edit_image_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.edit_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_image_label.setObjectName("edit_image_label")
        self.verticalLayout_5.addWidget(self.edit_image_label)
        self.line_3 = QtWidgets.QFrame(self.filters_frame)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        self.undo_btn = QtWidgets.QPushButton(self.filters_frame, clicked= lambda: self.undoImage())
        self.undo_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.undo_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.undo_btn.setIcon(icon8)
        self.undo_btn.setIconSize(QtCore.QSize(40, 40))
        self.undo_btn.setFlat(True)
        self.undo_btn.setObjectName("undo_btn")
        self.verticalLayout_5.addWidget(self.undo_btn)
        self.undo_label = QtWidgets.QLabel(self.filters_frame)
        self.undo_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.undo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.undo_label.setObjectName("undo_label")
        self.verticalLayout_5.addWidget(self.undo_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_4.addWidget(self.filters_frame)
        self.edit_image_frame = QtWidgets.QFrame(self.tools_frame)
        self.edit_image_frame.setMinimumSize(QtCore.QSize(75, 0))
        self.edit_image_frame.setMaximumSize(QtCore.QSize(50, height))
        self.edit_image_frame.setStyleSheet("color: rgb(255, 255, 255);")
        self.edit_image_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.edit_image_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.edit_image_frame.setObjectName("edit_image_frame")
        ######################################Set invisible from start
        self.edit_image_frame.setVisible(False)
        #######################################
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.edit_image_frame)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rotate_90_btn = QtWidgets.QPushButton(self.edit_image_frame, clicked= lambda: self.rotateImage90())
        self.rotate_90_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/rotate.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.rotate_90_btn.setIcon(icon9)
        self.rotate_90_btn.setIconSize(QtCore.QSize(40, 40))
        self.rotate_90_btn.setFlat(True)
        self.rotate_90_btn.setObjectName("rotate_90_btn")
        self.verticalLayout_2.addWidget(self.rotate_90_btn)
        self.rotate_90_label = QtWidgets.QLabel(self.edit_image_frame)
        self.rotate_90_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rotate_90_label.setObjectName("rotate_90_label")
        self.verticalLayout_2.addWidget(self.rotate_90_label)
        self.rotate_180_btn = QtWidgets.QPushButton(self.edit_image_frame, clicked= lambda: self.rotateImage180())
        self.rotate_180_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/rotate180.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.rotate_180_btn.setIcon(icon10)
        self.rotate_180_btn.setIconSize(QtCore.QSize(40, 40))
        self.rotate_180_btn.setFlat(True)
        self.rotate_180_btn.setObjectName("rotate_180_btn")
        self.verticalLayout_2.addWidget(self.rotate_180_btn)
        self.rotate_180_label = QtWidgets.QLabel(self.edit_image_frame)
        self.rotate_180_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rotate_180_label.setObjectName("rotate_180_label")
        self.verticalLayout_2.addWidget(self.rotate_180_label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.flip_horizontal_btn = QtWidgets.QPushButton(self.edit_image_frame,  clicked= lambda: self.flipImageHorizontal())
        self.flip_horizontal_btn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/flip_horizontal.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.flip_horizontal_btn.setIcon(icon11)
        self.flip_horizontal_btn.setIconSize(QtCore.QSize(40, 40))
        self.flip_horizontal_btn.setFlat(True)
        self.flip_horizontal_btn.setObjectName("flip_horizontal_btn")
        self.verticalLayout_2.addWidget(self.flip_horizontal_btn)
        self.flip_horizontal_label = QtWidgets.QLabel(self.edit_image_frame)
        self.flip_horizontal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flip_horizontal_label.setObjectName("flip_horizontal_label")
        self.verticalLayout_2.addWidget(self.flip_horizontal_label)
        self.flip_vertical_btn = QtWidgets.QPushButton(self.edit_image_frame,  clicked= lambda: self.flipImageVertical())
        self.flip_vertical_btn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/newPrefix/flip_vertical.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.flip_vertical_btn.setIcon(icon12)
        self.flip_vertical_btn.setIconSize(QtCore.QSize(40, 40))
        self.flip_vertical_btn.setFlat(True)
        self.flip_vertical_btn.setObjectName("flip_vertical_btn")
        self.verticalLayout_2.addWidget(self.flip_vertical_btn)
        self.flip_vertical_label = QtWidgets.QLabel(self.edit_image_frame)
        self.flip_vertical_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flip_vertical_label.setObjectName("flip_vertical_label")
        self.verticalLayout_2.addWidget(self.flip_vertical_label)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.cartoon_btn = QtWidgets.QPushButton(self.edit_image_frame, clicked= lambda: self.make_cartoon())
        self.cartoon_btn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/newPrefix/cartoon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cartoon_btn.setIcon(icon13)
        self.cartoon_btn.setIconSize(QtCore.QSize(40, 40))
        self.cartoon_btn.setFlat(True)
        self.cartoon_btn.setObjectName("cartoon_btn")
        self.verticalLayout_2.addWidget(self.cartoon_btn)
        self.cartoon_label = QtWidgets.QLabel(self.edit_image_frame)
        self.cartoon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cartoon_label.setObjectName("cartoon_label")
        self.verticalLayout_2.addWidget(self.cartoon_label)
        self.resize_half_btn = QtWidgets.QPushButton(self.edit_image_frame,  clicked= lambda: self.resizeImageHalf())
        self.resize_half_btn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/newPrefix/blur.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.resize_half_btn.setIcon(icon14)
        self.resize_half_btn.setIconSize(QtCore.QSize(40, 40))
        self.resize_half_btn.setFlat(True)
        self.resize_half_btn.setObjectName("resize_half_btn")
        self.verticalLayout_2.addWidget(self.resize_half_btn)
        self.label_46 = QtWidgets.QLabel(self.edit_image_frame)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_2.addWidget(self.label_46)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_4.addWidget(self.edit_image_frame)
        self.css_filter_frame = QtWidgets.QFrame(self.tools_frame)
        self.css_filter_frame.setMinimumSize(QtCore.QSize(82, 0))
        self.css_filter_frame.setMaximumSize(QtCore.QSize(50, height))
        self.css_filter_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.css_filter_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.css_filter_frame.setObjectName("css_filter_frame")
        ###################################set invisible from beginning
        self.css_filter_frame.setVisible(False)
        ########################################
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.css_filter_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.contrast_filter = QtWidgets.QPushButton(self.css_filter_frame, clicked= lambda: self.contrast_filter_x())
        self.contrast_filter.setMinimumSize(QtCore.QSize(80, 80))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/contrast.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.contrast_filter.setIcon(icon15)
        self.contrast_filter.setIconSize(QtCore.QSize(80, 80))
        self.contrast_filter.setObjectName("contrast_filter")
        self.verticalLayout_4.addWidget(self.contrast_filter)
        self.contrast_label = QtWidgets.QLabel(self.css_filter_frame)
        self.contrast_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.contrast_label.setAlignment(QtCore.Qt.AlignCenter)
        self.contrast_label.setObjectName("contrast_label")
        self.verticalLayout_4.addWidget(self.contrast_label)
        self.grayscale_filter = QtWidgets.QPushButton(self.css_filter_frame, clicked= lambda: self.grayscale_filter_x())
        self.grayscale_filter.setMinimumSize(QtCore.QSize(80, 80))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/grayscale.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.grayscale_filter.setIcon(icon16)
        self.grayscale_filter.setIconSize(QtCore.QSize(80, 80))
        self.grayscale_filter.setObjectName("grayscale_filter")
        self.verticalLayout_4.addWidget(self.grayscale_filter)
        self.grayscale_label = QtWidgets.QLabel(self.css_filter_frame)
        self.grayscale_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.grayscale_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grayscale_label.setObjectName("grayscale_label")
        self.verticalLayout_4.addWidget(self.grayscale_label)
        self.hue_rotate_filter = QtWidgets.QPushButton(self.css_filter_frame, clicked= lambda: self.hue_rotate_filter_x())
        self.hue_rotate_filter.setMinimumSize(QtCore.QSize(80, 80))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/hue_rotate.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.hue_rotate_filter.setIcon(icon17)
        self.hue_rotate_filter.setIconSize(QtCore.QSize(80, 80))
        self.hue_rotate_filter.setObjectName("hue_rotate_filter")
        self.verticalLayout_4.addWidget(self.hue_rotate_filter)
        self.hue_rotate_label = QtWidgets.QLabel(self.css_filter_frame)
        self.hue_rotate_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.hue_rotate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hue_rotate_label.setObjectName("hue_rotate_label")
        self.verticalLayout_4.addWidget(self.hue_rotate_label)
        self.saturate_filter = QtWidgets.QPushButton(self.css_filter_frame, clicked= lambda: self.saturate_filter_x())
        self.saturate_filter.setMinimumSize(QtCore.QSize(80, 80))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/saturate.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.saturate_filter.setIcon(icon18)
        self.saturate_filter.setIconSize(QtCore.QSize(80, 80))
        self.saturate_filter.setObjectName("saturate_filter")
        self.verticalLayout_4.addWidget(self.saturate_filter)
        self.saturate_label = QtWidgets.QLabel(self.css_filter_frame)
        self.saturate_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.saturate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.saturate_label.setObjectName("saturate_label")
        self.verticalLayout_4.addWidget(self.saturate_label)
        self.sepia_filter = QtWidgets.QPushButton(self.css_filter_frame, clicked= lambda: self.sepia_filter_x())
        self.sepia_filter.setMinimumSize(QtCore.QSize(80, 80))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/sepia.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.sepia_filter.setIcon(icon19)
        self.sepia_filter.setIconSize(QtCore.QSize(80, 80))
        self.sepia_filter.setObjectName("sepia_filter")
        self.verticalLayout_4.addWidget(self.sepia_filter)
        self.sepia_label = QtWidgets.QLabel(self.css_filter_frame)
        self.sepia_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.sepia_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sepia_label.setObjectName("sepia_label")
        self.verticalLayout_4.addWidget(self.sepia_label)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_4.addWidget(self.css_filter_frame)
        self.blender_filte_frame = QtWidgets.QFrame(self.tools_frame)
        self.blender_filte_frame.setMinimumSize(QtCore.QSize(115, 0))
        self.blender_filte_frame.setMaximumSize(QtCore.QSize(50, height))
        self.blender_filte_frame.setStyleSheet("color: rgb(255, 255, 255);")
        self.blender_filte_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.blender_filte_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.blender_filte_frame.setObjectName("blender_filte_frame")
        #####################################set invisible from start
        self.blender_filte_frame.setVisible(False)
        ###############################################
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.blender_filte_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.blender_filte_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(110, 0))
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 98, 1521))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.color_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.color_filter_x())
        self.color_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.color_btn.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/color.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.color_btn.setIcon(icon20)
        self.color_btn.setIconSize(QtCore.QSize(80, 80))
        self.color_btn.setObjectName("color_btn")
        self.verticalLayout_6.addWidget(self.color_btn)
        self.color_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.color_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_label.setObjectName("color_label")
        self.verticalLayout_6.addWidget(self.color_label)
        self.color_burn_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.color_burn_filter_x())
        self.color_burn_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.color_burn_btn.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/color_burn.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.color_burn_btn.setIcon(icon21)
        self.color_burn_btn.setIconSize(QtCore.QSize(80, 80))
        self.color_burn_btn.setObjectName("color_burn_btn")
        self.verticalLayout_6.addWidget(self.color_burn_btn)
        self.color_burn_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.color_burn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_burn_label.setObjectName("color_burn_label")
        self.verticalLayout_6.addWidget(self.color_burn_label)
        self.color_dodge_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.color_dodge_filter_x())
        self.color_dodge_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.color_dodge_btn.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/color_dodge.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.color_dodge_btn.setIcon(icon22)
        self.color_dodge_btn.setIconSize(QtCore.QSize(80, 80))
        self.color_dodge_btn.setObjectName("color_dodge_btn")
        self.verticalLayout_6.addWidget(self.color_dodge_btn)
        self.color_dodge_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.color_dodge_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_dodge_label.setObjectName("color_dodge_label")
        self.verticalLayout_6.addWidget(self.color_dodge_label)
        self.darken_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.darken_filter_x())
        self.darken_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.darken_btn.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/darken.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.darken_btn.setIcon(icon23)
        self.darken_btn.setIconSize(QtCore.QSize(80, 80))
        self.darken_btn.setObjectName("darken_btn")
        self.verticalLayout_6.addWidget(self.darken_btn)
        self.darken_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.darken_label.setAlignment(QtCore.Qt.AlignCenter)
        self.darken_label.setObjectName("darken_label")
        self.verticalLayout_6.addWidget(self.darken_label)
        self.difference_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.difference_filter_x())
        self.difference_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.difference_btn.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/difference.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.difference_btn.setIcon(icon24)
        self.difference_btn.setIconSize(QtCore.QSize(80, 80))
        self.difference_btn.setObjectName("difference_btn")
        self.verticalLayout_6.addWidget(self.difference_btn)
        self.difference_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.difference_label.setAlignment(QtCore.Qt.AlignCenter)
        self.difference_label.setObjectName("difference_label")
        self.verticalLayout_6.addWidget(self.difference_label)
        self.exclusio_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.exclusion_filter_x())
        self.exclusio_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.exclusio_btn.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/exclusion.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exclusio_btn.setIcon(icon25)
        self.exclusio_btn.setIconSize(QtCore.QSize(80, 80))
        self.exclusio_btn.setObjectName("exclusio_btn")
        self.verticalLayout_6.addWidget(self.exclusio_btn)
        self.exclusion_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.exclusion_label.setAlignment(QtCore.Qt.AlignCenter)
        self.exclusion_label.setObjectName("exclusion_label")
        self.verticalLayout_6.addWidget(self.exclusion_label)
        self.hard_light_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.hard_light_filter_x())
        self.hard_light_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.hard_light_btn.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/hard_light.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.hard_light_btn.setIcon(icon26)
        self.hard_light_btn.setIconSize(QtCore.QSize(80, 80))
        self.hard_light_btn.setObjectName("hard_light_btn")
        self.verticalLayout_6.addWidget(self.hard_light_btn)
        self.hard_light_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.hard_light_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hard_light_label.setObjectName("hard_light_label")
        self.verticalLayout_6.addWidget(self.hard_light_label)
        self.hue_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.hue_filter_x())
        self.hue_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.hue_btn.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/hue.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.hue_btn.setIcon(icon27)
        self.hue_btn.setIconSize(QtCore.QSize(80, 80))
        self.hue_btn.setObjectName("hue_btn")
        self.verticalLayout_6.addWidget(self.hue_btn)
        self.hue_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.hue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hue_label.setObjectName("hue_label")
        self.verticalLayout_6.addWidget(self.hue_label)
        self.lighten_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.lighten_filter_x())
        self.lighten_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.lighten_btn.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/lighten.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.lighten_btn.setIcon(icon28)
        self.lighten_btn.setIconSize(QtCore.QSize(80, 80))
        self.lighten_btn.setObjectName("lighten_btn")
        self.verticalLayout_6.addWidget(self.lighten_btn)
        self.lighten_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lighten_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lighten_label.setObjectName("lighten_label")
        self.verticalLayout_6.addWidget(self.lighten_label)
        self.multiply_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.multiply_filter_x())
        self.multiply_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.multiply_btn.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/multiply.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.multiply_btn.setIcon(icon29)
        self.multiply_btn.setIconSize(QtCore.QSize(80, 80))
        self.multiply_btn.setObjectName("multiply_btn")
        self.verticalLayout_6.addWidget(self.multiply_btn)
        self.multiply_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.multiply_label.setAlignment(QtCore.Qt.AlignCenter)
        self.multiply_label.setObjectName("multiply_label")
        self.verticalLayout_6.addWidget(self.multiply_label)
        self.normal_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.normal_filter_x())
        self.normal_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.normal_btn.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/normal.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.normal_btn.setIcon(icon30)
        self.normal_btn.setIconSize(QtCore.QSize(80, 80))
        self.normal_btn.setObjectName("normal_btn")
        self.verticalLayout_6.addWidget(self.normal_btn)
        self.normal_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.normal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.normal_label.setObjectName("normal_label")
        self.verticalLayout_6.addWidget(self.normal_label)
        self.overlay_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.overlay_filter_x())
        self.overlay_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.overlay_btn.setText("")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/overlay.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.overlay_btn.setIcon(icon31)
        self.overlay_btn.setIconSize(QtCore.QSize(80, 80))
        self.overlay_btn.setObjectName("overlay_btn")
        self.verticalLayout_6.addWidget(self.overlay_btn)
        self.ovelay_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ovelay_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ovelay_label.setObjectName("ovelay_label")
        self.verticalLayout_6.addWidget(self.ovelay_label)
        self.screen_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.screen_filter_x())
        self.screen_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.screen_btn.setText("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/screen.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.screen_btn.setIcon(icon32)
        self.screen_btn.setIconSize(QtCore.QSize(80, 80))
        self.screen_btn.setObjectName("screen_btn")
        self.verticalLayout_6.addWidget(self.screen_btn)
        self.screen_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.screen_label.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_label.setObjectName("screen_label")
        self.verticalLayout_6.addWidget(self.screen_label)
        self.soft_light_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2, clicked= lambda: self.soft_light_filter_x())
        self.soft_light_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.soft_light_btn.setText("")
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/blender/soft_light.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.soft_light_btn.setIcon(icon33)
        self.soft_light_btn.setIconSize(QtCore.QSize(80, 80))
        self.soft_light_btn.setObjectName("soft_light_btn")
        self.verticalLayout_6.addWidget(self.soft_light_btn)
        self.soft_light_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.soft_light_label.setAlignment(QtCore.Qt.AlignCenter)
        self.soft_light_label.setObjectName("soft_light_label")
        self.verticalLayout_6.addWidget(self.soft_light_label)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.horizontalLayout_4.addWidget(self.blender_filte_frame)
        self.instagram_filters_frame = QtWidgets.QFrame(self.tools_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instagram_filters_frame.sizePolicy().hasHeightForWidth())
        self.instagram_filters_frame.setSizePolicy(sizePolicy)
        self.instagram_filters_frame.setMinimumSize(QtCore.QSize(205, 0))
        self.instagram_filters_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.instagram_filters_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.instagram_filters_frame.setObjectName("instagram_filters_frame")
        ############################################set invisible from start
        self.instagram_filters_frame.setVisible(False)
        #######################################
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.instagram_filters_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.instagram_filters_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("color: rgb(255, 255, 255);")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 184, 1377))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.aden_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.aden_label.setAlignment(QtCore.Qt.AlignCenter)
        self.aden_label.setObjectName("aden_label")
        self.gridLayout_2.addWidget(self.aden_label, 1, 1, 1, 1)
        self.brooklyn_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.brooklyn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.brooklyn_label.setObjectName("brooklyn_label")
        self.gridLayout_2.addWidget(self.brooklyn_label, 3, 1, 1, 1)
        self.earlybird_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.earlybird_filter_x())
        self.earlybird_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/earlybird.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.earlybird_btn.setIcon(icon34)
        self.earlybird_btn.setIconSize(QtCore.QSize(80, 80))
        self.earlybird_btn.setObjectName("earlybird_btn")
        self.gridLayout_2.addWidget(self.earlybird_btn, 4, 1, 1, 1)
        self.clarendon_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.clarendon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.clarendon_label.setObjectName("clarendon_label")
        self.gridLayout_2.addWidget(self.clarendon_label, 5, 0, 1, 1)
        self.earlybird_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.earlybird_label.setAlignment(QtCore.Qt.AlignCenter)
        self.earlybird_label.setObjectName("earlybird_label")
        self.gridLayout_2.addWidget(self.earlybird_label, 5, 1, 1, 1)
        self.inkwell_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.inkwell_filter_x())
        self.inkwell_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/inkwell.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.inkwell_btn.setIcon(icon35)
        self.inkwell_btn.setIconSize(QtCore.QSize(80, 80))
        self.inkwell_btn.setObjectName("inkwell_btn")
        self.gridLayout_2.addWidget(self.inkwell_btn, 8, 0, 1, 1)
        self.inkwell_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.inkwell_label.setAlignment(QtCore.Qt.AlignCenter)
        self.inkwell_label.setObjectName("inkwell_label")
        self.gridLayout_2.addWidget(self.inkwell_label, 9, 0, 1, 1)
        self.aden_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.aden_filter_x())
        self.aden_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/aden.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aden_btn.setIcon(icon36)
        self.aden_btn.setIconSize(QtCore.QSize(80, 80))
        self.aden_btn.setObjectName("aden_btn")
        self.gridLayout_2.addWidget(self.aden_btn, 0, 1, 1, 1)
        self.gingham_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.gingham_filter_x())
        self.gingham_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/gingham.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.gingham_btn.setIcon(icon37)
        self.gingham_btn.setIconSize(QtCore.QSize(80, 80))
        self.gingham_btn.setObjectName("gingham_btn")
        self.gridLayout_2.addWidget(self.gingham_btn, 6, 0, 1, 1)
        self.hudson_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.hudson_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hudson_label.setObjectName("hudson_label")
        self.gridLayout_2.addWidget(self.hudson_label, 7, 1, 1, 1)
        self.kelvin_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.kelvin_filter_x())
        self.kelvin_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/kelvin.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.kelvin_btn.setIcon(icon38)
        self.kelvin_btn.setIconSize(QtCore.QSize(80, 80))
        self.kelvin_btn.setObjectName("kelvin_btn")
        self.gridLayout_2.addWidget(self.kelvin_btn, 8, 1, 1, 1)
        self.brooklyn_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.brooklyn_filter_x())
        self.brooklyn_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/brooklyn.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.brooklyn_btn.setIcon(icon39)
        self.brooklyn_btn.setIconSize(QtCore.QSize(80, 80))
        self.brooklyn_btn.setObjectName("brooklyn_btn")
        self.gridLayout_2.addWidget(self.brooklyn_btn, 2, 1, 1, 1)
        self.hudson_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.hudson_filter_x())
        self.hudson_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/hudson.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.hudson_btn.setIcon(icon40)
        self.hudson_btn.setIconSize(QtCore.QSize(80, 80))
        self.hudson_btn.setObjectName("hudson_btn")
        self.gridLayout_2.addWidget(self.hudson_btn, 6, 1, 1, 1)
        self.brannan_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.brannan_filter_x())
        self.brannan_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/brannan.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.brannan_btn.setIcon(icon41)
        self.brannan_btn.setIconSize(QtCore.QSize(80, 80))
        self.brannan_btn.setObjectName("brannan_btn")
        self.gridLayout_2.addWidget(self.brannan_btn, 2, 0, 1, 1)
        self.kelvin_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.kelvin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.kelvin_label.setObjectName("kelvin_label")
        self.gridLayout_2.addWidget(self.kelvin_label, 9, 1, 1, 1)
        self.lark_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.lark_filter_x())
        self.lark_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/lark.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.lark_btn.setIcon(icon42)
        self.lark_btn.setIconSize(QtCore.QSize(80, 80))
        self.lark_btn.setObjectName("lark_btn")
        self.gridLayout_2.addWidget(self.lark_btn, 10, 0, 1, 1)
        self.gingham_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.gingham_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gingham_label.setObjectName("gingham_label")
        self.gridLayout_2.addWidget(self.gingham_label, 7, 0, 1, 1)
        self.clarendon_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.clarendon_filter_x())
        self.clarendon_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/clarendon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.clarendon_btn.setIcon(icon43)
        self.clarendon_btn.setIconSize(QtCore.QSize(80, 80))
        self.clarendon_btn.setObjectName("clarendon_btn")
        self.gridLayout_2.addWidget(self.clarendon_btn, 4, 0, 1, 1)
        self.label_1977 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_1977.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1977.setObjectName("label_1977")
        self.gridLayout_2.addWidget(self.label_1977, 1, 0, 1, 1)
        self.brannan_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.brannan_label.setAlignment(QtCore.Qt.AlignCenter)
        self.brannan_label.setObjectName("brannan_label")
        self.gridLayout_2.addWidget(self.brannan_label, 3, 0, 1, 1)
        self.button_1977 = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self._1977_filter_x())
        self.button_1977.setMinimumSize(QtCore.QSize(80, 80))
        self.button_1977.setText("")
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/_1977.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_1977.setIcon(icon44)
        self.button_1977.setIconSize(QtCore.QSize(80, 80))
        self.button_1977.setObjectName("button_1977")
        self.gridLayout_2.addWidget(self.button_1977, 0, 0, 1, 1)
        self.xpro2_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.xpro2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.xpro2_label.setObjectName("xpro2_label")
        self.gridLayout_2.addWidget(self.xpro2_label, 25, 1, 1, 1)
        self.lofi_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.lofi_filter_x())
        self.lofi_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/lofi.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.lofi_btn.setIcon(icon45)
        self.lofi_btn.setIconSize(QtCore.QSize(80, 80))
        self.lofi_btn.setObjectName("lofi_btn")
        self.gridLayout_2.addWidget(self.lofi_btn, 10, 1, 1, 1)
        self.lark_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lark_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lark_label.setObjectName("lark_label")
        self.gridLayout_2.addWidget(self.lark_label, 11, 0, 1, 1)
        self.mayfair_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.mayfair_filter_x())
        self.mayfair_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/mayfair.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.mayfair_btn.setIcon(icon46)
        self.mayfair_btn.setIconSize(QtCore.QSize(80, 80))
        self.mayfair_btn.setObjectName("mayfair_btn")
        self.gridLayout_2.addWidget(self.mayfair_btn, 12, 1, 1, 1)
        self.nashville_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.nashville_filter_x())
        self.nashville_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/nashville.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nashville_btn.setIcon(icon47)
        self.nashville_btn.setIconSize(QtCore.QSize(80, 80))
        self.nashville_btn.setObjectName("nashville_btn")
        self.gridLayout_2.addWidget(self.nashville_btn, 14, 1, 1, 1)
        self.slumber_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.slumber_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slumber_label.setObjectName("slumber_label")
        self.gridLayout_2.addWidget(self.slumber_label, 19, 1, 1, 1)
        self.moon_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.moon_filter_x())
        self.moon_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/moon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.moon_btn.setIcon(icon48)
        self.moon_btn.setIconSize(QtCore.QSize(80, 80))
        self.moon_btn.setObjectName("moon_btn")
        self.gridLayout_2.addWidget(self.moon_btn, 14, 0, 1, 1)
        self.reyes_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.reyes_filter_x())
        self.reyes_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/reyes.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.reyes_btn.setIcon(icon49)
        self.reyes_btn.setIconSize(QtCore.QSize(80, 80))
        self.reyes_btn.setObjectName("reyes_btn")
        self.gridLayout_2.addWidget(self.reyes_btn, 16, 1, 1, 1)
        self.rise_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.rise_filter_x())
        self.rise_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/rise.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.rise_btn.setIcon(icon50)
        self.rise_btn.setIconSize(QtCore.QSize(80, 80))
        self.rise_btn.setObjectName("rise_btn")
        self.gridLayout_2.addWidget(self.rise_btn, 18, 0, 1, 1)
        self.stinson_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.stinson_filter_x())
        self.stinson_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/stinson.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.stinson_btn.setIcon(icon51)
        self.stinson_btn.setIconSize(QtCore.QSize(80, 80))
        self.stinson_btn.setObjectName("stinson_btn")
        self.gridLayout_2.addWidget(self.stinson_btn, 20, 0, 1, 1)
        self.toaster_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.toaster_label.setAlignment(QtCore.Qt.AlignCenter)
        self.toaster_label.setObjectName("toaster_label")
        self.gridLayout_2.addWidget(self.toaster_label, 21, 1, 1, 1)
        self.valencia_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.valencia_label.setAlignment(QtCore.Qt.AlignCenter)
        self.valencia_label.setObjectName("valencia_label")
        self.gridLayout_2.addWidget(self.valencia_label, 23, 0, 1, 1)
        self.stinson_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.stinson_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stinson_label.setObjectName("stinson_label")
        self.gridLayout_2.addWidget(self.stinson_label, 21, 0, 1, 1)
        self.maven_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.maven_filter_x())
        self.maven_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/maven.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.maven_btn.setIcon(icon52)
        self.maven_btn.setIconSize(QtCore.QSize(80, 80))
        self.maven_btn.setObjectName("maven_btn")
        self.gridLayout_2.addWidget(self.maven_btn, 12, 0, 1, 1)
        self.walden_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.walden_label.setAlignment(QtCore.Qt.AlignCenter)
        self.walden_label.setObjectName("walden_label")
        self.gridLayout_2.addWidget(self.walden_label, 23, 1, 1, 1)
        self.xpro2_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.xpro2_filter_x())
        self.xpro2_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon53 = QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/xpro2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.xpro2_btn.setIcon(icon53)
        self.xpro2_btn.setIconSize(QtCore.QSize(80, 80))
        self.xpro2_btn.setObjectName("xpro2_btn")
        self.gridLayout_2.addWidget(self.xpro2_btn, 24, 1, 1, 1)
        self.nashville_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nashville_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nashville_label.setObjectName("nashville_label")
        self.gridLayout_2.addWidget(self.nashville_label, 15, 1, 1, 1)
        self.lofi_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lofi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lofi_label.setObjectName("lofi_label")
        self.gridLayout_2.addWidget(self.lofi_label, 11, 1, 1, 1)
        self.moon_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.moon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.moon_label.setObjectName("moon_label")
        self.gridLayout_2.addWidget(self.moon_label, 15, 0, 1, 1)
        self.perpetua_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.perpetua_label.setAlignment(QtCore.Qt.AlignCenter)
        self.perpetua_label.setObjectName("perpetua_label")
        self.gridLayout_2.addWidget(self.perpetua_label, 17, 0, 1, 1)
        self.slumber_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.slumber_filter_x())
        self.slumber_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/slumber.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.slumber_btn.setIcon(icon54)
        self.slumber_btn.setIconSize(QtCore.QSize(80, 80))
        self.slumber_btn.setObjectName("slumber_btn")
        self.gridLayout_2.addWidget(self.slumber_btn, 18, 1, 1, 1)
        self.walden_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.walden_filter_x())
        self.walden_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/walden.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.walden_btn.setIcon(icon55)
        self.walden_btn.setIconSize(QtCore.QSize(80, 80))
        self.walden_btn.setObjectName("walden_btn")
        self.gridLayout_2.addWidget(self.walden_btn, 22, 1, 1, 1)
        self.valencia_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.valencia_filter_x())
        self.valencia_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon56 = QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/valencia.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.valencia_btn.setIcon(icon56)
        self.valencia_btn.setIconSize(QtCore.QSize(80, 80))
        self.valencia_btn.setObjectName("valencia_btn")
        self.gridLayout_2.addWidget(self.valencia_btn, 22, 0, 1, 1)
        self.maven_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.maven_label.setAlignment(QtCore.Qt.AlignCenter)
        self.maven_label.setObjectName("maven_label")
        self.gridLayout_2.addWidget(self.maven_label, 13, 0, 1, 1)
        self.mayfair_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.mayfair_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mayfair_label.setObjectName("mayfair_label")
        self.gridLayout_2.addWidget(self.mayfair_label, 13, 1, 1, 1)
        self.perpetua_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.perpetua_filter_x())
        self.perpetua_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon57 = QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/perpetua.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.perpetua_btn.setIcon(icon57)
        self.perpetua_btn.setIconSize(QtCore.QSize(80, 80))
        self.perpetua_btn.setObjectName("perpetua_btn")
        self.gridLayout_2.addWidget(self.perpetua_btn, 16, 0, 1, 1)
        self.reyes_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.reyes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.reyes_label.setObjectName("reyes_label")
        self.gridLayout_2.addWidget(self.reyes_label, 17, 1, 1, 1)
        self.rise_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.rise_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rise_label.setObjectName("rise_label")
        self.gridLayout_2.addWidget(self.rise_label, 19, 0, 1, 1)
        self.toaster_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.toaster_filter_x())
        self.toaster_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon58 = QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/toaster.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toaster_btn.setIcon(icon58)
        self.toaster_btn.setIconSize(QtCore.QSize(80, 80))
        self.toaster_btn.setObjectName("toaster_btn")
        self.gridLayout_2.addWidget(self.toaster_btn, 20, 1, 1, 1)
        self.willow_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked= lambda: self.willow_filter_x())
        self.willow_btn.setMinimumSize(QtCore.QSize(80, 80))
        icon59 = QtGui.QIcon()
        icon59.addPixmap(QtGui.QPixmap(":/newPrefix/saturn/normal/willow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.willow_btn.setIcon(icon59)
        self.willow_btn.setIconSize(QtCore.QSize(80, 80))
        self.willow_btn.setObjectName("willow_btn")
        self.gridLayout_2.addWidget(self.willow_btn, 24, 0, 1, 1)
        self.willow_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.willow_label.setAlignment(QtCore.Qt.AlignCenter)
        self.willow_label.setObjectName("willow_label")
        self.gridLayout_2.addWidget(self.willow_label, 25, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.addWidget(self.scrollArea)
        self.horizontalLayout_4.addWidget(self.instagram_filters_frame)
        self.horizontalLayout_2.addWidget(self.tools_frame)
        self.pic_window_frame = QtWidgets.QFrame(self.body_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_window_frame.sizePolicy().hasHeightForWidth())
        self.pic_window_frame.setSizePolicy(sizePolicy)
        self.pic_window_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pic_window_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pic_window_frame.setObjectName("pic_window_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.pic_window_frame)
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.pic_window_frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        self.label.setStyleSheet("background-color: rgb(27,32,35);")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.pic_window_frame)
        self.verticalLayout.addWidget(self.body_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1019, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tools.toggled['bool'].connect(self.filters_frame.setVisible) # type: ignore

        ################if instagram checked, others are unchecked
        self.instagram_filter.toggled['bool'].connect(self.instagram_filters_frame.setVisible) # type: ignore
        self.instagram_filter.toggled.connect(lambda checked: self.css_filter.setChecked(False))
        self.instagram_filter.toggled.connect(lambda checked: self.blender_filter.setChecked(False))
        self.instagram_filter.toggled.connect(lambda checked: self.edit_image.setChecked(False))

        ####################if css checked, others are unchecked
        self.css_filter.toggled['bool'].connect(self.css_filter_frame.setVisible) # type: ignore
        self.css_filter.toggled.connect(lambda checked: self.instagram_filter.setChecked(False))
        self.css_filter.toggled.connect(lambda checked: self.blender_filter.setChecked(False))
        self.css_filter.toggled.connect(lambda checked: self.edit_image.setChecked(False))

        ####################if blender checked, others are unchecked
        self.blender_filter.toggled['bool'].connect(self.blender_filte_frame.setVisible) # type: ignore
        self.blender_filter.toggled.connect(lambda checked: self.instagram_filter.setChecked(False))
        self.blender_filter.toggled.connect(lambda checked: self.css_filter.setChecked(False))
        self.blender_filter.toggled.connect(lambda checked: self.edit_image.setChecked(False))

        ####################if edit image checked, others are unchecked
        self.edit_image.toggled['bool'].connect(self.edit_image_frame.setVisible) # type: ignore
        self.edit_image.toggled.connect(lambda checked: self.instagram_filter.setChecked(False))
        self.edit_image.toggled.connect(lambda checked: self.css_filter.setChecked(False))
        self.edit_image.toggled.connect(lambda checked: self.blender_filter.setChecked(False))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Saturn editor"))
        self.tools_labe.setText(_translate("MainWindow", "Tools"))
        self.openfile_label.setText(_translate("MainWindow", "Open file"))
        self.label_8.setText(_translate("MainWindow", "Print"))
        self.save_file_label.setText(_translate("MainWindow", "Save file"))
        self.filters_label.setText(_translate("MainWindow", "Filters"))
        self.instagram_label.setText(_translate("MainWindow", "Instagram"))
        self.css_label.setText(_translate("MainWindow", "Css"))
        self.blender_label.setText(_translate("MainWindow", "Blender"))
        self.edit_image_label.setText(_translate("MainWindow", "Edit image"))
        self.undo_label.setText(_translate("MainWindow", "Undo"))
        self.rotate_90_label.setText(_translate("MainWindow", "Rotate 90"))
        self.rotate_180_label.setText(_translate("MainWindow", "Rotate 180"))
        self.flip_horizontal_label.setText(_translate("MainWindow", "Flip Horizontal"))
        self.flip_vertical_label.setText(_translate("MainWindow", "Flip Vertical"))
        self.cartoon_label.setText(_translate("MainWindow", "Cartoon"))
        self.label_46.setText(_translate("MainWindow", "Blur"))
        self.contrast_label.setText(_translate("MainWindow", "contrast"))
        self.grayscale_label.setText(_translate("MainWindow", "grayscale"))
        self.hue_rotate_label.setText(_translate("MainWindow", "hue rotate"))
        self.saturate_label.setText(_translate("MainWindow", "saturate"))
        self.sepia_label.setText(_translate("MainWindow", "sepia"))
        self.color_label.setText(_translate("MainWindow", "color"))
        self.color_burn_label.setText(_translate("MainWindow", "color burn"))
        self.color_dodge_label.setText(_translate("MainWindow", "color dodge"))
        self.darken_label.setText(_translate("MainWindow", "darken"))
        self.difference_label.setText(_translate("MainWindow", "difference"))
        self.exclusion_label.setText(_translate("MainWindow", "exclusion"))
        self.hard_light_label.setText(_translate("MainWindow", "hard light\n"
"same size"))
        self.hue_label.setText(_translate("MainWindow", "hue"))
        self.lighten_label.setText(_translate("MainWindow", "lighten"))
        self.multiply_label.setText(_translate("MainWindow", "multiply"))
        self.normal_label.setText(_translate("MainWindow", "normal"))
        self.ovelay_label.setText(_translate("MainWindow", "overlay\n"
"same size"))
        self.screen_label.setText(_translate("MainWindow", "screen"))
        self.soft_light_label.setText(_translate("MainWindow", "soft light\n"
"same size"))
        self.aden_label.setText(_translate("MainWindow", "aden"))
        self.brooklyn_label.setText(_translate("MainWindow", "brooklyn"))
        self.clarendon_label.setText(_translate("MainWindow", "clarendon"))
        self.earlybird_label.setText(_translate("MainWindow", "earlybird"))
        self.inkwell_label.setText(_translate("MainWindow", "inkwell"))
        self.hudson_label.setText(_translate("MainWindow", "hudson"))
        self.kelvin_label.setText(_translate("MainWindow", "kelvin"))
        self.gingham_label.setText(_translate("MainWindow", "gingham"))
        self.label_1977.setText(_translate("MainWindow", "_1977"))
        self.brannan_label.setText(_translate("MainWindow", "brannan"))
        self.xpro2_label.setText(_translate("MainWindow", "xpro2"))
        self.lark_label.setText(_translate("MainWindow", "lark"))
        self.slumber_label.setText(_translate("MainWindow", "slumber"))
        self.toaster_label.setText(_translate("MainWindow", "toaster"))
        self.valencia_label.setText(_translate("MainWindow", "valencia"))
        self.stinson_label.setText(_translate("MainWindow", "stinson"))
        self.walden_label.setText(_translate("MainWindow", "walden"))
        self.nashville_label.setText(_translate("MainWindow", "nashville"))
        self.lofi_label.setText(_translate("MainWindow", "lofi"))
        self.moon_label.setText(_translate("MainWindow", "moon"))
        self.perpetua_label.setText(_translate("MainWindow", "perpetua"))
        self.maven_label.setText(_translate("MainWindow", "maven"))
        self.mayfair_label.setText(_translate("MainWindow", "mayfair"))
        self.reyes_label.setText(_translate("MainWindow", "reyes"))
        self.rise_label.setText(_translate("MainWindow", "rise"))
        self.willow_label.setText(_translate("MainWindow", "willow"))


    def openImage(self):
        image_file, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if image_file:

            self.image = QPixmap(image_file)
            self.give_name = image_file

            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
        else:
            QMessageBox.information(self, "No Image",
                "No Image Selected.",
                QMessageBox.StandardButton.Ok)


    def saveImage(self):
        image_file, _ = QFileDialog.getSaveFileName(
            self, 'Save Image', '',
            'JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files (*.bmp);;GIF Files (*.gif)')

        if image_file and self.image.isNull() == False:
            self.image.save(image_file)
        else:
            QMessageBox.information(self, "Not Saved",
                "Image not saved.",
                QMessageBox.StandardButton.Ok)

    def printImage(self):
        printer = QPrinter()
        print_dialog = QPrintDialog(printer)
        if print_dialog.exec() == QDialog.DialogCode.Accepted:
            painter = QPainter()
            painter.begin(printer)
            rect = QRect(painter.viewport())
            size = QSize(self.label.pixmap().size())
            size.scale(rect.size(), Qt.AspectRatioMode.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.label.pixmap().rect())
            painter.drawPixmap(0, 0, self.label.pixmap())
            painter.end()

    def undoImage(self):
        if self.image.isNull() == False:
            self.image = QPixmap(self.give_name)
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            self.image2 = ''

    def rotateImage90(self):
        """Rotate image 90º clockwise."""
        if self.image.isNull() == False:
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            rotated = pixmap.transformed(transform90, 
                mode=mode)

            self.label.setPixmap(rotated.scaled(self.label.size(), 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(rotated) 
            self.label.repaint() # Repaint the child widget

    def rotateImage180(self):
        """Rotate image 180º clockwise."""
        if self.image.isNull() == False:
            transform180 = QTransform().rotate(180)
            pixmap = QPixmap(self.image)
            rotated = pixmap.transformed(transform180, 
                mode=Qt.TransformationMode.SmoothTransformation)

            self.label.setPixmap(rotated.scaled(self.label.size(), 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation))
            # In order to keep from being allowed to rotate 
            # the image, set the rotated image as self.image 
            self.image = QPixmap(rotated) 
            self.label.repaint() # Repaint the child widget

    def flipImageHorizontal(self):
        """Mirror the image across the horizontal axis."""
        if self.image.isNull() == False:
            flip_h = QTransform().scale(-1, 1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_h)

            self.label.setPixmap(flipped.scaled(self.label.size(), 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.label.repaint()

    def flipImageVertical(self):
        """Mirror the image across the vertical axis."""
        if self.image.isNull() == False:
            flip_v = QTransform().scale(1, -1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_v)

            self.label.setPixmap(flipped.scaled(self.label.size(), 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.label.repaint()

    def resizeImageHalf(self):
        """Resize the image to half its current size."""
        
        if self.image.isNull() == False:
            resize = QTransform().scale(0.95, 0.95)
            pixmap = QPixmap(self.image)
            resized = pixmap.transformed(resize)

            self.label.setPixmap(resized.scaled(self.label.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.SmoothTransformation))
            self.image = QPixmap(resized)
            self.label.repaint()

    #######################################CSS filters
    def contrast_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.css.contrast(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def grayscale_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.css.grayscale(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def hue_rotate_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.css.hue_rotate(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def saturate_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.css.saturate(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def sepia_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.css.sepia(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    #####################################INSTAGRAM filters
    def _1977_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram._1977(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def aden_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.aden(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def brannan_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.brannan(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def brooklyn_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.brooklyn(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def clarendon_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.clarendon(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def earlybird_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.earlybird(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def gingham_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.gingham(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def hudson_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.hudson(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def inkwell_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.inkwell(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def kelvin_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.kelvin(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def lark_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.lark(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def lofi_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.lofi(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def maven_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.maven(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def mayfair_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.mayfair(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def moon_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.moon(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def nashville_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.nashville(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def perpetua_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.perpetua(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def reyes_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.reyes(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def rise_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.rise(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def slumber_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.slumber(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def stinson_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.stinson(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def toaster_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.toaster(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def valencia_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.valencia(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def walden_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.walden(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def willow_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.willow(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def xpro2_filter_x(self):
        if self.image.isNull() == False:
            im = Image.open(self.give_name)
            pilgram.xpro2(im).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])



    ####################################################BLENDER filters

    def color_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.color(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def color_burn_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.color_burn(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def color_dodge_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.color_dodge(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def darken_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.darken(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def difference_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.difference(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def exclusion_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.exclusion(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def hue_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.hue(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def lighten_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.lighten(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def multiply_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.multiply(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def normal_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            pilgram.css.blending.normal(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def screen_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)

            pilgram.css.blending.screen(im, im2).save('temp.' + self.give_name.split('.')[-1])
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])

    def hard_light_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            if im.size == im2.size:
                pilgram.css.blending.hard_light(im, im2).save('temp.' + self.give_name.split('.')[-1])
                self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
                self.label.setPixmap(
                    self.image.scaled(self.label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation))
                os.remove('temp.' + self.give_name.split('.')[-1])
            else:
                QMessageBox.information(self, "Wrong Size",
                "Images need to be same size",
                QMessageBox.StandardButton.Ok)
                self.image2 = ''

    def soft_light_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            if im.size == im2.size:
                pilgram.css.blending.soft_light(im, im2).save('temp.' + self.give_name.split('.')[-1])
                self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
                self.label.setPixmap(
                    self.image.scaled(self.label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation))
                os.remove('temp.' + self.give_name.split('.')[-1])
            else:
                QMessageBox.information(self, "Wrong Size",
                "Images need to be same size",
                QMessageBox.StandardButton.Ok)
                self.image2 = ''


    def overlay_filter_x(self):
        if self.image2 == '':
            self.image2, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files(*.bmp);;GIF Files (*.gif)")
        if self.image.isNull() == False and self.image2 != '':
            im = Image.open(self.give_name)
            im2 = Image.open(self.image2)
            if im.size == im2.size:
                pilgram.css.blending.overlay(im, im2).save('temp.' + self.give_name.split('.')[-1])
                self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
                self.label.setPixmap(
                    self.image.scaled(self.label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation))
                os.remove('temp.' + self.give_name.split('.')[-1])
            else:
                QMessageBox.information(self, "Wrong Size",
                "Images need to be same size",
                QMessageBox.StandardButton.Ok)
                self.image2 = ''

###########################################Cartoon
    def make_cartoon(self):
        if self.image.isNull() == False:
            img = cv2.imread(self.give_name)
            grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            grey = cv2.medianBlur(grey, 5)
            edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
            color = cv2.bilateralFilter(img, 7, 250, 250)
            cartoon = cv2.bitwise_and(color, color, mask = edges)
            cv2.imwrite('temp.' + self.give_name.split('.')[-1], cartoon)
            self.image = QPixmap('temp.' + self.give_name.split('.')[-1])
            self.label.setPixmap(
                self.image.scaled(self.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            os.remove('temp.' + self.give_name.split('.')[-1])
    

import fotoeditorius_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())