import sys
# from Code.visual.wait_win import Ui_waiting_win
import ir_datasets as ird
from .win import *
from PyQt5 import QtWidgets as qtw, uic
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox, QCheckBox, QVBoxLayout, QWidget, QDialog, QFormLayout, QLabel, QGroupBox
import PyQt5.QtWidgets as QtWidgets
# from wait_win import Ui_waiting_win
import pandas as pd
from ..data_process import load_dataset, make_text_list
from ..retrieval import retrieval 
import json
import threading

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        # self.datasets = self.load_dataset()
        self.ui.btn_generate.clicked.connect(self.get_documents)

    def load_dataset(self):
        datasets = self.get_list_of_datasets()
        wd = self.generate_checkbox(datasets, self.ui.scrollArea_3)
        self.ui.scrollArea_3.setWidget(wd)
        return datasets

    def load_db_json(self, db):
        try:
            db = open(f'{db}_db.json', 'r')
            db = db.read()
            db = json.loads(db)
            return db
            
        except:
            print('Las bases de datos no fueron cargadas, lea las intrucciones del programa.')
            exit(1)

    def generate_checkbox(self, ds_name, environment):
        vbox = QVBoxLayout()
        widget = QWidget()
        for name in ds_name:
            cb = QCheckBox(name, environment)
            vbox.addWidget(cb)
        widget.setLayout(vbox)
        return widget

    def get_list_of_datasets(self):
        return ['vaswani', 'cranfield']

    def asign_ds_from_checkbox_list(widget, list):
        result = []
        for pos, item in enumerate(widget.children()[1:]):
            if item.isChecked():
                result.append(list[pos])
        return result

    def get_documents(self):
        # print( self.ui.comboBoxModel.currentText() , type( self.ui.comboBoxModel.currentText() ))
        mod_ = self.ui.comboBoxModel.currentText() 
        db = self.ui.comboBoxDB.currentText()
        query = self.ui.lineEdit.text()
        
        print("busqueda:", query)
        if not query: 
            msgbox = QMessageBox()
            msgbox.setText('La consulta no puede ser vacia')
            msgbox.exec()
            return
        
        documents = self.load_db_json(db)
        # print(type(documents))
        
        # ventana de espera
        # threading.Thread(target=self.show_messagebox, args=('Esperando a que termine la busqueda',))
        
        # retrieval
        ranked_list = ['modelo no implementado']
        
        if mod_ == 'modelo vectorial':
            print('busqueda por vectorial')
            ranked_list = retrieval(documents, query,db,'v')
        elif mod_ == 'modelo LSI':
            print("entre a LSI")
            ranked_list = retrieval(documents, query, db, 'lsi')
        else:
            ranked_list = retrieval(documents, query,db,'nn')
        
        # threading.Thread(target=self.show_messagebox, args=('Busqueda terminada',))
        msgbox = QMessageBox()
        msgbox.setText("La busqueda finalizo correctamente!")
        msgbox.exec()
        
        model = QtGui.QStandardItemModel()
        self.ui.listView.setModel(model)
        
        
        for i in ranked_list:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        # una vez obtenidos todos los documentos 
        # self.ui.listView.addItems(ranked_list)
    def show_messagebox(self, text):
        msgbox = QMessageBox()
        msgbox.setText(text)
        msgbox.exec()


# if __name__ == "__main__":
def execute_application():
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())

