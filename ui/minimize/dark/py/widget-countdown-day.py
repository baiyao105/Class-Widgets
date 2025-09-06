# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-countdown-day.ui'
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
        Form.resize(180, 110)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.countdown_custom_title = QLabel(Form)
        self.countdown_custom_title.setObjectName(u"countdown_custom_title")
        self.countdown_custom_title.setGeometry(QRect(10, 10, 161, 41))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.countdown_custom_title.setFont(font)
        self.countdown_custom_title.setStyleSheet(u"color: rgba(255, 255, 255, 150);\n"
"font-weight: bold;")
        self.countdown_custom_title.setTextFormat(Qt.PlainText)
        self.countdown_custom_title.setAlignment(Qt.AlignCenter)
        self.custom_countdown = QLabel(Form)
        self.custom_countdown.setObjectName(u"custom_countdown")
        self.custom_countdown.setGeometry(QRect(20, 30, 141, 61))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.custom_countdown.setFont(font1)
        self.custom_countdown.setStyleSheet(u"border: none;\n"
"color: rgba(255, 255, 255, 255);\n"
"font-weight: bold")
        self.custom_countdown.setTextFormat(Qt.PlainText)
        self.custom_countdown.setAlignment(Qt.AlignCenter)
        self.backgnd = QLabel(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setGeometry(QRect(10, 10, 161, 81))
        self.backgnd.setStyleSheet(u"background-color: rgba(15, 18, 22, 255);\n"
"border-radius: 8px\n"
"")
        self.backgnd.raise_()
        self.countdown_custom_title.raise_()
        self.custom_countdown.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Theme", u"\u5012\u8ba1\u65e5", None))
        self.countdown_custom_title.setText(QCoreApplication.translate("Theme", u"\u8ddd\u79bb \u4e2d\u8003 \u8fd8\u6709", None))
        self.custom_countdown.setText(QCoreApplication.translate("Theme", u"300 \u5929", None))
        self.backgnd.setText("")
    # retranslateUi
