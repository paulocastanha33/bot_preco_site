# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 477)
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(160, 50, 411, 111))
        self.groupBox.setStyleSheet("width: 98%;\n"
"padding: 10px;\n"
"border-radius: 12px;\n"
"\n"
"background-color: #323232;\n"
"color: white;\n"
"font-family: \'Orbitron\', sans-serif;\n"
"letter-spacing:4px;")
        self.groupBox.setObjectName("groupBox")
        self.btn_iniciar = QtWidgets.QPushButton(self.groupBox)
        self.btn_iniciar.setGeometry(QtCore.QRect(30, 50, 101, 41))
        self.btn_iniciar.setStyleSheet("QPushButton{\n"
"width: 98%;\n"
"padding: 10px;\n"
"border-color:white;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 12px;\n"
"border:2px solid green;\n"
"background-color: lime;\n"
"color: black;\n"
"font-family: \'Orbitron\', sans-serif;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:white;\n"
"    color:black;\n"
"}\n"
"")
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.btn_parar = QtWidgets.QPushButton(self.groupBox)
        self.btn_parar.setGeometry(QtCore.QRect(280, 50, 101, 41))
        self.btn_parar.setStyleSheet("QPushButton{\n"
"width: 98%;\n"
"padding: 10px;\n"
"border-color:white;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 12px;\n"
"border:2px solid yellow;\n"
"background-color: red;\n"
"color: black;\n"
"font-family: \'Orbitron\', sans-serif;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:white;\n"
"    color:black;\n"
"}\n"
"")
        self.btn_parar.setObjectName("btn_parar")
        self.lbl_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status.setGeometry(QtCore.QRect(37, 200, 671, 41))
        self.lbl_status.setStyleSheet("background-color: #323232;\n"
"color: lime;\n"
"border-radius: 12px;\n"
"font-size: 10pt;")
        self.lbl_status.setObjectName("lbl_status")
        self.table_historico = QtWidgets.QTableWidget(self.centralwidget)
        self.table_historico.setGeometry(QtCore.QRect(35, 321, 681, 121))
        self.table_historico.setMinimumSize(QtCore.QSize(681, 0))
        self.table_historico.setStyleSheet("font: 57 10pt \"Ubuntu\";\n"
"background-color: white;")
        self.table_historico.setObjectName("table_historico")
        self.table_historico.setColumnCount(4)
        self.table_historico.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_historico.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_historico.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_historico.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_historico.setHorizontalHeaderItem(3, item)
        self.table_historico.horizontalHeader().setDefaultSectionSize(169)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(196, 263, 161, 20))
        self.label.setObjectName("label")
        self.lbl_preco = QtWidgets.QLineEdit(self.centralwidget)
        self.lbl_preco.setGeometry(QtCore.QRect(370, 249, 131, 41))
        self.lbl_preco.setStyleSheet("width: 98%;\n"
"padding: 10px;\n"
"border-color:white;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 12px;\n"
"border:2px solid lime;\n"
"background-color: black;\n"
"color: white;\n"
"font-family: \'Orbitron\', sans-serif;")
        self.lbl_preco.setObjectName("lbl_preco")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(43, 179, 81, 16))
        self.label_2.setStyleSheet("background-color: rgb(230, 97, 0);\n"
"letter-spacing:4px;")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robô de Monitoramento Diário de Preço"))
        self.groupBox.setTitle(_translate("MainWindow", "   CONSULTA DE PREÇOS AUTOMATIZADA"))
        self.btn_iniciar.setText(_translate("MainWindow", "INICIAR"))
        self.btn_parar.setText(_translate("MainWindow", "PARAR"))
        self.lbl_status.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.table_historico.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PRODUTO"))
        item = self.table_historico.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DATA ATUAL"))
        item = self.table_historico.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "VALOR"))
        item = self.table_historico.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "LINK"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#26a269;\">PREÇO DO PRODUTO:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>STATUS:</p></body></html>"))
