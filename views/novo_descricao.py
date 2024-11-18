# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novo_descricao.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(485, 597)
        Form.setStyleSheet(u"background-color: #212121; \n"
"border-radius: 10px;")
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titulo_label = QLabel(self.frame)
        self.titulo_label.setObjectName(u"titulo_label")
        self.titulo_label.setStyleSheet(u"font-size: 24pt; \n"
"font-weight: 700; \n"
"color: #ECECEC;")

        self.verticalLayout_2.addWidget(self.titulo_label)

        self.imagem_label = QLabel(self.frame)
        self.imagem_label.setObjectName(u"imagem_label")
        self.imagem_label.setStyleSheet(u"border-radius: 10px;")
        self.imagem_label.setPixmap(QPixmap(u"../../GitHub/sistema-recoemendacao/view/assets/review.png"))
        self.imagem_label.setScaledContents(False)
        self.imagem_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.imagem_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.resumo_label = QLabel(self.frame)
        self.resumo_label.setObjectName(u"resumo_label")
        self.resumo_label.setStyleSheet(u"font-weight: 700; \n"
"color: #ECECEC;")

        self.verticalLayout.addWidget(self.resumo_label)

        self.resumo_textBrowser = QTextBrowser(self.frame)
        self.resumo_textBrowser.setObjectName(u"resumo_textBrowser")
        self.resumo_textBrowser.setStyleSheet(u"background-color: #2f2f2f;\n"
"border-radius: 10px;\n"
"font-weight: 700; \n"
"color: #ECECEC;\n"
"")

        self.verticalLayout.addWidget(self.resumo_textBrowser)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.main_tabWidget = QTabWidget(self.frame)
        self.main_tabWidget.setObjectName(u"main_tabWidget")
        self.main_tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.main_tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    background-color: #2f2f2f; /* Cor de fundo do painel */\n"
"    border-radius: 10px; /* Cantos arredondados */\n"
"    padding: 5px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #2f2f2f; /* Cor de fundo padr\u00e3o da aba */\n"
"    color: #ECECEC; /* Cor do texto */\n"
"    font-weight: 700; /* Texto em negrito */\n"
"    padding: 10px 20px; /* Espa\u00e7amento interno (horizontal e vertical) */\n"
"    border-radius: 10px; /* Cantos arredondados */\n"
"    margin: 3px; /* Espa\u00e7amento entre abas */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #414141; /* Cor da aba selecionada */\n"
"    font-weight: 700; /* Negrito extra para destacar */\n"
"    color: #FFFFFF; /* Cor do texto mais clara */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #3a3a3a; /* Cor ao passar o mouse sobre a aba */\n"
"    color: #F0F0F0; /* Cor do texto ao passar o mouse */\n"
"}\n"
"")
        self.genero_tab_widget = QWidget()
        self.genero_tab_widget.setObjectName(u"genero_tab_widget")
        self.gridLayout_3 = QGridLayout(self.genero_tab_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.genero_listWidget = QListWidget(self.genero_tab_widget)
        self.genero_listWidget.setObjectName(u"genero_listWidget")

        self.gridLayout_3.addWidget(self.genero_listWidget, 0, 0, 1, 1)

        self.main_tabWidget.addTab(self.genero_tab_widget, "")
        self.especificacao_tab_qwidget = QWidget()
        self.especificacao_tab_qwidget.setObjectName(u"especificacao_tab_qwidget")
        self.especificacao_tab_qwidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.gridLayout_2 = QGridLayout(self.especificacao_tab_qwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.especificacao_listWidget = QListWidget(self.especificacao_tab_qwidget)
        self.especificacao_listWidget.setObjectName(u"especificacao_listWidget")
        self.especificacao_listWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.especificacao_listWidget.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.especificacao_listWidget, 0, 0, 1, 1)

        self.main_tabWidget.addTab(self.especificacao_tab_qwidget, "")
        self.nota_tab_qwidget = QWidget()
        self.nota_tab_qwidget.setObjectName(u"nota_tab_qwidget")
        self.gridLayout = QGridLayout(self.nota_tab_qwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nota_listWidget = QListWidget(self.nota_tab_qwidget)
        self.nota_listWidget.setObjectName(u"nota_listWidget")

        self.gridLayout.addWidget(self.nota_listWidget, 0, 0, 1, 1)

        self.main_tabWidget.addTab(self.nota_tab_qwidget, "")

        self.verticalLayout_2.addWidget(self.main_tabWidget)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.main_tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titulo_label.setText(QCoreApplication.translate("Form", u"T\u00edtulo do Jogo", None))
        self.imagem_label.setText("")
        self.resumo_label.setText(QCoreApplication.translate("Form", u"Resumo", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.genero_tab_widget), QCoreApplication.translate("Form", u"G\u00eanero", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.especificacao_tab_qwidget), QCoreApplication.translate("Form", u"Especifica\u00e7\u00f5es", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.nota_tab_qwidget), QCoreApplication.translate("Form", u"Nota", None))
    # retranslateUi

