# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-time.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Theme(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(170, 110)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.date_text = QLabel(Form)
        self.date_text.setObjectName(u"date_text")
        self.date_text.setGeometry(QRect(10, 10, 151, 41))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.date_text.setFont(font)
        self.date_text.setStyleSheet(u"color: rgba(255, 255, 255, 150);\n"
"font-weight: bold;")
        self.date_text.setTextFormat(Qt.PlainText)
        self.date_text.setAlignment(Qt.AlignCenter)
        self.day_text = QLabel(Form)
        self.day_text.setObjectName(u"day_text")
        self.day_text.setGeometry(QRect(20, 30, 131, 61))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.day_text.setFont(font1)
        self.day_text.setStyleSheet(u"border: none;\n"
"color: rgba(255, 255, 255, 255);\n"
"font-weight: bold")
        self.day_text.setTextFormat(Qt.PlainText)
        self.day_text.setAlignment(Qt.AlignCenter)
        self.backgnd = QLabel(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setGeometry(QRect(10, 10, 151, 81))
        self.backgnd.setStyleSheet(u"background-color: rgba(15, 18, 22, 255);\n"
"border-radius: 8px\n"
"")
        self.backgnd.raise_()
        self.date_text.raise_()
        self.day_text.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Theme", u"\u65f6\u95f4", None))
        self.date_text.setText(QCoreApplication.translate("Theme", u"2025 \u5e74  13 \u6708", None))
        self.day_text.setText(QCoreApplication.translate("Theme", u"32 \u65e5 \u5468\u4e8c", None))
        self.backgnd.setText("")
    # retranslateUi
