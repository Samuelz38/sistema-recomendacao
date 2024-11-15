# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'descricao.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(443, 655)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(1677, 1677))
        self.widget.setStyleSheet(u"")
        self.imagem_label = QLabel(self.widget)
        self.imagem_label.setObjectName(u"imagem_label")
        self.imagem_label.setGeometry(QRect(-40, 60, 581, 291))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.imagem_label.sizePolicy().hasHeightForWidth())
        self.imagem_label.setSizePolicy(sizePolicy1)
        self.imagem_label.setMinimumSize(QSize(311, 291))
        self.imagem_label.setMaximumSize(QSize(1677, 1677))
        self.imagem_label.setStyleSheet(u"\n"
"border: 5px solid black; /* Define a espessura, estilo e cor da borda */\n"
"border-radius: 10px; /* Define o raio dos cantos em pixels */\n"
"")
        self.imagem_label.setPixmap(QPixmap(u"../assets/57412022-real-gamer-um-controlador-de-videogame-nas-m\u00e3os-do-homem-na-noite.jpg"))
        self.imagem_label.setScaledContents(True)
        self.Nome_Jogo_label = QLabel(self.widget)
        self.Nome_Jogo_label.setObjectName(u"Nome_Jogo_label")
        self.Nome_Jogo_label.setGeometry(QRect(0, 0, 162, 43))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Nome_Jogo_label.sizePolicy().hasHeightForWidth())
        self.Nome_Jogo_label.setSizePolicy(sizePolicy2)
        self.Nome_Jogo_label.setMinimumSize(QSize(5, 5))
        self.Nome_Jogo_label.setBaseSize(QSize(5, 5))

        self.verticalLayout.addWidget(self.widget)

        self.categoria_frame = QFrame(Form)
        self.categoria_frame.setObjectName(u"categoria_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.categoria_frame.sizePolicy().hasHeightForWidth())
        self.categoria_frame.setSizePolicy(sizePolicy3)
        self.categoria_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.categoria_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.categoria_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.categoria_frame)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet(u"element {\n"
"  border: 2px solid black; /* Define a espessura, estilo e cor da borda */\n"
"  border-radius: 10px; /* Define o raio dos cantos em pixels */\n"
"}")

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.especificacoes_label = QLabel(self.categoria_frame)
        self.especificacoes_label.setObjectName(u"especificacoes_label")

        self.gridLayout.addWidget(self.especificacoes_label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.categoria_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.texto_resumo_frame = QFrame(Form)
        self.texto_resumo_frame.setObjectName(u"texto_resumo_frame")
        sizePolicy3.setHeightForWidth(self.texto_resumo_frame.sizePolicy().hasHeightForWidth())
        self.texto_resumo_frame.setSizePolicy(sizePolicy3)
        self.texto_resumo_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.texto_resumo_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.texto_resumo_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser = QTextBrowser(self.texto_resumo_frame)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)

        self.resumo_label = QLabel(self.texto_resumo_frame)
        self.resumo_label.setObjectName(u"resumo_label")

        self.gridLayout_2.addWidget(self.resumo_label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.texto_resumo_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.imagem_label.setText("")
        self.Nome_Jogo_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">T\u00edtuloJogo</span></p></body></html>", None))
        self.especificacoes_label.setText(QCoreApplication.translate("Form", u"Especifica\u00e7\u00f5es", None))
        self.resumo_label.setText(QCoreApplication.translate("Form", u"Resumo", None))
    # retranslateUi

