# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-next-activity.ui'
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
        Form.resize(290, 125)
        Form.setMinimumSize(QSize(0, 100))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.next_subtitle = QLabel(Form)
        self.next_subtitle.setObjectName(u"next_subtitle")
        self.next_subtitle.setGeometry(QRect(40, 20, 211, 31))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(14)
        font.setBold(True)
        self.next_subtitle.setFont(font)
        self.next_subtitle.setStyleSheet(u"color: rgba(0, 0, 0, 90);\n"
"font-weight: bold;")
        self.next_subtitle.setTextFormat(Qt.PlainText)
        self.next_subtitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.next_lesson_text = QLabel(Form)
        self.next_lesson_text.setObjectName(u"next_lesson_text")
        self.next_lesson_text.setGeometry(QRect(40, 40, 221, 51))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(21)
        font1.setBold(True)
        self.next_lesson_text.setFont(font1)
        self.next_lesson_text.setStyleSheet(u"border: none;\n"
"color: rgba(37, 37, 37, 255);\n"
"font-weight: bold")
        self.next_lesson_text.setTextFormat(Qt.PlainText)
        self.next_lesson_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.backgnd = QLabel(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setGeometry(QRect(10, 10, 271, 91))
        self.backgnd.setStyleSheet(u"background-color: rgba(242, 243, 245, 255);\n"
"border-radius: 8px")
        self.backgnd.raise_()
        self.next_subtitle.raise_()
        self.next_lesson_text.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Theme", u"\u66f4\u591a\u6d3b\u52a8", None))
        self.next_subtitle.setText(QCoreApplication.translate("Theme", u"\u63a5\u4e0b\u6765", None))
        self.next_lesson_text.setText(QCoreApplication.translate("Theme", u"\u6d4b\u8bd5\u6d4b\u8bd5", None))
        self.backgnd.setText("")
    # retranslateUi
