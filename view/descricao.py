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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(457, 584)
        Form.setStyleSheet(u"background-color: #212121; \n"
"border-radius: 10px;")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_frame = QFrame(Form)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: #212121; \n"
"border-radius: 10px;")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titulo_label = QLabel(self.main_frame)
        self.titulo_label.setObjectName(u"titulo_label")
        self.titulo_label.setStyleSheet(u"font-size: 24pt; \n"
"font-weight: 700; \n"
"color: #ECECEC;")

        self.verticalLayout_2.addWidget(self.titulo_label)

        self.imagem_label = QLabel(self.main_frame)
        self.imagem_label.setObjectName(u"imagem_label")
        self.imagem_label.setStyleSheet(u"border-radius: 10px;")
        self.imagem_label.setPixmap(QPixmap("view/assets/review.png"))
        self.imagem_label.setScaledContents(False)
        self.imagem_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.imagem_label)

        self.resumo_label = QLabel(self.main_frame)
        self.resumo_label.setObjectName(u"resumo_label")
        self.resumo_label.setStyleSheet(u"font-weight: 700; \n"
"color: #ECECEC;")

        self.verticalLayout_2.addWidget(self.resumo_label)

        self.resumo_textBrowser = QTextBrowser(self.main_frame)
        self.resumo_textBrowser.setObjectName(u"resumo_textBrowser")
        self.resumo_textBrowser.setStyleSheet(u"background-color: #2f2f2f;\n"
"border-radius: 10px;\n"
"font-weight: 700; \n"
"color: #ECECEC;\n"
"")

        self.verticalLayout_2.addWidget(self.resumo_textBrowser)

        self.categoria_label = QLabel(self.main_frame)
        self.categoria_label.setObjectName(u"categoria_label")
        self.categoria_label.setStyleSheet(u"font-weight: 700; \n"
"color: #ECECEC;")

        self.verticalLayout_2.addWidget(self.categoria_label)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.categoria_listWidget = QListWidget(self.main_frame)
        self.categoria_listWidget.setObjectName(u"categoria_listWidget")
        self.categoria_listWidget.setStyleSheet(u"background-color: #2F2F2F; \n"
"border-radius: 10px;\n"
"\n"
"                ")

        self.verticalLayout.addWidget(self.categoria_listWidget)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.main_frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titulo_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">T\u00edtulo do Jogo</span></p></body></html>", None))
        self.imagem_label.setText("")
        self.resumo_label.setText(QCoreApplication.translate("Form", u"Resumo", None))
        self.categoria_label.setText(QCoreApplication.translate("Form", u"Categorias", None))
    # retranslateUi

