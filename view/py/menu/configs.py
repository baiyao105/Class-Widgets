# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configs.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidgetItem, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, ListWidget, PushButton, SmoothScrollArea,
    TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1073, 814)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background: transparent; border: none")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1025, 711))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.config_url = LineEdit(self.scrollAreaWidgetContents)
        self.config_url.setObjectName(u"config_url")

        self.horizontalLayout.addWidget(self.config_url)

        self.config_download = PushButton(self.scrollAreaWidgetContents)
        self.config_download.setObjectName(u"config_download")

        self.horizontalLayout.addWidget(self.config_download)

        self.config_update = PushButton(self.scrollAreaWidgetContents)
        self.config_update.setObjectName(u"config_update")

        self.horizontalLayout.addWidget(self.config_update)

        self.config_upload = PushButton(self.scrollAreaWidgetContents)
        self.config_upload.setObjectName(u"config_upload")

        self.horizontalLayout.addWidget(self.config_upload)

        self.config_new = PushButton(self.scrollAreaWidgetContents)
        self.config_new.setObjectName(u"config_new")

        self.horizontalLayout.addWidget(self.config_new)

        self.config_import = PushButton(self.scrollAreaWidgetContents)
        self.config_import.setObjectName(u"config_import")

        self.horizontalLayout.addWidget(self.config_import)

        self.config_db_edit = PushButton(self.scrollAreaWidgetContents)
        self.config_db_edit.setObjectName(u"config_db_edit")

        self.horizontalLayout.addWidget(self.config_db_edit)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.config_table = ListWidget(self.scrollAreaWidgetContents)
        self.config_table.setObjectName(u"config_table")

        self.verticalLayout_9.addWidget(self.config_table)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u914d\u7f6e\u6587\u4ef6", None))
        self.config_url.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f7f\u7528 {db}:{id} \u683c\u5f0f\u4ece\u9884\u8bbe\u6570\u636e\u5e93\u83b7\u53d6\uff0c\u6216\u8f93\u5165\u5b8c\u6574 url", None))
        self.config_download.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.config_update.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u5f53\u524d", None))
        self.config_upload.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u5f53\u524d", None))
        self.config_new.setText(QCoreApplication.translate("Form", u"\u65b0\u5efa", None))
        self.config_import.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165", None))
        self.config_db_edit.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5e93\u7f16\u8f91", None))
    # retranslateUi
