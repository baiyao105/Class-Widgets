# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advance.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CalendarPicker, CaptionLabel, CardWidget, ComboBox,
    HyperlinkLabel, LineEdit, PushButton, RadioButton,
    Slider, SmoothScrollArea, SpinBox, StrongBodyLabel,
    SubtitleLabel, SwitchButton, TitleLabel, ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(765, 2322)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 0)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.adv_scroll = SmoothScrollArea(Form)
        self.adv_scroll.setObjectName(u"adv_scroll")
        self.adv_scroll.setStyleSheet(u"background: transparent; border: none")
        self.adv_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 717, 2243))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.SubtitleLabel_3)

        self.CardWidget_8 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_8.setObjectName(u"CardWidget_8")
        self.CardWidget_8.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.StrongBodyLabel_8 = StrongBodyLabel(self.CardWidget_8)
        self.StrongBodyLabel_8.setObjectName(u"StrongBodyLabel_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_8.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_8.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_8.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.StrongBodyLabel_8)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_8)
        self.CaptionLabel_8.setObjectName(u"CaptionLabel_8")
        self.CaptionLabel_8.setWordWrap(True)
        self.CaptionLabel_8.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_8.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_13.addWidget(self.CaptionLabel_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_13)

        self.switch_enable_alt_schedule = SwitchButton(self.CardWidget_8)
        self.switch_enable_alt_schedule.setObjectName(u"switch_enable_alt_schedule")

        self.horizontalLayout_8.addWidget(self.switch_enable_alt_schedule)


        self.verticalLayout_5.addWidget(self.CardWidget_8)

        self.CardWidget_9 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_9.setObjectName(u"CardWidget_9")
        self.CardWidget_9.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_9 = QHBoxLayout(self.CardWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.CardWidget_9)
        self.StrongBodyLabel_9.setObjectName(u"StrongBodyLabel_9")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_9.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_9.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_9.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.StrongBodyLabel_9)

        self.CaptionLabel_7 = CaptionLabel(self.CardWidget_9)
        self.CaptionLabel_7.setObjectName(u"CaptionLabel_7")
        self.CaptionLabel_7.setWordWrap(True)
        self.CaptionLabel_7.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_7.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_12.addWidget(self.CaptionLabel_7)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)

        self.set_start_date = CalendarPicker(self.CardWidget_9)
        self.set_start_date.setObjectName(u"set_start_date")

        self.horizontalLayout_9.addWidget(self.set_start_date)


        self.verticalLayout_5.addWidget(self.CardWidget_9)


        self.verticalLayout_21.addLayout(self.verticalLayout_5)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(3)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.SubtitleLabel_5 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_5.setObjectName(u"SubtitleLabel_5")
        self.SubtitleLabel_5.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.SubtitleLabel_5)

        self.CardWidget_7 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_7.setObjectName(u"CardWidget_7")
        self.CardWidget_7.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.CardWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.StrongBodyLabel_7 = StrongBodyLabel(self.CardWidget_7)
        self.StrongBodyLabel_7.setObjectName(u"StrongBodyLabel_7")
        self.StrongBodyLabel_7.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.StrongBodyLabel_7)

        self.CaptionLabel_6 = CaptionLabel(self.CardWidget_7)
        self.CaptionLabel_6.setObjectName(u"CaptionLabel_6")
        self.CaptionLabel_6.setWordWrap(True)
        self.CaptionLabel_6.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_6.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_11.addWidget(self.CaptionLabel_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.offset_spin = SpinBox(self.CardWidget_7)
        self.offset_spin.setObjectName(u"offset_spin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.offset_spin.sizePolicy().hasHeightForWidth())
        self.offset_spin.setSizePolicy(sizePolicy2)
        self.offset_spin.setMinimum(-114514)
        self.offset_spin.setMaximum(114514)

        self.horizontalLayout_7.addWidget(self.offset_spin)


        self.verticalLayout_28.addWidget(self.CardWidget_7)

        self.CardWidget_18 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_18.setObjectName(u"CardWidget_18")
        self.CardWidget_18.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_19 = QHBoxLayout(self.CardWidget_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.StrongBodyLabel_20 = StrongBodyLabel(self.CardWidget_18)
        self.StrongBodyLabel_20.setObjectName(u"StrongBodyLabel_20")
        self.StrongBodyLabel_20.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.StrongBodyLabel_20)

        self.CaptionLabel_17 = CaptionLabel(self.CardWidget_18)
        self.CaptionLabel_17.setObjectName(u"CaptionLabel_17")
        self.CaptionLabel_17.setWordWrap(True)
        self.CaptionLabel_17.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_17.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_30.addWidget(self.CaptionLabel_17)


        self.horizontalLayout_19.addLayout(self.verticalLayout_30)

        self.conf_time_get = ComboBox(self.CardWidget_18)
        self.conf_time_get.setObjectName(u"conf_time_get")
        sizePolicy2.setHeightForWidth(self.conf_time_get.sizePolicy().hasHeightForWidth())
        self.conf_time_get.setSizePolicy(sizePolicy2)
        self.conf_time_get.setMinimumSize(QSize(151, 0))

        self.horizontalLayout_19.addWidget(self.conf_time_get)


        self.verticalLayout_28.addWidget(self.CardWidget_18)

        self.CardWidget_17 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_17.setObjectName(u"CardWidget_17")
        self.CardWidget_17.setMinimumSize(QSize(0, 70))
        self.verticalLayout_29 = QVBoxLayout(self.CardWidget_17)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(16, 16, 16, 16)
        self.CardWidget_19 = CardWidget(self.CardWidget_17)
        self.CardWidget_19.setObjectName(u"CardWidget_19")
        self.CardWidget_19.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_20 = QHBoxLayout(self.CardWidget_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.StrongBodyLabel_21 = StrongBodyLabel(self.CardWidget_19)
        self.StrongBodyLabel_21.setObjectName(u"StrongBodyLabel_21")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_21.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_21.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_21.setWordWrap(True)

        self.verticalLayout_31.addWidget(self.StrongBodyLabel_21)

        self.CaptionLabel_18 = CaptionLabel(self.CardWidget_19)
        self.CaptionLabel_18.setObjectName(u"CaptionLabel_18")
        self.CaptionLabel_18.setWordWrap(True)
        self.CaptionLabel_18.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_18.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_31.addWidget(self.CaptionLabel_18)


        self.horizontalLayout_20.addLayout(self.verticalLayout_31)

        self.ntp_refresh_button = ToolButton(self.CardWidget_19)
        self.ntp_refresh_button.setObjectName(u"ntp_refresh_button")

        self.horizontalLayout_20.addWidget(self.ntp_refresh_button)

        self.ntp_server_url = LineEdit(self.CardWidget_19)
        self.ntp_server_url.setObjectName(u"ntp_server_url")
        sizePolicy2.setHeightForWidth(self.ntp_server_url.sizePolicy().hasHeightForWidth())
        self.ntp_server_url.setSizePolicy(sizePolicy2)
        self.ntp_server_url.setMinimumSize(QSize(160, 33))

        self.horizontalLayout_20.addWidget(self.ntp_server_url)


        self.verticalLayout_29.addWidget(self.CardWidget_19)

        self.CardWidget_21 = CardWidget(self.CardWidget_17)
        self.CardWidget_21.setObjectName(u"CardWidget_21")
        self.CardWidget_21.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_22 = QHBoxLayout(self.CardWidget_21)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.StrongBodyLabel_23 = StrongBodyLabel(self.CardWidget_21)
        self.StrongBodyLabel_23.setObjectName(u"StrongBodyLabel_23")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_23.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_23.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_23.setWordWrap(True)

        self.verticalLayout_33.addWidget(self.StrongBodyLabel_23)

        self.CaptionLabel_21 = CaptionLabel(self.CardWidget_21)
        self.CaptionLabel_21.setObjectName(u"CaptionLabel_21")
        self.CaptionLabel_21.setWordWrap(True)
        self.CaptionLabel_21.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_21.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_33.addWidget(self.CaptionLabel_21)


        self.horizontalLayout_22.addLayout(self.verticalLayout_33)

        self.ntp_sync_timezone = ComboBox(self.CardWidget_21)
        self.ntp_sync_timezone.setObjectName(u"ntp_sync_timezone")
        self.ntp_sync_timezone.setMinimumSize(QSize(204, 0))

        self.horizontalLayout_22.addWidget(self.ntp_sync_timezone)


        self.verticalLayout_29.addWidget(self.CardWidget_21)

        self.CardWidget_20 = CardWidget(self.CardWidget_17)
        self.CardWidget_20.setObjectName(u"CardWidget_20")
        self.CardWidget_20.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_21 = QHBoxLayout(self.CardWidget_20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.StrongBodyLabel_22 = StrongBodyLabel(self.CardWidget_20)
        self.StrongBodyLabel_22.setObjectName(u"StrongBodyLabel_22")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_22.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_22.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_22.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.StrongBodyLabel_22)

        self.CaptionLabel_20 = CaptionLabel(self.CardWidget_20)
        self.CaptionLabel_20.setObjectName(u"CaptionLabel_20")
        self.CaptionLabel_20.setStyleSheet(u"")
        self.CaptionLabel_20.setWordWrap(True)
        self.CaptionLabel_20.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_20.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_32.addWidget(self.CaptionLabel_20)

        self.CaptionLabel_19 = CaptionLabel(self.CardWidget_20)
        self.CaptionLabel_19.setObjectName(u"CaptionLabel_19")
        self.CaptionLabel_19.setWordWrap(True)
        self.CaptionLabel_19.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_19.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_32.addWidget(self.CaptionLabel_19)


        self.horizontalLayout_21.addLayout(self.verticalLayout_32)

        self.ntp_refresh_picker = SpinBox(self.CardWidget_20)
        self.ntp_refresh_picker.setObjectName(u"ntp_refresh_picker")

        self.horizontalLayout_21.addWidget(self.ntp_refresh_picker)

        self.switch_enable_ntp_auto_sync = SwitchButton(self.CardWidget_20)
        self.switch_enable_ntp_auto_sync.setObjectName(u"switch_enable_ntp_auto_sync")

        self.horizontalLayout_21.addWidget(self.switch_enable_ntp_auto_sync)


        self.verticalLayout_29.addWidget(self.CardWidget_20)


        self.verticalLayout_28.addWidget(self.CardWidget_17)


        self.verticalLayout_21.addLayout(self.verticalLayout_28)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SubtitleLabel = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.StrongBodyLabel_201 = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel_201.setObjectName(u"StrongBodyLabel_201")
        self.StrongBodyLabel_201.setWordWrap(True)

        self.verticalLayout.addWidget(self.StrongBodyLabel_201)

        self.CaptionLabel_171 = CaptionLabel(self.scrollAreaWidgetContents)
        self.CaptionLabel_171.setObjectName(u"CaptionLabel_171")
        self.CaptionLabel_171.setWordWrap(True)
        self.CaptionLabel_171.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_171.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout.addWidget(self.CaptionLabel_171)

        self.CardWidget_191 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_191.setObjectName(u"CardWidget_191")
        self.CardWidget_191.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_211 = QHBoxLayout(self.CardWidget_191)
        self.horizontalLayout_211.setSpacing(16)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.horizontalLayout_211.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_301 = QVBoxLayout()
        self.verticalLayout_301.setSpacing(0)
        self.verticalLayout_301.setObjectName(u"verticalLayout_301")
        self.StrongBodyLabel_221 = StrongBodyLabel(self.CardWidget_191)
        self.StrongBodyLabel_221.setObjectName(u"StrongBodyLabel_221")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_221.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_221.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_221.setWordWrap(True)

        self.verticalLayout_301.addWidget(self.StrongBodyLabel_221)

        self.CaptionLabel_191 = CaptionLabel(self.CardWidget_191)
        self.CaptionLabel_191.setObjectName(u"CaptionLabel_191")
        self.CaptionLabel_191.setWordWrap(False)
        self.CaptionLabel_191.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_191.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_301.addWidget(self.CaptionLabel_191)


        self.horizontalLayout_211.addLayout(self.verticalLayout_301)

        self.language_combo_view = ComboBox(self.CardWidget_191)
        self.language_combo_view.setObjectName(u"language_combo_view")

        self.horizontalLayout_211.addWidget(self.language_combo_view)


        self.verticalLayout.addWidget(self.CardWidget_191)

        self.StrongBodyLabel_6 = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        self.StrongBodyLabel_6.setWordWrap(True)

        self.verticalLayout.addWidget(self.StrongBodyLabel_6)

        self.CaptionLabel_5 = CaptionLabel(self.scrollAreaWidgetContents)
        self.CaptionLabel_5.setObjectName(u"CaptionLabel_5")
        self.CaptionLabel_5.setWordWrap(True)
        self.CaptionLabel_5.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_5.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout.addWidget(self.CaptionLabel_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 6, -1, 12)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(200, 135))
        self.label.setMaximumSize(QSize(225, 135))
        self.label.setPixmap(QPixmap(u":/png/settings/default.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label)

        self.hide_method_default = RadioButton(self.scrollAreaWidgetContents)
        self.hide_method_default.setObjectName(u"hide_method_default")
        sizePolicy2.setHeightForWidth(self.hide_method_default.sizePolicy().hasHeightForWidth())
        self.hide_method_default.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.hide_method_default)


        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(200, 135))
        self.label_2.setMaximumSize(QSize(225, 135))
        self.label_2.setPixmap(QPixmap(u":/png/settings/hide_all.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_2)

        self.hide_method_all = RadioButton(self.scrollAreaWidgetContents)
        self.hide_method_all.setObjectName(u"hide_method_all")
        sizePolicy2.setHeightForWidth(self.hide_method_all.sizePolicy().hasHeightForWidth())
        self.hide_method_all.setSizePolicy(sizePolicy2)

        self.verticalLayout_20.addWidget(self.hide_method_all)


        self.horizontalLayout_12.addLayout(self.verticalLayout_20)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(200, 135))
        self.label_3.setMaximumSize(QSize(225, 135))
        self.label_3.setPixmap(QPixmap(u":/png/settings/floating.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_3)

        self.hide_method_floating = RadioButton(self.scrollAreaWidgetContents)
        self.hide_method_floating.setObjectName(u"hide_method_floating")
        sizePolicy2.setHeightForWidth(self.hide_method_floating.sizePolicy().hasHeightForWidth())
        self.hide_method_floating.setSizePolicy(sizePolicy2)

        self.verticalLayout_19.addWidget(self.hide_method_floating)


        self.horizontalLayout_12.addLayout(self.verticalLayout_19)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.StrongBodyLabel_13 = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel_13.setObjectName(u"StrongBodyLabel_13")
        self.StrongBodyLabel_13.setWordWrap(True)

        self.verticalLayout.addWidget(self.StrongBodyLabel_13)

        self.CardWidget_5 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_5.setObjectName(u"CardWidget_5")
        self.CardWidget_5.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_4 = QHBoxLayout(self.CardWidget_5)
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.StrongBodyLabel_4 = StrongBodyLabel(self.CardWidget_5)
        self.StrongBodyLabel_4.setObjectName(u"StrongBodyLabel_4")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_4.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_4.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_4.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.StrongBodyLabel_4)

        self.CaptionLabel_4 = CaptionLabel(self.CardWidget_5)
        self.CaptionLabel_4.setObjectName(u"CaptionLabel_4")
        self.CaptionLabel_4.setWordWrap(True)
        self.CaptionLabel_4.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_4.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_8.addWidget(self.CaptionLabel_4)

        self.what_is_hide_mode_3 = HyperlinkLabel(self.CardWidget_5)
        self.what_is_hide_mode_3.setObjectName(u"what_is_hide_mode_3")

        self.verticalLayout_8.addWidget(self.what_is_hide_mode_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.hide_mode_combo = ComboBox(self.CardWidget_5)
        self.hide_mode_combo.setObjectName(u"hide_mode_combo")

        self.horizontalLayout_4.addWidget(self.hide_mode_combo)


        self.verticalLayout.addWidget(self.CardWidget_5)

        self.CardWidget_14 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_14.setObjectName(u"CardWidget_14")
        self.CardWidget_14.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_15 = QHBoxLayout(self.CardWidget_14)
        self.horizontalLayout_15.setSpacing(16)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.StrongBodyLabel_16 = StrongBodyLabel(self.CardWidget_14)
        self.StrongBodyLabel_16.setObjectName(u"StrongBodyLabel_16")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_16.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_16.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_16.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.StrongBodyLabel_16)

        self.CaptionLabel_14 = CaptionLabel(self.CardWidget_14)
        self.CaptionLabel_14.setObjectName(u"CaptionLabel_14")
        self.CaptionLabel_14.setWordWrap(True)
        self.CaptionLabel_14.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_14.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_24.addWidget(self.CaptionLabel_14)


        self.horizontalLayout_15.addLayout(self.verticalLayout_24)

        self.switch_exclude_startup = SwitchButton(self.CardWidget_14)
        self.switch_exclude_startup.setObjectName(u"switch_exclude_startup")

        self.horizontalLayout_15.addWidget(self.switch_exclude_startup)


        self.verticalLayout.addWidget(self.CardWidget_14)

        self.CardWidget_15 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_15.setObjectName(u"CardWidget_15")
        self.CardWidget_15.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_16 = QHBoxLayout(self.CardWidget_15)
        self.horizontalLayout_16.setSpacing(16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.StrongBodyLabel_17 = StrongBodyLabel(self.CardWidget_15)
        self.StrongBodyLabel_17.setObjectName(u"StrongBodyLabel_17")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_17.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_17.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_17.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.StrongBodyLabel_17)

        self.CaptionLabel_141 = CaptionLabel(self.CardWidget_15)
        self.CaptionLabel_141.setObjectName(u"CaptionLabel_141")
        self.CaptionLabel_141.setWordWrap(True)
        self.CaptionLabel_141.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_141.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_25.addWidget(self.CaptionLabel_141)


        self.horizontalLayout_16.addLayout(self.verticalLayout_25)

        self.excluded_lessons = LineEdit(self.CardWidget_15)
        self.excluded_lessons.setObjectName(u"excluded_lessons")
        sizePolicy2.setHeightForWidth(self.excluded_lessons.sizePolicy().hasHeightForWidth())
        self.excluded_lessons.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.excluded_lessons)


        self.verticalLayout.addWidget(self.CardWidget_15)

        self.CardWidget_13 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_13.setObjectName(u"CardWidget_13")
        self.CardWidget_13.setMinimumSize(QSize(0, 70))
        self.verticalLayout_23 = QVBoxLayout(self.CardWidget_13)
        self.verticalLayout_23.setSpacing(16)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(16, 16, 16, 16)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.StrongBodyLabel_18 = StrongBodyLabel(self.CardWidget_13)
        self.StrongBodyLabel_18.setObjectName(u"StrongBodyLabel_18")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_18.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_18.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_18.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.StrongBodyLabel_18)

        self.CaptionLabel_15 = CaptionLabel(self.CardWidget_13)
        self.CaptionLabel_15.setObjectName(u"CaptionLabel_15")
        self.CaptionLabel_15.setWordWrap(True)
        self.CaptionLabel_15.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_15.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_22.addWidget(self.CaptionLabel_15)


        self.horizontalLayout_18.addLayout(self.verticalLayout_22)

        self.switch_enable_click = SwitchButton(self.CardWidget_13)
        self.switch_enable_click.setObjectName(u"switch_enable_click")

        self.horizontalLayout_18.addWidget(self.switch_enable_click)


        self.verticalLayout_23.addLayout(self.horizontalLayout_18)


        self.verticalLayout.addWidget(self.CardWidget_13)

        self.CardWidget_16 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_16.setObjectName(u"CardWidget_16")
        self.CardWidget_16.setMinimumSize(QSize(0, 70))
        self.verticalLayout_26 = QVBoxLayout(self.CardWidget_16)
        self.verticalLayout_26.setSpacing(16)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(16, 16, 16, 16)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.StrongBodyLabel_15 = StrongBodyLabel(self.CardWidget_16)
        self.StrongBodyLabel_15.setObjectName(u"StrongBodyLabel_15")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_15.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_15.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_15.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.StrongBodyLabel_15)

        self.CaptionLabel_13 = CaptionLabel(self.CardWidget_16)
        self.CaptionLabel_13.setObjectName(u"CaptionLabel_13")
        self.CaptionLabel_13.setWordWrap(True)
        self.CaptionLabel_13.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_13.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_9.addWidget(self.CaptionLabel_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_9)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.slider_scale_factor = Slider(self.CardWidget_16)
        self.slider_scale_factor.setObjectName(u"slider_scale_factor")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.slider_scale_factor.sizePolicy().hasHeightForWidth())
        self.slider_scale_factor.setSizePolicy(sizePolicy4)
        self.slider_scale_factor.setMinimum(100)
        self.slider_scale_factor.setMaximum(200)
        self.slider_scale_factor.setValue(100)
        self.slider_scale_factor.setOrientation(Qt.Horizontal)

        self.verticalLayout_27.addWidget(self.slider_scale_factor)

        self.text_scale_factor = LineEdit(self.CardWidget_16)
        self.text_scale_factor.setObjectName(u"text_scale_factor")
        sizePolicy4.setHeightForWidth(self.text_scale_factor.sizePolicy().hasHeightForWidth())
        self.text_scale_factor.setSizePolicy(sizePolicy4)
        self.text_scale_factor.setReadOnly(True)

        self.verticalLayout_27.addWidget(self.text_scale_factor)


        self.horizontalLayout_14.addLayout(self.verticalLayout_27)


        self.verticalLayout_26.addLayout(self.horizontalLayout_14)


        self.verticalLayout.addWidget(self.CardWidget_16)

        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setMinimumSize(QSize(0, 70))
        self.horizontalLayout = QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        self.StrongBodyLabel_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.StrongBodyLabel_2)

        self.CaptionLabel_3 = CaptionLabel(self.CardWidget)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        sizePolicy1.setHeightForWidth(self.CaptionLabel_3.sizePolicy().hasHeightForWidth())
        self.CaptionLabel_3.setSizePolicy(sizePolicy1)
        self.CaptionLabel_3.setWordWrap(True)
        self.CaptionLabel_3.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_3.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_4.addWidget(self.CaptionLabel_3)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.window_status_combo = ComboBox(self.CardWidget)
        self.window_status_combo.setObjectName(u"window_status_combo")

        self.horizontalLayout.addWidget(self.window_status_combo)


        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.StrongBodyLabel)

        self.CaptionLabel = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setWordWrap(True)
        self.CaptionLabel.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_3.addWidget(self.CaptionLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.margin_spin = SpinBox(self.CardWidget_2)
        self.margin_spin.setObjectName(u"margin_spin")
        sizePolicy2.setHeightForWidth(self.margin_spin.sizePolicy().hasHeightForWidth())
        self.margin_spin.setSizePolicy(sizePolicy2)
        self.margin_spin.setMinimumSize(QSize(130, 33))
        self.margin_spin.setMinimum(-15)

        self.horizontalLayout_2.addWidget(self.margin_spin)


        self.verticalLayout.addWidget(self.CardWidget_2)


        self.verticalLayout_21.addLayout(self.verticalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.SubtitleLabel_2 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.SubtitleLabel_2)

        self.CardWidget_4 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.CardWidget_4.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.StrongBodyLabel_3 = StrongBodyLabel(self.CardWidget_4)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_3.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_3.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_3.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.StrongBodyLabel_3)

        self.switch_startup = SwitchButton(self.CardWidget_4)
        self.switch_startup.setObjectName(u"switch_startup")

        self.horizontalLayout_3.addWidget(self.switch_startup)


        self.verticalLayout_7.addWidget(self.CardWidget_4)


        self.verticalLayout_21.addLayout(self.verticalLayout_7)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.SubtitleLabel_4 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")
        self.SubtitleLabel_4.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.SubtitleLabel_4)

        self.CardWidget_12 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_12.setObjectName(u"CardWidget_12")
        self.CardWidget_12.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_13 = QHBoxLayout(self.CardWidget_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.StrongBodyLabel_14 = StrongBodyLabel(self.CardWidget_12)
        self.StrongBodyLabel_14.setObjectName(u"StrongBodyLabel_14")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_14.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_14.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_14.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.StrongBodyLabel_14)

        self.CaptionLabel_12 = CaptionLabel(self.CardWidget_12)
        self.CaptionLabel_12.setObjectName(u"CaptionLabel_12")
        self.CaptionLabel_12.setWordWrap(True)
        self.CaptionLabel_12.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_12.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_18.addWidget(self.CaptionLabel_12)


        self.horizontalLayout_13.addLayout(self.verticalLayout_18)

        self.switch_safe_mode = SwitchButton(self.CardWidget_12)
        self.switch_safe_mode.setObjectName(u"switch_safe_mode")

        self.horizontalLayout_13.addWidget(self.switch_safe_mode)


        self.verticalLayout_14.addWidget(self.CardWidget_12)

        self.CardWidget_6 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_6.setObjectName(u"CardWidget_6")
        self.CardWidget_6.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.StrongBodyLabel_11 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_11.setObjectName(u"StrongBodyLabel_11")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_11.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_11.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_11.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.StrongBodyLabel_11)

        self.CaptionLabel_10 = CaptionLabel(self.CardWidget_6)
        self.CaptionLabel_10.setObjectName(u"CaptionLabel_10")
        self.CaptionLabel_10.setWordWrap(True)
        self.CaptionLabel_10.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_10.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_16.addWidget(self.CaptionLabel_10)


        self.horizontalLayout_6.addLayout(self.verticalLayout_16)

        self.switch_disable_log = SwitchButton(self.CardWidget_6)
        self.switch_disable_log.setObjectName(u"switch_disable_log")

        self.horizontalLayout_6.addWidget(self.switch_disable_log)


        self.verticalLayout_14.addWidget(self.CardWidget_6)

        self.CardWidget_11 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_11.setObjectName(u"CardWidget_11")
        self.CardWidget_11.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_11 = QHBoxLayout(self.CardWidget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.StrongBodyLabel_12 = StrongBodyLabel(self.CardWidget_11)
        self.StrongBodyLabel_12.setObjectName(u"StrongBodyLabel_12")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_12.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_12.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_12.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.StrongBodyLabel_12)

        self.CaptionLabel_11 = CaptionLabel(self.CardWidget_11)
        self.CaptionLabel_11.setObjectName(u"CaptionLabel_11")
        self.CaptionLabel_11.setWordWrap(True)
        self.CaptionLabel_11.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_11.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_17.addWidget(self.CaptionLabel_11)


        self.horizontalLayout_11.addLayout(self.verticalLayout_17)

        self.button_clear_log = PushButton(self.CardWidget_11)
        self.button_clear_log.setObjectName(u"button_clear_log")

        self.horizontalLayout_11.addWidget(self.button_clear_log)


        self.verticalLayout_14.addWidget(self.CardWidget_11)

        self.CardWidget_10 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_10.setObjectName(u"CardWidget_10")
        self.CardWidget_10.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_10 = QHBoxLayout(self.CardWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.StrongBodyLabel_10 = StrongBodyLabel(self.CardWidget_10)
        self.StrongBodyLabel_10.setObjectName(u"StrongBodyLabel_10")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_10.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_10.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_10.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.StrongBodyLabel_10)

        self.CaptionLabel_9 = CaptionLabel(self.CardWidget_10)
        self.CaptionLabel_9.setObjectName(u"CaptionLabel_9")
        self.CaptionLabel_9.setWordWrap(True)
        self.CaptionLabel_9.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_9.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_15.addWidget(self.CaptionLabel_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_15)

        self.switch_multiple_programs = SwitchButton(self.CardWidget_10)
        self.switch_multiple_programs.setObjectName(u"switch_multiple_programs")

        self.horizontalLayout_10.addWidget(self.switch_multiple_programs)


        self.verticalLayout_14.addWidget(self.CardWidget_10)


        self.verticalLayout_21.addLayout(self.verticalLayout_14)

        self.blank = QFrame(self.scrollAreaWidgetContents)
        self.blank.setObjectName(u"blank")
        self.blank.setMinimumSize(QSize(0, 25))
        self.blank.setFrameShape(QFrame.StyledPanel)
        self.blank.setFrameShadow(QFrame.Raised)
        self.blank.setLineWidth(5)

        self.verticalLayout_21.addWidget(self.blank)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer)

        self.adv_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.adv_scroll)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u9ad8\u7ea7\u9009\u9879", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b", None))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("Form", u"\u542f\u7528 \u5355/\u53cc \u5468\u8bfe\u8868", None))
        self.CaptionLabel_8.setText(QCoreApplication.translate("Form", u"\u82e5\u8981\u542f\u7528\u6b64\u9009\u9879\uff0c\u9700\u8bbe\u5b9a\u5f00\u5b66\u65e5\u671f\u4ee5\u8ba1\u7b97", None))
        self.switch_enable_alt_schedule.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_alt_schedule.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate("Form", u"\u9009\u53d6\u5f00\u5b66\u65e5\u671f", None))
        self.CaptionLabel_7.setText(QCoreApplication.translate("Form", u"\u5c06\u7528\u4e8e\u8ba1\u7b97\u5355/\u53cc\u5468\uff0c\u5f00\u5b66\u65e5\u671f\u9700\u8bbe\u7f6e\u4e3a\u5f00\u5b66\u7b2c\u4e00\u5468\u7b2c\u4e00\u5929\uff08\u5373\u5468\u4e00\uff09", None))
        self.set_start_date.setText(QCoreApplication.translate("Form", u"\u9009\u53d6\u5f00\u5b66\u65e5\u671f", None))
        self.SubtitleLabel_5.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("Form", u"\u65f6\u5dee\u504f\u79fb", None))
        self.CaptionLabel_6.setText(QCoreApplication.translate("Form", u"\u4fee\u6b63\u7cfb\u7edf\u65f6\u95f4\u4e0e\u5b66\u6821\u94c3\u58f0\u7684\u65f6\u5dee\uff0c\u5b66\u6821\u94c3\u58f0\u6162\u4e8e\u7cfb\u7edf\u65f6\u95f4\u4e3a\u6b63\u503c\uff0c\u53cd\u4e4b\u4e3a\u8d1f", None))
        self.StrongBodyLabel_20.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4\u83b7\u5f97\u65b9\u6cd5", None))
        self.CaptionLabel_17.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u65f6\u95f4\u83b7\u5f97\u65b9\u6cd5", None))
        self.conf_time_get.setText("")
        self.StrongBodyLabel_21.setText(QCoreApplication.translate("Form", u"NTP\u670d\u52a1\u5668", None))
        self.CaptionLabel_18.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528url\u94fe\u63a5NTP\u670d\u52a1\u5668\u540c\u6b65\u65f6\u95f4", None))
        self.StrongBodyLabel_23.setText(QCoreApplication.translate("Form", u"NTP\u540c\u6b65\u4f7f\u7528\u7684\u65f6\u533a", None))
        self.CaptionLabel_21.setText(QCoreApplication.translate("Form", u"NTP\u540c\u6b65\u65f6\u5e94\u4f7f\u7528\u7684\u65f6\u533a", None))
        self.StrongBodyLabel_22.setText(QCoreApplication.translate("Form", u"NTP\u81ea\u52a8\u6821\u51c6", None))
        self.CaptionLabel_20.setText(QCoreApplication.translate("Form", u"\u4e0a\u6b21\u6821\u51c6: 1145\u5e741\u67081\u65e5 - 11:45:14", None))
        self.CaptionLabel_19.setText(QCoreApplication.translate("Form", u"\u6309\u7167\u8bbe\u5b9a\u7684\u6821\u51c6\u5206\u949f\u6570\u81ea\u52a8\u6267\u884c\u6821\u51c6", None))
        self.switch_enable_ntp_auto_sync.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_ntp_auto_sync.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u5916\u89c2", None))
        self.StrongBodyLabel_201.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6587\u5b57", None))
        self.CaptionLabel_171.setText(QCoreApplication.translate("Form", u"\u5728\u6b64\u5904\u60a8\u53ef\u4ee5\u4fee\u6539\u754c\u9762\u6240\u663e\u793a\u7684\u8bed\u8a00", None))
        self.StrongBodyLabel_221.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u8bed\u8a00", None))
        self.CaptionLabel_191.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u4f60\u6240\u9700\u8981\u754c\u9762\u663e\u793a\u7684\u8bed\u8a00", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"\u9690\u85cf\u65b9\u5f0f", None))
        self.CaptionLabel_5.setText(QCoreApplication.translate("Form", u"\u9690\u85cf\u65b9\u5f0f\u5c06\u4f1a\u4fee\u6539\u5355\u51fb\u9690\u85cf\u548c\u81ea\u52a8\u9690\u85cf\u7684\u884c\u4e3a\uff0c\u53ef\u6309\u9700\u66f4\u6539\uff08\u91cd\u542f\u540e\u751f\u6548\uff09", None))
        self.hide_method_default.setText(QCoreApplication.translate("Form", u"\u9ed8\u8ba4", None))
        self.hide_method_all.setText(QCoreApplication.translate("Form", u"\u5168\u90e8\u9690\u85cf", None))
        self.hide_method_floating.setText(QCoreApplication.translate("Form", u"\u6700\u5c0f\u5316\u4e3a\u6d6e\u7a97\uff08\u63a8\u8350\uff09", None))
        self.StrongBodyLabel_13.setText(QCoreApplication.translate("Form", u"\u5176\u4ed6", None))
        self.StrongBodyLabel_4.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u9690\u85cf", None))
        self.CaptionLabel_4.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u4f60\u9700\u8981\u7684\u81ea\u52a8\u9690\u85cf\u65b9\u5f0f", None))
        self.what_is_hide_mode_3.setText(QCoreApplication.translate("Form", u"\u4ec0\u4e48\u662f\u7075\u6d3b\u9690\u85cf\uff1f", None))
        self.StrongBodyLabel_16.setText(QCoreApplication.translate("Form", u"\u7279\u5b9a\u8bfe\u7a0b\u4e0d\u81ea\u52a8\u9690\u85cf", None))
        self.CaptionLabel_14.setText(QCoreApplication.translate("Form", u"\u82e5\u542f\u7528\uff0c\u5728\u9047\u5230\u4e0b\u65b9\u8bbe\u7f6e\u7684\u7279\u5b9a\u8bfe\u7a0b\u65f6\u4e0d\u4f1a\u81ea\u52a8\u9690\u85cf\uff0c\u4ee5\u82f1\u6587\u9017\u53f7\u5206\u9694", None))
        self.switch_exclude_startup.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_exclude_startup.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_17.setText(QCoreApplication.translate("Form", u"\u4e0d\u81ea\u52a8\u9690\u85cf\u7684\u8bfe\u7a0b", None))
        self.CaptionLabel_141.setText(QCoreApplication.translate("Form", u"\u914d\u5408 \u7279\u5b9a\u8bfe\u7a0b\u4e0d\u81ea\u52a8\u9690\u85cf \u4f7f\u7528", None))
        self.StrongBodyLabel_18.setText(QCoreApplication.translate("Form", u"\u5141\u8bb8\u70b9\u51fb\u6216\u89e6\u6478\u5c0f\u7ec4\u4ef6", None))
        self.CaptionLabel_15.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u540e\uff1a\u8f7b\u70b9\u5c0f\u7ec4\u4ef6\u5373\u53ef\u5207\u6362\u663e\u793a/\u9690\u85cf, \u53f3\u952e\u4f1a\u5f39\u51fa\u66f4\u591a\u9009\u9879\u54df\n"
"\u7981\u7528\u65f6\uff1a\u70b9\u51fb\u5c0f\u7ec4\u4ef6\u4f1a\u50cf\u4e0d\u5b58\u5728\u4e00\u6837, \u76f4\u63a5\u7a7f\u900f\u5230\u540e\u9762\u7684\u7a97\u53e3", None))
        self.switch_enable_click.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_click.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_15.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u7f29\u653e", None))
        self.CaptionLabel_13.setText(QCoreApplication.translate("Form", u"\u66f4\u6539\u81ea\u5b9a\u4e49\u7f29\u653e\u7cfb\u6570\u767e\u5206\u6bd4\uff08\u91cd\u542f\u540e\u751f\u6548\uff09\n"
"*\u4e0d\u5efa\u8bae\u4f7f\u7528 180% \u4ee5\u4e0a\u7684\u503c\uff0c\u8fd9\u53ef\u80fd\u4f1a\u5bfc\u81f4\u663e\u793a\u5f02\u5e38", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"\u7f6e\u9876/\u7f6e\u5e95\u5c0f\u7ec4\u4ef6", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"\u66f4\u6539\u5c0f\u7ec4\u4ef6\u7684\u7a97\u53e3\u72b6\u6001\uff08\u91cd\u542f\u540e\u751f\u6548\uff09\n"
"*\u5f00\u542f\u201c\u7f6e\u5e95\u201d\u529f\u80fd\u65f6\uff0c\u5c06\u4f1a\u7981\u7528\u201c\u5355\u51fb\u9690\u85cf\u5c0f\u7ec4\u4ef6\u201d", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u5927\u5c0f", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u684c\u9762\u7ec4\u4ef6\u79bb\u5c4f\u5e55\u8fb9\u7f18\u7684\u5927\u5c0f\uff08\u5355\u4f4d\uff1apx\uff09", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u542f\u52a8", None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("Form", u"\u5f00\u673a\u81ea\u542f\u52a8", None))
        self.switch_startup.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_startup.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Form", u"\u5176\u4ed6", None))
        self.StrongBodyLabel_14.setText(QCoreApplication.translate("Form", u"\u5b89\u5168\u6a21\u5f0f", None))
        self.CaptionLabel_12.setText(QCoreApplication.translate("Form", u"\u82e5\u542f\u7528\uff0cClass Widgets \u5c06\u5728\u7a0b\u5e8f\u5d29\u6e83\u65f6\u81ea\u52a8\u5ffd\u7565\uff0c\u5e76\u4e0d\u518d\u5f39\u51fa\u7a97\u53e3\uff1b\u4ee5\u514d\u5f71\u54cd\u6559\u5b66\u4efb\u52a1\u3002", None))
        self.switch_safe_mode.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_safe_mode.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_11.setText(QCoreApplication.translate("Form", u"\u7981\u7528\u65e5\u5fd7", None))
        self.CaptionLabel_10.setText(QCoreApplication.translate("Form", u"\u82e5\u542f\u7528\uff0c\u5e94\u7528\u5c06\u4e0d\u518d\u4f1a\u4fdd\u5b58\u65e5\u5fd7\u5230\u672c\u5730", None))
        self.switch_disable_log.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_disable_log.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_12.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.CaptionLabel_11.setText(QCoreApplication.translate("Form", u"\u5c06\u4f1a\u6e05\u7a7a \u8f6f\u4ef6\u6839\u76ee\u5f55\u4e0blog. \u7684\u6240\u6709\u5185\u5bb9", None))
        self.button_clear_log.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.StrongBodyLabel_10.setText(QCoreApplication.translate("Form", u"\u5141\u8bb8\u7a0b\u5e8f\u591a\u5f00", None))
        self.CaptionLabel_9.setText(QCoreApplication.translate("Form", u"\u7a0b\u5e8f\u591a\u5f00\u540e\u53ef\u80fd\u51fa\u73b0\u672a\u77e5\u7684\u95ee\u9898\uff0c\u8bf7\u8c28\u614e\u4f7f\u7528", None))
        self.switch_multiple_programs.setText(QCoreApplication.translate("Form", u"\u4e0d\u5141\u8bb8", None))
        self.switch_multiple_programs.setOnText(QCoreApplication.translate("Form", u"\u5141\u8bb8", None))
        self.switch_multiple_programs.setOffText(QCoreApplication.translate("Form", u"\u4e0d\u5141\u8bb8", None))
    # retranslateUi
