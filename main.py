from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QIcon
from view.novo_descricao import Ui_Form
from view.mainwindow import Ui_MainWindow
from view.pagina_pesquisa import Ui_PesquisaPagina
from PySide6.QtCore import Qt
import sys
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema de Recomendação')
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.enviar_pushButton.clicked.connect(self.abrir_pagina_pesquisa)

    def abrir_pagina_pesquisa(self):
        self.pesquisa_pagina = PaginaPesquisa()
        self.pesquisa_pagina.show()
        self.close()


class PaginaPesquisa(QWidget, Ui_PesquisaPagina):
    def __init__(self):
        super(PaginaPesquisa, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Página de Pesquisa')
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
       
        self.lista_listWidget.itemClicked.connect(self.abrir_pagina_descricao)
        self.voltar_pushButton.clicked.connect(self.abrir_pagina_main)

    def abrir_pagina_descricao(self):
        self.pagina_desscricao = DescricaoIntem()
        self.pagina_desscricao.show()
    
    def abrir_pagina_main(self):
        self.pagina_desscricao = MainWindow()
        self.pagina_desscricao.show()
        self.close()


class DescricaoIntem(QWidget, Ui_Form):
    def __init__(self):
        super(DescricaoIntem, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Descrição')
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)       


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('view/assets/icons8-controle-64.png'))
    window = MainWindow()
    window.show()
    app.exec()
