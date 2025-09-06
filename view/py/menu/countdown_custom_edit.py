# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'countdown_custom_edit.ui'
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

from qfluentwidgets import (BodyLabel, CalendarPicker, ComboBox, LineEdit,
    ListWidget, PrimaryPushButton, PushButton, SpinBox,
    SubtitleLabel, TitleLabel, ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(648, 627)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.SubtitleLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.countdown_list = ListWidget(Form)
        self.countdown_list.setObjectName(u"countdown_list")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countdown_list.sizePolicy().hasHeightForWidth())
        self.countdown_list.setSizePolicy(sizePolicy)
        self.countdown_list.setDefaultDropAction(Qt.IgnoreAction)
        self.countdown_list.setAlternatingRowColors(True)

        self.horizontalLayout_6.addWidget(self.countdown_list)


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

        self.text_cd = LineEdit(Form)
        self.text_cd.setObjectName(u"text_cd")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.text_cd.sizePolicy().hasHeightForWidth())
        self.text_cd.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.text_cd)

        self.BodyLabel_3 = BodyLabel(Form)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy1.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy1)
        self.BodyLabel_3.setWordWrap(True)

        self.horizontalLayout.addWidget(self.BodyLabel_3)

        self.set_countdown_date = CalendarPicker(Form)
        self.set_countdown_date.setObjectName(u"set_countdown_date")
        sizePolicy2.setHeightForWidth(self.set_countdown_date.sizePolicy().hasHeightForWidth())
        self.set_countdown_date.setSizePolicy(sizePolicy2)
        self.set_countdown_date.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.set_countdown_date)

        self.add_button_cd = ToolButton(Form)
        self.add_button_cd.setObjectName(u"add_button_cd")

        self.horizontalLayout.addWidget(self.add_button_cd)

        self.set_button_cd = ToolButton(Form)
        self.set_button_cd.setObjectName(u"set_button_cd")

        self.horizontalLayout.addWidget(self.set_button_cd)

        self.clear_button_cd = ToolButton(Form)
        self.clear_button_cd.setObjectName(u"clear_button_cd")

        self.horizontalLayout.addWidget(self.clear_button_cd)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BodyLabel_4 = BodyLabel(Form)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        sizePolicy1.setHeightForWidth(self.BodyLabel_4.sizePolicy().hasHeightForWidth())
        self.BodyLabel_4.setSizePolicy(sizePolicy1)
        self.BodyLabel_4.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.BodyLabel_4)

        self.countdown_mode = ComboBox(Form)
        self.countdown_mode.setObjectName(u"countdown_mode")
        sizePolicy2.setHeightForWidth(self.countdown_mode.sizePolicy().hasHeightForWidth())
        self.countdown_mode.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.countdown_mode)

        self.BodyLabel = BodyLabel(Form)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy1.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy1)
        self.BodyLabel.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.BodyLabel)

        self.countdown_upd_cd = SpinBox(Form)
        self.countdown_upd_cd.setObjectName(u"countdown_upd_cd")
        sizePolicy2.setHeightForWidth(self.countdown_upd_cd.sizePolicy().hasHeightForWidth())
        self.countdown_upd_cd.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.countdown_upd_cd)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.save_countdown = PrimaryPushButton(Form)
        self.save_countdown.setObjectName(u"save_countdown")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.save_countdown.sizePolicy().hasHeightForWidth())
        self.save_countdown.setSizePolicy(sizePolicy3)
        self.save_countdown.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.save_countdown)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u5012\u8ba1\u65f6\u7f16\u8f91", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u5012\u8ba1\u65f6", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u6587\u672c", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u65e5\u671f", None))
        self.set_countdown_date.setText(QCoreApplication.translate("Form", u"\u9009\u5b9a\u4e00\u4e2a\u65e5\u671f", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"\u5012\u8ba1\u65f6\u6a21\u5f0f", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u8f6e\u64ad\u95f4\u9694\uff08\u79d2\uff09", None))
        self.save_countdown.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi
