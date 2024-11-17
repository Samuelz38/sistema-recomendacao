# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagina_pesquisa.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_PesquisaPagina(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(823, 595)
        Form.setStyleSheet(u"background-color: #212121; \n"
"border-radius: 10px;")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.voltar_pushButton = QPushButton(self.frame)
        self.voltar_pushButton.setObjectName(u"voltar_pushButton")
        self.voltar_pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.voltar_pushButton)

        self.direita_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.direita_horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.jogos_achados_label = QLabel(Form)
        self.jogos_achados_label.setObjectName(u"jogos_achados_label")
        self.jogos_achados_label.setStyleSheet(u"color: #ECECEC;")

        self.verticalLayout.addWidget(self.jogos_achados_label)

        self.lista_listWidget = QListWidget(Form)
        self.lista_listWidget.setObjectName(u"lista_listWidget")
        self.lista_listWidget.setStyleSheet(u"background-color: #2f2f2f;\n"
"border-radius: 10px;\n"
"font-weight: 700; \n"
"color: #ECECEC;\n"
"")

        self.verticalLayout.addWidget(self.lista_listWidget)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.voltar_pushButton.setText(QCoreApplication.translate("Form", u"Voltar", None))
        self.jogos_achados_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Jogos Achados...</span></p></body></html>", None))
    # retranslateUi

