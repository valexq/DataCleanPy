import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import pandas as pd
import datetime



def __init__(self):
    self.fecha_inicial = None
    self.fecha_final = None
    self.df = None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def __init__(self):
          self.fecha_inicial = None
          self.fecha_final = None
          self.df = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1021, 491))
        self.widget.setStyleSheet("background: rgb(132, 176, 177);")
        self.widget.setObjectName("widget")
        self.ButtonCargar = QtWidgets.QPushButton(self.widget)
        self.ButtonCargar.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.ButtonCargar.setStyleSheet("background: rgb(132, 176, 177);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font-weight: bold;\n"
"")
        self.ButtonCargar.setObjectName("ButtonCargar")
        self.ButtoBorrarTodo = QtWidgets.QPushButton(self.widget)
        self.ButtoBorrarTodo.setGeometry(QtCore.QRect(220, 0, 101, 31))
        self.ButtoBorrarTodo.setStyleSheet("background: rgb(132, 176, 177);\n"
"font-weight: bold;\n"
"\n"
"")
        self.ButtoBorrarTodo.setObjectName("ButtoBorrarTodo")
        self.ButtonDescargar = QtWidgets.QPushButton(self.widget)
        self.ButtonDescargar.setGeometry(QtCore.QRect(100, 0, 121, 31))
        self.ButtonDescargar.setStyleSheet("background: rgb(132, 176, 177);\n"
"font-weight: bold;\n"
"")
        self.ButtonDescargar.setObjectName("ButtonDescargar")
        self.pushButton_ = QtWidgets.QPushButton(self.widget)
        self.pushButton_.setGeometry(QtCore.QRect(930, 0, 91, 31))
        self.pushButton_.setStyleSheet("background: rgb(132, 176, 177);\n"
"border-color: rgb(0, 0, 0);\n"
"font-weight: bold;\n"
"")
        
        self.pushButton_.setObjectName("pushButton_")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 30, 781, 401))
        self.graphicsView.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0)")
        self.graphicsView.setObjectName("graphicsView")

        self.scene = QtWidgets.QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)
        self.pushButton_.clicked.connect(self.salir)
        self.ButtoBorrarTodo.clicked.connect(self.borrarTodo)

        
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(780, 30, 251, 451))
        self.groupBox.setStyleSheet("background:  rgb(165, 200, 202)")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBoxTipo = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxTipo.setGeometry(QtCore.QRect(20, 100, 191, 22))
        self.comboBoxTipo.setObjectName("comboBoxTipo")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 140, 171, 16))
        self.label.setStyleSheet("font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_2.setStyleSheet("font-weight: bold;\n"
"")
        self.label_2.setObjectName("label_2")
        ##self.InicialDate = QtWidgets.QDateEdit(self.groupBox)
        ##self.InicialDate.setGeometry(QtCore.QRect(70, 90, 141, 22))
        ##self.InicialDate.setObjectName("InicialDate")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 47, 13))
        self.label_3.setStyleSheet("font-weight: bold;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.label_4.setStyleSheet("font-weight: bold;\n"
"")
        self.label_4.setObjectName("label_4")
        ##self.FinalDate = QtWidgets.QDateEdit(self.groupBox)
        ##self.FinalDate.setGeometry(QtCore.QRect(70, 130, 141, 22))
        ##self.FinalDate.setObjectName("FinalDate")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 121, 16))
        self.label_5.setStyleSheet("font-weight: bold;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 81, 16))
        self.label_6.setStyleSheet("font-weight: bold;\n"
"")
        self.label_6.setObjectName("label_6")
        self.LabelNombreSensor = QtWidgets.QLabel(self.groupBox)
        self.LabelNombreSensor.setGeometry(QtCore.QRect(140, 310, 71, 16))
        self.LabelNombreSensor.setText("")
        self.LabelNombreSensor.setObjectName("LabelNombreSensor")
        self.LabelTipodeDato = QtWidgets.QLabel(self.groupBox)
        self.LabelTipodeDato.setGeometry(QtCore.QRect(110, 340, 71, 16))
        self.LabelTipodeDato.setText("")
        self.LabelTipodeDato.setObjectName("LabelTipodeDato")
        self.ButtonAplicar = QtWidgets.QPushButton(self.groupBox)
        self.ButtonAplicar.setGeometry(QtCore.QRect(130, 260, 75, 23))
        self.ButtonAplicar.setStyleSheet("font-weight: bold;\n"
"")
        self.ButtonAplicar.setObjectName("ButtonAplicar")
        self.message = QtWidgets.QLineEdit(self.groupBox)
        self.message.setGeometry(QtCore.QRect(20, 370, 201, 20))
        self.message.setObjectName("message")
        self.message.setReadOnly(True)
        self.message.setObjectName("message")
        self.labelDato = QtWidgets.QLabel(self.groupBox)
        self.labelDato.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.labelDato.setStyleSheet("font-weight: bold;\n"
"")
        self.labelDato.setObjectName("labelDato")
        self.Comboboxtipodato = QtWidgets.QComboBox(self.groupBox)
        self.Comboboxtipodato.setGeometry(QtCore.QRect(20, 50, 191, 22))
        self.Comboboxtipodato.setObjectName("Comboboxtipodato")
        self.Comboboxtipodato.addItem("")
        self.Comboboxtipodato.addItem("")
        self.Comboboxtipodato.addItem("")

        self.comboInicio_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboInicio_2.setGeometry(QtCore.QRect(100, 180, 111, 22))
        self.comboInicio_2.setObjectName("comboInicio_2")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboInicio_2.addItem("")
        self.comboFinal = QtWidgets.QComboBox(self.groupBox)
        self.comboFinal.setGeometry(QtCore.QRect(100, 220, 111, 22))
        self.comboFinal.setObjectName("comboFinal")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        self.comboFinal.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DataCleanPy", "DataCleanPy"))
        self.ButtonCargar.setText(_translate("MainWindow", "Cargar datos"))
        self.ButtoBorrarTodo.setText(_translate("MainWindow", "Borrar todo"))
        self.ButtonDescargar.setText(_translate("MainWindow", "Descargar datos"))
        self.pushButton_.setText(_translate("MainWindow", "Salir"))
        self.comboBoxTipo.setItemText(0, _translate("MainWindow", "Promediar"))
        self.comboBoxTipo.setItemText(1, _translate("MainWindow", "Filtro de Kalmann"))
        self.comboBoxTipo.setItemText(3, _translate("MainWindow", "Interpolación"))
        self.label.setText(_translate("MainWindow", "Rango de filtrado por fecha:"))
        self.label_2.setText(_translate("MainWindow", "Tipo de filtrado:"))
        self.label_3.setText(_translate("MainWindow", "Inicio:"))
        self.label_4.setText(_translate("MainWindow", "Fin:"))
        self.label_5.setText(_translate("MainWindow", "Nombre del sensor:"))
        self.label_6.setText(_translate("MainWindow", "Tipo de datos:"))
        self.ButtonAplicar.setText(_translate("MainWindow", "Aplicar"))
        self.labelDato.setText(_translate("MainWindow", "Dato:"))
        self.Comboboxtipodato.setItemText(0, _translate("MainWindow", "Dato 1"))
        self.Comboboxtipodato.setItemText(1, _translate("MainWindow", "Dato 2"))
        self.Comboboxtipodato.setItemText(2, _translate("MainWindow", "Dato 3"))
        self.comboInicio_2.setItemText(0, _translate("MainWindow", "1000"))
        self.comboInicio_2.setItemText(1, _translate("MainWindow", "2000"))
        self.comboInicio_2.setItemText(2, _translate("MainWindow", "3000"))
        self.comboInicio_2.setItemText(3, _translate("MainWindow", "4000"))
        self.comboInicio_2.setItemText(4, _translate("MainWindow", "5000"))
        self.comboInicio_2.setItemText(5, _translate("MainWindow", "6000"))
        self.comboInicio_2.setItemText(6, _translate("MainWindow", "7000"))
        self.comboInicio_2.setItemText(7, _translate("MainWindow", "8000"))
        self.comboInicio_2.setItemText(8, _translate("MainWindow", "9000"))
        self.comboInicio_2.setItemText(9, _translate("MainWindow", "10000"))
        self.comboInicio_2.setItemText(10, _translate("MainWindow", "11000"))
        self.comboInicio_2.setItemText(11, _translate("MainWindow", "12000"))
        self.comboInicio_2.setItemText(12, _translate("MainWindow", "13000"))
        self.comboInicio_2.setItemText(13, _translate("MainWindow", "14000"))
        self.comboInicio_2.setItemText(14, _translate("MainWindow", "15000"))
        self.comboInicio_2.setItemText(15, _translate("MainWindow", "16000"))
        self.comboInicio_2.setItemText(16, _translate("MainWindow", "17000"))
        self.comboInicio_2.setItemText(17, _translate("MainWindow", "1800"))
        self.comboFinal.setItemText(0, _translate("MainWindow", "1000"))
        self.comboFinal.setItemText(1, _translate("MainWindow", "2000"))
        self.comboFinal.setItemText(2, _translate("MainWindow", "3000"))
        self.comboFinal.setItemText(3, _translate("MainWindow", "4000"))
        self.comboFinal.setItemText(4, _translate("MainWindow", "5000"))
        self.comboFinal.setItemText(5, _translate("MainWindow", "6000"))
        self.comboFinal.setItemText(6, _translate("MainWindow", "7000"))
        self.comboFinal.setItemText(7, _translate("MainWindow", "8000"))
        self.comboFinal.setItemText(8, _translate("MainWindow", "9000"))
        self.comboFinal.setItemText(9, _translate("MainWindow", "10000"))
        self.comboFinal.setItemText(10, _translate("MainWindow", "11000"))
        self.comboFinal.setItemText(11, _translate("MainWindow", "12000"))
        self.comboFinal.setItemText(12, _translate("MainWindow", "13000"))
        self.comboFinal.setItemText(13, _translate("MainWindow", "14000"))
        self.comboFinal.setItemText(14, _translate("MainWindow", "15000"))
        self.comboFinal.setItemText(15, _translate("MainWindow", "16000"))
        self.comboFinal.setItemText(16, _translate("MainWindow", "17000"))
        self.comboFinal.setItemText(17, _translate("MainWindow", "18000"))
