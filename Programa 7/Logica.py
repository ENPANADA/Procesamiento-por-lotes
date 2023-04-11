# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Programa7.ui'
# Created by: PyQt5 UI code generator 5.9.2

'''
Seminario de Sistemas Operativos - D02
    Actividad de Aprendizaje 14
Programa 7. Paginación Simple
Integrantes:
    Saul Alejandro Castañeda Perez
    Daniel Martinez Martinez
    
Sonday, May 14, 2023
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import random

'''

███████╗██╗░░░██╗███╗░░██╗░█████╗░██╗░█████╗░███╗░░██╗███████╗░██████╗
██╔════╝██║░░░██║████╗░██║██╔══██╗██║██╔══██╗████╗░██║██╔════╝██╔════╝
█████╗░░██║░░░██║██╔██╗██║██║░░╚═╝██║██║░░██║██╔██╗██║█████╗░░╚█████╗░
██╔══╝░░██║░░░██║██║╚████║██║░░██╗██║██║░░██║██║╚████║██╔══╝░░░╚═══██╗
██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝██║╚█████╔╝██║░╚███║███████╗██████╔╝
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

                 ¶
              ¶  ¶   ¶¶
              ¶ ¶¶ ¶¶
         ¶¶¶¶      ¶¶¶¶¶¶
       ¶¶                ¶¶
     ¶¶        ¶¶          ¶¶
   ¶¶                        ¶¶
  ¶¶                          ¶¶
  ¶                           ¶ ¶
 ¶                ¶             ¶
 ¶             ¶¶¶¶              ¶
 ¶            ¶¶ ¶           ¶   ¶
 ¶          ¶¶¶¶¶¶       ¶¶¶¶    ¶
 ¶         ¶¶¶¶¶¶¶      ¶¶  ¶    ¶
  ¶        ¶¶¶¶¶ ¶     ¶¶¶¶¶¶   ¶
  ¶¶       ¶     ¶    ¶¶¶¶¶¶   ¶¶
   ¶¶      ¶    ¶    ¶¶¶¶     ¶
    ¶      ¶   ¶     ¶       ¶
    ¶      ¶¶¶¶         ¶  ¶¶
    ¶¶               ¶¶¶  ¶
     ¶¶¶       ¶¶¶¶¶      ¶
        ¶¶¶     ¶¶       ¶¶
            ¶¶     ¶¶¶¶¶¶ 
          ¶¶      ¶¶ ¶
       ¶¶¶¶        ¶ ¶¶
         ¶  ¶¶     ¶   ¶
    ¶¶¶¶¶¶ ¶       ¶  ¶ 
  ¶¶   ¶¶¶¶ ¶      ¶   ¶¶¶¶¶¶¶
  ¶¶      ¶¶¶¶     ¶ ¶¶     ¶¶
  ¶          ¶¶¶¶¶¶¶¶         ¶
   ¶¶         ¶   ¶          ¶
    ¶¶¶¶¶¶¶¶¶¶¶   ¶¶¶¶¶¶¶¶¶¶¶


'''
def MostrarMenu(self):
    if self.MenuDesplegable.isHidden():
        self.MenuDesplegable.show()
        self.BotonMenu.setMinimumSize(QtCore.QSize(200, 40))
    else:
        self.MenuDesplegable.hide()
        self.BotonMenu.setMinimumSize(QtCore.QSize(50, 40))
def Maximizar(self,MainWindow):
    if MainWindow.isMaximized():
        MainWindow.showNormal()
    else:
        MainWindow.showMaximized()
def Minimizar(self,MainWindow):
    MainWindow.showMinimized()
def close(self,MainWindow):
    MainWindow.close()

#Funciones del menu
def MostrarPestañaAsignar(self):
    self.stackedWidget.setCurrentWidget(self.page_Asignar)
def MostrarPestañaProcesos(self):
    self.stackedWidget.setCurrentWidget(self.page_Procesos)
def MostrarPestañaPaginacion(self):
    VerMercadoSexual(self)
    self.stackedWidget.setCurrentWidget(self.page_Paginacion)
def MostrarPestañaTiempos(self):
    LlenarTablaBCP(self)
    self.stackedWidget.setCurrentWidget(self.page_Tiempos)
def OcultarMenu(self):
    self.MenuDesplegable.hide()
    self.BotonMenu.setMinimumSize(QtCore.QSize(50, 40))

#PaginaAsignar
def EstadoInicial2(self):
    self.lineEdit_2.setStyleSheet("")
def EstadoInicial3(self):
    self.lineEdit_3.setStyleSheet("")
def PesstañaAsignar_Boton(self):
    bandera=False
    try:
        Gatas=int(self.lineEdit_2.text())
    except:
        self.lineEdit_2.setStyleSheet("border-bottom:2px solid red;")
        bandera=True
    try:
        QuantumCebo=int(self.lineEdit_3.text())
    except:
        self.lineEdit_3.setStyleSheet("border-bottom:2px solid red;")
        bandera=True
    if bandera:
        return
    if Gatas<self.MinProcesos or Gatas>self.MaxProcesos:
        self.lineEdit_2.setStyleSheet("border-bottom:2px solid yellow;")
        bandera=True
    if QuantumCebo<self.MinQuantum:
        self.lineEdit_3.setStyleSheet("border-bottom:2px solid yellow;")
        bandera=True
    if bandera:
        return
    self.Quantum=QuantumCebo
    self.stackedWidget.setCurrentWidget(self.page_Procesos)
    self.lineEdit_2.setReadOnly(True)
    self.lineEdit_3.setReadOnly(True)
    self.pushButton_2.setEnabled(False)
    for ID_Proceso in range(Gatas):
        FabricarNuevoMiniom(self,ID_Proceso+1)
    self.stackedWidget.setCurrentWidget(self.page_Procesos)
    IniciarCorrida(self)  
def FabricarNuevoMiniom(self,ID_Proceso):
    if not ID_Proceso > self.MaxProcesos:
        Operadores = ['+','-','*','/','%']
        Operacion = ('{}{}{}'.format(random.randint((self.MaxNumeroAleatorio*-1)
                                                    , self.MaxNumeroAleatorio)      #Digito
                                     ,random.choice(Operadores)                     #Operador
                                     ,random.randint(1, self.MaxNumeroAleatorio)))  #Digito
        Lote=[ID_Proceso                                #[0] -> ID del proceso
              ,random.randint(self.MinTME,self.MaxTME)  #[1] -> Tiempo maximo estimado
              ,random.randint(self.MinTamanioProceso
                              ,self.MaxTamanioProceso)  #[2] -> Tamaño del proceso
              ,-1                                       #[3] -> Tiempo de llegada
              ,-1                                       #[4] -> Tiempo de finalizacion
              ,-1                                       #[5] -> Tiempo de retorno
              ,-1                                       #[6] -> Tiempo de respuesta
              ,0                                        #[7] -> Tiempo de espera
              ,0                                        #[8] -> Tiempo de servicio
              ,Operacion                                #[9] -> Operacion
              ,str(int(eval(Operacion)))                #[10] -> Resultado
              ,'Nuevo']                                 #[11] -> Estado por defecto
        self.Lotes.append(Lote)        
#PaginaProcesos
def aMimir(self,time):
    loop = QtCore.QEventLoop()
    QtCore.QTimer.singleShot(time, loop.quit)
    loop.exec_()
def MinitasSecandose(self):
    for Gata in self.Lotes:
        if Gata[self.getPos['Estado']] == 'Listo' or Gata[self.getPos['Estado']] == 'Bloqueado':
            Gata[self.getPos['TE']] += 1
def CaidaAlAnexo(self, Gil):
    self.tableWidget_2.setRowCount(self.tableWidget_2.rowCount() + 1)
    item = QtWidgets.QTableWidgetItem(str(Gil))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 0, item)
    item = QtWidgets.QTableWidgetItem('0')
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 1, item)
    aMimir(self,500)
def RehabilitarRecluso(self, paciente):
    self.tableWidget_5.setRowCount(self.tableWidget_5.rowCount() + 1)
    item = QtWidgets.QTableWidgetItem(str(paciente[self.getPos['ID']]))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    self.tableWidget_5.setItem(self.tableWidget_5.rowCount() - 1, 0, item)
    item = QtWidgets.QTableWidgetItem(str(paciente[self.getPos['TME']]))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    self.tableWidget_5.setItem(self.tableWidget_5.rowCount() - 1, 1, item)
    item = QtWidgets.QTableWidgetItem(str(paciente[self.getPos['TS']]))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    self.tableWidget_5.setItem(self.tableWidget_5.rowCount() - 1, 2, item)
def SalidaDelAnexo(self):
    if self.tableWidget_2.rowCount() == 0:
        return
    celda=0
    celdas = self.tableWidget_2.rowCount()
    while celda != celdas:
        TTB = self.tableWidget_2.item(celda,1)
        TTB = int(TTB.text())
        if TTB == 8:
            convicto = self.tableWidget_2.item(celda,0)
            convicto = int(convicto.text())
            self.Lotes[convicto - 1][self.getPos['Estado']] = 'Listo'
            self.tableWidget_2.removeRow(celda)
            RehabilitarRecluso(self,self.Lotes[convicto - 1])
            TirarADN(self,self.Lotes[convicto - 1])
            celdas-=1
            celda-=1
        else:
            item = QtWidgets.QTableWidgetItem(str(TTB+1))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_2.setItem(celda, 1, item)
        celda+=1
def Totos_A_Llenar(self, totoSize):
    MacetasPaLlenar = [self.MarcoTamaño] * ( totoSize // self.MarcoTamaño )
    if (totoSize % self.MarcoTamaño) != 0:
        MacetasPaLlenar.append(totoSize % self.MarcoTamaño)
    return MacetasPaLlenar
def BuscarBellakas(self, totoSize):
    TotosALlenar = Totos_A_Llenar(self,totoSize)
    NumToto=0
    for toto in self.Marcos:
        if toto[0] == 'Libre':
            NumToto+=1
            if NumToto == len(TotosALlenar):
                return True
    return False
def PagarMinita(self, sateo):
    Total = Totos_A_Llenar(self,sateo[self.getPos['Tamaño']])
    PlataPagada = 0
    for plaza in self.Marcos:
        if plaza[1] == sateo[self.getPos['ID']]:
            plaza[0] = 'Libre'
            plaza[1] = 0
            plaza[2] = 0
            plaza[3] = 0
            PlataPagada+=1
            if PlataPagada == len(Total):
                return
def TirarADN(self, semental, turra='Listo'):
    TotosALlenar = Totos_A_Llenar(self,semental[self.getPos['Tamaño']])
    NumToto = 0
    for row in range(self.tableWidget_6.rowCount()):
        for col in range(self.tableWidget_6.columnCount()//2):
            if self.Marcos[NumToto][1] == semental[self.getPos['ID']]:
                item = QtWidgets.QTableWidgetItem('█' * TotosALlenar[0])
                if turra == 'Finalizado':
                    item = QtWidgets.QTableWidgetItem('LIBRE')
                if turra == 'Listo':
                    brush = QtGui.QBrush(QtGui.QColor(225, self.Marcos[NumToto][2], 0))
                elif turra == 'Ejecucion':
                    brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
                elif turra == 'Bloqueado':
                    brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                else:
                    brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.tableWidget_6.setItem(row, col*2 + 1, item)
                TotosALlenar.pop(0)
                if len(TotosALlenar) == 0:
                    break
            NumToto+=1
        else:
            continue
        break
    if turra == 'Finalizado':
        PagarMinita(self,semental)
def PlantarSemilla(self, sateo):
    TotosALlenar = Totos_A_Llenar(self,sateo[self.getPos['Tamaño']])
    TotosLlenos = 0
    ColorDelToto = random.randint(1, 12) * 10 + 100
    i = 0
    for toto in self.Marcos:
        if toto[0] == 'Libre':
            toto[0] = 'Lleno'
            toto[1] = sateo[self.getPos['ID']]
            toto[2] = ColorDelToto
            toto[3] = TotosALlenar[i]
            TotosLlenos+=1
            i += 1
            if TotosLlenos == len(TotosALlenar):
                TirarADN(self,sateo)
                return
def DarDeAltaBecario(self):
    GatasDespachadas = self.tableWidget_5.rowCount() + self.tableWidget.rowCount() + self.tableWidget_2.rowCount()
    if GatasDespachadas == len(self.Lotes):
        return False
    if BuscarBellakas(self,self.Lotes[GatasDespachadas][self.getPos['Tamaño']]):
        self.tableWidget_5.setRowCount(self.tableWidget_5.rowCount() + 1)
        item = QtWidgets.QTableWidgetItem(str(self.Lotes[GatasDespachadas][self.getPos['ID']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_5.setItem(self.tableWidget_5.rowCount() - 1, 0, item)
        item = QtWidgets.QTableWidgetItem(str(self.Lotes[GatasDespachadas][self.getPos['TME']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_5.setItem(self.tableWidget_5.rowCount() - 1, 1, item)
        item = QtWidgets.QTableWidgetItem(str(self.Lotes[GatasDespachadas][self.getPos['TS']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_5.setItem(self.tableWidget_5.rowCount() - 1, 2, item)
        self.Lotes[GatasDespachadas][self.getPos['Estado']] = 'Listo'
        PlantarSemilla(self,self.Lotes[GatasDespachadas])
        
        try:
            self.lineEdit_23.setText('{}'.format(self.Lotes[GatasDespachadas + 1][self.getPos['ID']]))
            self.lineEdit_24.setText('{}'.format(self.Lotes[GatasDespachadas + 1][self.getPos['Tamaño']]))
            self.lineEdit_21.setText(str(len(self.Lotes) - (self.tableWidget_5.rowCount() + self.tableWidget.rowCount() + self.tableWidget_2.rowCount())))
            return True
        except:
            self.lineEdit_23.setText('Null')
            self.lineEdit_24.setText('Null')
            self.lineEdit_21.setText(str(len(self.Lotes) - (self.tableWidget_5.rowCount() + self.tableWidget.rowCount() + self.tableWidget_2.rowCount())))
            return False
    else:
        self.lineEdit_23.setText('{}'.format(self.Lotes[GatasDespachadas][self.getPos['ID']]))
        self.lineEdit_24.setText('{}'.format(self.Lotes[GatasDespachadas][self.getPos['Tamaño']]))
        self.lineEdit_21.setText(str(len(self.Lotes) - (self.tableWidget_5.rowCount() + self.tableWidget.rowCount() + self.tableWidget_2.rowCount())))
        return False
def IniciarCorrida(self):
    self.isAlgoritmoCorriendo = True
    self.lineEdit_22.setText('0')
    bandera = True
    while bandera:
        bandera = DarDeAltaBecario(self)
        aMimir(self,300)
    Victima = 0
    while self.tableWidget_5.rowCount() != 0 or self.tableWidget_2.rowCount() != 0:
        if self.tableWidget_5.rowCount() == 0:
            SalidaDelAnexo(self)
            MinitasSecandose(self)
            SubirImpuestos(self)
            aMimir(self,500)
            continue
        Victima = Victima % self.tableWidget_5.rowCount()
        ID_Victima = self.tableWidget_5.item(Victima, 0)
        ID_Victima = int(ID_Victima.text()) - 1
        if EsclavizarMiniom(self,self.Lotes[ID_Victima]):
            if self.BanderaInterrupcion:
                self.tableWidget_5.removeRow(Victima)
                self.BanderaInterrupcion = False
            else:
                item = QtWidgets.QTableWidgetItem(str(self.Lotes[ID_Victima][self.getPos['TS']]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_5.setItem(Victima, 2, item)
                Victima += 1
        else:
            self.tableWidget_5.removeRow(Victima)
            DarDeAltaBecario(self)
    self.isAlgoritmoCorriendo = False
    self.lineEdit_22.setStyleSheet("border:2px solid rgb(0, 255, 0);")
    self.pushButton_8.setStyleSheet("")
def EsclavizarMiniom(self,ProcesoEnEjecucion):
    self.BanderaEjecucion = True
    TirarADN(self,ProcesoEnEjecucion,'Ejecucion')
    if ProcesoEnEjecucion[self.getPos['TRa']] == -1:
        ProcesoEnEjecucion[self.getPos['TRa']] = self.ContadorGlobal - ProcesoEnEjecucion[self.getPos['TL']]
    ProcesoEnEjecucion[self.getPos['Estado']] ='Ejecucion'
    self.lineEdit_10.setText(str(ProcesoEnEjecucion[self.getPos['TME']]))
    self.lineEdit_11.setText(str(ProcesoEnEjecucion[self.getPos['TS']]))
    self.lineEdit_12.setText(str(ProcesoEnEjecucion[self.getPos['TME']] - ProcesoEnEjecucion[self.getPos['TS']]))
    self.lineEdit_27.setText(str(self.Quantum))
    aMimir(self,500)
    self.lineEdit_7.setText(str(ProcesoEnEjecucion[self.getPos['ID']]))
    self.lineEdit_9.setText(ProcesoEnEjecucion[self.getPos['Operacion']])
    QuantumTranscurrido =- 1
    for time in range(ProcesoEnEjecucion[self.getPos['TS']],ProcesoEnEjecucion[self.getPos['TME']]):
        QuantumTranscurrido += 1
        if self.Quantum - QuantumTranscurrido == 0:
            ProcesoEnEjecucion[self.getPos['Estado']] ='Listo'
            TirarADN(self,ProcesoEnEjecucion)
            self.lineEdit_7.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()
            self.lineEdit_12.clear()
            self.lineEdit_27.clear()
            return True
        if self.Bandera_Error:
            break
        if self.Bandera_P_C:
            while True:
                if not self.Bandera_P_C:
                    break
                aMimir(self,50)
        if self.BanderaInterrupcion:
            self.lineEdit_7.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()
            self.lineEdit_12.clear()
            self.lineEdit_27.clear()
            ProcesoEnEjecucion[self.getPos['Estado']] ='Bloqueado'
            TirarADN(self,ProcesoEnEjecucion,'Bloqueado')
            CaidaAlAnexo(self,ProcesoEnEjecucion[self.getPos['ID']])
            self.BanderaEjecucion = False
            return True
        self.lineEdit_11.setText(str(time + 1))
        self.lineEdit_12.setText(str(ProcesoEnEjecucion[self.getPos['TME']] - time - 1))
        self.lineEdit_27.setText(str(self.Quantum - QuantumTranscurrido - 1))
        ProcesoEnEjecucion[self.getPos['TS']] += 1
        MinitasSecandose(self)
        SubirImpuestos(self)
        SalidaDelAnexo(self)
        LlenarTablaBCP(self)
        VerMercadoSexual(self)
        if time != ProcesoEnEjecucion[self.getPos['TME']] - 1:
            aMimir(self,500)
    self.BanderaEjecucion = False
    aMimir(self,500)
    TirarADN(self,ProcesoEnEjecucion,'Finalizado')
    ProcesoEnEjecucion[self.getPos['TF']] = self.ContadorGlobal
    ProcesoEnEjecucion[self.getPos['TRo']] = ProcesoEnEjecucion[self.getPos['TF']] - ProcesoEnEjecucion[self.getPos['TL']]
    aMimir(self,200)
    self.lineEdit_7.clear()
    self.lineEdit_9.clear()
    self.lineEdit_10.clear()
    self.lineEdit_11.clear()
    self.lineEdit_12.clear()
    self.lineEdit_27.clear()
    aMimir(self,100)
    if self.Bandera_Error:
        ProcesoEnEjecucion[self.getPos['Resultado']] = 'ERROR'
    ProcesoEnEjecucion[self.getPos['Estado']] = 'Finalizado'
    ProcesosFinalizados(self,ProcesoEnEjecucion)
    LlenarTablaBCP(self)
    aMimir(self,500)
    return False
#Pagina Paginacion
def VerMercadoSexual(self):
    for celda in range(self.tableWidget_4.rowCount()-1):
        turro = self.Marcos[celda * 2][1]  
        if turro == 0:
            self.tableWidget_4.setSpan(celda, 1, 1, 2)
            item = QtWidgets.QTableWidgetItem('L I B R E')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_4.setItem(celda, 1, item)
            item = QtWidgets.QTableWidgetItem('')
            self.tableWidget_4.setItem(celda, 3, item)
        else:
            Estado = str(self.Lotes[turro - 1][self.getPos['Estado']])
            self.tableWidget_4.setSpan(celda, 1, 1, 1)
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[turro - 1][self.getPos['ID']]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_4.setItem(celda, 1, item)
            item = QtWidgets.QTableWidgetItem(Estado)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_4.setItem(celda, 2, item)
            item = QtWidgets.QTableWidgetItem('██' * self.Marcos[celda * 2][3])
            if Estado == 'Listo':
                brush = QtGui.QBrush(QtGui.QColor(225, self.Marcos[celda * 2][2], 0))
            elif Estado == 'Ejecucion':
                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
            elif Estado == 'Bloqueado':
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.tableWidget_4.setItem(celda, 3, item)
        turro = self.Marcos[celda * 2 + 1][1]  
        if turro == 0:
            self.tableWidget_4.setSpan(celda, 5, 1, 2)
            item = QtWidgets.QTableWidgetItem('L I B R E')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_4.setItem(celda, 5, item)
            item = QtWidgets.QTableWidgetItem('')
            self.tableWidget_4.setItem(celda, 4, item)
        else:
            Estado = str(self.Lotes[turro - 1][self.getPos['Estado']])
            self.tableWidget_4.setSpan(celda, 5, 1, 1)
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[turro - 1][self.getPos['ID']]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_4.setItem(celda, 6, item)
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[turro - 1][self.getPos['Estado']]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_4.setItem(celda, 5, item)
            item = QtWidgets.QTableWidgetItem('██' * self.Marcos[celda * 2 + 1][3])
            if Estado == 'Listo':
                brush = QtGui.QBrush(QtGui.QColor(225, self.Marcos[celda * 2 + 1][2], 0))
            elif Estado == 'Ejecucion':
                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
            elif Estado == 'Bloqueado':
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.tableWidget_4.setItem(celda, 4, item)
#PaginaFinalizados
def ProcesosFinalizados(self, Turro):
    MinitasLlenas = self.tableWidget.rowCount()
    self.tableWidget.setRowCount(MinitasLlenas + 1)
    item = QtWidgets.QTableWidgetItem(str(Turro[self.getPos['ID']]))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    if self.Bandera_Error:
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.FDiagPattern)
        item.setBackground(brush)
    self.tableWidget.setItem(MinitasLlenas, 0, item)
    item = QtWidgets.QTableWidgetItem(str(Turro[self.getPos['Operacion']]))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    if self.Bandera_Error:
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.FDiagPattern)
        item.setBackground(brush)
    self.tableWidget.setItem(MinitasLlenas, 1, item)
    item = QtWidgets.QTableWidgetItem(str(Turro[self.getPos['Resultado']]))
    if self.Bandera_Error:
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.FDiagPattern)
        item.setBackground(brush)
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    self.tableWidget.setItem(MinitasLlenas, 2, item)        
    self.Bandera_Error=False
def LlenarTablaBCP(self):
    self.tableWidget_3.setRowCount(len(self.Lotes))
    for i in range(self.tableWidget_3.rowCount()):
        item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['ID']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 0, item)
        item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['Estado']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 1, item)
        item = QtWidgets.QTableWidgetItem('Null')
        if self.Lotes[i][self.getPos['TL']] != -1:
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['TL']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 2, item)
        item = QtWidgets.QTableWidgetItem('Null')
        if self.Lotes[i][self.getPos['TF']] != -1:
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['TF']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 3, item)
        item = QtWidgets.QTableWidgetItem('Null')
        if self.Lotes[i][self.getPos['TRo']] != -1:
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['TRo']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 4, item)
        item = QtWidgets.QTableWidgetItem('Null')
        if self.Lotes[i][self.getPos['TRa']] != -1:
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['TRa']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 5, item)
        item = QtWidgets.QTableWidgetItem('Null')
        if self.Lotes[i][self.getPos['Estado']] != 'Nuevo':
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['TE']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 6, item)
        item = QtWidgets.QTableWidgetItem('Null')
        if self.Lotes[i][self.getPos['Estado']] != 'Nuevo':
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['TS']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 7, item)
        item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['TME']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 8, item)
        item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['Operacion']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 9, item)
        item = QtWidgets.QTableWidgetItem('Null')
        if self.Lotes[i][self.getPos['Estado']] =='Finalizado':
            item = QtWidgets.QTableWidgetItem(str(self.Lotes[i][self.getPos['Resultado']]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(i, 10, item)
def RestablecerValores(self):
    if not self.isAlgoritmoCorriendo:
        self.Lotes = []
        self.Quantum = 0
        self.ContadorGlobal = 0
        self.isAlgoritmoCorriendo = False
        self.BanderaEjecucion = False
        self.Bandera_Error = False
        self.Bandera_P_C = False
        self.BanderaInterrupcion = False
        self.lineEdit_2.clear()
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_3.clear()
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setReadOnly(False)
        self.pushButton_2.setEnabled(True)
        
        self.lineEdit_21.clear()
        self.lineEdit_23.clear()
        self.lineEdit_24.clear()
        
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_5.setRowCount(0)
        self.lineEdit_22.clear()
        self.lineEdit_22.setStyleSheet("border:2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(225, 190, 0, 255), stop:1 rgba(225, 100, 0, 255));")
        
        self.stackedWidget.setCurrentWidget(self.page_Asignar)
    else:
        self.pushButton_8.setStyleSheet("border:2px solid red")
def SubirImpuestos(self):
    self.ContadorGlobal += 1
    self.lineEdit_22.setText(str(self.ContadorGlobal))
