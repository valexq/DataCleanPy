import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 590)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: black\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.grafica = QtWidgets.QGraphicsView(self.frame_2)
        self.grafica.setGeometry(QtCore.QRect(0, -10, 631, 361))
        self.grafica.setStyleSheet("background-color: gray\n"
"")
        self.grafica.setObjectName("grafica")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(690, 0, 261, 361))
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 241, 401))
        self.groupBox.setStyleSheet("background-color : rgb(255, 255, 255)")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBoxTipo = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxTipo.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.comboBoxTipo.setObjectName("comboBoxTipo")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 60, 131, 16))
        self.label.setObjectName("label")
        self.Buttonaplicar = QtWidgets.QPushButton(self.groupBox)
        self.Buttonaplicar.setGeometry(QtCore.QRect(150, 180, 75, 23))
        self.Buttonaplicar.setObjectName("Buttonaplicar")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.InicialDate = QtWidgets.QDateEdit(self.groupBox)
        self.InicialDate.setGeometry(QtCore.QRect(70, 90, 110, 22))
        self.InicialDate.setObjectName("InicialDate")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.label_4.setObjectName("label_4")
        self.FinalDate = QtWidgets.QDateEdit(self.groupBox)
        self.FinalDate.setGeometry(QtCore.QRect(70, 130, 110, 22))
        self.FinalDate.setObjectName("FinalDate")
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 963, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setTearOffEnabled(False)
        self.menuMenu.setObjectName("menuMenu")
        self.menuCargar_archivo = QtWidgets.QMenu(self.menubar)
        self.menuCargar_archivo.setObjectName("menuCargar_archivo")
        
        self.menuIntegraci_n_de_servicios = QtWidgets.QMenu(self.menubar)
        self.menuIntegraci_n_de_servicios.setObjectName("menuIntegraci_n_de_servicios")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbrir_archivo = QtWidgets.QAction(MainWindow)
        self.actionAbrir_archivo.setIconVisibleInMenu(True)
        self.actionAbrir_archivo.setPriority(QtWidgets.QAction.HighPriority)
        self.actionAbrir_archivo.setObjectName("actionAbrir_archivo")
        self.actionAbrir_archivo.triggered.connect(self.cargarArchivo)# CARGAR EL ARCHIVO
        ##self.actionAbrir_archivo.triggered.connect(self.cargarArchivo)
        self.actionGuardar_resultados = QtWidgets.QAction(MainWindow)
        self.actionGuardar_resultados.setObjectName("actionGuardar_resultados")
        self.actionTXT = QtWidgets.QAction(MainWindow)
        self.actionTXT.setObjectName("actionTXT")
        self.actionCSV = QtWidgets.QAction(MainWindow)
        self.actionCSV.setObjectName("actionCSV")
        self.actionThingsboard = QtWidgets.QAction(MainWindow)
        self.actionThingsboard.setObjectName("actionThingsboard")
        self.actionBorra_todo = QtWidgets.QAction(MainWindow)
        self.actionBorra_todo.setObjectName("actionBorra_todo")
        self.menuMenu.addAction(self.actionAbrir_archivo)
        self.menuMenu.addAction(self.actionGuardar_resultados)
        self.menuMenu.addAction(self.actionBorra_todo)
        self.menuCargar_archivo.addAction(self.actionTXT)
        self.menuCargar_archivo.addAction(self.actionCSV)
        self.menuIntegraci_n_de_servicios.addAction(self.actionThingsboard)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuCargar_archivo.menuAction())
        self.menubar.addAction(self.menuIntegraci_n_de_servicios.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataCleanPy"))
        self.comboBoxTipo.setItemText(0, _translate("MainWindow", "Promediar"))
        self.comboBoxTipo.setItemText(1, _translate("MainWindow", "Filtro de Kalmann"))
        self.comboBoxTipo.setItemText(2, _translate("MainWindow", "Limpiar"))
        self.comboBoxTipo.setItemText(3, _translate("MainWindow", "Interpolación"))
        self.label.setText(_translate("MainWindow", "Rango de filtrado por fecha"))
        self.Buttonaplicar.setText(_translate("MainWindow", "Aplicar"))
        self.label_2.setText(_translate("MainWindow", "Tipo de filtrado"))
        self.label_3.setText(_translate("MainWindow", "Inicio:"))
        self.label_4.setText(_translate("MainWindow", "Fin:"))
        self.menuMenu.setTitle(_translate("MainWindow", "Archivo"))
        self.menuIntegraci_n_de_servicios.setTitle(_translate("MainWindow", "Integración de servicios"))
        self.actionAbrir_archivo.setText(_translate("MainWindow", "Cargar archivo"))
        self.actionAbrir_archivo.setIconText(_translate("MainWindow", "Cargar archivo"))
        self.actionGuardar_resultados.setText(_translate("MainWindow", "Descargar archivo"))
        self.actionThingsboard.setText(_translate("MainWindow", "Thingsboard"))
        self.actionBorra_todo.setText(_translate("MainWindow", "Eliminar cambios"))

    #Función para abrir archivo
    def cargarArchivo():
    # Abre una ventana de selección de archivo
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos de Texto (*.txt);;Todos los archivos (*)", options=options)

        if fileName:
            # Inicializa los datos válidos
            datosValidos = []

            # Define las columnas
            columns = ["Timestamp1", "Timestamps", "Sensor", "Data Type", "Data 1", "Data 2", "Data 3"]

            # Abre el archivo de texto y procesa cada línea
            with open(fileName, 'r') as file:
                for line in file:
                    parts = line.strip().split(' ')
                # Verifica que la línea tenga la cantidad esperada de campos
                    if len(parts) == 7:
                    # Convertir los campos numéricos a float si es necesario
                        try:
                            parts[4] = float(parts[4])
                            parts[5] = float(parts[5])
                            parts[6] = float(parts[6])
                            datosValidos.append(parts)
                        except ValueError:
                            print(f"Error en la línea: {line.strip()}")
                            continue  # Saltar esta línea si hay un error en los campos numéricos

        # Crea un DataFrame a partir de los datos válidos
        df = pd.DataFrame(datosValidos, columns=columns)

        # Almacenar el nombre del sensor y el tipo de dato
        sensorName = df.iloc[0, 2]
        dataType = df.iloc[0, 3]

        # Eliminar las columnas "Timestamps1", "Sensor" y "TipoDato" del DataFrame
        df = df.drop(["Timestamp1", "Sensor", "Data Type"], axis=1)

        
        #print("Nombre del sensor:", sensorName)
        #print("Tipo de dato:", dataType)
        #print(df)
                
                

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
