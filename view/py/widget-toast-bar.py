# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-toast-bar.ui'
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
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(646, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 22)
        self.backgnd = QFrame(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setStyleSheet(u"border: none;\n"
"color: rgba(255, 255, 255, 255);\n"
"font-weight: bold;\n"
"border-radius: 8px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 200, 150, 255), stop:1 rgba(217, 147, 107, 255));")
        self.backgnd.setFrameShape(QFrame.StyledPanel)
        self.backgnd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.backgnd)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(52)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(23)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon = QLabel(self.backgnd)
        self.icon.setObjectName(u"icon")
        self.icon.setStyleSheet(u"background: transparent")
        self.icon.setPixmap(QPixmap(u":/svg/attend_class.svg"))
        self.icon.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.icon)

        self.title = QLabel(self.backgnd)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(22)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent")
        self.title.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.title)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.subtitle = QLabel(self.backgnd)
        self.subtitle.setObjectName(u"subtitle")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        self.subtitle.setFont(font1)
        self.subtitle.setStyleSheet(u"background: transparent;\n"
"font-weight: bold;\n"
"color: rgba(255, 255, 255, 200);")
        self.subtitle.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.subtitle)

        self.lesson = QLabel(self.backgnd)
        self.lesson.setObjectName(u"lesson")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.lesson.setFont(font2)
        self.lesson.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent")
        self.lesson.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lesson.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lesson)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.backgnd)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("Form", u"\u4e0a\u8bfe", None))
        self.subtitle.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8bfe\u7a0b", None))
        self.lesson.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
    # retranslateUi
