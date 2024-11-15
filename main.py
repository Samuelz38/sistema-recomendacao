from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLayout
from PySide6.QtGui import QIcon
from sistema_recomendacao.view.descricao import Ui_Form
from sistema_recomendacao.view.mainwindow import Ui_MainWindow
from PySide6.QtCore import Qt
import sys
import os


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema de Recomendação')
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.intem_lista = self.lista_listWidget
        self.intem_lista.itemClicked.connect(self.open_system)

    def open_system(self):
            self.w = DescricaoIntem()
            self.w.show()
            
            

class DescricaoIntem(QWidget,Ui_Form):
    def __init__(self):
        super(DescricaoIntem,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Descrição')

    
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('sistema_recomendacao/view/assets/icons8-controle-64.png'))
    window = MainWindow()
    window.show()
    app.exec()