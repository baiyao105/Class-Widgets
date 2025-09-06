# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timeline_edit.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateTimeEdit, QHBoxLayout,
    QListWidgetItem, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, ComboBox, EditableComboBox,
    LineEdit, ListWidget, PrimaryPushButton, PushButton,
    SpinBox, SubtitleLabel, TimeEdit, TitleLabel,
    ToolButton, VerticalSeparator)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(843, 658)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SubtitleLabel_2 = SubtitleLabel(Form)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setMinimumSize(QSize(0, 33))
        self.SubtitleLabel_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.SubtitleLabel_2)

        self.tips_1 = CaptionLabel(Form)
        self.tips_1.setObjectName(u"tips_1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tips_1.sizePolicy().hasHeightForWidth())
        self.tips_1.setSizePolicy(sizePolicy)
        self.tips_1.setStyleSheet(u"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#7d000000}")
        self.tips_1.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.tips_1.setWordWrap(True)
        self.tips_1.setProperty("lightColor", QColor(0, 0, 0, 125))
        self.tips_1.setProperty("darkColor", QColor(255, 255, 255, 155))
        self.tips_1.setProperty("pixelFontSize", 14)

        self.verticalLayout.addWidget(self.tips_1)

        self.part_list = ListWidget(Form)
        self.part_list.setObjectName(u"part_list")
        sizePolicy.setHeightForWidth(self.part_list.sizePolicy().hasHeightForWidth())
        self.part_list.setSizePolicy(sizePolicy)
        self.part_list.setMinimumSize(QSize(0, 0))
        self.part_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.part_list.setDefaultDropAction(Qt.MoveAction)
        self.part_list.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.part_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BodyLabel_4 = BodyLabel(Form)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BodyLabel_4.sizePolicy().hasHeightForWidth())
        self.BodyLabel_4.setSizePolicy(sizePolicy1)
        self.BodyLabel_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BodyLabel_4.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.BodyLabel_4)

        self.name_part_combo = EditableComboBox(Form)
        self.name_part_combo.setObjectName(u"name_part_combo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.name_part_combo.sizePolicy().hasHeightForWidth())
        self.name_part_combo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.name_part_combo)

        self.BodyLabel_6 = BodyLabel(Form)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")
        sizePolicy1.setHeightForWidth(self.BodyLabel_6.sizePolicy().hasHeightForWidth())
        self.BodyLabel_6.setSizePolicy(sizePolicy1)
        self.BodyLabel_6.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.BodyLabel_6)

        self.part_type = ComboBox(Form)
        self.part_type.setObjectName(u"part_type")
        sizePolicy2.setHeightForWidth(self.part_type.sizePolicy().hasHeightForWidth())
        self.part_type.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.part_type)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.BodyLabel_5 = BodyLabel(Form)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")
        sizePolicy1.setHeightForWidth(self.BodyLabel_5.sizePolicy().hasHeightForWidth())
        self.BodyLabel_5.setSizePolicy(sizePolicy1)
        self.BodyLabel_5.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.BodyLabel_5)

        self.part_time = TimeEdit(Form)
        self.part_time.setObjectName(u"part_time")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.part_time.sizePolicy().hasHeightForWidth())
        self.part_time.setSizePolicy(sizePolicy3)
        self.part_time.setMinimumSize(QSize(150, 33))
        self.part_time.setCurrentSection(QDateTimeEdit.HourSection)
        self.part_time.setTime(QTime(7, 0, 0))

        self.horizontalLayout_5.addWidget(self.part_time)

        self.add_part_button = ToolButton(Form)
        self.add_part_button.setObjectName(u"add_part_button")

        self.horizontalLayout_5.addWidget(self.add_part_button)

        self.edit_part_button = ToolButton(Form)
        self.edit_part_button.setObjectName(u"edit_part_button")

        self.horizontalLayout_5.addWidget(self.edit_part_button)

        self.delete_part_button = ToolButton(Form)
        self.delete_part_button.setObjectName(u"delete_part_button")

        self.horizontalLayout_5.addWidget(self.delete_part_button)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.VerticalSeparator = VerticalSeparator(Form)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout.addWidget(self.VerticalSeparator)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.SubtitleLabel.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel.setSizePolicy(sizePolicy4)
        self.SubtitleLabel.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.SubtitleLabel)

        self.copy_timeline = PushButton(Form)
        self.copy_timeline.setObjectName(u"copy_timeline")
        sizePolicy3.setHeightForWidth(self.copy_timeline.sizePolicy().hasHeightForWidth())
        self.copy_timeline.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.copy_timeline)

        self.select_week_type = ComboBox(Form)
        self.select_week_type.setObjectName(u"select_week_type")
        sizePolicy3.setHeightForWidth(self.select_week_type.sizePolicy().hasHeightForWidth())
        self.select_week_type.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.select_week_type)

        self.select_timeline = ComboBox(Form)
        self.select_timeline.setObjectName(u"select_timeline")
        sizePolicy3.setHeightForWidth(self.select_timeline.sizePolicy().hasHeightForWidth())
        self.select_timeline.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.select_timeline)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tips_2 = CaptionLabel(Form)
        self.tips_2.setObjectName(u"tips_2")
        sizePolicy.setHeightForWidth(self.tips_2.sizePolicy().hasHeightForWidth())
        self.tips_2.setSizePolicy(sizePolicy)
        self.tips_2.setStyleSheet(u"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#7d000000}")
        self.tips_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.tips_2.setWordWrap(True)
        self.tips_2.setProperty("lightColor", QColor(0, 0, 0, 125))
        self.tips_2.setProperty("darkColor", QColor(255, 255, 255, 155))
        self.tips_2.setProperty("pixelFontSize", 14)

        self.verticalLayout_3.addWidget(self.tips_2)

        self.timeline_list = ListWidget(Form)
        self.timeline_list.setObjectName(u"timeline_list")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.timeline_list.sizePolicy().hasHeightForWidth())
        self.timeline_list.setSizePolicy(sizePolicy5)
        self.timeline_list.setMinimumSize(QSize(0, 0))
        self.timeline_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.timeline_list.setDefaultDropAction(Qt.MoveAction)
        self.timeline_list.setAlternatingRowColors(True)

        self.verticalLayout_3.addWidget(self.timeline_list)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.BodyLabel_2 = BodyLabel(Form)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy1.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy1)
        self.BodyLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BodyLabel_2.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.BodyLabel_2)

        self.class_activity = ComboBox(Form)
        self.class_activity.setObjectName(u"class_activity")
        sizePolicy2.setHeightForWidth(self.class_activity.sizePolicy().hasHeightForWidth())
        self.class_activity.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.class_activity)

        self.BodyLabel_3 = BodyLabel(Form)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy1.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy1)
        self.BodyLabel_3.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.BodyLabel_3)

        self.time_period = ComboBox(Form)
        self.time_period.setObjectName(u"time_period")
        sizePolicy2.setHeightForWidth(self.time_period.sizePolicy().hasHeightForWidth())
        self.time_period.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.time_period)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BodyLabel = BodyLabel(Form)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy1.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy1)
        self.BodyLabel.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.BodyLabel)

        self.spin_time = SpinBox(Form)
        self.spin_time.setObjectName(u"spin_time")
        sizePolicy2.setHeightForWidth(self.spin_time.sizePolicy().hasHeightForWidth())
        self.spin_time.setSizePolicy(sizePolicy2)
        self.spin_time.setMaximum(999)
        self.spin_time.setSingleStep(5)
        self.spin_time.setValue(40)

        self.horizontalLayout_3.addWidget(self.spin_time)

        self.add_button = ToolButton(Form)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout_3.addWidget(self.add_button)

        self.edit_button = ToolButton(Form)
        self.edit_button.setObjectName(u"edit_button")

        self.horizontalLayout_3.addWidget(self.edit_button)

        self.delete_button = ToolButton(Form)
        self.delete_button.setObjectName(u"delete_button")

        self.horizontalLayout_3.addWidget(self.delete_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.save = PrimaryPushButton(Form)
        self.save.setObjectName(u"save")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy6)
        self.save.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4\u7ebf\u7f16\u8f91", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u8282\u70b9", None))
        self.tips_1.setText(QCoreApplication.translate("Form", u"\u8fd8\u672a\u6dfb\u52a0\u4efb\u4f55\u8282\u70b9", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"\u8282\u70b9\u540d\u79f0", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u65f6\u95f4", None))
        self.part_time.setDisplayFormat(QCoreApplication.translate("Form", u"h:mm", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4\u7ebf", None))
        self.copy_timeline.setText(QCoreApplication.translate("Form", u"\u590d\u5236\u65f6\u95f4\u7ebf", None))
        self.tips_2.setText(QCoreApplication.translate("Form", u"\u8fd8\u672a\u6dfb\u52a0\u4efb\u4f55\u65f6\u95f4\u7ebf", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u6d3b\u52a8\u7c7b\u578b", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u65f6\u6bb5", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u65f6\u957f\uff08\u5206\u949f\uff09", None))
        self.save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi
