# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Programa1.ui'
# Created by: PyQt5 UI code generator 5.9.2

'''
Seminario de Sistemas Operativos - D02
    Actividad de Aprendizaje 2
Programa 1. Simular el Procesamiento por Lotes
Integrantes:
    Saul Alejandro Castañeda Perez
    Daniel Martinez Martinez
    
Thursday, February 8, 2023
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import re

#Variables Globales
Programadores=0
ContadorMinioms=0
Lotes = []
LotesTerminados=0
Pos_lote=0
ContadorGlobal=0
BanderaProcesos=True
BanderaID=False
BanderaNombre=False
BanderaOperacion=False
BanderaTME=False
mouse_click=0
grip=0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global grip
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 600))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_superior.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"border:2px solid rgb(225, 131, 0); \n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#000000ff;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"border-radius:20px;\n"
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BotonMenu = QtWidgets.QPushButton(self.frame_superior)
        self.BotonMenu.setMinimumSize(QtCore.QSize(200, 0))
        self.BotonMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonMenu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotonMenu.setIcon(icon)
        self.BotonMenu.setIconSize(QtCore.QSize(38, 38))
        self.BotonMenu.setObjectName("BotonMenu")
        self.horizontalLayout.addWidget(self.BotonMenu)
        spacerItem = QtWidgets.QSpacerItem(544, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.BotonMinimizar = QtWidgets.QPushButton(self.frame_superior)
        self.BotonMinimizar.setMinimumSize(QtCore.QSize(50, 40))
        self.BotonMinimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonMinimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagenes/minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotonMinimizar.setIcon(icon1)
        self.BotonMinimizar.setIconSize(QtCore.QSize(38, 38))
        self.BotonMinimizar.setObjectName("BotonMinimizar")
        self.horizontalLayout.addWidget(self.BotonMinimizar)
        self.BotonMaximizar = QtWidgets.QPushButton(self.frame_superior)
        self.BotonMaximizar.setMinimumSize(QtCore.QSize(50, 40))
        self.BotonMaximizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonMaximizar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagenes/maximizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotonMaximizar.setIcon(icon2)
        self.BotonMaximizar.setIconSize(QtCore.QSize(38, 38))
        self.BotonMaximizar.setObjectName("BotonMaximizar")
        self.horizontalLayout.addWidget(self.BotonMaximizar)
        self.BotonSalir = QtWidgets.QPushButton(self.frame_superior)
        self.BotonSalir.setMinimumSize(QtCore.QSize(50, 40))
        self.BotonSalir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonSalir.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Imagenes/exportar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotonSalir.setIcon(icon3)
        self.BotonSalir.setIconSize(QtCore.QSize(38, 38))
        self.BotonSalir.setObjectName("BotonSalir")
        self.horizontalLayout.addWidget(self.BotonSalir)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_contenido = QtWidgets.QFrame(self.frame)
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MenuDesplegable = QtWidgets.QFrame(self.frame_contenido)
        self.MenuDesplegable.setMinimumSize(QtCore.QSize(200, 0))
        self.MenuDesplegable.setMaximumSize(QtCore.QSize(0, 16777215))
        self.MenuDesplegable.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.034, y1:0.983364, x2:1, y2:0, stop:0.0795455 rgba(239, 187, 0, 248), stop:1 rgba(239, 99, 0, 255));\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"color:rgb(225, 131, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"}")
        self.MenuDesplegable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MenuDesplegable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MenuDesplegable.setObjectName("MenuDesplegable")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MenuDesplegable)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Asignar = QtWidgets.QPushButton(self.MenuDesplegable)
        self.Asignar.setMinimumSize(QtCore.QSize(135, 45))
        self.Asignar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Asignar.setObjectName("Asignar")
        self.verticalLayout.addWidget(self.Asignar)
        self.Registrar = QtWidgets.QPushButton(self.MenuDesplegable)
        self.Registrar.setMinimumSize(QtCore.QSize(135, 45))
        self.Registrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Registrar.setObjectName("Registrar")
        self.verticalLayout.addWidget(self.Registrar)
        self.Procesos = QtWidgets.QPushButton(self.MenuDesplegable)
        self.Procesos.setMinimumSize(QtCore.QSize(135, 45))
        self.Procesos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Procesos.setObjectName("Procesos")
        self.verticalLayout.addWidget(self.Procesos)
        spacerItem1 = QtWidgets.QSpacerItem(20, 191, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.Ocultar = QtWidgets.QPushButton(self.MenuDesplegable)
        self.Ocultar.setMinimumSize(QtCore.QSize(135, 45))
        self.Ocultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ocultar.setObjectName("Ocultar")
        self.verticalLayout.addWidget(self.Ocultar)
        self.horizontalLayout_2.addWidget(self.MenuDesplegable)
        self.Contenido = QtWidgets.QFrame(self.frame_contenido)
        self.Contenido.setStyleSheet("")
        self.Contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Contenido.setObjectName("Contenido")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Contenido)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Contenido)
        self.stackedWidget.setStyleSheet("QFrame{\n"
"background-color: rgb(0,0, 0);\n"
"}\n"
"\n"
"QLabel{\n"
"background-color:rgb(0,0, 0);\n"
"font: 77 16pt \"Arial Black\";\n"
"color:rgb(225, 131, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:0px;\n"
"font: 77 12pt \"Arial Black\";\n"
"color:rgb(225,225,225);\n"
"border-bottom:2px solid rgb(225, 131, 0); \n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(0,0, 0);\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"border:2px solid#ff8300;\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:20px;\n"
"color:rgb(225, 131, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"border:2px solid#ffffff;\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0, 0);\n"
"gridline-color:rgb(225, 131, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"border:0px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color:rgb(0,0, 0);\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"border:2px solid rgb(225, 131, 0);\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color:rgb(0,0,0);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_Asignar = QtWidgets.QWidget()
        self.page_Asignar.setObjectName("page_Asignar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_Asignar)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 103, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.page_Asignar)
        self.label_2.setStyleSheet("font: 77 20pt \"Arial Black\";")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_Asignar)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 35))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 40))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_Asignar)
        self.pushButton_2.setMinimumSize(QtCore.QSize(135, 45))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 104, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.stackedWidget.addWidget(self.page_Asignar)
        self.page_Registrar = QtWidgets.QWidget()
        self.page_Registrar.setObjectName("page_Registrar")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_Registrar)
        self.verticalLayout_7.setSpacing(25)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.label_7 = QtWidgets.QLabel(self.page_Registrar)
        self.label_7.setStyleSheet("font: 77 20pt \"Arial Black\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.page_Registrar)
        self.label_3.setMinimumSize(QtCore.QSize(0, 35))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.page_Registrar)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.page_Registrar)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.page_Registrar)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_Registrar)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(200, 35))
        self.lineEdit_3.setMaxLength(5)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_6.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_Registrar)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(200, 35))
        self.lineEdit_4.setMaxLength(50)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_Registrar)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(200, 35))
        self.lineEdit_5.setMaxLength(30)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_6.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_Registrar)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(200, 35))
        self.lineEdit_6.setMaxLength(20)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_6.addWidget(self.lineEdit_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(88, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.pushButton_4 = QtWidgets.QPushButton(self.page_Registrar)
        self.pushButton_4.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_4.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.page_Registrar)
        self.pushButton_7.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_7.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_7.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_Registrar)
        self.pushButton_6.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_6.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.page_Registrar)
        self.pushButton_5.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_5.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_Registrar)
        self.pushButton_3.setMinimumSize(QtCore.QSize(135, 45))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_8.addWidget(self.pushButton_3)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        spacerItem15 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem15)
        self.stackedWidget.addWidget(self.page_Registrar)
        self.page_Procesos = QtWidgets.QWidget()
        self.page_Procesos.setStyleSheet("")
        self.page_Procesos.setObjectName("page_Procesos")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_Procesos)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(25)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem16 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem16)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QtWidgets.QLabel(self.page_Procesos)
        self.label.setMaximumSize(QtCore.QSize(270, 16777215))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_21.setMaximumSize(QtCore.QSize(60, 35))
        self.lineEdit_21.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"")
        self.lineEdit_21.setText("")
        self.lineEdit_21.setMaxLength(30)
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_12.addWidget(self.lineEdit_21)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_12)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem18)
        self.verticalLayout_15.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem19 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem19)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.page_Procesos)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 34))
        self.label_9.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"color: rgb(225,225,225);\n"
"")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.page_Procesos)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_12.addWidget(self.label_16)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(150, 35))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(0, 35))
        self.lineEdit_13.setMaxLength(5)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_12.addWidget(self.lineEdit_13)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_14.setMaxLength(5)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_12.addWidget(self.lineEdit_14)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_16.setMaxLength(5)
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_12.addWidget(self.lineEdit_16)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_15.setMaxLength(5)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_12.addWidget(self.lineEdit_15)
        self.horizontalLayout_10.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_17 = QtWidgets.QLabel(self.page_Procesos)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_11.addWidget(self.label_17)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_17.setMaximumSize(QtCore.QSize(80, 35))
        self.lineEdit_17.setMaxLength(30)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_11.addWidget(self.lineEdit_17)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(80, 35))
        self.lineEdit_18.setMaxLength(30)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_11.addWidget(self.lineEdit_18)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_19.setMaximumSize(QtCore.QSize(80, 35))
        self.lineEdit_19.setMaxLength(30)
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.verticalLayout_11.addWidget(self.lineEdit_19)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_20.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_20.setMaximumSize(QtCore.QSize(80, 35))
        self.lineEdit_20.setMaxLength(30)
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.verticalLayout_11.addWidget(self.lineEdit_20)
        self.horizontalLayout_10.addLayout(self.verticalLayout_11)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11.addLayout(self.verticalLayout_13)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.page_Procesos)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 34))
        self.label_8.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"color: rgb(225,225,225);\n"
"")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.page_Procesos)
        self.label_10.setMinimumSize(QtCore.QSize(0, 35))
        self.label_10.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.page_Procesos)
        self.label_11.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.page_Procesos)
        self.label_12.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.page_Procesos)
        self.label_13.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.page_Procesos)
        self.label_14.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.page_Procesos)
        self.label_15.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_7.setMaxLength(5)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_8.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_8.setMaxLength(50)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_8.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_9.setMaxLength(30)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_8.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_10.setMaxLength(20)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_8.addWidget(self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_11.setMaxLength(20)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_8.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_12.setMaxLength(20)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_8.addWidget(self.lineEdit_12)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_18 = QtWidgets.QLabel(self.page_Procesos)
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 34))
        self.label_18.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"color: rgb(225,225,225);\n"
"")
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_14.addWidget(self.label_18)
        self.tableWidget = QtWidgets.QTableWidget(self.page_Procesos)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(287, 200))
        self.tableWidget.setMaximumSize(QtCore.QSize(287, 600))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_14.addWidget(self.tableWidget)
        self.horizontalLayout_11.addLayout(self.verticalLayout_14)
        spacerItem20 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem20)
        self.verticalLayout_15.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem21)
        self.label_19 = QtWidgets.QLabel(self.page_Procesos)
        self.label_19.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_16.addWidget(self.label_19)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_22.setMinimumSize(QtCore.QSize(60, 35))
        self.lineEdit_22.setMaximumSize(QtCore.QSize(60, 35))
        self.lineEdit_22.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"")
        self.lineEdit_22.setText("")
        self.lineEdit_22.setMaxLength(30)
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.horizontalLayout_16.addWidget(self.lineEdit_22)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem22)
        self.verticalLayout_15.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem23)
        self.pushButton_8 = QtWidgets.QPushButton(self.page_Procesos)
        self.pushButton_8.setMinimumSize(QtCore.QSize(135, 45))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_13.addWidget(self.pushButton_8)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem24)
        self.verticalLayout_15.addLayout(self.horizontalLayout_13)
        spacerItem25 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem25)
        self.stackedWidget.addWidget(self.page_Procesos)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.Contenido)
        self.verticalLayout_2.addWidget(self.frame_contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.horizontalLayout_3.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #De aqui empezamos
        self.MenuDesplegable.hide()
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #Botones frameSuperior
        self.BotonMenu.clicked.connect(lambda: self.MostrarMenu())
        self.BotonMaximizar.clicked.connect(lambda: self.Maximizar())
        self.BotonMinimizar.clicked.connect(lambda: self.Minimizar())
        self.BotonSalir.clicked.connect(lambda: self.close())
        #Botones del menu
        self.Asignar.clicked.connect(lambda: self.MostrarPestañaAsignar())
        self.Registrar.clicked.connect(lambda: self.MostrarPestañaRegistrar())
        self.Procesos.clicked.connect(lambda: self.MostrarPestañaProcesos())
        self.Ocultar.clicked.connect(lambda: self.OcultarMenu())
        #PaginaAsignar
        self.lineEdit_2.textChanged.connect(lambda: self.EstadoInicial2())
        self.pushButton_2.clicked.connect(lambda: self.PesstañaAsignar_Boton())
        #PaginaRegistrar
        self.pushButton_3.clicked.connect(lambda: self.PreReclutamiento())
        self.lineEdit_3.textChanged.connect(lambda: self.ValidarID())
        self.lineEdit_4.textChanged.connect(lambda: self.ValidarNombre())
        self.lineEdit_5.textChanged.connect(lambda: self.ValidarOperacion())
        self.lineEdit_6.textChanged.connect(lambda: self.ValidarTME())
        #PaginaProcesos
        self.pushButton_8.clicked.connect(lambda: self.RestablecerValores())
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.MoverVentana
        self.frame_superior.mousePressEvent = self.GetMousePos
        #Creacion de SizeGrip
        grip=QtWidgets.QSizeGrip(MainWindow)
        grip.resize(20, 20)
        #Acomodo de SizeGrip
        MainWindow.resizeEvent = self.RedimencionarVentana
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Asignar.setText(_translate("MainWindow", "Asignar"))
        self.Registrar.setText(_translate("MainWindow", "Registrar"))
        self.Procesos.setText(_translate("MainWindow", "Procesos"))
        self.Ocultar.setText(_translate("MainWindow", "Ocultar"))
        self.label_2.setText(_translate("MainWindow", "¿Cuantos registros deseas realizar?"))
        self.pushButton_2.setText(_translate("MainWindow", "Continuar"))
        self.label_7.setText(_translate("MainWindow", "Ingresar programador"))
        self.label_3.setText(_translate("MainWindow", "ID: "))
        self.label_4.setText(_translate("MainWindow", "Nombre: "))
        self.label_5.setText(_translate("MainWindow", "Operacion: "))
        self.label_6.setText(_translate("MainWindow", "TME: "))
        self.pushButton_3.setText(_translate("MainWindow", "Agregar"))
        self.label.setText(_translate("MainWindow", "No. Lotes pendientes: "))
        self.label_9.setText(_translate("MainWindow", "Lote actual"))
        self.label_16.setText(_translate("MainWindow", "Nombre "))
        self.label_17.setText(_translate("MainWindow", "TME"))
        self.label_8.setText(_translate("MainWindow", "Proceso en ejecución"))
        self.label_10.setText(_translate("MainWindow", "ID: "))
        self.label_11.setText(_translate("MainWindow", "Nombre: "))
        self.label_12.setText(_translate("MainWindow", "Operacion: "))
        self.label_13.setText(_translate("MainWindow", "TME: "))
        self.label_14.setText(_translate("MainWindow", "TT: "))
        self.label_15.setText(_translate("MainWindow", "TR: "))
        self.label_18.setText(_translate("MainWindow", "Terminados"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Operacion"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Resultado"))
        self.label_19.setText(_translate("MainWindow", "Contador global: "))
        self.pushButton_8.setText(_translate("MainWindow", "Restablecer"))

    #Funciones
    def MostrarMenu(self):
        if self.MenuDesplegable.isHidden():
            self.MenuDesplegable.show()
        else:
            self.MenuDesplegable.hide()
    def Maximizar(self):
        if MainWindow.isMaximized():
            MainWindow.showNormal()
        else:
            MainWindow.showMaximized()
    def Minimizar(self):
        MainWindow.showMinimized()
    def close(self):
        MainWindow.close()
    
    #Funciones del menu
    def MostrarPestañaAsignar(self):
        self.stackedWidget.setCurrentWidget(self.page_Asignar)
    def MostrarPestañaRegistrar(self):
        self.stackedWidget.setCurrentWidget(self.page_Registrar)
    def MostrarPestañaProcesos(self):
        self.stackedWidget.setCurrentWidget(self.page_Procesos)
    def OcultarMenu(self):
        self.MenuDesplegable.hide()
    
    #PaginaAsignar
    def EstadoInicial2(self):
        self.lineEdit_2.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
    def PesstañaAsignar_Boton(self):
        global Programadores
        if Programadores!=0:
            self.lineEdit_2.setStyleSheet("border-bottom:2px solid red;")
            return
        try:
            Cebo=int(self.lineEdit_2.text())
        except:
            self.lineEdit_2.setStyleSheet("border-bottom:2px solid red;")
            return
        if Cebo<1:
            self.lineEdit_2.setStyleSheet("border-bottom:2px solid yellow;")
            return
        Programadores=Cebo
        self.ReclutarProgramadores_Title()
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_6.setReadOnly(False)
        self.stackedWidget.setCurrentWidget(self.page_Registrar)
        self.lineEdit_2.setReadOnly(True)
    
    #PaginaRegistrar
    def ValidarID(self):
        global ContadorMinioms,BanderaID
        ID=self.lineEdit_3.text()
        if len(ID)==0:
            self.lineEdit_3.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            BanderaID=False
            return
        try:
            ID=int(self.lineEdit_3.text())
            if ID<1:
                self.lineEdit_3.setStyleSheet("border-bottom:2px solid yellow;")
                BanderaID=False
            else:
                for x in range(ContadorMinioms):
                    if Lotes[x][0]==ID:
                        self.lineEdit_3.setStyleSheet("border-bottom:2px solid yellow;")
                        BanderaID=False
                        return
                self.lineEdit_3.setStyleSheet("border-bottom:2px solid rgb(0,255,0);")
                BanderaID=True
        except:
            self.lineEdit_3.setStyleSheet("border-bottom:2px solid red;")
            BanderaID=False
    def ValidarNombre(self):
        global BanderaNombre
        Nombre=self.lineEdit_4.text()
        if len(Nombre)==0:
            self.lineEdit_4.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            BanderaNombre=False
            return
        if re.match('^[a-z\sñáéíóú]+$',Nombre,re.I):
            self.lineEdit_4.setStyleSheet("border-bottom:2px solid rgb(0,255,0);")
            BanderaNombre=True
            return
        self.lineEdit_4.setStyleSheet("border-bottom:2px solid red;")
        BanderaNombre=False
    def ValidarOperacion(self):
        global BanderaOperacion
        Operacion=self.lineEdit_5.text()
        if len(Operacion)==0:
            self.lineEdit_5.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            BanderaOperacion=False
            return
        if re.match('^-?[\d]+[\+\-\*\/\%]-?[\d]+$',Operacion):
            try:
                Operacion=eval(Operacion)
                self.lineEdit_5.setStyleSheet("border-bottom:2px solid rgb(0,255,0);")
                BanderaOperacion=True
            except:
                self.lineEdit_5.setStyleSheet("border-bottom:2px solid yellow;")
                BanderaOperacion=False
            return
        self.lineEdit_5.setStyleSheet("border-bottom:2px solid red;")   
        BanderaOperacion=False
    def ValidarTME(self):
        global BanderaTME
        TME=self.lineEdit_6.text()
        if len(TME)==0:
            self.lineEdit_6.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            BanderaTME=False
            return
        try:
            TME=int(self.lineEdit_6.text())
            if TME<1:
                self.lineEdit_6.setStyleSheet("border-bottom:2px solid yellow;")
                BanderaTME=False
                return
            self.lineEdit_6.setStyleSheet("border-bottom:2px solid rgb(0,255,0);")
            BanderaTME=True
        except:
            self.lineEdit_6.setStyleSheet("border-bottom:2px solid red;")
            BanderaTME=False
    def ReclutarProgramadores_Title(self):
        global ContadorMinioms
        self.label_7.setText("Ingresar Programador #{}".format(ContadorMinioms+1))
    def PreReclutamiento(self):
        global ContadorMinioms,Programadores
        if Programadores==ContadorMinioms:
            self.stackedWidget.setCurrentWidget(self.page_Procesos)
            return
        self.ReclutarProgramadores()  
    def ReclutarProgramadores(self):
        global ContadorMinioms,Programadores,BanderaID,BanderaNombre,BanderaOperacion,BanderaTME
        Bandera=False
        isEmpty=self.lineEdit_3.text()
        if len(isEmpty)==0:
            self.lineEdit_3.setStyleSheet("border-bottom:2px solid red;")
            Bandera=True
        isEmpty=self.lineEdit_4.text()
        if len(isEmpty)==0:
            self.lineEdit_4.setStyleSheet("border-bottom:2px solid red;")
            Bandera=True
        isEmpty=self.lineEdit_5.text()
        if len(isEmpty)==0:
            self.lineEdit_5.setStyleSheet("border-bottom:2px solid red;")
            Bandera=True
        isEmpty=self.lineEdit_6.text()
        if len(isEmpty)==0:
            self.lineEdit_6.setStyleSheet("border-bottom:2px solid red;")
            Bandera=True
        if Bandera:
            return
        if BanderaID and BanderaNombre and BanderaOperacion and BanderaTME:
            ID=int(self.lineEdit_3.text())
            Nombre=self.lineEdit_4.text()
            Operacion=self.lineEdit_5.text()
            TME=int(self.lineEdit_6.text())
            SubLote=[]
            SubLote.append(ID)
            SubLote.append(Nombre)
            SubLote.append(Operacion)
            SubLote.append(TME)
            Lotes.append(SubLote)
            self.lineEdit_3.clear()
            self.lineEdit_3.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.aMimir(100)
            self.lineEdit_4.clear()
            self.lineEdit_4.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.aMimir(100)
            self.lineEdit_5.clear()
            self.lineEdit_5.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.aMimir(100)
            self.lineEdit_6.clear()
            self.lineEdit_6.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.aMimir(100)
            ContadorMinioms+=1
            if ContadorMinioms%4==1:
                self.pushButton_4.setStyleSheet("background-color:rgb(225,131,0);")
                self.pushButton_5.setStyleSheet("background-color:rgb(0,0,0);")
                self.pushButton_6.setStyleSheet("background-color:rgb(0,0,0);")
                self.pushButton_7.setStyleSheet("background-color:rgb(0,0,0);")
            elif ContadorMinioms%4==2:
                self.pushButton_7.setStyleSheet("background-color:rgb(225,131,0);")
            elif ContadorMinioms%4==3:
                self.pushButton_6.setStyleSheet("background-color:rgb(225,131,0);")
            else:
                self.pushButton_5.setStyleSheet("background-color:rgb(225,131,0);")
            self.aMimir(300)
            if Programadores==ContadorMinioms:
                self.stackedWidget.setCurrentWidget(self.page_Procesos)
                self.lineEdit_3.setReadOnly(True)
                self.lineEdit_4.setReadOnly(True)
                self.lineEdit_5.setReadOnly(True)
                self.lineEdit_6.setReadOnly(True)
                self.LlenadoDeDatos()
                return
            self.ReclutarProgramadores_Title()
        
    #PaginaProcesos
    def aMimir(self,time):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(time, loop.quit)
        loop.exec_()
    def ProcesarDatos(self,x):
        SumTT=int(2000/Lotes[x][3])
        self.lineEdit_10.setText('{}'.format(Lotes[x][3]))
        self.lineEdit_11.setText("0")
        self.lineEdit_12.setText('{}'.format(Lotes[x][3]))
        self.aMimir(500)
        for i in range(Lotes[x][3]):
            if SumTT>=0:
                self.lineEdit_7.setText('{}'.format(Lotes[x][0]))
            if SumTT>=700:
                self.lineEdit_8.setText(Lotes[x][1])
            if SumTT>=1400:
                self.lineEdit_9.setText(Lotes[x][2])
            self.lineEdit_11.setText('{}'.format(i+1))
            self.lineEdit_12.setText('{}'.format(Lotes[x][3]-i-1))
            self.ContadorGlobal()
            self.aMimir(int(2000/Lotes[x][3]))
            SumTT+=int(2000/Lotes[x][3])
        self.aMimir(200)
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.aMimir(100)
        self.ProcesosFinalizados(x,Lotes[x][0],Lotes[x][2])
        self.aMimir(500)

    def LlenadoDeDatos(self):
        global Programadores,BanderaProcesos
        LotesPendientes=int(Programadores/4)
        if Programadores%4!=0:
            LotesPendientes+=1
        ContadorMinioms=0;
        ContadorMinioms2=0;
        BanderaProcesos=False
        for i in range(LotesPendientes,0,-1):
            self.lineEdit_21.setText('{}'.format(i-1))
            self.aMimir(1000)
            if ContadorMinioms<Programadores:
                self.lineEdit_13.setText(Lotes[ContadorMinioms][1])
                self.lineEdit_17.setText('{}'.format(Lotes[ContadorMinioms][3]))
                ContadorMinioms+=1
                self.aMimir(1000)
                if ContadorMinioms<Programadores:
                    self.lineEdit_14.setText(Lotes[ContadorMinioms][1])
                    self.lineEdit_18.setText('{}'.format(Lotes[ContadorMinioms][3]))
                    ContadorMinioms+=1
                    self.aMimir(1000)
                    if ContadorMinioms<Programadores:
                        self.lineEdit_16.setText(Lotes[ContadorMinioms][1])
                        self.lineEdit_19.setText('{}'.format(Lotes[ContadorMinioms][3]))
                        ContadorMinioms+=1
                        self.aMimir(1000)
                        if ContadorMinioms<Programadores:
                            self.lineEdit_15.setText(Lotes[ContadorMinioms][1])
                            self.lineEdit_20.setText('{}'.format(Lotes[ContadorMinioms][3]))
                            ContadorMinioms+=1
                            self.aMimir(1000)
            if ContadorMinioms2<ContadorMinioms:
                self.lineEdit_13.clear()
                self.lineEdit_17.clear()
                self.aMimir(1000)
                self.ProcesarDatos(ContadorMinioms2)
                ContadorMinioms2+=1
                if ContadorMinioms2<ContadorMinioms:
                    self.lineEdit_14.clear()
                    self.lineEdit_18.clear()
                    self.aMimir(1000)
                    self.ProcesarDatos(ContadorMinioms2)
                    ContadorMinioms2+=1
                    if ContadorMinioms2<ContadorMinioms:
                        self.lineEdit_16.clear()
                        self.lineEdit_19.clear()
                        self.aMimir(1000)
                        self.ProcesarDatos(ContadorMinioms2)
                        ContadorMinioms2+=1
                        if ContadorMinioms2<ContadorMinioms:
                            self.lineEdit_15.clear()
                            self.lineEdit_20.clear()
                            self.aMimir(1000)
                            self.ProcesarDatos(ContadorMinioms2)
                            ContadorMinioms2+=1
        BanderaProcesos=True
        self.pushButton_8.setStyleSheet("QPushButton{border:2px solid#ff8300}\nQPushButton:Hover{border:2px solid#ffffff}")
        self.lineEdit_22.setStyleSheet("border:2px solid rgb(0, 255, 0);")
    
    #PaginaFinalizados
    def ProcesosFinalizados(self,Pos,ID,Operacion):
        global LotesTerminados,Pos_lote
        if Pos%4==0:
            LotesTerminados+=1
            self.tableWidget.setRowCount(Pos_lote+1)
            item = QtWidgets.QTableWidgetItem("Lote")
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            brush = QtGui.QBrush(QtGui.QColor(225, 131, 0))
            brush.setStyle(QtCore.Qt.DiagCrossPattern)
            item.setBackground(brush)
            self.tableWidget.setItem(Pos_lote, 0, item)
            item = QtWidgets.QTableWidgetItem("#")
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            brush = QtGui.QBrush(QtGui.QColor(225, 131, 0))
            brush.setStyle(QtCore.Qt.DiagCrossPattern)
            item.setBackground(brush)
            self.tableWidget.setItem(Pos_lote, 1, item)
            item = QtWidgets.QTableWidgetItem('{}'.format(LotesTerminados))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            brush = QtGui.QBrush(QtGui.QColor(225, 131, 0))
            brush.setStyle(QtCore.Qt.DiagCrossPattern)
            item.setBackground(brush)
            self.tableWidget.setItem(Pos_lote, 2, item)
            Pos_lote+=1
        self.tableWidget.setRowCount(Pos_lote+1)
        self.tableWidget.setRowCount(Pos_lote+1)
        item = QtWidgets.QTableWidgetItem('{}'.format(ID))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(Pos_lote, 0, item)
        item = QtWidgets.QTableWidgetItem(Operacion)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(Pos_lote, 1, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(eval(Operacion)))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(Pos_lote, 2, item)
        Pos_lote+=1
    def ContadorGlobal(self):
        global ContadorGlobal
        ContadorGlobal+=1
        self.lineEdit_22.setText('{}'.format(ContadorGlobal))
    def RestablecerValores(self):
        global Programadores,ContadorMinioms,ContadorGlobal,BanderaProcesos,BanderaID,BanderaNombre,BanderaOperacion,BanderaTME,LotesTerminados,Pos_lote
        if BanderaProcesos:
            Programadores=0
            ContadorMinioms=0
            ContadorGlobal=0
            LotesTerminados=0
            Pos_lote=0
            BanderaID=False
            BanderaNombre=False
            BanderaOperacion=False
            BanderaTME=False
            for x in range(len(Lotes)):
                Lotes.pop()
            self.lineEdit_2.clear()
            self.lineEdit_2.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_2.setReadOnly(False)
            
            self.label_7.setText("Ingresar Programador")
            self.lineEdit_3.setReadOnly(True)
            self.lineEdit_4.setReadOnly(True)
            self.lineEdit_5.setReadOnly(True)
            self.lineEdit_6.setReadOnly(True)
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_3.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_4.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_5.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_6.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.pushButton_4.setStyleSheet("background-color:rgb(0,0,0);")
            self.pushButton_5.setStyleSheet("background-color:rgb(0,0,0);")
            self.pushButton_6.setStyleSheet("background-color:rgb(0,0,0);")
            self.pushButton_7.setStyleSheet("background-color:rgb(0,0,0);")
            
            self.lineEdit_21.clear()
            
            self.tableWidget.setRowCount(0)
            self.lineEdit_22.clear()
            self.lineEdit_22.setStyleSheet("border:2px solid rgb(225, 131, 0);")
            
            self.stackedWidget.setCurrentWidget(self.page_Asignar)
        else:
            self.pushButton_8.setStyleSheet("border:2px solid red")
    def GetMousePos(self,event):
        global mouse_click
        mouse_click = event.globalPos()
    def MoverVentana(self,event):
        global mouse_click
        if not MainWindow.isMaximized():
            if event.buttons() == QtCore.Qt.LeftButton:
                MainWindow.move(MainWindow.pos() + event.globalPos() - mouse_click)
                mouse_click = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 10:
            MainWindow.showMaximized()
        else:
            MainWindow.showNormal()
    def RedimencionarVentana(self,event):
        global grip
        rect = MainWindow.rect()
        grip.move(rect.right()-20, rect.bottom()-20)
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

