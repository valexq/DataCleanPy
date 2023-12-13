import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import pandas as pd
import datetime
from scipy.signal import savgol_filter
from filterpy.kalman import KalmanFilter
import numpy as np


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                self.df = None
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1021, 498)
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
        "font-weight: bold;\n""")
                self.ButtonCargar.setObjectName("ButtonCargar")
                self.ButtoBorrarTodo = QtWidgets.QPushButton(self.widget)
                self.ButtoBorrarTodo.setGeometry(QtCore.QRect(220, 0, 101, 31))
                self.ButtoBorrarTodo.setStyleSheet("background: rgb(132, 176, 177);\n"
        "font-weight: bold;\n"
        "\n""")
                self.ButtoBorrarTodo.setObjectName("ButtoBorrarTodo")
                self.ButtonDescargar = QtWidgets.QPushButton(self.widget)
                self.ButtonDescargar.setGeometry(QtCore.QRect(100, 0, 121, 31))
                self.ButtonDescargar.setStyleSheet("background: rgb(132, 176, 177);\n"
        "font-weight: bold;\n""")
                self.ButtonDescargar.setObjectName("ButtonDescargar")
                self.pushButton_ = QtWidgets.QPushButton(self.widget)
                self.pushButton_.setGeometry(QtCore.QRect(930, 0, 91, 31))
                self.pushButton_.setStyleSheet("background: rgb(132, 176, 177);\n"
        "border-color: rgb(0, 0, 0);\n"
        "font-weight: bold;\n""")
                self.pushButton_.setObjectName("pushButton_")
                self.graphicsView = QtWidgets.QGraphicsView(self.widget)
                self.graphicsView.setGeometry(QtCore.QRect(0, 30, 781, 450))
                self.graphicsView.setStyleSheet("background: rgb(255, 255, 255);\n"
        "border-color: rgb(0, 0, 0)")      
                self.scene = QtWidgets.QGraphicsScene(self.graphicsView)
                self.graphicsView.setScene(self.scene)
                self.pushButton_.clicked.connect(self.salir)
                self.ButtoBorrarTodo.clicked.connect(self.borrarTodo)
                self.graphicsView.setObjectName("graphicsView")
                self.groupBox = QtWidgets.QGroupBox(self.widget)
                self.groupBox.setGeometry(QtCore.QRect(780, 30, 251, 451))
                self.groupBox.setStyleSheet("background: rgb(165, 200, 202)")
                self.groupBox.setTitle("")
                self.groupBox.setObjectName("groupBox")
                self.comboBoxFiltrado = QtWidgets.QComboBox(self.groupBox)
                self.comboBoxFiltrado.setGeometry(QtCore.QRect(20, 100, 191, 22))
                self.comboBoxFiltrado.setObjectName("comboBoxTipo")
                self.label = QtWidgets.QLabel(self.groupBox)
                self.label.setGeometry(QtCore.QRect(20, 140, 171, 16))
                self.label.setStyleSheet("font-weight: bold;\n"
        "")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.groupBox)
                self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 16))
                self.label_2.setStyleSheet("font-weight: bold;\n""")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.groupBox)
                self.label_3.setGeometry(QtCore.QRect(40, 180, 47, 13))
                self.label_3.setStyleSheet("font-weight: bold;\n""")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.groupBox)
                self.label_4.setGeometry(QtCore.QRect(40, 220, 47, 13))
                self.label_4.setStyleSheet("font-weight: bold;\n""")
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.groupBox)
                self.label_5.setGeometry(QtCore.QRect(20, 310, 121, 16))
                self.label_5.setStyleSheet("font-weight: bold;\n""")
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.groupBox)
                self.label_6.setGeometry(QtCore.QRect(20, 340, 81, 16))
                self.label_6.setStyleSheet("font-weight: bold;\n""")
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
                self.ButtonAplicar.setStyleSheet("font-weight: bold;\n""")
                self.ButtonAplicar.setObjectName("ButtonAplicar")
                self.message = QtWidgets.QLineEdit(self.groupBox)
                self.message.setGeometry(QtCore.QRect(20, 370, 191, 31))
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
                self.Comboboxtipodato.addItem("")
                self.Comboboxtipodato.addItem("")
                self.comborangoinicio = QtWidgets.QComboBox(self.groupBox)
                self.comborangoinicio.setGeometry(QtCore.QRect(80, 170, 131, 22))
                self.comborangoinicio.setObjectName("comborangoinicio")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangoinicio.addItem("")
                self.comborangofinal = QtWidgets.QComboBox(self.groupBox)
                self.comborangofinal.setGeometry(QtCore.QRect(80, 210, 131, 22))
                self.comborangofinal.setObjectName("comborangofinal")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                self.comborangofinal.addItem("")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.figure, self.ax = plt.subplots()
                self.ax_smooth = self.ax.twinx()
                self.canvas = FigureCanvas(self.figure)
                self.layout = QtWidgets.QVBoxLayout(self.graphicsView)
                self.layout.addWidget(self.canvas)
                self.scene = QtWidgets.QGraphicsScene(self.graphicsView)
                self.graphicsView.setScene(self.scene)
                self.df = None
                
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "DataCleanPy"))
                self.ButtonCargar.setText(_translate("MainWindow", "Cargar datos"))
                self.ButtoBorrarTodo.setText(_translate("MainWindow", "Borrar todo"))
                ##self.ButtonDescargar.setText(_translate("MainWindow", "Descargar datos"))
                self.pushButton_.setText(_translate("MainWindow", "Salir"))
                self.comboBoxFiltrado.addItem("Interpolación")
                self.comboBoxFiltrado.addItem("Por desviación estándar")
                self.comboBoxFiltrado.addItem("Suavizado")
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
                self.comborangoinicio.setItemText(0, _translate("MainWindow", "0"))
                self.comborangoinicio.setItemText(1, _translate("MainWindow", "1000"))
                self.comborangoinicio.setItemText(2, _translate("MainWindow", "2000"))
                self.comborangoinicio.setItemText(3, _translate("MainWindow", "3000"))
                self.comborangoinicio.setItemText(4, _translate("MainWindow", "4000"))
                self.comborangoinicio.setItemText(5, _translate("MainWindow", "5000"))
                self.comborangoinicio.setItemText(6, _translate("MainWindow", "6000"))
                self.comborangoinicio.setItemText(7, _translate("MainWindow", "7000"))
                self.comborangoinicio.setItemText(8, _translate("MainWindow", "8000"))
                self.comborangoinicio.setItemText(9, _translate("MainWindow", "9000"))
                self.comborangoinicio.setItemText(10, _translate("MainWindow", "10000"))
                self.comborangoinicio.setItemText(11, _translate("MainWindow", "11000"))
                self.comborangoinicio.setItemText(12, _translate("MainWindow", "12000"))
                self.comborangoinicio.setItemText(13, _translate("MainWindow", "13000"))
                self.comborangoinicio.setItemText(14, _translate("MainWindow", "14000"))
                self.comborangoinicio.setItemText(15, _translate("MainWindow", "15000"))
                self.comborangoinicio.setItemText(16, _translate("MainWindow", "16000"))
                self.comborangoinicio.setItemText(17, _translate("MainWindow", "17000"))
                self.comborangofinal.setItemText(0, _translate("MainWindow", "0"))
                self.comborangofinal.setItemText(1, _translate("MainWindow", "1000"))
                self.comborangofinal.setItemText(2, _translate("MainWindow", "2000"))
                self.comborangofinal.setItemText(3, _translate("MainWindow", "3000"))
                self.comborangofinal.setItemText(4, _translate("MainWindow", "4000"))
                self.comborangofinal.setItemText(5, _translate("MainWindow", "5000"))
                self.comborangofinal.setItemText(6, _translate("MainWindow", "6000"))
                self.comborangofinal.setItemText(7, _translate("MainWindow", "7000"))
                self.comborangofinal.setItemText(8, _translate("MainWindow", "8000"))
                self.comborangofinal.setItemText(9, _translate("MainWindow", "9000"))
                self.comborangofinal.setItemText(10, _translate("MainWindow", "10000"))
                self.comborangofinal.setItemText(11, _translate("MainWindow", "11000"))
                self.comborangofinal.setItemText(12, _translate("MainWindow", "12000"))
                self.comborangofinal.setItemText(13, _translate("MainWindow", "13000"))
                self.comborangofinal.setItemText(14, _translate("MainWindow", "14000"))
                self.comborangofinal.setItemText(15, _translate("MainWindow", "15000"))
                self.comborangofinal.setItemText(16, _translate("MainWindow", "16000"))
                self.comborangofinal.setItemText(17, _translate("MainWindow", "17000"))
        
        #Función para abrir archivo
        def cargarDatos(self):
                # Abre una ventana de selección de archivo
                options = QFileDialog.Options()
                options |= QFileDialog.ReadOnly
                fileName, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos de Texto (*.txt);;Todos los archivos (*)", options=options)

                if fileName:
                        datosValidos = []                         # Inicializa los datos válidos
                        columns = ["Timestamp1", "Timestamps", "Sensor", "Data Type", "Dato 1", "Dato 2", "Dato 3"]                       # Define las columnas
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

                # Crea un DataFrame a partir de los datos validados 
                self.df = pd.DataFrame(datosValidos, columns=columns)

                # Almacenar el nombre del sensor y el tipo de dato
                sensorName = self.df.iloc[0, 2]
                dataType = self.df.iloc[0, 3]
                # Eliminar las columnas "Timestamps1", "Sensor" y "TipoDato" del DataFrame
                self.df = self.df.drop(["Timestamp1", "Sensor", "Data Type"], axis=1)
                self.LabelNombreSensor.setText(sensorName)
                self.LabelTipodeDato.setText(dataType)
                self.message.setText("Datos cargados correctamente")

        def FiltroKalman(self, df, columna):
                # Crear una copia del DataFrame original
                df_copy = df.copy()
                # Asegurarse de que la columna sea numérica
                df_copy[columna] = pd.to_numeric(df_copy[columna], errors='coerce')
                # Obtener solo la columna de interés
                datos = df_copy[columna].values
                # Crear un filtro de Kalman
                kf = KalmanFilter(dim_x=2, dim_z=1)
                # Inicializar el estado inicial y la matriz de covarianza
                kf.x = np.array([datos[0], 0])
                kf.P *= 1e6

                # Establecer las matrices de transición y observación
                kf.F = np.array([[1, 1], [0, 1]])
                kf.H = np.array([[1, 0]])

                # Establecer las covarianzas del proceso y de la medición
                kf.Q = np.array([[1, 1], [1, 2]])
                kf.R = 5

                # Aplicar el filtro de Kalman a los datos
                predicciones, _ = kf.batch_filter(datos)

                # Reemplazar la columna original con las predicciones del filtro de Kalman
                df_copy[columna] = predicciones[:, 0]

                return df_copy
        

        def FiltroInterpolacion(self, df,columna):
        # Crear una copia del DataFrame original
                df_filtrado = df.copy()
        # Asegurarse de que la columna sea numérica
                df_filtrado[columna] = pd.to_numeric(df_filtrado[columna], errors='coerce')
        # Interpolar los valores faltantes en la columna especificada
                df_filtrado[columna] = df_filtrado[columna].interpolate()
                return df_filtrado     

        #Creamos un filtro para realizar un suavizado de los datos
        def FiltroSuavizado(self, df, columna):
                # Copiar el DataFrame para evitar modificar el original
                df_filtrado = df.copy()
                datos_originales = df[columna].values
                datos_suavizados = savgol_filter(datos_originales, window_length=5, polyorder=3)
                df_filtrado[columna] = datos_suavizados
                return df_filtrado
        
        # Creamos una función para aplicar el filtro por desviación estándar
        def FiltroDesviacionEstandar(self, df, columna):
                 # Copiar el DataFrame para evitar modificar el original
                df_filtrado = df.copy()
                mediaData = df_filtrado[columna].mean()
                deviationData = df_filtrado[columna].std()
                # Definimos un umbral fijo en 3
                umbral = 3
                # Encontramos los valores que están dentro del rango y aplicamos el filtro por desviación estándar
                df_filtrado = df_filtrado[(df_filtrado[columna] >= mediaData - umbral * deviationData) & (df_filtrado[columna] <= mediaData + umbral * deviationData)]

                # Graficar los datos después de aplicar el filtro
                #self.graficarDatos(df_filtrado, rango_inicio, rango_final)
                return df_filtrado


        def graficarDatos(self, df_filtrado, columna):
                if df_filtrado is None or df_filtrado.empty:
                        self.message.setText("Aplique un filtro antes de graficar.")
                        return
                self.ax_smooth.cla()
                self.ax.cla()
                # Graficar los datos en el eje 'ax'
                current_tipo = self.Comboboxtipodato.currentText()
                
                self.ax.plot(df_filtrado['Timestamps'], df_filtrado[columna], label=columna)
                self.message.setText(f" {columna} graficado correctamente")
               
                # Restricción para mostrar cada 1000 puntos
                interval = 1000
                xticks_indices = range(0, len(df_filtrado), interval)
                xticks = df_filtrado['Timestamps'].iloc[xticks_indices]
                self.ax.tick_params(axis='x', rotation=45)
                # Configurar las marcas de tiempo en el eje x
                self.ax.set_xticks(xticks)
                self.ax.set_xticklabels([str(i) for i in xticks_indices])
                #self.ax.set_xlim(df_filtrado['Timestamps'].iloc[rango_inicio], df_filtrado['Timestamps'].iloc[rango_final])
                # Configurar la leyenda y los ejes
                self.ax.legend()
                self.ax.set_xlabel('Timestamps')
                self.ax.set_ylabel('Values')
                self.ax.autoscale()
                # Mostrar la figura en el lienzo
                # Configurar las marcas de tiempo en el eje x
                self.ax.set_xticks(xticks)
                self.ax.set_xticklabels([str(i) for i in xticks_indices])
                self.canvas.draw()

        def aplicar(self):
                inicio = int(self.comborangoinicio.currentText())
                final = int(self.comborangofinal.currentText())
                
                print(f"Rango Inicio: {inicio} - Rango final: {final}")
                df_filtrado = self.df.iloc[inicio:final]
                print(f"Dataset Filtrado: {df_filtrado.shape[0]}")

                columna = self.Comboboxtipodato.currentText()
                filtro = self.comboBoxFiltrado.currentText()
                if filtro == "Por desviación estándar":
                        df_resultado = self.FiltroDesviacionEstandar(df_filtrado, columna)
                        self.message.setText("Datos graficados correctamente por desviación")
                elif filtro == "Suavizado":
                        df_resultado = self.FiltroSuavizado(df_filtrado, columna)
                        self.message.setText("Datos graficados correctamente por suavizado")
                elif filtro == "Interpolación":
                        df_resultado = self.FiltroInterpolacion(df_filtrado, columna)
                        self.message.setText("Datos graficados correctamente por interpolación")
                elif filtro == "Filtro de Kallman":
                        df_resultado = self.FiltroInterpolacion(df_filtrado, columna)
                        self.message.setText("Datos graficados correctamente por interpolación")
                self.graficarDatos(df_resultado, columna)
                
        def borrarTodo(self):
                # Borrar el DataFrame si existe
                if self.df is not None:
                        self.df = None
                        self.LabelNombreSensor.clear()
                        self.LabelTipodeDato.clear()
                        self.message.setText("Datos borrados con éxito")

                        # Borrar los gráficos de la escena
                        if self.scene:
                                self.scene.clear()
                                self.ax.cla()
                                self.ax_smooth.cla()
                                self.canvas.draw()
        def salir(self):
                # Cerrar la ventana
                MainWindow.close()
                self.LabelNombreSensor.clear()
                self.LabelTipodeDato.clear()
                if self.scene:
                        self.scene.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_.clicked.connect(ui.salir)
    ui.ButtonCargar.clicked.connect(ui.cargarDatos)
    ui.ButtonAplicar.clicked.connect(ui.aplicar)
    ui.ButtoBorrarTodo.clicked.connect(ui.borrarTodo)
    MainWindow.show()
    sys.exit(app.exec_())
