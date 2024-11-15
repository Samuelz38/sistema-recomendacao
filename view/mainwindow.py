# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.campo_pesquisa_lineEdit = QLineEdit(self.frame_menu)
        self.campo_pesquisa_lineEdit.setObjectName(u"campo_pesquisa_lineEdit")

        self.horizontalLayout.addWidget(self.campo_pesquisa_lineEdit)

        self.enviar_pushButton = QPushButton(self.frame_menu)
        self.enviar_pushButton.setObjectName(u"enviar_pushButton")

        self.horizontalLayout.addWidget(self.enviar_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.genero_comboBox = QComboBox(self.frame_menu)
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

        self.horizontalLayout.addWidget(self.genero_comboBox)

        self.modo_de_jogo_comboBox = QComboBox(self.frame_menu)
        self.modo_de_jogo_comboBox.addItem("")
        self.modo_de_jogo_comboBox.addItem("")
        self.modo_de_jogo_comboBox.addItem("")
        self.modo_de_jogo_comboBox.addItem("")
        self.modo_de_jogo_comboBox.addItem("")
        self.modo_de_jogo_comboBox.addItem("")
        self.modo_de_jogo_comboBox.addItem("")
        self.modo_de_jogo_comboBox.setObjectName(u"modo_de_jogo_comboBox")

        self.horizontalLayout.addWidget(self.modo_de_jogo_comboBox)


        self.verticalLayout.addWidget(self.frame_menu)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lista_listWidget = QListWidget(self.main_frame)
        self.lista_listWidget.setObjectName(u"lista_listWidget")

        self.gridLayout.addWidget(self.lista_listWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.main_frame)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.enviar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.genero_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"A\u00e7\u00e3o", None))
        self.genero_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Aventura", None))
        self.genero_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"RPG", None))
        self.genero_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roguelike", None))
        self.genero_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Simula\u00e7\u00e3o", None))
        self.genero_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Corrida", None))
        self.genero_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Esportes", None))
        self.genero_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"FPS", None))
        self.genero_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Hack and Lash", None))

        self.modo_de_jogo_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Cooperativo", None))
        self.modo_de_jogo_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Cooperativo On-line", None))
        self.modo_de_jogo_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"MMO", None))
        self.modo_de_jogo_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Multijogador", None))
        self.modo_de_jogo_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Multijogardo Local e em Grupo", None))
        self.modo_de_jogo_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Rede Local (LAN)", None))
        self.modo_de_jogo_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Um Jogador", None))

        self.lista_listWidget.addItem('TESTE01')

    # retranslateUi

