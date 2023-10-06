import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DataCleanPy")
        MainWindow.resize(1023, 480)
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
        self.graphicsView.setGeometry(QtCore.QRect(0, 30, 781, 371))
        self.graphicsView.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0)")
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(780, 30, 251, 371))
        self.groupBox.setStyleSheet("background: rgb(165, 200, 202)")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBoxTipo = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxTipo.setGeometry(QtCore.QRect(20, 30, 191, 22))
        self.comboBoxTipo.setObjectName("comboBoxTipo")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 60, 141, 16))
        self.label.setStyleSheet("font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label_2.setStyleSheet("font-weight: bold;\n"
"")
        self.label_2.setObjectName("label_2")
        self.InicialDate = QtWidgets.QDateEdit(self.groupBox)
        self.InicialDate.setGeometry(QtCore.QRect(70, 90, 141, 22))
        self.InicialDate.setObjectName("InicialDate")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.label_3.setStyleSheet("font-weight: bold;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.label_4.setStyleSheet("font-weight: bold;\n"
"")
        self.label_4.setObjectName("label_4")
        self.FinalDate = QtWidgets.QDateEdit(self.groupBox)
        self.FinalDate.setGeometry(QtCore.QRect(70, 130, 141, 22))
        self.FinalDate.setObjectName("FinalDate")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 101, 16))
        self.label_5.setStyleSheet("font-weight: bold;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 81, 16))
        self.label_6.setStyleSheet("font-weight: bold;\n"
"")
        self.label_6.setObjectName("label_6")
        self.LabelNombreSensor = QtWidgets.QLabel(self.groupBox)
        self.LabelNombreSensor.setGeometry(QtCore.QRect(140, 270, 71, 16))
        self.LabelNombreSensor.setText("")
        self.LabelNombreSensor.setObjectName("LabelNombreSensor")
        self.LabelTipodeDato = QtWidgets.QLabel(self.groupBox)
        self.LabelTipodeDato.setGeometry(QtCore.QRect(110, 300, 71, 16))
        self.LabelTipodeDato.setText("")
        self.LabelTipodeDato.setObjectName("LabelTipodeDato")
        self.ButtonAplicar = QtWidgets.QPushButton(self.groupBox)
        self.ButtonAplicar.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.ButtonAplicar.setStyleSheet("font-weight: bold;\n"
"")
        self.ButtonAplicar.setObjectName("ButtonAplicar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_.clicked.connect(self.salir)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonCargar.setText(_translate("MainWindow", "Cargar Archivo"))
        self.ButtoBorrarTodo.setText(_translate("MainWindow", "Borrar todo"))
        self.ButtonDescargar.setText(_translate("MainWindow", "Descargar archivo"))
        self.pushButton_.setText(_translate("MainWindow", "Salir"))
        self.comboBoxTipo.setItemText(0, _translate("MainWindow", "Promediar"))
        self.comboBoxTipo.setItemText(1, _translate("MainWindow", "Filtro de Kalmann"))
        self.comboBoxTipo.setItemText(2, _translate("MainWindow", "Limpiar"))
        self.comboBoxTipo.setItemText(3, _translate("MainWindow", "Interpolación"))
        self.label.setText(_translate("MainWindow", "Rango de filtrado por fecha:"))
        self.label_2.setText(_translate("MainWindow", "Tipo de filtrado:"))
        self.label_3.setText(_translate("MainWindow", "Inicio:"))
        self.label_4.setText(_translate("MainWindow", "Fin:"))
        self.label_5.setText(_translate("MainWindow", "Nombre del sensor:"))
        self.label_6.setText(_translate("MainWindow", "Tipo de datos:"))
        self.ButtonAplicar.setText(_translate("MainWindow", "Aplicar"))


#Función para abrir archivo
    def cargarArchivo(self):
    # Abre una ventana de selección de archivo
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos de Texto (*.txt);;Todos los archivos (*)", options=options)

        if fileName:
                datosValidos = []                         # Inicializa los datos válidos
                columns = ["Timestamp1", "Timestamps", "Sensor", "Data Type", "Data 1", "Data 2", "Data 3"]                       # Define las columnas
                with open(fileName, 'r') as file:         # Abre el archivo de texto                    y                                                  procesa cada línea      
                        for line in file:
                                parts = line.strip().split(' ') # Verifica que la línea tenga la cantidad esperada de           campos
                                if len(parts) == 7: # Convierte los campos numéricos a float si es necesario
                                        try:
                                                parts[4] = float(parts[4])
                                                parts[5] = float(parts[5])
                                                parts[6] = float(parts[6])
                                                datosValidos.append(parts)
                                        except ValueError:
                                                print(f"Error en la línea: {line.strip()}")
                                        continue  # Salta esta línea si hay un error en los campos numéricos

        # Crea un DataFrame a partir de los datos válidos
        df = pd.DataFrame(datosValidos, columns=columns)

        # Almacenar el nombre del sensor y el tipo de dato
        sensorName = df.iloc[0, 2]
        dataType = df.iloc[0, 3]
        # Eliminar las columnas "Timestamps1", "Sensor" y "TipoDato" del DataFrame
        df = df.drop(["Timestamp1", "Sensor", "Data Type"], axis=1)
        self.LabelNombreSensor.setText(sensorName)
        self.LabelTipodeDato.setText(dataType)
        self.graficarDatos(df)
        print("Datos cargados con exito")
        
    def graficarDatos(self, df):
        if self.scene is None:
            self.scene = QtWidgets.QGraphicsScene(self.graphicsView)
            self.graphicsView.setScene(self.scene)
            self.scene.clear()
        
        # Crear una figura de Matplotlib y un lienzo para Qt
        figure, ax = plt.subplots()
        canvas = FigureCanvas(figure)
        layout = QtWidgets.QVBoxLayout(self.graphicsView)
        layout.addWidget(canvas)

        # Graficar los datos en el eje 'ax'
        ax.plot(df['Timestamps'], df['Data 1'], label='Data 1')
        ax.plot(df['Timestamps'], df['Data 2'], label='Data 2')
        ax.plot(df['Timestamps'], df['Data 3'], label='Data 3')

        # Configurar la leyenda y los ejes
        ax.legend()
        ax.set_xlabel('Timestamps')
        ax.set_ylabel('Values')

        
        # Mostrar la figura en el lienzo
        canvas.draw()

    def salir(self):
        # Cerrar la ventana
        MainWindow.close()
        self.LabelNombreSensor.clear()
        self.LabelTipodeDato.clear()
        if self.scene:
            self.scene.clear()

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        ui.ButtonCargar.clicked.connect(ui.cargarArchivo)

        MainWindow.show()
        sys.exit(app.exec_())
