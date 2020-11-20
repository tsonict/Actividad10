from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from random import randint
from particulas import Particulas
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.particulas = Particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar_pushbutton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushbutton.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.ordenID_pushButton.clicked.connect(self.orden_ID)
        self.ui.orden_distancia_pushButton.clicked.connect(self.orden_Distancia)
        self.ui.orden_velocidad_pushButton.clicked.connect(self.orden_Velocidad)

    def wheelEvent(self, event):
        if event.delta() >0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def orden_ID(self):
        self.particulas.orden_id()

    @Slot()
    def orden_Distancia(self):
        self.particulas.orden_distancia()

    @Slot()
    def orden_Velocidad(self):
        self.particulas.orden_velocidad()

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.particulas:
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)

            self.scene.addEllipse(particula.origenx, particula.origeny, 3, 3, pen)
            self.scene.addEllipse(particula.destinox, particula.destinoy, 3, 3, pen)
            self.scene.addLine(particula.origenx, particula.origeny, particula.destinox, particula.destinoy, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def buscar_id(self):
        id_buscado = self.ui.busca_lineEdit.text()
        encontrado = False
        for particula in self.particulas:
            if id_buscado == particula.id:
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(1)
                self.ui.tableWidget.setColumnCount(10)
                headers = ["Id", "Origen x", "Origen y", "Destino x", "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)

                id_widget = QTableWidgetItem(particula.id)
                origenx_widget = QTableWidgetItem(str(particula.origenx))
                origeny_widget = QTableWidgetItem(str(particula.origeny))
                destinox_widget = QTableWidgetItem(str(particula.destinox))
                destinoy_widget = QTableWidgetItem(str(particula.destinoy))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tableWidget.setItem(0, 0, id_widget)
                self.ui.tableWidget.setItem(0, 1, origenx_widget)
                self.ui.tableWidget.setItem(0, 2, origeny_widget)
                self.ui.tableWidget.setItem(0, 3, destinox_widget)
                self.ui.tableWidget.setItem(0, 4, destinoy_widget)
                self.ui.tableWidget.setItem(0, 5, velocidad_widget)
                self.ui.tableWidget.setItem(0, 6, red_widget)
                self.ui.tableWidget.setItem(0, 7, green_widget)
                self.ui.tableWidget.setItem(0, 8, blue_widget)
                self.ui.tableWidget.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            self.ui.tableWidget.clear()
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el id "{id_buscado}" no fue encontrado'
            )
        


    @Slot()
    def mostrar_tabla(self):
        self.ui.tableWidget.setColumnCount(10)
        headers = ["Id", "Origen x", "Origen y", "Destino x", "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        self.ui.tableWidget.setRowCount(len(self.particulas))
        row =0
        for particula in self.particulas:
            id_widget = QTableWidgetItem(particula.id)
            origenx_widget = QTableWidgetItem(str(particula.origenx))
            origeny_widget = QTableWidgetItem(str(particula.origeny))
            destinox_widget = QTableWidgetItem(str(particula.destinox))
            destinoy_widget = QTableWidgetItem(str(particula.destinoy))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tableWidget.setItem(row, 0, id_widget)
            self.ui.tableWidget.setItem(row, 1, origenx_widget)
            self.ui.tableWidget.setItem(row, 2, origeny_widget)
            self.ui.tableWidget.setItem(row, 3, destinox_widget)
            self.ui.tableWidget.setItem(row, 4, destinoy_widget)
            self.ui.tableWidget.setItem(row, 5, velocidad_widget)
            self.ui.tableWidget.setItem(row, 6, red_widget)
            self.ui.tableWidget.setItem(row, 7, green_widget)
            self.ui.tableWidget.setItem(row, 8, blue_widget)
            self.ui.tableWidget.setItem(row, 9, distancia_widget)

            row += 1

    @Slot()
    def action_abrir_archivo(self):
         # print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo" + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        # print('guardar archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se creo el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))
