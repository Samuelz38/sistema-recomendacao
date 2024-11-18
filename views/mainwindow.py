# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem, 
                               QVBoxLayout,QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #1a1a1a;")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.inicial_line = QFrame(self.centralwidget)
        self.inicial_line.setObjectName(u"inicial_line")
        self.inicial_line.setStyleSheet(u"line {\n"
"    height: 3px; /* Espessura da linha */\n"
"    width: 100%; /* Largura total */\n"
"    background: linear-gradient(90deg, #ff6f91, #ff9671, #ffc75f); /* Gradiente suave */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"    box-shadow: 0 0 10px rgba(255, 255, 255, 0.1); /* Brilho suave */\n"
"    margin: 20px 0; /* Espa\u00e7amento vertical */\n"
"}\n"
"\n"
"/* Adicionando anima\u00e7\u00e3o ao gradiente */\n"
"line.animated {\n"
"    background-size: 200% 200%; /* Permite o deslocamento */\n"
"    animation: gradientMove 3s infinite; /* Anima\u00e7\u00e3o cont\u00ednua */\n"
"}\n"
"\n"
"color: rgb(255, 255, 255);")
        self.inicial_line.setFrameShape(QFrame.Shape.HLine)
        self.inicial_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.inicial_line)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #2d2d2d;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        
        self.imagem_label = QLabel(self.frame)
        self.imagem_label.setObjectName(u"imagem_label")
        self.imagem_label.setPixmap(QPixmap("view/assets/icons8-controle-64.png"))
        self.imagem_label.setScaledContents(False)
        self.imagem_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.imagem_label, 2, 0, 1, 1)

        self.imagem_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.imagem_verticalSpacer, 0, 0, 1, 1)

        self.filtro_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.filtro_verticalSpacer, 8, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.esquerda_filtro_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.esquerda_filtro_horizontalSpacer)

        self.genero_comboBox = QComboBox(self.frame)
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.setObjectName(u"genero_comboBox")
        self.genero_comboBox.setStyleSheet(u" QComboBox {\n"
"                padding: 8px;\n"
"                background-color: #3d3d3d;\n"
"                border: 1px solid #4d4d4d;\n"
"                border-radius: 5px;\n"
"                color: white;\n"
"            }\n"
"            QComboBox:drop-down {\n"
"                border: none;\n"
"            }\n"
"            QComboBox:down-arrow {\n"
"                image: none;\n"
"                border: none;\n"
"            }\n"
"            QComboBox QAbstractItemView {\n"
"                background-color: #3d3d3d;\n"
"                color: white;\n"
"                selection-background-color: #10a37f;\n"
"            }")

        self.horizontalLayout_2.addWidget(self.genero_comboBox)

        self.centro_filtro_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.centro_filtro_horizontalSpacer)

        self.categoria_comboBox = QComboBox(self.frame)
        self.categoria_comboBox.addItem("")
        self.categoria_comboBox.addItem("")
        self.categoria_comboBox.addItem("")
        self.categoria_comboBox.addItem("")
        self.categoria_comboBox.addItem("")
        self.categoria_comboBox.addItem("")
        self.categoria_comboBox.addItem("")
        self.categoria_comboBox.addItem("")
        self.categoria_comboBox.addItem("")
        self.categoria_comboBox.setObjectName(u"categoria_comboBox")
        self.categoria_comboBox.setStyleSheet(u" QComboBox {\n"
"                padding: 8px;\n"
"                background-color: #3d3d3d;\n"
"                border: 1px solid #4d4d4d;\n"
"                border-radius: 5px;\n"
"                color: white;\n"
"            }\n"
"            QComboBox:drop-down {\n"
"                border: none;\n"
"            }\n"
"            QComboBox:down-arrow {\n"
"                image: none;\n"
"                border: none;\n"
"            }\n"
"            QComboBox QAbstractItemView {\n"
"                background-color: #3d3d3d;\n"
"                color: white;\n"
"                selection-background-color: #10a37f;\n"
"            }")

        self.horizontalLayout_2.addWidget(self.categoria_comboBox)

        self.direita_filtro_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.direita_filtro_horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_menu = QFrame(self.frame)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.campo_pesquisa_lineEdit = QLineEdit(self.frame_menu)
        self.campo_pesquisa_lineEdit.setObjectName(u"campo_pesquisa_lineEdit")
        self.campo_pesquisa_lineEdit.setStyleSheet(u"QLineEdit {\n"
"                padding: 8px;\n"
"                background-color: #3d3d3d;\n"
"                border: 1px solid #4d4d4d;\n"
"                border-radius: 5px;\n"
"                color: #ffffff;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #10a37f;\n"
"            }")

        self.gridLayout.addWidget(self.campo_pesquisa_lineEdit, 0, 1, 1, 1)

        self.esquerda_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.esquerda_horizontalSpacer, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.enviar_pushButton = QPushButton(self.frame)
        self.enviar_pushButton.setObjectName(u"enviar_pushButton")
        self.enviar_pushButton.setStyleSheet(u"QPushButton {\n"
"                background-color: #10a37f;\n"
"                color: white;\n"
"                border: none;\n"
"                padding: 8px 16px;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"\n"
" QPushButton:hover {\n"
"                background-color: #0d816a;\n"
"		}")

        self.horizontalLayout.addWidget(self.enviar_pushButton)

        self.direita_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.direita_horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.separa_menu_filtro_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_2.addItem(self.separa_menu_filtro_verticalSpacer, 6, 0, 1, 1)

        self.texto_introducao_label = QLabel(self.frame)
        self.texto_introducao_label.setObjectName(u"texto_introducao_label")
        self.texto_introducao_label.setStyleSheet(u"font-size: 1.875rem;\n"
"color: rgb(206, 206, 206);\n"
"font-weight: 600;\n"
"line-height: 2.25rem;")

        self.gridLayout_2.addWidget(self.texto_introducao_label, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.final_line = QFrame(self.centralwidget)
        self.final_line.setObjectName(u"final_line")
        self.final_line.setStyleSheet(u"custom-line {\n"
"    height: 3px; /* Espessura da linha */\n"
"    width: 100%; /* Largura total */\n"
"    background: linear-gradient(90deg, #ff6f91, #ff9671, #ffc75f); /* Gradiente suave */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"    box-shadow: 0 0 10px rgba(255, 255, 255, 0.1); /* Brilho suave */\n"
"    margin: 20px 0; /* Espa\u00e7amento vertical */\n"
"}\n"
"\n"
"/* Adicionando anima\u00e7\u00e3o ao gradiente */\n"
".custom-line.animated {\n"
"    background-size: 200% 200%; /* Permite o deslocamento */\n"
"    animation: gradientMove 3s infinite; /* Anima\u00e7\u00e3o cont\u00ednua */\n"
"}")
        self.final_line.setFrameShape(QFrame.Shape.HLine)
        self.final_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.final_line)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imagem_label.setText("")
        self.genero_comboBox.setItemText(0, "")
        self.genero_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"TODOS", None))
        self.genero_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"A\u00e7\u00e3o", None))
        self.genero_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Aventura", None))
        self.genero_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"RPG", None))
        self.genero_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Roguelike", None))
        self.genero_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Simula\u00e7\u00e3o", None))
        self.genero_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Corrida", None))
        self.genero_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Esportes", None))
        self.genero_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"FPS", None))
        self.genero_comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Hack and Lash", None))

        self.categoria_comboBox.setItemText(0, "")
        self.categoria_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"TODOS", None))
        self.categoria_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cooperativo", None))
        self.categoria_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Cooperativo On-line", None))
        self.categoria_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"MMO", None))
        self.categoria_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Multijogador", None))
        self.categoria_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Multijogardo Local e em Grupo", None))
        self.categoria_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Rede Local (LAN)", None))
        self.categoria_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Um Jogador", None))

        self.enviar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.texto_introducao_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Digite o nome de um jogo ou defina o g\u00eanero e o modo de jogo.</span></p></body></html>", None))
    # retranslateUi

