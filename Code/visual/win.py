# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Code\visual\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(-1, 11, 11, 11)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btn_generate = QtWidgets.QPushButton(self.frame_2)
        self.btn_generate.setObjectName("btn_generate")
        self.horizontalLayout.addWidget(self.btn_generate)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_10)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.comboBoxDB = QtWidgets.QComboBox(self.frame_10)
        self.comboBoxDB.setObjectName("comboBoxDB")
        self.comboBoxDB.addItem("")
        self.comboBoxDB.addItem("")
        self.verticalLayout_4.addWidget(self.comboBoxDB)
        self.line = QtWidgets.QFrame(self.frame_10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.comboBoxModel = QtWidgets.QComboBox(self.frame_10)
        self.comboBoxModel.setObjectName("comboBoxModel")
        self.comboBoxModel.addItem("")
        self.comboBoxModel.addItem("")
        self.comboBoxModel.addItem("")
        self.verticalLayout_4.addWidget(self.comboBoxModel)
        self.line_2 = QtWidgets.QFrame(self.frame_10)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.frame_10)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.query_exp = QtWidgets.QComboBox(self.frame_10)
        self.query_exp.setObjectName("query_exp")
        self.query_exp.addItem("")
        self.query_exp.addItem("")
        self.verticalLayout_4.addWidget(self.query_exp)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.listView = QtWidgets.QListView(self.frame_10)
        self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listView.setObjectName("listView")
        self.horizontalLayout_5.addWidget(self.listView)
        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 10)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Buscador bien molon"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Entre la consulta deseada"))
        self.btn_generate.setText(_translate("MainWindow", "Buscar"))
        self.label.setText(_translate("MainWindow", "Modelo de Busqueda:"))
        self.comboBoxDB.setItemText(0, _translate("MainWindow", "vaswani"))
        self.comboBoxDB.setItemText(1, _translate("MainWindow", "cranfield"))
        self.label_2.setText(_translate("MainWindow", "Base de Datos:"))
        self.comboBoxModel.setItemText(0, _translate("MainWindow", "modelo vectorial"))
        self.comboBoxModel.setItemText(1, _translate("MainWindow", "modelo LSI"))
        self.comboBoxModel.setItemText(2, _translate("MainWindow", "red neuronal"))
        self.label_3.setText(_translate("MainWindow", "Expanci??n de Consulta"))
        self.query_exp.setItemText(0, _translate("MainWindow", "no"))
        self.query_exp.setItemText(1, _translate("MainWindow", "si"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
