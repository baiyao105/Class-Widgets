# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-floating.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (ProgressBar, ProgressRing)

class Ui_Theme(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 145)
        Form.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 22)
        self.backgnd = QFrame(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setStyleSheet(u"background-color: rgba(242, 243, 245, 255);\n"
"border-radius: 8px")
        self.backgnd.setFrameShape(QFrame.StyledPanel)
        self.backgnd.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.backgnd)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(16, 4, 16, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.backgnd)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(50, 5))
        self.label.setStyleSheet(u"background-color:#503D3D3D;\n"
"border-radius: 2px")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.subject = QLabel(self.backgnd)
        self.subject.setObjectName(u"subject")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(22)
        font.setBold(True)
        self.subject.setFont(font)
        self.subject.setStyleSheet(u"color: rgba(37, 37, 37, 255);\n"
"font-weight: bold")

        self.verticalLayout_4.addWidget(self.subject)

        self.activity_countdown = QLabel(self.backgnd)
        self.activity_countdown.setObjectName(u"activity_countdown")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.activity_countdown.setFont(font1)
        self.activity_countdown.setStyleSheet(u"color: rgba(0, 0, 0, 90);\n"
"font-weight: bold;")

        self.verticalLayout_4.addWidget(self.activity_countdown)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.progressBar = ProgressRing(self.backgnd)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMinimumSize(QSize(60, 60))
        self.progressBar.setMaximumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.progressBar.setFont(font2)
        self.progressBar.setStyleSheet(u"font-weight: bold;")
        self.progressBar.setTextVisible(True)
        self.progressBar.setVal(0.000000000000000)
        self.progressBar.setStrokeWidth(7)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.backgnd)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Theme", u"Form", None))
        self.subject.setText(QCoreApplication.translate("Theme", u"\u6d4b\u8bd5", None))
        self.activity_countdown.setText(QCoreApplication.translate("Theme", u"<0\u5206\u949f", None))
        self.progressBar.setFormat(QCoreApplication.translate("Theme", u"%p%", None))
    # retranslateUi
