import sys
import ir_datasets as ird
from .win import *
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox, QCheckBox, QVBoxLayout, QWidget, QDialog, QFormLayout, QLabel, QGroupBox
import PyQt5.QtWidgets as QtWidgets
import pandas as pd

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.datasets = self.load_dataset()
        self.ui.btn_generate.clicked.connect(self.get_documents)

    def load_dataset(self):
        datasets = self.get_list_of_datasets()
        wd = self.generate_checkbox(datasets, self.ui.scrollArea_3)
        self.ui.scrollArea.setWidget(wd)
        return datasets

    def generate_checkbox(ds_name, environment):
        vbox = QVBoxLayout()
        widget = QWidget()
        for name in ds_name:
            cb = QCheckBox(name, environment)
            vbox.addWidget(cb)
        widget.setLayout(vbox)
        return widget

    def get_list_of_datasets(self):
        return ['vaswani', 'cranfield', 'beir/arguana']

    def asign_ds_from_checkbox_list(widget, list):
        result = []
        for pos, item in enumerate(widget.children()[1:]):
            if item.isChecked():
                result.append(list[pos])
        return result

    def get_documents(self):
        pass	


# if __name__ == "__main__":
def execute_application():
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())

