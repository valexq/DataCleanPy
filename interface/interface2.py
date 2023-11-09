import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import pandas as pd
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
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
                self.label_3 = QtWidgets.QLabel(self.groupBox)
                self.label_3.setGeometry(QtCore.QRect(40, 180, 47, 13))
                self.label_3.setStyleSheet("font-weight: bold;\n"
        "")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.groupBox)
                self.label_4.setGeometry(QtCore.QRect(40, 220, 47, 13))
                self.label_4.setStyleSheet("font-weight: bold;\n"
        "")
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.groupBox)
                self.label_5.setGeometry(QtCore.QRect(20, 310, 121, 16))
                self.label_5.setStyleSheet("font-weight: bold;\n"
        "")
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.groupBox)
                self.label_6.setGeometry(QtCore.QRect(20, 340, 81, 16))
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
                #self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
                #self.dateTimeEdit.setGeometry(QtCore.QRect(100, 180, 131, 22))
                #self.dateTimeEdit.setObjectName("dateTimeEdit")
                #self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox)
                #self.dateTimeEdit_2.setGeometry(QtCore.QRect(100, 220, 131, 22))
                #self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                
                self.figure, self.ax = plt.subplots()
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
                self.ButtonDescargar.setText(_translate("MainWindow", "Descargar datos"))
                self.pushButton_.setText(_translate("MainWindow", "Salir"))
                self.comboBoxTipo.setItemText(0, _translate("MainWindow", "Ninguno"))
                self.comboBoxTipo.setItemText(1, _translate("MainWindow", "Filtro de Kalmann"))
                self.comboBoxTipo.setItemText(2, _translate("MainWindow", "Interpolación"))
                self.comboBoxTipo.setItemText(3, _translate("MainWindow", "Por desviación estándar"))
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

                # Eliminar el "0" al principio de los timestamps y convertirlos a fechas
                self.df['Timestamps'] = self.df['Timestamps'].str.lstrip('0')  # Eliminar el "0" al principio
                self.df['Timestamps'] = pd.to_datetime(self.df['Timestamps'].astype(int), unit='s') # Convertir a fechas

                #Eliminamos los datos menores a la fecha del 2020 para establecer un rango favorable para los datos en este caso específico
                specific_date = pd.to_datetime('2020-01-01')
                self.df = self.df[self.df['Timestamps'] >= specific_date]        
                
                # Obtener el timestamp mínimo y máximo del DataFrame
                #min_timestamp = self.df['Timestamps'].min()
                #max_timestamp = self.df['Timestamps'].max()

                # Configurar el rango en los QDateEdit
                #fecha_min = min_timestamp.to_pydatetime()
                #qdate_min = fecha_min.date()
                #self.dateTimeEdit.setDate(qdate_min)
                #fecha_max = max_timestamp.to_pydatetime()
                #qdate_max = fecha_max.date()
                #self.dateTimeEdit_2.setDate(qdate_max)
                
        # Creamos una función para aplicar el filtro por desviación estándar
        def FiltroDesviacionEstandar(self):
                mediaData1 = self.df['Data 1'].mean()
                mediaData2 = self.df['Data 2'].mean()
                mediaData3 = self.df['Data 3'].mean()
                deviationData1 = self.df['Data 1'].std()
                deviationData2 = self.df['Data 2'].std()
                deviationData3 = self.df['Data 3'].std()
                # Definimos un umbral fijo en 3
                umbral = 3
                # Encontramos los valores que están dentro del rango y aplicamos el filtro por desviación estándar
                self.df = self.df[(self.df['Data 1'] >= mediaData1 - umbral * deviationData1 ) & (self.df['Data 1'] <= mediaData1 + umbral * deviationData1)]
                self.df = self.df[(self.df['Data 2'] >= mediaData2 - umbral * deviationData2 ) & (self.df['Data 2'] <= mediaData2 + umbral * deviationData2)]
                self.df = self.df[(self.df['Data 3'] >= mediaData3 - umbral * deviationData3 ) & (self.df['Data 3'] <= mediaData3 + umbral * deviationData3)]
                # Imprimir el resultado
                print('La desviación estándar dato 1:', deviationData1)
                print('La desviación estándar dato 2:', deviationData2)
                print('La desviación estándar dato 3:', deviationData3)

                # Graficar los datos después de aplicar el filtro
                self.graficarDatos(self.df)


        def aplicarFiltro(self, tipo_filtro):
                # Obtener los límites seleccionados por el usuario en los combobox
                rango_inicio = int(self.comborangoinicio.currentText())
                rango_final = int(self.comborangofinal.currentText())

                # Filtrar por el rango seleccionado por el usuario
                self.df = self.df[(self.df['Timestamps'] >= rango_inicio) & (self.df['Timestamps'] <= rango_final)]

                # Llamar a la función específica del tipo de filtro
                if tipo_filtro == 'Filtro de Kalman':
                        self.aplicarFiltroKalman()
                elif tipo_filtro == 'Por desviación estándar':
                        self.aplicarFiltroDesviacionEstandar()
                elif tipo_filtro == 'Interpolación':
                        self.aplicarInterpolacion()

                # Graficar los datos después de aplicar el filtro
                self.graficarDatos(self.df)

        def graficarDatos(self, df):
                # Crear una figura de Matplotlib y un lienzo para Qt
                #figure, ax = plt.subplots()
                #canvas = FigureCanvas(figure)
                #layout = QtWidgets.QVBoxLayout(self.graphicsView)
                #layout.addWidget(canvas)
                # ... (código previo)

                # ... (código previo)

              # ... (código previo)

# ... (código posterior)

# ... (código posterior)

# ... (código posterior)
                if self.df is None:
                        self.message.setText("Cargue un archivo")
                        return
                self.ax.cla()
                self.scene.clear()

                # Graficar los datos en el eje 'ax'
                #ax.plot(df['Timestamps'], df['Data 1'], label='Data 1')
                currentTipo = ui.Comboboxtipodato.currentText()
                currentFiltro = ui.comboBoxTipo.currentText()
                print('current tipo', currentTipo)

                if currentTipo == 'Dato 1' :
                        self.ax.plot(self.df['Timestamps'], self.df['Data 1'], label='Data 1')
                        self.message.setText("Data 1 graficada correctamente")

                elif currentTipo == 'Dato 2' :
                        self.ax.plot(self.df['Timestamps'], self.df['Data 2'], label='Data 2')
                        self.message.setText("Data 2 graficada correctamente")
                elif currentTipo == 'Dato 3':
                        self.ax.plot(self.df['Timestamps'], self.df['Data 3'], label='Data 3')
                        self.message.setText("Data 2 graficada correctamente")
                
                # Graficar los datos en el eje 'ax'
                # Restricción para mostrar cada 1000 puntos
                 # Restricción para mostrar cada 1000 puntos
                interval = 1000
                xticks_indices = range(0, len(self.df), interval)
                xticks = self.df['Timestamps'].iloc[xticks_indices]
                self.ax.tick_params(axis='x', rotation=45)  # Puedes ajustar el ángulo de rotación según tus preferencias

                # Configurar las marcas de tiempo en el eje x
                self.ax.set_xticks(xticks)
                self.ax.set_xticklabels([str(i) for i in xticks_indices])

                # Establecer límites del eje x para mostrar cada 12 horas
                #start_timestamp =self. df['Timestamps'].min()
                #end_timestamp = self.df['Timestamps'].max()
                # Ajustar el límite inferior para alinear con  un múltiplo de 12 horas
                #start_timestamp = start_timestamp.replace(hour=(start_timestamp.hour // 12) * 12)
                # Crear una lista de marcas de tiempo cada 12 horas
                #interval = pd.Timedelta(hours=12)       
                #xticks = pd.date_range(start=start_timestamp, end=end_timestamp, freq=interval)
                #self.ax.set_xlim(start_timestamp, end_timestamp)
                # Formatear las marcas de tiempo en el eje x
                #self.ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d %H:%M'))
                # Configurar la leyenda y los ejes
                self.ax.legend()
                self.ax.set_xlabel('Timestamps')
                self.ax.set_ylabel('Values')
        # Mostrar la figura en el lienzo
                self.canvas.draw()
                #self.graficarDatos(self.df)
                self.message.setText("Datos procesados")

                
                
        def ButtonAplicarClicked(self):
                if self.df is None:
                        self.message.setText("Cargue un archivo antes de aplicar el filtro.")
                        return
                self.aplicarFiltro()
  
        def borrarTodo(self):
        # Borrar el DataFrame si existe
                if self.df is not None:
                        self.df = None
                        self.LabelNombreSensor.clear()
                        self.LabelTipodeDato.clear()
                        self.message.setText("Datos borrados con éxito")


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
    ui.ButtonAplicar.clicked.connect(ui.graficarDatos)
    ui.ButtoBorrarTodo.clicked.connect(ui.borrarTodo)
    ui.pushButton_.clicked.connect(ui.ButtonAplicarClicked)
    MainWindow.show()
    sys.exit(app.exec_())
