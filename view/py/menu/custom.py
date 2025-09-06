# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom.ui'
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
    QLayout, QListView, QListWidgetItem, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, CardWidget, ComboBox,
    HyperlinkLabel, ListWidget, PrimaryPushButton, PushButton,
    Slider, SmoothScrollArea, StrongBodyLabel, SubtitleLabel,
    SwitchButton, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(706, 1134)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 12)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.widgets_preview = QHBoxLayout()
        self.widgets_preview.setSpacing(0)
        self.widgets_preview.setObjectName(u"widgets_preview")
        self.widgets_preview.setSizeConstraint(QLayout.SetFixedSize)

        self.verticalLayout_2.addLayout(self.widgets_preview)

        self.ct_scroll = SmoothScrollArea(Form)
        self.ct_scroll.setObjectName(u"ct_scroll")
        self.ct_scroll.setStyleSheet(u"background: transparent; border: none")
        self.ct_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 658, 1007))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.CaptionLabel_3 = CaptionLabel(self.scrollAreaWidgetContents)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setAlignment(Qt.AlignCenter)
        self.CaptionLabel_3.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.CaptionLabel_3)

        self.widgets_list = ListWidget(self.scrollAreaWidgetContents)
        self.widgets_list.setObjectName(u"widgets_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widgets_list.sizePolicy().hasHeightForWidth())
        self.widgets_list.setSizePolicy(sizePolicy1)
        self.widgets_list.setMinimumSize(QSize(0, 0))
        self.widgets_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.widgets_list.setDragDropMode(QAbstractItemView.DragDrop)
        self.widgets_list.setDefaultDropAction(Qt.MoveAction)
        self.widgets_list.setFlow(QListView.LeftToRight)
        self.widgets_list.setProperty("isWrapping", True)
        self.widgets_list.setResizeMode(QListView.Adjust)
        self.widgets_list.setLayoutMode(QListView.Batched)

        self.verticalLayout_9.addWidget(self.widgets_list)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BodyLabel = BodyLabel(self.scrollAreaWidgetContents)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy2)
        self.BodyLabel.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.BodyLabel)

        self.widgets_combo = ComboBox(self.scrollAreaWidgetContents)
        self.widgets_combo.setObjectName(u"widgets_combo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widgets_combo.sizePolicy().hasHeightForWidth())
        self.widgets_combo.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.widgets_combo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.add_widget = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.add_widget.setObjectName(u"add_widget")

        self.horizontalLayout_3.addWidget(self.add_widget)

        self.remove_widget = PushButton(self.scrollAreaWidgetContents)
        self.remove_widget.setObjectName(u"remove_widget")

        self.horizontalLayout_3.addWidget(self.remove_widget)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.SubtitleLabel = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.SubtitleLabel)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SubtitleLabel_2 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setProperty("pixelFontSize", 18)
        self.SubtitleLabel_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.SubtitleLabel_2)

        self.open_theme_folder = HyperlinkLabel(self.scrollAreaWidgetContents)
        self.open_theme_folder.setObjectName(u"open_theme_folder")

        self.verticalLayout_3.addWidget(self.open_theme_folder)

        self.CardWidget_4 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.CardWidget_4.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_4 = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.StrongBodyLabel_3 = StrongBodyLabel(self.CardWidget_4)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")
        self.StrongBodyLabel_3.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.StrongBodyLabel_3)

        self.CaptionLabel_5 = CaptionLabel(self.CardWidget_4)
        self.CaptionLabel_5.setObjectName(u"CaptionLabel_5")
        self.CaptionLabel_5.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_5.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_5.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.CaptionLabel_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.combo_theme_select = ComboBox(self.CardWidget_4)
        self.combo_theme_select.setObjectName(u"combo_theme_select")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.combo_theme_select.sizePolicy().hasHeightForWidth())
        self.combo_theme_select.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.combo_theme_select)


        self.verticalLayout_3.addWidget(self.CardWidget_4)

        self.CardWidget_9 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_9.setObjectName(u"CardWidget_9")
        self.CardWidget_9.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_11 = QHBoxLayout(self.CardWidget_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.CardWidget_9)
        self.StrongBodyLabel_9.setObjectName(u"StrongBodyLabel_9")
        self.StrongBodyLabel_9.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.StrongBodyLabel_9)

        self.CaptionLabel_10 = CaptionLabel(self.CardWidget_9)
        self.CaptionLabel_10.setObjectName(u"CaptionLabel_10")
        self.CaptionLabel_10.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_10.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_10.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.CaptionLabel_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_15)

        self.combo_color_mode = ComboBox(self.CardWidget_9)
        self.combo_color_mode.setObjectName(u"combo_color_mode")
        sizePolicy4.setHeightForWidth(self.combo_color_mode.sizePolicy().hasHeightForWidth())
        self.combo_color_mode.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.combo_color_mode)


        self.verticalLayout_3.addWidget(self.CardWidget_9)

        self.CardWidget_10 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_10.setObjectName(u"CardWidget_10")
        self.CardWidget_10.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_12 = QHBoxLayout(self.CardWidget_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.StrongBodyLabel_11 = StrongBodyLabel(self.CardWidget_10)
        self.StrongBodyLabel_11.setObjectName(u"StrongBodyLabel_11")
        self.StrongBodyLabel_11.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.StrongBodyLabel_11)

        self.CaptionLabel_11 = CaptionLabel(self.CardWidget_10)
        self.CaptionLabel_11.setObjectName(u"CaptionLabel_11")
        self.CaptionLabel_11.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_11.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_11.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.CaptionLabel_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_16)

        self.slider_opacity = Slider(self.CardWidget_10)
        self.slider_opacity.setObjectName(u"slider_opacity")
        sizePolicy3.setHeightForWidth(self.slider_opacity.sizePolicy().hasHeightForWidth())
        self.slider_opacity.setSizePolicy(sizePolicy3)
        self.slider_opacity.setMinimumSize(QSize(100, 0))
        self.slider_opacity.setMaximumSize(QSize(200, 16777215))
        self.slider_opacity.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.slider_opacity)


        self.verticalLayout_3.addWidget(self.CardWidget_10)

        self.CardWidget_5 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_5.setObjectName(u"CardWidget_5")
        self.CardWidget_5.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.StrongBodyLabel_7 = StrongBodyLabel(self.CardWidget_5)
        self.StrongBodyLabel_7.setObjectName(u"StrongBodyLabel_7")
        self.StrongBodyLabel_7.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.StrongBodyLabel_7)

        self.CaptionLabel_7 = CaptionLabel(self.CardWidget_5)
        self.CaptionLabel_7.setObjectName(u"CaptionLabel_7")
        self.CaptionLabel_7.setWordWrap(True)
        self.CaptionLabel_7.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_7.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_10.addWidget(self.CaptionLabel_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.set_ac_color = PushButton(self.CardWidget_5)
        self.set_ac_color.setObjectName(u"set_ac_color")
        sizePolicy4.setHeightForWidth(self.set_ac_color.sizePolicy().hasHeightForWidth())
        self.set_ac_color.setSizePolicy(sizePolicy4)

        self.horizontalLayout_8.addWidget(self.set_ac_color)


        self.verticalLayout_3.addWidget(self.CardWidget_5)

        self.CardWidget_7 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_7.setObjectName(u"CardWidget_7")
        self.CardWidget_7.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.CardWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.StrongBodyLabel_4 = StrongBodyLabel(self.CardWidget_7)
        self.StrongBodyLabel_4.setObjectName(u"StrongBodyLabel_4")
        self.StrongBodyLabel_4.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.StrongBodyLabel_4)

        self.CaptionLabel_6 = CaptionLabel(self.CardWidget_7)
        self.CaptionLabel_6.setObjectName(u"CaptionLabel_6")
        self.CaptionLabel_6.setWordWrap(True)
        self.CaptionLabel_6.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_6.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_8.addWidget(self.CaptionLabel_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.set_fc_color = PushButton(self.CardWidget_7)
        self.set_fc_color.setObjectName(u"set_fc_color")
        sizePolicy4.setHeightForWidth(self.set_fc_color.sizePolicy().hasHeightForWidth())
        self.set_fc_color.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.set_fc_color)


        self.verticalLayout_3.addWidget(self.CardWidget_7)

        self.CardWidget_13 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_13.setObjectName(u"CardWidget_13")
        self.CardWidget_13.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_15 = QHBoxLayout(self.CardWidget_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.StrongBodyLabel_13 = StrongBodyLabel(self.CardWidget_13)
        self.StrongBodyLabel_13.setObjectName(u"StrongBodyLabel_13")
        self.StrongBodyLabel_13.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.StrongBodyLabel_13)

        self.CaptionLabel_14 = CaptionLabel(self.CardWidget_13)
        self.CaptionLabel_14.setObjectName(u"CaptionLabel_14")
        self.CaptionLabel_14.setWordWrap(True)
        self.CaptionLabel_14.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_14.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_19.addWidget(self.CaptionLabel_14)


        self.horizontalLayout_15.addLayout(self.verticalLayout_19)

        self.set_fc_color_2 = PushButton(self.CardWidget_13)
        self.set_fc_color_2.setObjectName(u"set_fc_color_2")
        sizePolicy4.setHeightForWidth(self.set_fc_color_2.sizePolicy().hasHeightForWidth())
        self.set_fc_color_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_15.addWidget(self.set_fc_color_2)


        self.verticalLayout_3.addWidget(self.CardWidget_13)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.SubtitleLabel_4 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")
        self.SubtitleLabel_4.setProperty("pixelFontSize", 18)
        self.SubtitleLabel_4.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.SubtitleLabel_4)

        self.CardWidget_2 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        self.StrongBodyLabel_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.StrongBodyLabel_2)

        self.CaptionLabel_4 = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel_4.setObjectName(u"CaptionLabel_4")
        self.CaptionLabel_4.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_4.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_4.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.CaptionLabel_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.switch_blur_countdown = SwitchButton(self.CardWidget_2)
        self.switch_blur_countdown.setObjectName(u"switch_blur_countdown")
        sizePolicy2.setHeightForWidth(self.switch_blur_countdown.sizePolicy().hasHeightForWidth())
        self.switch_blur_countdown.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.switch_blur_countdown)


        self.verticalLayout_11.addWidget(self.CardWidget_2)

        self.CardWidget_6 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_6.setObjectName(u"CardWidget_6")
        self.CardWidget_6.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_9 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        self.StrongBodyLabel_6.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.StrongBodyLabel_6)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_6)
        self.CaptionLabel_8.setObjectName(u"CaptionLabel_8")
        self.CaptionLabel_8.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_8.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_8.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.CaptionLabel_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)

        self.switch_blur_countdown_2 = SwitchButton(self.CardWidget_6)
        self.switch_blur_countdown_2.setObjectName(u"switch_blur_countdown_2")
        sizePolicy2.setHeightForWidth(self.switch_blur_countdown_2.sizePolicy().hasHeightForWidth())
        self.switch_blur_countdown_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.switch_blur_countdown_2)


        self.verticalLayout_11.addWidget(self.CardWidget_6)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.SubtitleLabel_6 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_6.setObjectName(u"SubtitleLabel_6")
        self.SubtitleLabel_6.setProperty("pixelFontSize", 18)
        self.SubtitleLabel_6.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.SubtitleLabel_6)

        self.CardWidget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.CardWidget_3.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_13 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.StrongBodyLabel_5 = StrongBodyLabel(self.CardWidget_3)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")
        self.StrongBodyLabel_5.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.StrongBodyLabel_5)

        self.CaptionLabel_12 = CaptionLabel(self.CardWidget_3)
        self.CaptionLabel_12.setObjectName(u"CaptionLabel_12")
        self.CaptionLabel_12.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_12.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_12.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.CaptionLabel_12)


        self.horizontalLayout_13.addLayout(self.verticalLayout_5)

        self.switch_enable_display_full_next_lessons = SwitchButton(self.CardWidget_3)
        self.switch_enable_display_full_next_lessons.setObjectName(u"switch_enable_display_full_next_lessons")
        sizePolicy2.setHeightForWidth(self.switch_enable_display_full_next_lessons.sizePolicy().hasHeightForWidth())
        self.switch_enable_display_full_next_lessons.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.switch_enable_display_full_next_lessons)


        self.verticalLayout_17.addWidget(self.CardWidget_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_17)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.ct_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.ct_scroll)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.save_config = PrimaryPushButton(Form)
        self.save_config.setObjectName(u"save_config")
        sizePolicy4.setHeightForWidth(self.save_config.sizePolicy().hasHeightForWidth())
        self.save_config.setSizePolicy(sizePolicy4)
        self.save_config.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.save_config)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"*\u5bf9\u5c0f\u7ec4\u4ef6\u7684\u663e\u793a\u3001\u9690\u85cf\u548c\u62d6\u62fd\u64cd\u4f5c\u5c06\u5728\u91cd\u542f\u540e\u751f\u6548\u3002", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u5c0f\u7ec4\u4ef6", None))
        self.add_widget.setText(QCoreApplication.translate("Form", u"  \u6dfb\u52a0  ", None))
        self.remove_widget.setText(QCoreApplication.translate("Form", u"  \u79fb\u9664  ", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u5c0f\u7ec4\u4ef6", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u4e3b\u9898", None))
        self.open_theme_folder.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u201c\u4e3b\u9898\u201d\u6587\u4ef6\u5939", None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("Form", u"\u4e3b\u9898", None))
        self.CaptionLabel_5.setText(QCoreApplication.translate("Form", u"\u5c06\u7528\u4e8e\u66f4\u6539\u5c0f\u7ec4\u4ef6\u7684\u6837\u5f0f\uff08\u91cd\u542f\u540e\u751f\u6548\uff09", None))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate("Form", u"\u989c\u8272\u6a21\u5f0f", None))
        self.CaptionLabel_10.setText(QCoreApplication.translate("Form", u"\u5c06\u6539\u53d8\u5e94\u7528\u7684\u6d45/\u6df1\u8272\u5916\u89c2", None))
        self.StrongBodyLabel_11.setText(QCoreApplication.translate("Form", u"\u5c0f\u7ec4\u4ef6\u900f\u660e\u5ea6", None))
        self.CaptionLabel_11.setText(QCoreApplication.translate("Form", u"\u66f4\u6539\u5c0f\u7ec4\u4ef6\u5728\u5c4f\u5e55\u4e0a\u663e\u793a\u7684\u900f\u660e\u5ea6", None))
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("Form", u"\u4e0a\u8bfe\u65f6\u4e3b\u9898\u8272", None))
        self.CaptionLabel_7.setText(QCoreApplication.translate("Form", u"\u5c06\u7528\u4e8e\u8bbe\u7f6e\u7a97\u53e3\u3001\u8fdb\u5ea6\u6761\u548c\u63d0\u9192\u5f39\u7a97 (\u4e3a\u4e86\u63d0\u9192\u5f39\u7a97\u53ef\u8bfb\u6027\uff0c\u8bf7\u4e0d\u8981\u8bbe\u7f6e\u8fc7\u6d45\u7684\u989c\u8272)", None))
        self.set_ac_color.setText(QCoreApplication.translate("Form", u"\u66f4\u6539\u989c\u8272", None))
        self.StrongBodyLabel_4.setText(QCoreApplication.translate("Form", u"\u4e0b\u8bfe\u65f6\u4e3b\u9898\u8272", None))
        self.CaptionLabel_6.setText(QCoreApplication.translate("Form", u"\u5c06\u7528\u4e8e\u8bbe\u7f6e\u7a97\u53e3\u3001\u8fdb\u5ea6\u6761\u548c\u63d0\u9192\u5f39\u7a97 (\u4e3a\u4e86\u63d0\u9192\u5f39\u7a97\u53ef\u8bfb\u6027\uff0c\u8bf7\u4e0d\u8981\u8bbe\u7f6e\u8fc7\u6d45\u7684\u989c\u8272)", None))
        self.set_fc_color.setText(QCoreApplication.translate("Form", u"\u66f4\u6539\u989c\u8272", None))
        self.StrongBodyLabel_13.setText(QCoreApplication.translate("Form", u"\u6d6e\u7a97\u65f6\u95f4\u989c\u8272", None))
        self.CaptionLabel_14.setText(QCoreApplication.translate("Form", u"\u5c06\u7528\u4e8e\u8bbe\u7f6e\u6d6e\u7a97\u65f6\u95f4\u989c\u8272 (\u4e3a\u4e86\u65f6\u95f4\u7684\u53ef\u8bfb\u6027\uff0c\u8bf7\u4e0d\u8981\u8bbe\u7f6e\u8fc7\u6d45\u7684\u989c\u8272&\u8fc7\u9ad8\u7684\u900f\u660e\u5ea6)", None))
        self.set_fc_color_2.setText(QCoreApplication.translate("Form", u"\u66f4\u6539\u989c\u8272", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Form", u"\u5012\u8ba1\u65f6\u6a21\u7cca", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"\u6a21\u7cca\u4e3b\u7ec4\u4ef6\u5012\u8ba1\u65f6", None))
        self.CaptionLabel_4.setText(QCoreApplication.translate("Form", u"\u5c06\u4f1a\u4ee5\u201c< x \u5206\u949f\u201d\u7684\u5f62\u5f0f\u6a21\u7cca\u5730\u663e\u793a\u5012\u8ba1\u65f6", None))
        self.switch_blur_countdown.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.switch_blur_countdown.setOnText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.switch_blur_countdown.setOffText(QCoreApplication.translate("Form", u"\u5173", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"\u6a21\u7cca\u6d6e\u7a97\u5012\u8ba1\u65f6", None))
        self.CaptionLabel_8.setText(QCoreApplication.translate("Form", u"\u5c06\u4f1a\u4ee5\u201c< x \u5206\u949f\u201d\u7684\u5f62\u5f0f\u6a21\u7cca\u5730\u663e\u793a\u5012\u8ba1\u65f6", None))
        self.switch_blur_countdown_2.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.switch_blur_countdown_2.setOnText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.switch_blur_countdown_2.setOffText(QCoreApplication.translate("Form", u"\u5173", None))
        self.SubtitleLabel_6.setText(QCoreApplication.translate("Form", u"\u663e\u793a", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", u"\u5141\u8bb8 \u201c\u63a5\u4e0b\u6765\u201d \u7ec4\u4ef6\u663e\u793a\u591a\u4e2a\u8bfe\u7a0b", None))
        self.CaptionLabel_12.setText(QCoreApplication.translate("Form", u"\u82e5\u5f00\u542f\uff0c\u5219\u663e\u793a\u4e0b\u6765\u7684\u591a\u4e2a\u8bfe\u7a0b\uff1b\u82e5\u5173\u95ed\uff0c\u4ec5\u663e\u793a\u4e00\u4e2a", None))
        self.switch_enable_display_full_next_lessons.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.switch_enable_display_full_next_lessons.setOnText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.switch_enable_display_full_next_lessons.setOffText(QCoreApplication.translate("Form", u"\u5173", None))
        self.save_config.setText(QCoreApplication.translate("Form", u"\u5e94\u7528", None))
    # retranslateUi
