# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-weather.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Theme(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(180, 110)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.current_city = QLabel(Form)
        self.current_city.setObjectName(u"current_city")
        self.current_city.setGeometry(QRect(10, 10, 161, 41))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.current_city.setFont(font)
        self.current_city.setStyleSheet(u"color: rgba(255, 255, 255, 185);\n"
"font-weight: bold;")
        self.current_city.setTextFormat(Qt.PlainText)
        self.current_city.setAlignment(Qt.AlignCenter)
        self.backgnd = QLabel(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setGeometry(QRect(10, 10, 161, 81))
        self.backgnd.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 60, 110, 245), stop:1 rgba(75, 175, 245, 245));\n"
"border-radius: 8px;\n"
"border-image: url();\n"
"")
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 121, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.weather_icon = QLabel(self.horizontalLayoutWidget)
        self.weather_icon.setObjectName(u"weather_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_icon.sizePolicy().hasHeightForWidth())
        self.weather_icon.setSizePolicy(sizePolicy)
        self.weather_icon.setPixmap(QPixmap(u":/svg/img/weather/0.svg"))
        self.weather_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.weather_icon)

        self.temperature = QLabel(self.horizontalLayoutWidget)
        self.temperature.setObjectName(u"temperature")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.temperature.sizePolicy().hasHeightForWidth())
        self.temperature.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.temperature.setFont(font1)
        self.temperature.setStyleSheet(u"border: none;\n"
"color: rgba(255, 255, 255, 255);\n"
"font-weight: bold")
        self.temperature.setTextFormat(Qt.PlainText)
        self.temperature.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.temperature)

        self.backgnd.raise_()
        self.current_city.raise_()
        self.horizontalLayoutWidget.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Theme", u"\u5929\u6c14", None))
        self.current_city.setText(QCoreApplication.translate("Theme", u"\u5f53\u524d\u57ce\u5e02", None))
        self.backgnd.setText("")
        self.weather_icon.setText("")
        self.temperature.setText(QCoreApplication.translate("Theme", u"114\u2109", None))
    # retranslateUi
