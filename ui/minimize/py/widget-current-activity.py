# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-current-activity.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Theme(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(290, 110)
        Form.setMinimumSize(QSize(0, 100))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.subject = QPushButton(Form)
        self.subject.setObjectName(u"subject")
        self.subject.setGeometry(QRect(20, 30, 251, 61))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(19)
        font.setBold(True)
        self.subject.setFont(font)
        self.subject.setStyleSheet(u"border: none;\n"
"color: rgba(37, 37, 37, 255);\n"
"font-weight: bold;")
        icon = QIcon()
        icon.addFile(u":/svg/img/subject/it.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.subject.setIcon(icon)
        self.subject.setIconSize(QSize(36, 26))
        self.blurEffect = QLabel(Form)
        self.blurEffect.setObjectName(u"blurEffect")
        self.blurEffect.setGeometry(QRect(130, 35, 25, 25))
        self.blurEffect.setStyleSheet(u"background-color: rgb(0, 255, 127);\n"
"border-radius:20px")
        self.sub_title = QLabel(Form)
        self.sub_title.setObjectName(u"sub_title")
        self.sub_title.setGeometry(QRect(30, 10, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.sub_title.setFont(font1)
        self.sub_title.setStyleSheet(u"color: rgba(0, 0, 0, 90);\n"
"font-weight: bold;")
        self.sub_title.setTextFormat(Qt.PlainText)
        self.sub_title.setAlignment(Qt.AlignCenter)
        self.backgnd = QLabel(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setGeometry(QRect(10, 10, 271, 81))
        self.backgnd.setStyleSheet(u"background-color: rgba(242, 243, 245, 255);\n"
"border-radius: 8px\n"
"")
        self.backgnd.raise_()
        self.blurEffect.raise_()
        self.sub_title.raise_()
        self.subject.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Theme", u"\u5f53\u524d\u6d3b\u52a8", None))
        self.subject.setText(QCoreApplication.translate("Theme", u"  \u6d4b\u8bd5", None))
        self.blurEffect.setText("")
        self.sub_title.setText(QCoreApplication.translate("Theme", u"\u5f53\u524d\u6d3b\u52a8", None))
        self.backgnd.setText("")
    # retranslateUi
