# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extra_menu.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QListView, QListWidgetItem, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, CardWidget, ComboBox,
    HyperlinkButton, LineEdit, ListWidget, PrimaryPushButton,
    PushButton, StrongBodyLabel, SubtitleLabel, TitleLabel,
    ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(764, 683)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SubtitleLabel_2 = SubtitleLabel(self.widget)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.SubtitleLabel_2)

        self.CardWidget_2 = CardWidget(self.widget)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CardWidget_2.sizePolicy().hasHeightForWidth())
        self.CardWidget_2.setSizePolicy(sizePolicy)
        self.CardWidget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        self.StrongBodyLabel_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.StrongBodyLabel_2)

        self.CaptionLabel = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.CaptionLabel)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.select_temp_schedule = ComboBox(self.CardWidget_2)
        self.select_temp_schedule.setObjectName(u"select_temp_schedule")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.select_temp_schedule.sizePolicy().hasHeightForWidth())
        self.select_temp_schedule.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.select_temp_schedule)

        self.select_temp_week = ComboBox(self.CardWidget_2)
        self.select_temp_week.setObjectName(u"select_temp_week")
        sizePolicy1.setHeightForWidth(self.select_temp_week.sizePolicy().hasHeightForWidth())
        self.select_temp_week.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.select_temp_week)


        self.verticalLayout_3.addWidget(self.CardWidget_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SubtitleLabel = SubtitleLabel(self.widget)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.SubtitleLabel)

        self.CaptionLabel_3 = CaptionLabel(self.widget)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.CaptionLabel_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.schedule_list = ListWidget(self.widget)
        self.schedule_list.setObjectName(u"schedule_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.schedule_list.sizePolicy().hasHeightForWidth())
        self.schedule_list.setSizePolicy(sizePolicy2)
        self.schedule_list.setMinimumSize(QSize(0, 275))
        self.schedule_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.schedule_list.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.schedule_list.setDefaultDropAction(Qt.MoveAction)
        self.schedule_list.setMovement(QListView.Static)
        self.schedule_list.setProperty("isWrapping", False)
        self.schedule_list.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.schedule_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_3.addWidget(self.schedule_list)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel_2 = BodyLabel(self.widget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy3)
        self.BodyLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BodyLabel_2.setWordWrap(True)

        self.horizontalLayout.addWidget(self.BodyLabel_2)

        self.class_combo = ComboBox(self.widget)
        self.class_combo.setObjectName(u"class_combo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.class_combo.sizePolicy().hasHeightForWidth())
        self.class_combo.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.class_combo)

        self.BodyLabel_3 = BodyLabel(self.widget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy3.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy3)
        self.BodyLabel_3.setWordWrap(True)

        self.horizontalLayout.addWidget(self.BodyLabel_3)

        self.custom_class = LineEdit(self.widget)
        self.custom_class.setObjectName(u"custom_class")
        sizePolicy4.setHeightForWidth(self.custom_class.sizePolicy().hasHeightForWidth())
        self.custom_class.setSizePolicy(sizePolicy4)
        self.custom_class.setReadOnly(False)

        self.horizontalLayout.addWidget(self.custom_class)

        self.set_button = ToolButton(self.widget)
        self.set_button.setObjectName(u"set_button")

        self.horizontalLayout.addWidget(self.set_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.CaptionLabel_2 = CaptionLabel(Form)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.CaptionLabel_2)

        self.redirect_to_settings = HyperlinkButton(Form)
        self.redirect_to_settings.setObjectName(u"redirect_to_settings")

        self.horizontalLayout_4.addWidget(self.redirect_to_settings)

        self.save_temp_conf = PrimaryPushButton(Form)
        self.save_temp_conf.setObjectName(u"save_temp_conf")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.save_temp_conf.sizePolicy().hasHeightForWidth())
        self.save_temp_conf.setSizePolicy(sizePolicy5)
        self.save_temp_conf.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.save_temp_conf)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u989d\u5916\u9009\u9879", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u8c03\u4f11", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u8c03\u4f11\u661f\u671f", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u5c06\u66ff\u6362\u5f53\u524d\u8c03\u4f11\u65e5\u7684\u8bfe\u7a0b\u8868\u4e3a\u9009\u5b9a\u661f\u671f", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u6362\u8bfe", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"\u4e34\u65f6\u66ff\u6362\u5f53\u5929\u7684\u8bfe\u7a0b\uff0c\u91cd\u542f\u540e\u5931\u6548", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b/\u6d3b\u52a8", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u8bfe\u7a0b", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", u"*\u6240\u6709\u66f4\u6539\u5728\u91cd\u542f\u540e\u91cd\u7f6e", None))
        self.redirect_to_settings.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8\u66f4\u591a\u8bbe\u7f6e", None))
        self.save_temp_conf.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi
