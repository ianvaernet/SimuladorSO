# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_Resultado.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Ui_Form_Resultado(object):
    def setupUi(self, Form_Resultado):
        Form_Resultado.setObjectName("Form_Resultado")
        Form_Resultado.resize(800, 600)
        Form_Resultado.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form_Resultado)
        self.gridLayout.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(Form_Resultado)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.navegador = QtWebEngineWidgets.QWebEngineView(self.splitter)
        self.navegador.setStyleSheet("background-image: url();")
        self.navegador.setObjectName("graphicsView")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tableWidget_Procesos = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget_Procesos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_Procesos.setStyleSheet("background-image: url();")
        self.tableWidget_Procesos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_Procesos.setAlternatingRowColors(True)
        self.tableWidget_Procesos.setObjectName("tableWidget_Procesos")
        self.tableWidget_Procesos.setColumnCount(10)
        self.tableWidget_Procesos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(9, item)
        self.horizontalLayout.addWidget(self.tableWidget_Procesos)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout.addWidget(self.splitter, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_Minimizar = QtWidgets.QPushButton(Form_Resultado)
        self.pushButton_Minimizar.setStyleSheet("background-image: url();")
        self.pushButton_Minimizar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Recursos/Minimizar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Minimizar.setIcon(icon)
        self.pushButton_Minimizar.setObjectName("pushButton_Minimizar")
        self.horizontalLayout_2.addWidget(self.pushButton_Minimizar)
        self.pushButton_Ventana = QtWidgets.QPushButton(Form_Resultado)
        self.pushButton_Ventana.setStyleSheet("background-image: url();")
        self.pushButton_Ventana.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Recursos/Ventana.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Ventana.setIcon(icon1)
        self.pushButton_Ventana.setObjectName("pushButton_Ventana")
        self.horizontalLayout_2.addWidget(self.pushButton_Ventana)
        self.pushButton_Cerrar = QtWidgets.QPushButton(Form_Resultado)
        self.pushButton_Cerrar.setStyleSheet("background-image: url();")
        self.pushButton_Cerrar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Recursos/Cerrar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cerrar.setIcon(icon2)
        self.pushButton_Cerrar.setObjectName("pushButton_Cerrar")
        self.horizontalLayout_2.addWidget(self.pushButton_Cerrar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Form_Resultado)
        QtCore.QMetaObject.connectSlotsByName(Form_Resultado)

    def retranslateUi(self, Form_Resultado):
        _translate = QtCore.QCoreApplication.translate
        Form_Resultado.setWindowTitle(_translate("Form_Resultado", "Simulador de Sistema Operativo"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(0)
        item.setText(_translate("Form_Resultado", "Tiempo"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(1)
        item.setText(_translate("Form_Resultado", "Listo"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(2)
        item.setText(_translate("Form_Resultado", "Bloqueado"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(3)
        item.setText(_translate("Form_Resultado", "Ejecución"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(4)
        item.setText(_translate("Form_Resultado", "Cola de Listos"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(5)
        item.setText(_translate("Form_Resultado", "Cola de Entrada"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(6)
        item.setText(_translate("Form_Resultado", "Cola de Salida"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(7)
        item.setText(_translate("Form_Resultado", "CPU"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(8)
        item.setText(_translate("Form_Resultado", "Entrada"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(9)
        item.setText(_translate("Form_Resultado", "Salida"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Resultado = QtWidgets.QWidget()
    ui = Ui_Form_Resultado()
    ui.setupUi(Form_Resultado)
    Form_Resultado.show()
    sys.exit(app.exec_())
