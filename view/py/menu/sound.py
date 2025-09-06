# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sound.ui'
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

from qfluentwidgets import (CaptionLabel, CardWidget, PrimaryDropDownPushButton, PrimaryPushButton,
    PushButton, Slider, SmoothScrollArea, SpinBox,
    StrongBodyLabel, SwitchButton, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(745, 773)
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

        self.sd_scroll = SmoothScrollArea(Form)
        self.sd_scroll.setObjectName(u"sd_scroll")
        self.sd_scroll.setStyleSheet(u"background: transparent; border: none")
        self.sd_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 697, 734))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.CardWidget_6 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_6.setObjectName(u"CardWidget_6")
        self.CardWidget_6.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_6.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_6.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_6.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.StrongBodyLabel_6)

        self.CaptionLabel_5 = CaptionLabel(self.CardWidget_6)
        self.CaptionLabel_5.setObjectName(u"CaptionLabel_5")
        self.CaptionLabel_5.setWordWrap(True)
        self.CaptionLabel_5.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_5.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_10.addWidget(self.CaptionLabel_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.switch_enable_attend = SwitchButton(self.CardWidget_6)
        self.switch_enable_attend.setObjectName(u"switch_enable_attend")

        self.horizontalLayout_6.addWidget(self.switch_enable_attend)


        self.verticalLayout_5.addWidget(self.CardWidget_6)

        self.CardWidget_10 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_10.setObjectName(u"CardWidget_10")
        self.CardWidget_10.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.StrongBodyLabel_8 = StrongBodyLabel(self.CardWidget_10)
        self.StrongBodyLabel_8.setObjectName(u"StrongBodyLabel_8")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_8.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_8.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_8.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.StrongBodyLabel_8)

        self.CaptionLabel_7 = CaptionLabel(self.CardWidget_10)
        self.CaptionLabel_7.setObjectName(u"CaptionLabel_7")
        self.CaptionLabel_7.setWordWrap(True)
        self.CaptionLabel_7.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_7.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_12.addWidget(self.CaptionLabel_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)

        self.switch_enable_finish = SwitchButton(self.CardWidget_10)
        self.switch_enable_finish.setObjectName(u"switch_enable_finish")

        self.horizontalLayout_8.addWidget(self.switch_enable_finish)


        self.verticalLayout_5.addWidget(self.CardWidget_10)

        self.CardWidget_14 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_14.setObjectName(u"CardWidget_14")
        self.CardWidget_14.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_9 = QHBoxLayout(self.CardWidget_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.CardWidget_14)
        self.StrongBodyLabel_9.setObjectName(u"StrongBodyLabel_9")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_9.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_9.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_9.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.StrongBodyLabel_9)

        self.CaptionLabel_10 = CaptionLabel(self.CardWidget_14)
        self.CaptionLabel_10.setObjectName(u"CaptionLabel_10")
        self.CaptionLabel_10.setWordWrap(True)
        self.CaptionLabel_10.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_10.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_15.addWidget(self.CaptionLabel_10)


        self.horizontalLayout_9.addLayout(self.verticalLayout_15)

        self.switch_enable_schoolout = SwitchButton(self.CardWidget_14)
        self.switch_enable_schoolout.setObjectName(u"switch_enable_schoolout")

        self.horizontalLayout_9.addWidget(self.switch_enable_schoolout)


        self.verticalLayout_5.addWidget(self.CardWidget_14)

        self.CardWidget_8 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_8.setObjectName(u"CardWidget_8")
        self.CardWidget_8.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_11 = QHBoxLayout(self.CardWidget_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.StrongBodyLabel_11 = StrongBodyLabel(self.CardWidget_8)
        self.StrongBodyLabel_11.setObjectName(u"StrongBodyLabel_11")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_11.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_11.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_11.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.StrongBodyLabel_11)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_8)
        self.CaptionLabel_8.setObjectName(u"CaptionLabel_8")
        self.CaptionLabel_8.setWordWrap(True)
        self.CaptionLabel_8.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_8.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_13.addWidget(self.CaptionLabel_8)


        self.horizontalLayout_11.addLayout(self.verticalLayout_13)

        self.spin_prepare_class = SpinBox(self.CardWidget_8)
        self.spin_prepare_class.setObjectName(u"spin_prepare_class")
        self.spin_prepare_class.setMinimumSize(QSize(130, 33))
        self.spin_prepare_class.setMaximum(9)

        self.horizontalLayout_11.addWidget(self.spin_prepare_class)

        self.switch_enable_prepare = SwitchButton(self.CardWidget_8)
        self.switch_enable_prepare.setObjectName(u"switch_enable_prepare")

        self.horizontalLayout_11.addWidget(self.switch_enable_prepare)


        self.verticalLayout_5.addWidget(self.CardWidget_8)

        self.CardWidget_13 = CardWidget(self.scrollAreaWidgetContents)
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
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_14.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_14.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_14.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.StrongBodyLabel_14)

        self.CaptionLabel_13 = CaptionLabel(self.CardWidget_13)
        self.CaptionLabel_13.setObjectName(u"CaptionLabel_13")
        self.CaptionLabel_13.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_13.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_13.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.CaptionLabel_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_18)

        self.TTS_PushButton = PushButton(self.CardWidget_13)
        self.TTS_PushButton.setObjectName(u"TTS_PushButton")

        self.horizontalLayout_14.addWidget(self.TTS_PushButton)


        self.verticalLayout_5.addWidget(self.CardWidget_13)

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
        self.CaptionLabel_6.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_6.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_6.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.CaptionLabel_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.slider_volume = Slider(self.CardWidget_7)
        self.slider_volume.setObjectName(u"slider_volume")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slider_volume.sizePolicy().hasHeightForWidth())
        self.slider_volume.setSizePolicy(sizePolicy2)
        self.slider_volume.setMinimumSize(QSize(200, 0))
        self.slider_volume.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.slider_volume)


        self.verticalLayout_5.addWidget(self.CardWidget_7)

        self.CardWidget_12 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_12.setObjectName(u"CardWidget_12")
        self.CardWidget_12.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_13 = QHBoxLayout(self.CardWidget_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.StrongBodyLabel_13 = StrongBodyLabel(self.CardWidget_12)
        self.StrongBodyLabel_13.setObjectName(u"StrongBodyLabel_13")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_13.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_13.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_13.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.StrongBodyLabel_13)

        self.CaptionLabel_12 = CaptionLabel(self.CardWidget_12)
        self.CaptionLabel_12.setObjectName(u"CaptionLabel_12")
        self.CaptionLabel_12.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_12.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_12.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.CaptionLabel_12)


        self.horizontalLayout_13.addLayout(self.verticalLayout_17)

        self.switch_enable_pin_toast = SwitchButton(self.CardWidget_12)
        self.switch_enable_pin_toast.setObjectName(u"switch_enable_pin_toast")

        self.horizontalLayout_13.addWidget(self.switch_enable_pin_toast)


        self.verticalLayout_5.addWidget(self.CardWidget_12)

        self.CardWidget_9 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_9.setObjectName(u"CardWidget_9")
        self.CardWidget_9.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_12 = QHBoxLayout(self.CardWidget_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.StrongBodyLabel_12 = StrongBodyLabel(self.CardWidget_9)
        self.StrongBodyLabel_12.setObjectName(u"StrongBodyLabel_12")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_12.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_12.setSizePolicy(sizePolicy1)
        self.StrongBodyLabel_12.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.StrongBodyLabel_12)

        self.CaptionLabel_9 = CaptionLabel(self.CardWidget_9)
        self.CaptionLabel_9.setObjectName(u"CaptionLabel_9")
        self.CaptionLabel_9.setWordWrap(True)
        self.CaptionLabel_9.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_9.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_14.addWidget(self.CaptionLabel_9)


        self.horizontalLayout_12.addLayout(self.verticalLayout_14)

        self.switch_enable_wave = SwitchButton(self.CardWidget_9)
        self.switch_enable_wave.setObjectName(u"switch_enable_wave")

        self.horizontalLayout_12.addWidget(self.switch_enable_wave)


        self.verticalLayout_5.addWidget(self.CardWidget_9)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.blank = QFrame(self.scrollAreaWidgetContents)
        self.blank.setObjectName(u"blank")
        self.blank.setMinimumSize(QSize(0, 25))
        self.blank.setFrameShape(QFrame.StyledPanel)
        self.blank.setFrameShadow(QFrame.Raised)
        self.blank.setLineWidth(5)

        self.verticalLayout_9.addWidget(self.blank)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.preview = PrimaryDropDownPushButton(self.scrollAreaWidgetContents)
        self.preview.setObjectName(u"preview")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.preview)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.sd_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.sd_scroll)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e0b\u8bfe\u63d0\u9192", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u4e0a\u8bfe\u63d0\u9192", None))
        self.CaptionLabel_5.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u540e\u5c06\u5728\u4e0a\u8bfe\u65f6\u5f39\u7a97\u4e14\u53d1\u51fa\u63d0\u793a\u97f3\u63d0\u9192", None))
        self.switch_enable_attend.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_attend.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u4e0b\u8bfe\u63d0\u9192", None))
        self.CaptionLabel_7.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u540e\u5c06\u5728\u4e0b\u8bfe\u65f6\u5f39\u7a97\u4e14\u53d1\u51fa\u63d0\u793a\u97f3\u63d0\u9192", None))
        self.switch_enable_finish.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_finish.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u653e\u5b66\u63d0\u9192", None))
        self.CaptionLabel_10.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u540e\u5c06\u5728\u653e\u5b66\u65f6\u5f39\u7a97\u4e14\u53d1\u51fa\u63d0\u793a\u97f3\u63d0\u9192", None))
        self.switch_enable_schoolout.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_schoolout.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_11.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u9884\u5907\u94c3", None))
        self.CaptionLabel_8.setText(QCoreApplication.translate("Form", u"\u5728\u6b63\u5f0f\u4e0a\u8bfe\u524d\u53d1\u51fa\u9884\u5907\u94c3\uff08\u8f93\u5165\u63d0\u524d\u7684\u5206\u949f\u6570\uff09", None))
        self.switch_enable_prepare.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_prepare.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_14.setText(QCoreApplication.translate("Form", u"TTS\u8bed\u97f3\u64ad\u62a5", None))
        self.CaptionLabel_13.setText(QCoreApplication.translate("Form", u"\u8c03\u6574\u5173\u4e8eTTS\u8bed\u97f3\u5408\u6210\u76f8\u5173\u9009\u9879", None))
        self.TTS_PushButton.setText(QCoreApplication.translate("Form", u"TTS\u8bed\u97f3\u8bbe\u7f6e", None))
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("Form", u"\u97f3\u91cf", None))
        self.CaptionLabel_6.setText(QCoreApplication.translate("Form", u"\u5c06\u8c03\u6574\u63d0\u9192\u58f0\u97f3\u7684\u97f3\u91cf\u5927\u5c0f", None))
        self.StrongBodyLabel_13.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u7f6e\u9876", None))
        self.CaptionLabel_12.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u540e\u5c06\u5728\u63d0\u9192\u65f6\u7f6e\u9876\u5f39\u7a97", None))
        self.switch_enable_pin_toast.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_pin_toast.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_12.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u5f3a\u8c03\u7279\u6548", None))
        self.CaptionLabel_9.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u540e\u5f39\u51fa\u63d0\u9192\u5f39\u7a97\u540c\u65f6\u4f1a\u6709\u6c34\u6ce2\u5f3a\u8c03\u53ca\u6a21\u7cca\u6de1\u5165\u6de1\u51fa\u6548\u679c\n"
"*\u53ef\u80fd\u5f71\u54cd\u6027\u80fd", None))
        self.switch_enable_wave.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_wave.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.preview.setText(QCoreApplication.translate("Form", u"\u9884\u89c8", None))
    # retranslateUi
