# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toast-open_dialog.ui'
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

from qfluentwidgets import (HyperlinkButton, ProgressBar, ProgressRing, PushButton)

class Ui_Theme(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(281, 112)
        Form.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 8, 8, 22)
        self.backgnd = QFrame(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setStyleSheet(u"background-color: rgba(10, 10, 15, 245);\n"
"border-radius: 38px")
        self.backgnd.setFrameShape(QFrame.StyledPanel)
        self.backgnd.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.backgnd)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.opening_countdown = ProgressRing(self.backgnd)
        self.opening_countdown.setObjectName(u"opening_countdown")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opening_countdown.sizePolicy().hasHeightForWidth())
        self.opening_countdown.setSizePolicy(sizePolicy)
        self.opening_countdown.setMinimumSize(QSize(58, 58))
        self.opening_countdown.setMaximumSize(QSize(58, 58))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(12)
        font.setBold(True)
        self.opening_countdown.setFont(font)
        self.opening_countdown.setStyleSheet(u"font-weight: bold;")
        self.opening_countdown.setTextVisible(False)
        self.opening_countdown.setVal(0.000000000000000)
        self.opening_countdown.setStrokeWidth(7)

        self.horizontalLayout.addWidget(self.opening_countdown)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.subtitle_label = QLabel(self.backgnd)
        self.subtitle_label.setObjectName(u"subtitle_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.subtitle_label.sizePolicy().hasHeightForWidth())
        self.subtitle_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.subtitle_label.setFont(font1)
        self.subtitle_label.setStyleSheet(u"color: rgba(188, 188, 188, 200);\n"
"background-color: rgba(0,0,0,0);\n"
"font-weight: bold;")
        self.subtitle_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.subtitle_label)

        self.action_name = QLabel(self.backgnd)
        self.action_name.setObjectName(u"action_name")
        sizePolicy1.setHeightForWidth(self.action_name.sizePolicy().hasHeightForWidth())
        self.action_name.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(17)
        font2.setBold(True)
        self.action_name.setFont(font2)
        self.action_name.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(0,0,0,0);\n"
"font-weight: bold")
        self.action_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.action_name)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_opening = HyperlinkButton(self.backgnd)
        self.cancel_opening.setObjectName(u"cancel_opening")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cancel_opening.sizePolicy().hasHeightForWidth())
        self.cancel_opening.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.cancel_opening.setFont(font3)

        self.horizontalLayout.addWidget(self.cancel_opening)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addWidget(self.backgnd)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Theme", u"Form", None))
        self.opening_countdown.setFormat(QCoreApplication.translate("Theme", u"%p", None))
        self.subtitle_label.setText(QCoreApplication.translate("Theme", u"\u5373\u5c06\u6253\u5f00", None))
        self.action_name.setText(QCoreApplication.translate("Theme", u"\u6d4b\u8bd5", None))
        self.cancel_opening.setText(QCoreApplication.translate("Theme", u"\u53d6\u6d88", None))
    # retranslateUi
