# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tts_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CaptionLabel, CardWidget, ComboBox, HyperlinkLabel,
    LineEdit, PrimaryDropDownPushButton, PrimaryPushButton, PushButton,
    Slider, SmoothScrollArea, StrongBodyLabel, SubtitleLabel,
    SwitchButton, TitleLabel)

class Ui_TTSAdvancedSettings(object):
    def setupUi(self, TTSAdvancedSettings):
        if not TTSAdvancedSettings.objectName():
            TTSAdvancedSettings.setObjectName(u"TTSAdvancedSettings")
        TTSAdvancedSettings.resize(778, 1047)
        TTSAdvancedSettings.setStyleSheet(u"background: transparent; border: none")
        self.verticalLayout_Main = QVBoxLayout(TTSAdvancedSettings)
        self.verticalLayout_Main.setSpacing(18)
        self.verticalLayout_Main.setObjectName(u"verticalLayout_Main")
        self.verticalLayout_Main.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = SmoothScrollArea(TTSAdvancedSettings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 778, 1047))
        self.verticalLayout_Scroll = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_Scroll.setSpacing(24)
        self.verticalLayout_Scroll.setObjectName(u"verticalLayout_Scroll")
        self.verticalLayout_Scroll.setContentsMargins(24, 24, 24, 24)
        self.sd_scroll = SmoothScrollArea(self.scrollAreaWidgetContents)
        self.sd_scroll.setObjectName(u"sd_scroll")
        self.sd_scroll.setStyleSheet(u"background: transparent; border: none")
        self.sd_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 730, 999))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.TitleLabel = TitleLabel(self.scrollAreaWidgetContents_2)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.TitleLabel)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.CardWidget_13 = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget_13.setObjectName(u"CardWidget_13")
        self.CardWidget_13.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_14 = QHBoxLayout(self.CardWidget_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.StrongBodyLabel_14 = StrongBodyLabel(self.CardWidget_13)
        self.StrongBodyLabel_14.setObjectName(u"StrongBodyLabel_14")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_14.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_14.setSizePolicy(sizePolicy)
        self.StrongBodyLabel_14.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.StrongBodyLabel_14)

        self.CaptionLabel_13 = CaptionLabel(self.CardWidget_13)
        self.CaptionLabel_13.setObjectName(u"CaptionLabel_13")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CaptionLabel_13.sizePolicy().hasHeightForWidth())
        self.CaptionLabel_13.setSizePolicy(sizePolicy1)
        self.CaptionLabel_13.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_13.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_13.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.CaptionLabel_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_18)

        self.switch_enable_tts = SwitchButton(self.CardWidget_13)
        self.switch_enable_tts.setObjectName(u"switch_enable_tts")
        self.switch_enable_tts.setEnabled(True)

        self.horizontalLayout_14.addWidget(self.switch_enable_tts)


        self.verticalLayout_5.addWidget(self.CardWidget_13)

        self.CardWidget_9 = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget_9.setObjectName(u"CardWidget_9")
        self.CardWidget_9.setMinimumSize(QSize(0, 80))
        self.gridLayout = QGridLayout(self.CardWidget_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.CardWidget_9)
        self.StrongBodyLabel_9.setObjectName(u"StrongBodyLabel_9")
        self.StrongBodyLabel_9.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.StrongBodyLabel_9)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_9)
        self.CaptionLabel_8.setObjectName(u"CaptionLabel_8")
        self.CaptionLabel_8.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_8.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_8.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.CaptionLabel_8)

        self.verticalSpacer_for_note = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_for_note)

        self.engine_note = HyperlinkLabel(self.CardWidget_9)
        self.engine_note.setObjectName(u"engine_note")

        self.verticalLayout_13.addWidget(self.engine_note)


        self.gridLayout.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.engine_selector = ComboBox(self.CardWidget_9)
        self.engine_selector.setObjectName(u"engine_selector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.engine_selector.sizePolicy().hasHeightForWidth())
        self.engine_selector.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.engine_selector, 0, 2, 1, 1)

        self.voice_language = ComboBox(self.CardWidget_9)
        self.voice_language.setObjectName(u"voice_language")
        self.voice_language.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.voice_language.sizePolicy().hasHeightForWidth())
        self.voice_language.setSizePolicy(sizePolicy3)
        self.voice_language.setMinimumSize(QSize(10, 0))

        self.gridLayout.addWidget(self.voice_language, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.CardWidget_9)

        self.CardWidget_8 = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget_8.setObjectName(u"CardWidget_8")
        self.CardWidget_8.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.StrongBodyLabel_8 = StrongBodyLabel(self.CardWidget_8)
        self.StrongBodyLabel_8.setObjectName(u"StrongBodyLabel_8")
        self.StrongBodyLabel_8.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.StrongBodyLabel_8)

        self.CaptionLabel_7 = CaptionLabel(self.CardWidget_8)
        self.CaptionLabel_7.setObjectName(u"CaptionLabel_7")
        self.CaptionLabel_7.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_7.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_7.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.CaptionLabel_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)

        self.voice_selector = ComboBox(self.CardWidget_8)
        self.voice_selector.setObjectName(u"voice_selector")
        self.voice_selector.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.voice_selector.sizePolicy().hasHeightForWidth())
        self.voice_selector.setSizePolicy(sizePolicy4)
        self.voice_selector.setMaximumSize(QSize(450, 16777215))

        self.horizontalLayout_8.addWidget(self.voice_selector)


        self.verticalLayout_5.addWidget(self.CardWidget_8)

        self.verticalSpacer_for_note_2 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_for_note_2)

        self.CardWidget_7 = CardWidget(self.scrollAreaWidgetContents_2)
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
        self.CaptionLabel_6.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_6.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_6.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.CaptionLabel_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.slider_tts_speed = Slider(self.CardWidget_7)
        self.slider_tts_speed.setObjectName(u"slider_tts_speed")
        sizePolicy3.setHeightForWidth(self.slider_tts_speed.sizePolicy().hasHeightForWidth())
        self.slider_tts_speed.setSizePolicy(sizePolicy3)
        self.slider_tts_speed.setMinimumSize(QSize(200, 0))
        self.slider_tts_speed.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.slider_tts_speed)


        self.verticalLayout_5.addWidget(self.CardWidget_7)

        self.SubtitleLabel_CustomText = SubtitleLabel(self.scrollAreaWidgetContents_2)
        self.SubtitleLabel_CustomText.setObjectName(u"SubtitleLabel_CustomText")
        self.SubtitleLabel_CustomText.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.SubtitleLabel_CustomText)

        self.CardWidget_11 = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget_11.setObjectName(u"CardWidget_11")
        self.CardWidget_11.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_15 = QHBoxLayout(self.CardWidget_11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.StrongBodyLabel_15 = StrongBodyLabel(self.CardWidget_11)
        self.StrongBodyLabel_15.setObjectName(u"StrongBodyLabel_15")
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_15.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_15.setSizePolicy(sizePolicy)
        self.StrongBodyLabel_15.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.StrongBodyLabel_15)

        self.text_attend_class = LineEdit(self.CardWidget_11)
        self.text_attend_class.setObjectName(u"text_attend_class")

        self.verticalLayout_16.addWidget(self.text_attend_class)


        self.horizontalLayout_15.addLayout(self.verticalLayout_16)


        self.verticalLayout_5.addWidget(self.CardWidget_11)

        self.CardWidget_14 = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget_14.setObjectName(u"CardWidget_14")
        self.CardWidget_14.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_16 = QHBoxLayout(self.CardWidget_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.StrongBodyLabel_16 = StrongBodyLabel(self.CardWidget_14)
        self.StrongBodyLabel_16.setObjectName(u"StrongBodyLabel_16")
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_16.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_16.setSizePolicy(sizePolicy)
        self.StrongBodyLabel_16.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.StrongBodyLabel_16)

        self.text_prepare_class = LineEdit(self.CardWidget_14)
        self.text_prepare_class.setObjectName(u"text_prepare_class")

        self.verticalLayout_20.addWidget(self.text_prepare_class)


        self.horizontalLayout_16.addLayout(self.verticalLayout_20)


        self.verticalLayout_5.addWidget(self.CardWidget_14)

        self.CardWidget_15 = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget_15.setObjectName(u"CardWidget_15")
        self.CardWidget_15.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_17 = QHBoxLayout(self.CardWidget_15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.StrongBodyLabel_17 = StrongBodyLabel(self.CardWidget_15)
        self.StrongBodyLabel_17.setObjectName(u"StrongBodyLabel_17")
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_17.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_17.setSizePolicy(sizePolicy)
        self.StrongBodyLabel_17.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.StrongBodyLabel_17)

        self.text_finish_class = LineEdit(self.CardWidget_15)
        self.text_finish_class.setObjectName(u"text_finish_class")

        self.verticalLayout_21.addWidget(self.text_finish_class)


        self.horizontalLayout_17.addLayout(self.verticalLayout_21)


        self.verticalLayout_5.addWidget(self.CardWidget_15)

        self.CardWidget_16 = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget_16.setObjectName(u"CardWidget_16")
        self.CardWidget_16.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_18 = QHBoxLayout(self.CardWidget_16)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.StrongBodyLabel_18 = StrongBodyLabel(self.CardWidget_16)
        self.StrongBodyLabel_18.setObjectName(u"StrongBodyLabel_18")
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_18.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_18.setSizePolicy(sizePolicy)
        self.StrongBodyLabel_18.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.StrongBodyLabel_18)

        self.text_after_school = LineEdit(self.CardWidget_16)
        self.text_after_school.setObjectName(u"text_after_school")

        self.verticalLayout_22.addWidget(self.text_after_school)


        self.horizontalLayout_18.addLayout(self.verticalLayout_22)


        self.verticalLayout_5.addWidget(self.CardWidget_16)

        self.CardWidget_17 = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget_17.setObjectName(u"CardWidget_17")
        self.CardWidget_17.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_19 = QHBoxLayout(self.CardWidget_17)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.StrongBodyLabel_19 = StrongBodyLabel(self.CardWidget_17)
        self.StrongBodyLabel_19.setObjectName(u"StrongBodyLabel_19")
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_19.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_19.setSizePolicy(sizePolicy)
        self.StrongBodyLabel_19.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.StrongBodyLabel_19)

        self.text_notification = LineEdit(self.CardWidget_17)
        self.text_notification.setObjectName(u"text_notification")

        self.verticalLayout_23.addWidget(self.text_notification)


        self.horizontalLayout_19.addLayout(self.verticalLayout_23)


        self.verticalLayout_5.addWidget(self.CardWidget_17)

        self.CardWidget_18 = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget_18.setObjectName(u"CardWidget_18")
        self.CardWidget_18.setMinimumSize(QSize(0, 70))
        self.horizontalLayout = QHBoxLayout(self.CardWidget_18)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.tts_vocab_button = PushButton(self.CardWidget_18)
        self.tts_vocab_button.setObjectName(u"tts_vocab_button")

        self.horizontalLayout.addWidget(self.tts_vocab_button)

        self.preview = PrimaryDropDownPushButton(self.CardWidget_18)
        self.preview.setObjectName(u"preview")
        self.preview.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.preview)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.CardWidget_18)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.sd_scroll.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_Scroll.addWidget(self.sd_scroll)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_Main.addWidget(self.scrollArea)


        self.retranslateUi(TTSAdvancedSettings)

        QMetaObject.connectSlotsByName(TTSAdvancedSettings)
    # setupUi

    def retranslateUi(self, TTSAdvancedSettings):
        TTSAdvancedSettings.setWindowTitle(QCoreApplication.translate("TTSAdvancedSettings", u"TTS \u9ad8\u7ea7\u8bbe\u7f6e", None))
        self.TitleLabel.setText(QCoreApplication.translate("TTSAdvancedSettings", u"TTS\u8bed\u97f3\u8bbe\u7f6e", None))
        self.StrongBodyLabel_14.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u4f7f\u7528TTS\u8bed\u97f3", None))
        self.CaptionLabel_13.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u542f\u7528\u540e\u5c06\u5728\u63d0\u9192\u540e\u4f7f\u7528TTS\u64ad\u62a5\u4fe1\u606f", None))
        self.switch_enable_tts.setOnText(QCoreApplication.translate("TTSAdvancedSettings", u"\u542f\u7528", None))
        self.switch_enable_tts.setOffText(QCoreApplication.translate("TTSAdvancedSettings", u"\u7981\u7528", None))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate("TTSAdvancedSettings", u"TTS\u751f\u6210\u5f15\u64ce", None))
        self.CaptionLabel_8.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u9009\u62e9\u7528\u4e8e\u751f\u6210TTS\u8bed\u97f3\u7684\u5f15\u64ce", None))
        self.engine_note.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u6e29\u99a8\u63d0\u793a", None))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("TTSAdvancedSettings", u"TTS\u751f\u6210\u4eba", None))
        self.CaptionLabel_7.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u7528\u4e8e\u751f\u6210TTS\u8bed\u97f3\u6240\u7528\u7684\u8bed\u97f3id", None))
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u8bed\u901f\u8c03\u8282", None))
        self.CaptionLabel_6.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u8c03\u6574TTS\u7684\u64ad\u653e\u901f\u5ea6", None))
        self.SubtitleLabel_CustomText.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u81ea\u5b9a\u4e49\u64ad\u62a5\u6587\u672c", None))
        self.StrongBodyLabel_15.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u6d3b\u52a8\u5f00\u59cb\u65f6:", None))
        self.text_attend_class.setPlaceholderText(QCoreApplication.translate("TTSAdvancedSettings", u"\u4f8b\u5982\uff1a\u540c\u5b66\u4eec\u597d\uff0c\u73b0\u5728\u5f00\u59cb{lesson_name}\u8bfe\u3002", None))
        self.StrongBodyLabel_16.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u5373\u5c06\u5f00\u59cb\u65f6 (\u9884\u5907\u94c3):", None))
        self.text_prepare_class.setPlaceholderText(QCoreApplication.translate("TTSAdvancedSettings", u"\u4f8b\u5982\uff1a\u8ddd\u79bb{lesson_name}\u8bfe\u8fd8\u6709{minutes}\u5206\u949f\uff0c\u8bf7\u505a\u597d\u51c6\u5907\u3002", None))
        self.StrongBodyLabel_17.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u6d3b\u52a8\u7ed3\u675f\u65f6:", None))
        self.text_finish_class.setPlaceholderText(QCoreApplication.translate("TTSAdvancedSettings", u"\u4f8b\u5982\uff1a{lesson_name}\u8bfe\u7ed3\u675f\uff0c\u8bf7\u540c\u5b66\u4eec\u51c6\u5907\u4e0b\u4e00\u8282\u8bfe\u3002", None))
        self.StrongBodyLabel_18.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u653e\u5b66\u65f6:", None))
        self.text_after_school.setPlaceholderText(QCoreApplication.translate("TTSAdvancedSettings", u"\u4f8b\u5982\uff1a\u653e\u5b66\u65f6\u95f4\u5230\uff0c\u8bf7\u540c\u5b66\u4eec\u6574\u7406\u597d\u7269\u54c1\uff0c\u5b89\u5168\u79bb\u6821\u3002", None))
        self.StrongBodyLabel_19.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u5176\u4ed6\u901a\u77e5 (\u7528\u4e8e\u63d2\u4ef6\u6216\u624b\u52a8\u89e6\u53d1):", None))
        self.text_notification.setPlaceholderText(QCoreApplication.translate("TTSAdvancedSettings", u"\u4f8b\u5982\uff1a{title}\uff0c{content}", None))
        self.tts_vocab_button.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u53ef\u7528\u5360\u4f4d\u7b26", None))
        self.preview.setText(QCoreApplication.translate("TTSAdvancedSettings", u"\u9884\u89c8", None))
    # retranslateUi
