# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_item.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, DropDownToolButton, StrongBodyLabel, ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 60)
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(16, 8, 16, 8)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 4, 0, 4)
        self.horizontalSpacer_2 = QSpacerItem(3, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.file_name = StrongBodyLabel(self.frame)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setFrameShadow(QFrame.Plain)
        self.file_name.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        self.file_name.setWordWrap(True)

        self.verticalLayout.addWidget(self.file_name)

        self.file_path = BodyLabel(self.frame)
        self.file_path.setObjectName(u"file_path")
        self.file_path.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        self.file_path.setWordWrap(True)

        self.verticalLayout.addWidget(self.file_path)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.horizontalLayout_4.addWidget(self.frame)

        self.horizontalSpacer_3 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.file_item_settings = DropDownToolButton(Form)
        self.file_item_settings.setObjectName(u"file_item_settings")
        self.file_item_settings.setMinimumSize(QSize(32, 32))
        self.file_item_settings.setMaximumSize(QSize(32, 32))
        self.file_item_settings.setStyleSheet(u"background: rgba(255, 255, 255, 0.1); border: none")

        self.horizontalLayout_4.addWidget(self.file_item_settings)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.file_name.setText(QCoreApplication.translate("Form", u"File name", None))
        self.file_path.setText(QCoreApplication.translate("Form", u"file url file url file url file url file url file url ", None))
    # retranslateUi
