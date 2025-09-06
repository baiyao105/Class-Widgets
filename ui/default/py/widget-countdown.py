# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-countdown.ui'
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

from qfluentwidgets import ProgressBar

class Ui_Theme(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.progressBar = ProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 90, 161, 5))
        self.progressBar.setMinimumSize(QSize(0, 5))
        self.progressBar.setMaximumSize(QSize(16777215, 6))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setUseAni(True)
        self.progressBar.setVal(0.000000000000000)
        self.activity_countdown_title = QLabel(Form)
        self.activity_countdown_title.setObjectName(u"activity_countdown_title")
        self.activity_countdown_title.setGeometry(QRect(20, 20, 161, 31))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(14)
        font.setBold(True)
        self.activity_countdown_title.setFont(font)
        self.activity_countdown_title.setStyleSheet(u"color: rgba(0, 0, 0, 90);\n"
"font-weight: bold;")
        self.activity_countdown_title.setTextFormat(Qt.PlainText)
        self.activity_countdown_title.setAlignment(Qt.AlignCenter)
        self.activity_countdown = QLabel(Form)
        self.activity_countdown.setObjectName(u"activity_countdown")
        self.activity_countdown.setGeometry(QRect(20, 40, 161, 51))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(21)
        font1.setBold(True)
        self.activity_countdown.setFont(font1)
        self.activity_countdown.setStyleSheet(u"border: none;\n"
"color: rgba(37, 37, 37, 255);\n"
"font-weight: bold")
        self.activity_countdown.setTextFormat(Qt.PlainText)
        self.activity_countdown.setAlignment(Qt.AlignCenter)
        self.backgnd = QLabel(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setGeometry(QRect(10, 10, 181, 91))
        self.backgnd.setStyleSheet(u"background-color: rgba(242, 243, 245, 255);\n"
"border-radius: 8px")
        self.backgnd.raise_()
        self.progressBar.raise_()
        self.activity_countdown_title.raise_()
        self.activity_countdown.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Theme", u"\u6d3b\u52a8\u5012\u8ba1\u65f6", None))
        self.activity_countdown_title.setText(QCoreApplication.translate("Theme", u"\u5012\u8ba1\u65f6", None))
        self.activity_countdown.setText(QCoreApplication.translate("Theme", u"00:00", None))
        self.backgnd.setText("")
    # retranslateUi
