# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-base.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Theme(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(160, 110)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 125))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(22)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 24)
        self.backgnd = QFrame(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setStyleSheet(u"background-color: rgba(242, 243, 245, 255);\n"
"border-radius: 8px")
        self.backgnd.setFrameShape(QFrame.StyledPanel)
        self.backgnd.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.backgnd)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 12, -1, 12)
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.title = QLabel(self.backgnd)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgba(0, 0, 0, 90);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font-weight: bold;")
        self.title.setTextFormat(Qt.PlainText)
        self.title.setAlignment(Qt.AlignCenter)

        self.titleLayout.addWidget(self.title)


        self.verticalLayout.addLayout(self.titleLayout)

        self.contentLayout = QHBoxLayout()
        self.contentLayout.setObjectName(u"contentLayout")
        self.content = QLabel(self.backgnd)
        self.content.setObjectName(u"content")
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.content.setFont(font1)
        self.content.setStyleSheet(u"border: none;\n"
"color: rgba(37, 37, 37, 255);\n"
"font-weight: bold;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.content.setTextFormat(Qt.PlainText)
        self.content.setAlignment(Qt.AlignCenter)

        self.contentLayout.addWidget(self.content)


        self.verticalLayout.addLayout(self.contentLayout)


        self.horizontalLayout.addWidget(self.backgnd)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Theme", u"\u57fa\u672c\u7ec4\u4ef6", None))
        self.title.setText(QCoreApplication.translate("Theme", u"Title", None))
        self.content.setText(QCoreApplication.translate("Theme", u"Content", None))
    # retranslateUi
