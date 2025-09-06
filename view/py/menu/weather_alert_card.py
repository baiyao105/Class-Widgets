# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather_alert_card.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, ElevatedCardWidget, ProgressBar, SimpleCardWidget,
    StrongBodyLabel)

class Ui_WeatherAlertCard(object):
    def setupUi(self, WeatherAlertCard):
        if not WeatherAlertCard.objectName():
            WeatherAlertCard.setObjectName(u"WeatherAlertCard")
        WeatherAlertCard.resize(161, 161)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WeatherAlertCard.sizePolicy().hasHeightForWidth())
        WeatherAlertCard.setSizePolicy(sizePolicy)
        WeatherAlertCard.setMinimumSize(QSize(161, 161))
        WeatherAlertCard.setMaximumSize(QSize(161, 161))
        self.verticalLayout = QVBoxLayout(WeatherAlertCard)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.topSpacer_3 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.topSpacer_3)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.alert_icon = QLabel(WeatherAlertCard)
        self.alert_icon.setObjectName(u"alert_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.alert_icon.sizePolicy().hasHeightForWidth())
        self.alert_icon.setSizePolicy(sizePolicy1)
        self.alert_icon.setMaximumSize(QSize(75, 75))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.alert_icon.setFont(font)
        self.alert_icon.setStyleSheet(u"color: rgba(120, 120, 120, 180);\n"
"font-weight: bold;")
        self.alert_icon.setTextFormat(Qt.PlainText)
        self.alert_icon.setPixmap(QPixmap(u":/png/weather/alerts/blue.png"))
        self.alert_icon.setScaledContents(True)
        self.alert_icon.setAlignment(Qt.AlignCenter)
        self.alert_icon.setWordWrap(False)

        self.verticalLayout_34.addWidget(self.alert_icon, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_7.addLayout(self.verticalLayout_34)

        self.topSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.topSpacer_2)

        self.progressBar = ProgressBar(WeatherAlertCard)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QSize(0, 5))
        self.progressBar.setMaximumSize(QSize(50, 5))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setUseAni(True)
        self.progressBar.setVal(0.000000000000000)

        self.verticalLayout_7.addWidget(self.progressBar, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.alerts_label = StrongBodyLabel(WeatherAlertCard)
        self.alerts_label.setObjectName(u"alerts_label")
        font1 = QFont()
        font1.setFamilies([u"HarmonyOS Sans SC"])
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.alerts_label.setFont(font1)
        self.alerts_label.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.alerts_label, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addLayout(self.verticalLayout_30)


        self.verticalLayout.addLayout(self.verticalLayout_7)


        self.retranslateUi(WeatherAlertCard)

        QMetaObject.connectSlotsByName(WeatherAlertCard)
    # setupUi

    def retranslateUi(self, WeatherAlertCard):
        self.alert_icon.setText("")
        self.alerts_label.setText(QCoreApplication.translate("WeatherAlertCard", u"-- \u9884\u8b66", None))
        pass
    # retranslateUi
