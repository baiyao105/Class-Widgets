# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedule_db_edit.ui'
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

from qfluentwidgets import (BodyLabel, LineEdit, ListWidget, PrimaryPushButton,
    PushButton, TitleLabel, ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(537, 627)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.db_list = ListWidget(Form)
        self.db_list.setObjectName(u"db_list")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_list.sizePolicy().hasHeightForWidth())
        self.db_list.setSizePolicy(sizePolicy)
        self.db_list.setDefaultDropAction(Qt.IgnoreAction)
        self.db_list.setAlternatingRowColors(True)

        self.horizontalLayout_6.addWidget(self.db_list)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel_2 = BodyLabel(Form)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy1)
        self.BodyLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BodyLabel_2.setWordWrap(True)

        self.horizontalLayout.addWidget(self.BodyLabel_2)

        self.db_short = LineEdit(Form)
        self.db_short.setObjectName(u"db_short")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.db_short.sizePolicy().hasHeightForWidth())
        self.db_short.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.db_short)

        self.BodyLabel_3 = BodyLabel(Form)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy1.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy1)
        self.BodyLabel_3.setWordWrap(True)

        self.horizontalLayout.addWidget(self.BodyLabel_3)

        self.db_url = LineEdit(Form)
        self.db_url.setObjectName(u"db_url")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.db_url.sizePolicy().hasHeightForWidth())
        self.db_url.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.db_url)

        self.add_button = ToolButton(Form)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout.addWidget(self.add_button)

        self.set_button = ToolButton(Form)
        self.set_button.setObjectName(u"set_button")

        self.horizontalLayout.addWidget(self.set_button)

        self.clear_button = ToolButton(Form)
        self.clear_button.setObjectName(u"clear_button")

        self.horizontalLayout.addWidget(self.clear_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.save = PrimaryPushButton(Form)
        self.save.setObjectName(u"save")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy4)
        self.save.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u8bfe\u8868\u6570\u636e\u5e93\u7f16\u8f91", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5e93\u7b80\u79f0", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5e93\u5730\u5740", None))
        self.save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi
