# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedule_edit.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QListView,
    QListWidgetItem, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, CardWidget, ComboBox,
    ElevatedCardWidget, LineEdit, ListWidget, PrimaryPushButton,
    PushButton, SimpleCardWidget, StrongBodyLabel, SubtitleLabel,
    TitleLabel, ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(662, 627)
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

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CardWidget.sizePolicy().hasHeightForWidth())
        self.CardWidget.setSizePolicy(sizePolicy)
        self.CardWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.CardWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.StrongBodyLabel)

        self.week_combo = ComboBox(self.CardWidget)
        self.week_combo.setObjectName(u"week_combo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.week_combo.sizePolicy().hasHeightForWidth())
        self.week_combo.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.week_combo)


        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(Form)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.StrongBodyLabel_2.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_2.setSizePolicy(sizePolicy2)
        self.StrongBodyLabel_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.StrongBodyLabel_2)

        self.CaptionLabel = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setWordWrap(True)
        self.CaptionLabel.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_3.addWidget(self.CaptionLabel)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.week_type_combo = ComboBox(self.CardWidget_2)
        self.week_type_combo.setObjectName(u"week_type_combo")

        self.horizontalLayout_3.addWidget(self.week_type_combo)

        self.copy_schedule = PushButton(self.CardWidget_2)
        self.copy_schedule.setObjectName(u"copy_schedule")

        self.horizontalLayout_3.addWidget(self.copy_schedule)


        self.verticalLayout.addWidget(self.CardWidget_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.schedule_list = ListWidget(Form)
        self.schedule_list.setObjectName(u"schedule_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.schedule_list.sizePolicy().hasHeightForWidth())
        self.schedule_list.setSizePolicy(sizePolicy3)
        self.schedule_list.setDefaultDropAction(Qt.IgnoreAction)
        self.schedule_list.setAlternatingRowColors(True)

        self.horizontalLayout_6.addWidget(self.schedule_list)

        self.ElevatedCardWidget = ElevatedCardWidget(Form)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.verticalLayout_4 = QVBoxLayout(self.ElevatedCardWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(16, 16, 16, 16)
        self.StrongBodyLabel_3 = StrongBodyLabel(self.ElevatedCardWidget)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")
        self.StrongBodyLabel_3.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.StrongBodyLabel_3)

        self.subject_list = ListWidget(self.ElevatedCardWidget)
        self.subject_list.setObjectName(u"subject_list")
        sizePolicy3.setHeightForWidth(self.subject_list.sizePolicy().hasHeightForWidth())
        self.subject_list.setSizePolicy(sizePolicy3)
        self.subject_list.setProperty("showDropIndicator", False)
        self.subject_list.setDragEnabled(False)
        self.subject_list.setDragDropOverwriteMode(False)
        self.subject_list.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.subject_list.setDefaultDropAction(Qt.IgnoreAction)
        self.subject_list.setAlternatingRowColors(False)
        self.subject_list.setMovement(QListView.Static)
        self.subject_list.setProperty("isWrapping", True)
        self.subject_list.setResizeMode(QListView.Adjust)
        self.subject_list.setLayoutMode(QListView.SinglePass)
        self.subject_list.setViewMode(QListView.IconMode)

        self.verticalLayout_4.addWidget(self.subject_list)

        self.quick_select_week = PushButton(self.ElevatedCardWidget)
        self.quick_select_week.setObjectName(u"quick_select_week")

        self.verticalLayout_4.addWidget(self.quick_select_week)


        self.horizontalLayout_6.addWidget(self.ElevatedCardWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel_2 = BodyLabel(Form)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy4)
        self.BodyLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BodyLabel_2.setWordWrap(True)

        self.horizontalLayout.addWidget(self.BodyLabel_2)

        self.class_combo = ComboBox(Form)
        self.class_combo.setObjectName(u"class_combo")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.class_combo.sizePolicy().hasHeightForWidth())
        self.class_combo.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.class_combo)

        self.BodyLabel_3 = BodyLabel(Form)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy4.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy4)
        self.BodyLabel_3.setWordWrap(True)

        self.horizontalLayout.addWidget(self.BodyLabel_3)

        self.custom_class = LineEdit(Form)
        self.custom_class.setObjectName(u"custom_class")
        sizePolicy5.setHeightForWidth(self.custom_class.sizePolicy().hasHeightForWidth())
        self.custom_class.setSizePolicy(sizePolicy5)
        self.custom_class.setReadOnly(False)

        self.horizontalLayout.addWidget(self.custom_class)

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

        self.save_schedule = PrimaryPushButton(Form)
        self.save_schedule.setObjectName(u"save_schedule")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.save_schedule.sizePolicy().hasHeightForWidth())
        self.save_schedule.setSizePolicy(sizePolicy6)
        self.save_schedule.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.save_schedule)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b\u8868\u7f16\u8f91", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b\u8868", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u661f\u671f", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u5355/\u53cc\u5468\u8bfe\u8868", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u82e5\u8981\u542f\u7528\u53cc\u5468\u8bfe\u8868\uff0c\u8bf7\u5728\u201c\u9ad8\u7ea7\u9009\u9879\u201d\u4e2d \u542f\u7528\u5355\u53cc\u5468\u8bfe\u8868\u548c\u8bbe\u7f6e\u5f00\u5b66\u65e5\u671f", None))
        self.copy_schedule.setText(QCoreApplication.translate("Form", u"\u590d\u5236\u5355\u5468\u8bfe\u8868", None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("Form", u"\u5feb\u901f\u6dfb\u52a0\u8bfe\u7a0b", None))
        self.quick_select_week.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u5929", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b/\u6d3b\u52a8", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u8bfe\u7a0b", None))
        self.save_schedule.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi
