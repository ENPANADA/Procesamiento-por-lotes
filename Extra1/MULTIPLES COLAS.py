# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'MULTIPLES COLAS.ui'
# Created by: PyQt5 UI code generator 5.9.2

from PyQt5 import QtCore, QtGui, QtWidgets
import random

#Variables Globales
mouse_click=0
grip=0

class NuevoHilo(QtCore.QThread):
    chv=QtCore.pyqtSignal(int)
    def __init__(self, parent=None, timeSleep=50):
        super(NuevoHilo,self).__init__(parent)
        self.timeSleep = timeSleep
        self.isRunning = True
    def run(self):
        cont=0
        while cont<100:
            cont+=2
            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(self.timeSleep, loop.quit)
            loop.exec_()
            self.chv.emit(cont) 
        self.isRunning = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global grip
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)
        MainWindow.setMinimumSize(QtCore.QSize(900, 550))
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
"font: 77 15pt\"Arial Black\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"color:rgb(225, 131, 0);\n"
"font: 77 15pt\"Arial Black\";\n"
"border: 0;\n"
"border-bottom: 2px solid rgb(225, 131, 0);\n"
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
"}\n"
"\n"
"QProgressBar{\n"
"color:rgb(225, 131, 0);\n"
"border: 2px solid rgb(225, 131, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"background:rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"background:rgb(255, 255, 255);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:10px;\n"
"}")
        self.Contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Contenido.setObjectName("Contenido")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Contenido)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.Titulo = QtWidgets.QLabel(self.Contenido)
        self.Titulo.setStyleSheet("font: 77 20pt\"Arial Black\";\n"
"")
        self.Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo.setObjectName("Titulo")
        self.verticalLayout_5.addWidget(self.Titulo)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.Contenido)
        self.label.setStyleSheet("font: 77 17pt\"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.Contenido)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.Contenido)
        self.lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(3)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.progressBar = QtWidgets.QProgressBar(self.Contenido)
        self.progressBar.setMinimumSize(QtCore.QSize(200, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(300, 16777215))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.label_5 = QtWidgets.QLabel(self.Contenido)
        self.label_5.setMinimumSize(QtCore.QSize(140, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Contenido)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("border: 2px solid rgb(225, 131, 0);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(3)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.Contenido)
        self.label_4.setStyleSheet("font: 77 17pt\"Arial Black\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.label_3 = QtWidgets.QLabel(self.Contenido)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Contenido)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.progressBar_2 = QtWidgets.QProgressBar(self.Contenido)
        self.progressBar_2.setMinimumSize(QtCore.QSize(200, 30))
        self.progressBar_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_5.addWidget(self.progressBar_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.label_6 = QtWidgets.QLabel(self.Contenido)
        self.label_6.setMinimumSize(QtCore.QSize(140, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Contenido)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("border: 2px solid rgb(225, 131, 0);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setMaxLength(3)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.Ocultar_2 = QtWidgets.QPushButton(self.Contenido)
        self.Ocultar_2.setEnabled(True)
        self.Ocultar_2.setMinimumSize(QtCore.QSize(150, 45))
        self.Ocultar_2.setMaximumSize(QtCore.QSize(150, 45))
        self.Ocultar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ocultar_2.setObjectName("Ocultar_2")
        self.horizontalLayout_4.addWidget(self.Ocultar_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem13 = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "PLANIFICADOR MULTIPLES COLAS"))
        self.Ocultar.setText(_translate("MainWindow", "Ocultar"))
        self.Titulo.setText(_translate("MainWindow", "PLANIFICADOR MULTIPLES COLAS"))
        self.label.setText(_translate("MainWindow", "Cola FCFS"))
        self.label_2.setText(_translate("MainWindow", "Proceso:"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%  "))
        self.label_5.setText(_translate("MainWindow", "Pendientes:"))
        self.label_4.setText(_translate("MainWindow", "Cola SRT"))
        self.label_3.setText(_translate("MainWindow", "Proceso:"))
        self.progressBar_2.setFormat(_translate("MainWindow", "%p%  "))
        self.label_6.setText(_translate("MainWindow", "Pendientes:"))
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
    #Ejecucion del programa
    def CorrerAlgoritmo(self):
        self.Ocultar_2.setEnabled(False)
        self.lineEdit_3.setStyleSheet("border: 2px solid rgb(225, 131, 0);")
        self.lineEdit_4.setStyleSheet("border: 2px solid rgb(225, 131, 0);")
        MaxProcesos = 10
        ColaFCFS = []
        ColaSRT = []
        #Llenado de colas :) 🥵🥵🥵
        for x in range(MaxProcesos):
            datos=[x+1,random.randint(50, 300)]
            ColaFCFS.append(datos)
            datos=[x+1,random.randint(50, 300)]
            ColaSRT.append(datos)
        #Mostrar colitas 🥵🥵🥵
        print('Cola FCFS')
        print(ColaFCFS)
        print('Cola SRT')
        print(ColaSRT)
        #Ordenar colita SRT 🥵🥵🥵
        ColaSRT.sort(key=lambda x: x[1])
        #Inicializar colitas 🥵🥵🥵
        self.hiloColaFCFS = NuevoHilo()
        self.hiloColaFCFS.isRunning = False
        self.hiloColaSRT = NuevoHilo()
        self.hiloColaSRT.isRunning = False
        #Correr procesos
        while True:
            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(50, loop.quit)
            loop.exec_()
            if not self.hiloColaFCFS.isRunning and len(ColaFCFS)!=0:
                print('Hilo ColaFCFS en ejecucion.\tId:', ColaFCFS[0][0], '\tTME: ', ColaFCFS[0][1])
                self.lineEdit.setText('{}'.format(ColaFCFS[0][0]))
                self.hiloColaFCFS = NuevoHilo(timeSleep=ColaFCFS[0][1])
                self.hiloColaFCFS.chv.connect(self.ActualizarBarraFCFS)
                self.hiloColaFCFS.start()
                ColaFCFS.pop(0)
                self.lineEdit_3.setText('{}'.format(len(ColaFCFS)))
                if len(ColaFCFS)==0:
                    self.lineEdit_3.setStyleSheet('border: 2px solid rgb(0,255,0);')
            if not self.hiloColaSRT.isRunning and len(ColaSRT)!=0:
                print('Hilo ColaSRT en ejecucion.\tId:', ColaSRT[0][0], '\tTME: ', ColaSRT[0][1])
                self.lineEdit_2.setText('{}'.format(ColaSRT[0][0]))
                self.hiloColaSRT = NuevoHilo(timeSleep=ColaSRT[0][1])
                self.hiloColaSRT.chv.connect(self.ActualizarBarraSRT)
                self.hiloColaSRT.start()
                ColaSRT.pop(0)
                self.lineEdit_4.setText('{}'.format(len(ColaSRT)))
                if len(ColaSRT)==0:
                    self.lineEdit_4.setStyleSheet('border: 2px solid rgb(0,255,0);')
            if len(ColaFCFS)==0 and len(ColaSRT)==0:
                break
        print('Procesos terminados, las colas estan vacias 🥵🥵🥵')
        self.Ocultar_2.setEnabled(True)   
    def ActualizarBarraFCFS(self,Progreso):
        self.progressBar.setValue(Progreso)  
    def ActualizarBarraSRT(self,Progreso):
        self.progressBar_2.setValue(Progreso)
    #Funciones extra
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


import Imagenes

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

