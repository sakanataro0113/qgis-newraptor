from qgis.PyQt.QtWidgets import *
from .impact_table_dialog import Ui_dlgImpacts


class Dlgtable(QDialog,Ui_dlgImpacts):
    def __init__(self):
        super(Dlgtable,self).__init__()
        self.setupUi(self)

        self.tblImpacts.setColumnWidth(1,350)