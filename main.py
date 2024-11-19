from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt

from views.novo_descricao import Ui_Form
from views.mainwindow import Ui_MainWindow
from views.pagina_pesquisa import Ui_PesquisaPagina

from controllers.main_controller import MainController
from controllers.item_description_controller import ItemDescriptionController

from utils.text_translator import translateText
from utils.filepath_getter import getFilepathFromURL

import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.setWindowTitle('Sistema de Recomendação')
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.enviar_pushButton.clicked.connect(self.abrir_pagina_pesquisa)

        # Tenta pegar a lista toda vez que o usuário alterar o campo de texto
        self.campo_pesquisa_lineEdit.textEdited.connect(lambda: MainController.getGameList(self.campo_pesquisa_lineEdit.text()))

    def abrir_pagina_pesquisa(self):
        
        self.pesquisa_pagina = PaginaPesquisa()
        self.pesquisa_pagina.show()
        self.close()

        if MainController.GAME_LIST:
            
            self.pesquisa_pagina.lista_listWidget.addItems(list(map(lambda x: x.name, MainController.GAME_LIST)))

class PaginaPesquisa(QWidget, Ui_PesquisaPagina):
    
    def __init__(self):
        
        super(PaginaPesquisa, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Página de Pesquisa')
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
       
        self.lista_listWidget.itemClicked.connect(lambda x: ItemDescriptionController.getGameData(x.text()))
        self.lista_listWidget.itemClicked.connect(self.abrir_pagina_descricao)

        self.voltar_pushButton.clicked.connect(self.abrir_pagina_main)

    def abrir_pagina_descricao(self):
        
        self.pagina_desscricao = DescricaoIntem()
        self.pagina_desscricao.show()

        if ItemDescriptionController.CONTEXT_GAME:
        
          context_game = ItemDescriptionController.CONTEXT_GAME

          self.pagina_desscricao.titulo_label.setText(context_game.name)
          self.pagina_desscricao.resumo_textBrowser.setText(translateText(context_game.description, "en", "pt"))
          self.pagina_desscricao.genero_listWidget.addItems(list(map(lambda x: translateText(x, "en", "pt"), context_game.genres)))
          self.pagina_desscricao.imagem_label.setPixmap(QPixmap(getFilepathFromURL(context_game.image_url,
                                                                                    context_game.name)).scaled(300, 300))

          self.pagina_desscricao.nota_listWidget.addItem(str(context_game.rating).replace('.', ','))

          self.pagina_desscricao.especificacao_listWidget.addItem(f"Data de Lançamento: {context_game.released_date}")
          self.pagina_desscricao.especificacao_listWidget.addItem(f"Plataformas: {', '.join(context_game.platforms)}")
          self.pagina_desscricao.especificacao_listWidget.addItem(f"Desenvolvedores: {', '.join(context_game.developers)}")
    
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
    app.setWindowIcon(QIcon('views/assets/icons8-controle-64.png'))
    window = MainWindow()
    window.show()
    app.exec()