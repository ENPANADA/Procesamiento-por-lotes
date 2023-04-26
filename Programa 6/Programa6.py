# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Programa6.ui'
# Created by: PyQt5 UI code generator 5.9.2

'''
Seminario de Sistemas Operativos - D02
Actividad de Aprendizaje 12
    Programa 6. Productor-Consumidor
Integrantes:
    Saul Alejandro Castañeda Perez
    Daniel Martinez Martinez
    
Friday, April 28, 2023
'''

from PyQt5 import QtCore, QtGui, QtWidgets

import threading
import time
import random
#Variables Globales
mouse_click=0
grip=0

#Variables globales del algoritmo
# Creamos una cola compartida para que el productor y el consumidor la utilicen
shared_queue = ['🍆'] * 22
#Creamos una variale que funje como el indice donde se han ido poniendo hamburguesas
indice=0
#Creamos un segundo indice para llevar seguimiento a la puesta de berenjenas (donde nos quedamos)
indice2=0
# Creamos un objeto Event
stop_event = threading.Event()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global grip
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 604)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 600))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
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
        self.BotonMenu.setMinimumSize(QtCore.QSize(200, 40))
        self.BotonMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonMenu.setStyleSheet("image: url(:/BN/menu.png);")
        self.BotonMenu.setText("")
        self.BotonMenu.setIconSize(QtCore.QSize(38, 38))
        self.BotonMenu.setObjectName("BotonMenu")
        self.horizontalLayout.addWidget(self.BotonMenu)
        spacerItem = QtWidgets.QSpacerItem(544, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.BotonMinimizar = QtWidgets.QPushButton(self.frame_superior)
        self.BotonMinimizar.setMinimumSize(QtCore.QSize(50, 40))
        self.BotonMinimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonMinimizar.setStyleSheet("image: url(:/BN/minimizar.png);")
        self.BotonMinimizar.setText("")
        self.BotonMinimizar.setIconSize(QtCore.QSize(38, 38))
        self.BotonMinimizar.setObjectName("BotonMinimizar")
        self.horizontalLayout.addWidget(self.BotonMinimizar)
        self.BotonMaximizar = QtWidgets.QPushButton(self.frame_superior)
        self.BotonMaximizar.setMinimumSize(QtCore.QSize(50, 40))
        self.BotonMaximizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonMaximizar.setStyleSheet("image: url(:/BN/maximizar.png);")
        self.BotonMaximizar.setText("")
        self.BotonMaximizar.setIconSize(QtCore.QSize(38, 38))
        self.BotonMaximizar.setObjectName("BotonMaximizar")
        self.horizontalLayout.addWidget(self.BotonMaximizar)
        self.BotonSalir = QtWidgets.QPushButton(self.frame_superior)
        self.BotonSalir.setMinimumSize(QtCore.QSize(50, 40))
        self.BotonSalir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonSalir.setStyleSheet("image: url(:/BN/exportar.png);")
        self.BotonSalir.setText("")
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
        self.MenuDesplegable.setEnabled(True)
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
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 191, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.Ocultar = QtWidgets.QPushButton(self.MenuDesplegable)
        self.Ocultar.setEnabled(True)
        self.Ocultar.setMinimumSize(QtCore.QSize(135, 45))
        self.Ocultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ocultar.setObjectName("Ocultar")
        self.verticalLayout.addWidget(self.Ocultar)
        self.horizontalLayout_2.addWidget(self.MenuDesplegable)
        self.Contenido = QtWidgets.QFrame(self.frame_contenido)
        self.Contenido.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Contenido.setStyleSheet("QLabel{\n"
"border-radius:10px;\n"
"color:rgb(225, 131, 0);\n"
"border: 2px solid rgb(225, 131, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"border: 2px solid rgb(225, 131, 0);\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"border: 2px solid rgb(255,255,255);\n"
"color:rgb(225, 131, 0);\n"
"}")
        self.Contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Contenido.setObjectName("Contenido")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Contenido)
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.Titulo = QtWidgets.QLabel(self.Contenido)
        self.Titulo.setStyleSheet("border:0px;\n"
"font: 77 20pt\"Arial Black\";\n"
"")
        self.Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo.setObjectName("Titulo")
        self.verticalLayout_6.addWidget(self.Titulo)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Personaje1 = QtWidgets.QLabel(self.Contenido)
        self.Personaje1.setMinimumSize(QtCore.QSize(150, 200))
        self.Personaje1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Personaje1.setStyleSheet("image: url(:/PC/bobtoronja.png);")
        self.Personaje1.setText("")
        self.Personaje1.setAlignment(QtCore.Qt.AlignCenter)
        self.Personaje1.setObjectName("Personaje1")
        self.verticalLayout_3.addWidget(self.Personaje1)
        self.descripcion1 = QtWidgets.QLabel(self.Contenido)
        self.descripcion1.setMinimumSize(QtCore.QSize(150, 50))
        self.descripcion1.setMaximumSize(QtCore.QSize(150, 50))
        self.descripcion1.setAlignment(QtCore.Qt.AlignCenter)
        self.descripcion1.setObjectName("descripcion1")
        self.verticalLayout_3.addWidget(self.descripcion1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.Contenedor_1 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_1.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_1.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_1.setStyleSheet(";")
        self.Contenedor_1.setText("")
        self.Contenedor_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_1.setObjectName("Contenedor_1")
        self.gridLayout.addWidget(self.Contenedor_1, 0, 0, 1, 1)
        self.Contenedor_2 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_2.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_2.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_2.setStyleSheet(';')
        self.Contenedor_2.setText("")
        self.Contenedor_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_2.setObjectName("Contenedor_2")
        self.gridLayout.addWidget(self.Contenedor_2, 0, 1, 1, 1)
        self.Contenedor_3 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_3.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_3.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_3.setStyleSheet(";")
        self.Contenedor_3.setText("")
        self.Contenedor_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_3.setObjectName("Contenedor_3")
        self.gridLayout.addWidget(self.Contenedor_3, 0, 2, 1, 1)
        self.Contenedor_4 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_4.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_4.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_4.setText("")
        self.Contenedor_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_4.setObjectName("Contenedor_4")
        self.gridLayout.addWidget(self.Contenedor_4, 0, 3, 1, 1)
        self.Contenedor_5 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_5.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_5.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_5.setText("")
        self.Contenedor_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_5.setObjectName("Contenedor_5")
        self.gridLayout.addWidget(self.Contenedor_5, 0, 4, 1, 1)
        self.Contenedor_6 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_6.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_6.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_6.setText("")
        self.Contenedor_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_6.setObjectName("Contenedor_6")
        self.gridLayout.addWidget(self.Contenedor_6, 1, 0, 1, 1)
        self.Contenedor_7 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_7.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_7.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_7.setText("")
        self.Contenedor_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_7.setObjectName("Contenedor_7")
        self.gridLayout.addWidget(self.Contenedor_7, 1, 1, 1, 1)
        self.Contenedor_8 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_8.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_8.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_8.setText("")
        self.Contenedor_8.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_8.setObjectName("Contenedor_8")
        self.gridLayout.addWidget(self.Contenedor_8, 1, 2, 1, 1)
        self.Contenedor_9 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_9.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_9.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_9.setText("")
        self.Contenedor_9.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_9.setObjectName("Contenedor_9")
        self.gridLayout.addWidget(self.Contenedor_9, 1, 3, 1, 1)
        self.Contenedor_10 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_10.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_10.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_10.setText("")
        self.Contenedor_10.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_10.setObjectName("Contenedor_10")
        self.gridLayout.addWidget(self.Contenedor_10, 1, 4, 1, 1)
        self.Contenedor_11 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_11.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_11.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_11.setText("")
        self.Contenedor_11.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_11.setObjectName("Contenedor_11")
        self.gridLayout.addWidget(self.Contenedor_11, 2, 0, 1, 1)
        self.Contenedor_12 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_12.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_12.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_12.setText("")
        self.Contenedor_12.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_12.setObjectName("Contenedor_12")
        self.gridLayout.addWidget(self.Contenedor_12, 2, 1, 1, 1)
        self.Contenedor_13 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_13.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_13.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_13.setText("")
        self.Contenedor_13.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_13.setObjectName("Contenedor_13")
        self.gridLayout.addWidget(self.Contenedor_13, 2, 2, 1, 1)
        self.Contenedor_14 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_14.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_14.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_14.setText("")
        self.Contenedor_14.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_14.setObjectName("Contenedor_14")
        self.gridLayout.addWidget(self.Contenedor_14, 2, 3, 1, 1)
        self.Contenedor_15 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_15.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_15.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_15.setText("")
        self.Contenedor_15.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_15.setObjectName("Contenedor_15")
        self.gridLayout.addWidget(self.Contenedor_15, 2, 4, 1, 1)
        self.Contenedor_16 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_16.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_16.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_16.setText("")
        self.Contenedor_16.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_16.setObjectName("Contenedor_16")
        self.gridLayout.addWidget(self.Contenedor_16, 3, 0, 1, 1)
        self.Contenedor_17 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_17.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_17.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_17.setText("")
        self.Contenedor_17.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_17.setObjectName("Contenedor_17")
        self.gridLayout.addWidget(self.Contenedor_17, 3, 1, 1, 1)
        self.Contenedor_18 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_18.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_18.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_18.setText("")
        self.Contenedor_18.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_18.setObjectName("Contenedor_18")
        self.gridLayout.addWidget(self.Contenedor_18, 3, 2, 1, 1)
        self.Contenedor_19 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_19.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_19.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_19.setText("")
        self.Contenedor_19.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_19.setObjectName("Contenedor_19")
        self.gridLayout.addWidget(self.Contenedor_19, 3, 3, 1, 1)
        self.Contenedor_20 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_20.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_20.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_20.setText("")
        self.Contenedor_20.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_20.setObjectName("Contenedor_20")
        self.gridLayout.addWidget(self.Contenedor_20, 3, 4, 1, 1)
        self.Contenedor_21 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_21.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_21.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_21.setText("")
        self.Contenedor_21.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_21.setObjectName("Contenedor_21")
        self.gridLayout.addWidget(self.Contenedor_21, 4, 0, 1, 1)
        self.Contenedor_22 = QtWidgets.QLabel(self.Contenido)
        self.Contenedor_22.setMinimumSize(QtCore.QSize(50, 50))
        self.Contenedor_22.setMaximumSize(QtCore.QSize(50, 50))
        self.Contenedor_22.setText("")
        self.Contenedor_22.setAlignment(QtCore.Qt.AlignCenter)
        self.Contenedor_22.setObjectName("Contenedor_22")
        self.gridLayout.addWidget(self.Contenedor_22, 4, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Personaje2 = QtWidgets.QLabel(self.Contenido)
        self.Personaje2.setMinimumSize(QtCore.QSize(150, 200))
        self.Personaje2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Personaje2.setStyleSheet("image: url(:/PC/pez promedio.png);")
        self.Personaje2.setText("")
        self.Personaje2.setAlignment(QtCore.Qt.AlignCenter)
        self.Personaje2.setObjectName("Personaje2")
        self.verticalLayout_5.addWidget(self.Personaje2)
        self.descripcion2 = QtWidgets.QLabel(self.Contenido)
        self.descripcion2.setMinimumSize(QtCore.QSize(150, 50))
        self.descripcion2.setMaximumSize(QtCore.QSize(150, 50))
        self.descripcion2.setAlignment(QtCore.Qt.AlignCenter)
        self.descripcion2.setObjectName("descripcion2")
        self.verticalLayout_5.addWidget(self.descripcion2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.Ocultar_2 = QtWidgets.QPushButton(self.Contenido)
        self.Ocultar_2.setEnabled(True)
        self.Ocultar_2.setMinimumSize(QtCore.QSize(150, 45))
        self.Ocultar_2.setMaximumSize(QtCore.QSize(150, 45))
        self.Ocultar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ocultar_2.setObjectName("Ocultar_2")
        self.horizontalLayout_4.addWidget(self.Ocultar_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_2.addWidget(self.Contenido)
        self.verticalLayout_2.addWidget(self.frame_contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.horizontalLayout_9.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #De aqui empezamos
        self.BotonMenu.setMinimumSize(QtCore.QSize(50, 40))
        self.MenuDesplegable.hide()
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #Botones frameSuperior
        self.BotonMenu.clicked.connect(lambda: self.MostrarMenu())
        self.BotonMaximizar.clicked.connect(lambda: self.Maximizar())
        self.BotonMinimizar.clicked.connect(lambda: self.Minimizar())
        self.BotonSalir.clicked.connect(lambda: self.close())
        #Botones del menu
        self.Ocultar.clicked.connect(lambda: self.OcultarMenu())
        #PaginaPrincipal
        self.Ocultar_2.clicked.connect(lambda: self.CorrerAlgoritmo())
        #CapturarEntradas
        MainWindow.keyPressEvent = self.CapturarTeclas
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.MoverVentana
        self.frame_superior.mousePressEvent = self.GetMousePos
        #Creacion de SizeGrip
        grip=QtWidgets.QSizeGrip(MainWindow)
        grip.resize(20, 20)
        #Acomodo de SizeGrip
        MainWindow.resizeEvent = self.RedimensionarVentana

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Productor-Consumidor"))
        self.Ocultar.setText(_translate("MainWindow", "Ocultar"))
        self.Titulo.setText(_translate("MainWindow", "Productor-Consumidor"))
        self.descripcion1.setText(_translate("MainWindow", "Durmiendo"))
        self.descripcion2.setText(_translate("MainWindow", "Durmiendo"))
        self.Ocultar_2.setText(_translate("MainWindow", "Comenzar"))
        

    #Funciones
    def MostrarMenu(self):
        if self.MenuDesplegable.isHidden():
            self.MenuDesplegable.show()
            self.BotonMenu.setMinimumSize(QtCore.QSize(200, 40))
        else:
            self.MenuDesplegable.hide()
            self.BotonMenu.setMinimumSize(QtCore.QSize(50, 40))
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
    def OcultarMenu(self):
        self.MenuDesplegable.hide()
        self.BotonMenu.setMinimumSize(QtCore.QSize(50, 40))
        
    #Retardo para poder apreciar los cambios progresivamente    
    def Retardo(self,time):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(time, loop.quit)
        loop.exec_()   
        
    #Aqui comienza la logica del programa
    """Funciones Auxiliares"""
    #Esta funcion define si la lista esta llena, dado la no existencia de berenejas indicaria que no hay espacios libres
    def HayBerenjenas(self):
        global shared_queue
        try:
            return shared_queue.index('🍆')
        except:
            return -1
    #Esta funcion define si la lista esta vacia, dado que no encontrar alguna hamburguesa significaria que esta vacia    
    def HayAnvorguesas(self):
        global shared_queue
        try:
            return shared_queue.index('🍔')
        except:
            return -1 
    #Funcion auxiliar para limpiar las casillas
    def LimpiarCasillas(self):
        global shared_queue
        for i in range (1,23):
           operacion="self.Contenedor_"+str(i)+".setStyleSheet(';')"
           eval(operacion) 
    
    """
    Aqui buscamos la posicion desde donde empezaremos a consumir, localizando donde comienzan las 
    hamburguesas despues de los espacios vacios   |comenzamos de aqui
                                                  v
                      🍔🍔🍔🍔🍔🍆🍆🍆🍆🍆🍆🍔🍔🍔🍔
    """
    def indice2Inicial(self):
        global shared_queue,indice
        try:
            #Comenzamos a buscar asumiendo que se colocaron hamburguesas en el inicio por la circularidad
            indiceAux=shared_queue.index('🍆')
            return shared_queue.index('🍔',indiceAux)
        except:
            try:
                #En caso de que no se encontrara ninguna hamburguesa de la forma anterior, ahora si buscamos alguna desde el inicio
                return shared_queue.index('🍔',0)
            except:
                return -1
    # Creamos una variable de condición para que el productor espere cuando la cola esté llena
    condition = threading.Condition()
    
    # Definimos una función para el productor que agregará elementos a la cola compartida
    def producer(self,stop_event):
        global indice
        while not stop_event.is_set():
            # Esperamos un tiempo aleatorio antes de producir un elemento
            time.sleep(random.randint(0, 1))
            # Consideramos una cantidad aleatoria de elementos a agregar a la cola
            numeroItems = random.randint(3, 6)
            
            # Bloqueamos la cola compartida con la variable de condición
            with self.condition:
                # Si la cola está llena, esperamos a que se vacíe un espacio
                while (self.HayBerenjenas()) == -1:
                    self.condition.wait()
                _translate = QtCore.QCoreApplication.translate
                self.descripcion2.setText(_translate("MainWindow", "Durmiendo"))
                self.descripcion2.setStyleSheet('border: 2px solid rgb(225, 131, 0);')
                self.descripcion1.setText(_translate("MainWindow", "Produciendo"))
                self.descripcion1.setStyleSheet('border: 2px solid rgb(0, 255, 0);')
                # Agregamos los N items a la cola
                for i in range (numeroItems):
                    #En caso de que haya una hamburguesa en el indice actual, terminamos de colocar
                    #hamburguesas, dado que esto indicaria que ya está llena la cola
                    if (shared_queue[indice]=='🍔') or stop_event.is_set():
                        if(not stop_event.is_set()):
                            self.descripcion1.setText(_translate("MainWindow", "Intentando\nproducir"))
                            self.descripcion1.setStyleSheet('border: 2px solid rgb(255, 255, 0);')
                            time.sleep(2)
                        elif (stop_event.is_set()):
                            self.Titulo.setText(_translate("MainWindow", "Programa finalizado"))
                            self.descripcion1.setText(_translate("MainWindow", "Durmiendo"))
                            self.descripcion2.setText(_translate("MainWindow", "Durmiendo"))
                            self.descripcion1.setStyleSheet('border: 2px solid rgb(225, 131, 0);')
                            self.descripcion2.setStyleSheet('border: 2px solid rgb(225, 131, 0);')
                            self.LimpiarCasillas()
                        break
                    #Cambiamos una apestosa berenjena por una deliciosa cangreburguer
                    shared_queue[indice]='🍔'
                    self.descripcion1.setText(_translate("MainWindow", "Produciendo ({})").format(numeroItems-i-1))
                    operacion="self.Contenedor_"+str(indice+1)+".setStyleSheet('image: url(:/PC/cangreburger.png);border: 2px solid rgb(0,255,0);')"
                    eval(operacion)
                    self.Retardo(1000)
                    operacion="self.Contenedor_"+str(indice+1)+".setStyleSheet('image: url(:/PC/cangreburger.png);border: 2px solid rgb(225, 131, 0);')"
                    eval(operacion)
                    #Incrementamos el indice
                    indice=indice+1
                    #Consideramos circularidad
                    if indice==22:
                        indice=0
                # Notificamos a los threads en espera que la cola ha cambiado
                self.condition.notify_all()
             

    # Definimos una función para el consumidor que quitará elementos de la cola compartida
    def consumer(self,stop_event):
        global indice2,indice
        while not stop_event.is_set():
            # Esperamos un tiempo aleatorio antes de intentar consumir un elemento
            time.sleep(random.randint(0,1))
            
            # Consideramos una cantidad aleatoria de elementos a quitar de la cola
            numeroItems = random.randint(3, 6)
            
            # Bloqueamos la cola compartida con la variable de condición
            with self.condition:
                # Si la cola está vacía, esperamos a que se agregue un elemento
                while (self.HayAnvorguesas()) == -1:
                    _translate = QtCore.QCoreApplication.translate
                    self.descripcion2.setText(_translate("MainWindow", "Intentando\nconsumir"))
                    self.descripcion2.setStyleSheet('border: 2px solid rgb(255, 255, 0);')
                    time.sleep(2)
                    self.condition.wait()
                    
                # Liberamos espacios de la cola, reemplazando las hamburguesas con berenjenas
                #Comenzamos a colocar berenjenas donde nos habiamos quedado
                _translate = QtCore.QCoreApplication.translate
                self.descripcion1.setText(_translate("MainWindow", "Durmiendo"))
                self.descripcion1.setStyleSheet('border: 2px solid rgb(225, 131, 0);')
                self.descripcion2.setText(_translate("MainWindow", "Consumiendo"))
                self.descripcion2.setStyleSheet('border: 2px solid rgb(0, 255, 255);')
                if((self.HayBerenjenas()) == -1):
                    indice2=indice
                else:
                    indice2=self.indice2Inicial()
                for i in range (numeroItems):
                    #SI de donde estamos ya hay una berenjena, nos detenemos, dado que esto significa que
                    #No hay kangreburguers para consumir
                    if (shared_queue[indice2]=='🍆' or stop_event.is_set()):
                        if(not stop_event.is_set()):
                            self.descripcion2.setText(_translate("MainWindow", "Intentando\nconsumir"))
                            self.descripcion2.setStyleSheet('border: 2px solid rgb(255, 255, 0);')
                            time.sleep(2)
                        elif (stop_event.is_set()):
                            self.Titulo.setText(_translate("MainWindow", "Programa finalizado"))
                            self.descripcion1.setText(_translate("MainWindow", "Durmiendo"))
                            self.descripcion2.setText(_translate("MainWindow", "Durmiendo"))
                            self.descripcion1.setStyleSheet('border: 2px solid rgb(225, 131, 0);')
                            self.descripcion2.setStyleSheet('border: 2px solid rgb(225, 131, 0);')
                            self.LimpiarCasillas()
                        break
                    #Cambiamos una hamburguesa por una sucia berenjena
                    shared_queue[indice2]='🍆'
                    self.descripcion2.setText(_translate("MainWindow", "Consumiendo ({})").format(numeroItems-i-1))
                    operacion="self.Contenedor_"+str(indice2+1)+".setStyleSheet('border: 2px solid rgb(0, 255, 255);')"
                    eval(operacion)
                    self.Retardo(1000)
                    operacion="self.Contenedor_"+str(indice2+1)+".setStyleSheet('border: 2px solid rgb(225, 131, 0);')"
                    eval(operacion)
                    #Incrementamos el indice para continuar a la siguiente posicion de la lista
                    indice2=indice2+1
                    #Consideramos la circularidad
                    if indice2==22:
                        indice2=0
                # Notificamos a los threads en espera que la cola ha cambiado
                self.condition.notify_all()
    
    #Ejecucion del programa
    def CorrerAlgoritmo(self):
        global bnd,stop_event
        # Creamos los threads para el productor y el consumidor
        producer_thread = threading.Thread(target=self.producer, args=(stop_event,))
        consumer_thread = threading.Thread(target=self.consumer, args=(stop_event,))

        # Iniciamos los threads
        producer_thread.start()
        consumer_thread.start()
        
        
    #Funciones extra
    def CapturarTeclas(self,event):
        global bnd,stop_event
        if event.key()==QtCore.Qt.Key_Escape:
            print("ESC PRESIONADA")
            stop_event.set()
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
    def RedimensionarVentana(self,event):
        global grip
        rect = MainWindow.rect()
        grip.move(rect.right()-20, rect.bottom()-20)

import Imagenes

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
