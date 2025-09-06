# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather_alert_msgbox.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_WeatherAlertMsgbox(object):
    def setupUi(self, WeatherAlertMsgbox):
        if not WeatherAlertMsgbox.objectName():
            WeatherAlertMsgbox.setObjectName(u"WeatherAlertMsgbox")
        WeatherAlertMsgbox.resize(592, 374)
        font = QFont()
        font.setStrikeOut(False)
        WeatherAlertMsgbox.setFont(font)
        WeatherAlertMsgbox.setStyleSheet(u"background: transparent; border: none")
        self.verticalLayout_Main = QVBoxLayout(WeatherAlertMsgbox)
        self.verticalLayout_Main.setSpacing(18)
        self.verticalLayout_Main.setObjectName(u"verticalLayout_Main")
        self.verticalLayout_Main.setContentsMargins(24, 24, 24, 24)
        self.verticalSpacer_2 = QSpacerItem(5, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_Main.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.headerLayout_2 = QHBoxLayout()
        self.headerLayout_2.setSpacing(12)
        self.headerLayout_2.setObjectName(u"headerLayout_2")
        self.alertIcon = QLabel(WeatherAlertMsgbox)
        self.alertIcon.setObjectName(u"alertIcon")
        self.alertIcon.setMinimumSize(QSize(32, 32))
        self.alertIcon.setMaximumSize(QSize(32, 32))
        self.alertIcon.setPixmap(QPixmap(u":/png/weather/alerts/red.png"))
        self.alertIcon.setScaledContents(True)
        self.alertIcon.setAlignment(Qt.AlignCenter)
        self.alertIcon.setWordWrap(True)

        self.headerLayout_2.addWidget(self.alertIcon)

        self.alertTitle = QLabel(WeatherAlertMsgbox)
        self.alertTitle.setObjectName(u"alertTitle")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.alertTitle.setFont(font1)
        self.alertTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.alertTitle.setWordWrap(True)

        self.headerLayout_2.addWidget(self.alertTitle)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.headerLayout_2.addItem(self.horizontalSpacer)

        self.publishTime = QLabel(WeatherAlertMsgbox)
        self.publishTime.setObjectName(u"publishTime")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(12)
        self.publishTime.setFont(font2)
        self.publishTime.setStyleSheet(u"color: #888888;")
        self.publishTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.publishTime.setWordWrap(True)

        self.headerLayout_2.addWidget(self.publishTime)

        self.horizontalSpacer_2 = QSpacerItem(1, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.headerLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.headerLayout_2)

        self.descriptionScrollArea = QScrollArea(WeatherAlertMsgbox)
        self.descriptionScrollArea.setObjectName(u"descriptionScrollArea")
        self.descriptionScrollArea.setStyleSheet(u"QScrollArea {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollArea QWidget {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #F5F5F5;\n"
"    width: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #C0C0C0;\n"
"    border-radius: 4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #A0A0A0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}")
        self.descriptionScrollArea.setFrameShape(QFrame.NoFrame)
        self.descriptionScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 542, 252))
        self.contentLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.contentLayout.setSpacing(12)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(16, 16, 16, 16)
        self.alertDescription = QLabel(self.scrollAreaWidgetContents)
        self.alertDescription.setObjectName(u"alertDescription")
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(16)
        self.alertDescription.setFont(font3)
        self.alertDescription.setLayoutDirection(Qt.LeftToRight)
        self.alertDescription.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.alertDescription.setWordWrap(True)
        self.alertDescription.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.contentLayout.addWidget(self.alertDescription)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.contentLayout.addItem(self.verticalSpacer)

        self.descriptionScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.descriptionScrollArea)


        self.verticalLayout_Main.addLayout(self.verticalLayout)


        self.retranslateUi(WeatherAlertMsgbox)

        QMetaObject.connectSlotsByName(WeatherAlertMsgbox)
    # setupUi

    def retranslateUi(self, WeatherAlertMsgbox):
        WeatherAlertMsgbox.setWindowTitle(QCoreApplication.translate("WeatherAlertMsgbox", u"WeatherAlertMsgbox", None))
        self.alertIcon.setText("")
        self.alertTitle.setText(QCoreApplication.translate("WeatherAlertMsgbox", u"-- \u7ea2\u8272\u9884\u8b66", None))
        self.publishTime.setText(QCoreApplication.translate("WeatherAlertMsgbox", u"0000-00-00 00:00", None))
        self.alertDescription.setText(QCoreApplication.translate("WeatherAlertMsgbox", u"NAN", None))
    # retranslateUi
