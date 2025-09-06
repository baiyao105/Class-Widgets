# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CaptionLabel, CardWidget, ComboBox, PrimaryPushButton,
    PushButton, SmoothScrollArea, StrongBodyLabel, SubtitleLabel,
    SwitchButton, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(821, 839)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.ab_scroll = SmoothScrollArea(Form)
        self.ab_scroll.setObjectName(u"ab_scroll")
        self.ab_scroll.setStyleSheet(u"background: transparent; border: none")
        self.ab_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 773, 765))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 14, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(48, 0, 48, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(128, 128))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/png/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.SubtitleLabel = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setAlignment(Qt.AlignCenter)
        self.SubtitleLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.CaptionLabel_3 = CaptionLabel(self.scrollAreaWidgetContents)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setAlignment(Qt.AlignCenter)
        self.CaptionLabel_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.CaptionLabel_3)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.version_info_card = CardWidget(self.scrollAreaWidgetContents)
        self.version_info_card.setObjectName(u"version_info_card")
        self.version_info_card.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_version_info = QHBoxLayout(self.version_info_card)
        self.horizontalLayout_version_info.setObjectName(u"horizontalLayout_version_info")
        self.horizontalLayout_version_info.setContentsMargins(16, 16, 16, 16)
        self.info_icon = QLabel(self.version_info_card)
        self.info_icon.setObjectName(u"info_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info_icon.sizePolicy().hasHeightForWidth())
        self.info_icon.setSizePolicy(sizePolicy1)
        self.info_icon.setMinimumSize(QSize(24, 24))
        self.info_icon.setMaximumSize(QSize(24, 24))
        self.info_icon.setPixmap(QPixmap(u":/png/logo/favicon-update.png"))
        self.info_icon.setScaledContents(True)
        self.info_icon.setWordWrap(True)

        self.horizontalLayout_version_info.addWidget(self.info_icon)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_version_info.addItem(self.horizontalSpacer)

        self.verticalLayout_version_details = QVBoxLayout()
        self.verticalLayout_version_details.setSpacing(0)
        self.verticalLayout_version_details.setObjectName(u"verticalLayout_version_details")
        self.version_number_label = StrongBodyLabel(self.version_info_card)
        self.version_number_label.setObjectName(u"version_number_label")
        self.version_number_label.setWordWrap(True)

        self.verticalLayout_version_details.addWidget(self.version_number_label)

        self.verticalSpacer_3 = QSpacerItem(0, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_version_details.addItem(self.verticalSpacer_3)

        self.horizontalLayout_build_info = QHBoxLayout()
        self.horizontalLayout_build_info.setObjectName(u"horizontalLayout_build_info")
        self.verticalLayout_build_date = QVBoxLayout()
        self.verticalLayout_build_date.setSpacing(0)
        self.verticalLayout_build_date.setObjectName(u"verticalLayout_build_date")
        self.build_date_title_label = StrongBodyLabel(self.version_info_card)
        self.build_date_title_label.setObjectName(u"build_date_title_label")
        self.build_date_title_label.setWordWrap(True)

        self.verticalLayout_build_date.addWidget(self.build_date_title_label)

        self.build_date_label = CaptionLabel(self.version_info_card)
        self.build_date_label.setObjectName(u"build_date_label")
        self.build_date_label.setWordWrap(True)

        self.verticalLayout_build_date.addWidget(self.build_date_label)


        self.horizontalLayout_build_info.addLayout(self.verticalLayout_build_date)

        self.horizontalSpacer_3 = QSpacerItem(2, 2, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_build_info.addItem(self.horizontalSpacer_3)

        self.verticalLayout_build_commit = QVBoxLayout()
        self.verticalLayout_build_commit.setSpacing(0)
        self.verticalLayout_build_commit.setObjectName(u"verticalLayout_build_commit")
        self.build_commit_title_label = StrongBodyLabel(self.version_info_card)
        self.build_commit_title_label.setObjectName(u"build_commit_title_label")
        self.build_commit_title_label.setWordWrap(True)

        self.verticalLayout_build_commit.addWidget(self.build_commit_title_label)

        self.build_commit_label = CaptionLabel(self.version_info_card)
        self.build_commit_label.setObjectName(u"build_commit_label")
        self.build_commit_label.setWordWrap(True)

        self.verticalLayout_build_commit.addWidget(self.build_commit_label)


        self.horizontalLayout_build_info.addLayout(self.verticalLayout_build_commit)

        self.horizontalSpacer_2 = QSpacerItem(2, 2, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_build_info.addItem(self.horizontalSpacer_2)

        self.verticalLayout_build_uuid = QVBoxLayout()
        self.verticalLayout_build_uuid.setSpacing(0)
        self.verticalLayout_build_uuid.setObjectName(u"verticalLayout_build_uuid")
        self.build_uuid_title_label = StrongBodyLabel(self.version_info_card)
        self.build_uuid_title_label.setObjectName(u"build_uuid_title_label")
        self.build_uuid_title_label.setWordWrap(True)

        self.verticalLayout_build_uuid.addWidget(self.build_uuid_title_label)

        self.build_uuid_label = CaptionLabel(self.version_info_card)
        self.build_uuid_label.setObjectName(u"build_uuid_label")
        self.build_uuid_label.setWordWrap(True)

        self.verticalLayout_build_uuid.addWidget(self.build_uuid_label)


        self.horizontalLayout_build_info.addLayout(self.verticalLayout_build_uuid)


        self.verticalLayout_version_details.addLayout(self.horizontalLayout_build_info)


        self.horizontalLayout_version_info.addLayout(self.verticalLayout_version_details)

        self.check_update = PrimaryPushButton(self.version_info_card)
        self.check_update.setObjectName(u"check_update")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.check_update.sizePolicy().hasHeightForWidth())
        self.check_update.setSizePolicy(sizePolicy2)

        self.horizontalLayout_version_info.addWidget(self.check_update)


        self.horizontalLayout_5.addWidget(self.version_info_card)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.button_github = PushButton(self.scrollAreaWidgetContents)
        self.button_github.setObjectName(u"button_github")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_github.sizePolicy().hasHeightForWidth())
        self.button_github.setSizePolicy(sizePolicy3)
        self.button_github.setMinimumSize(QSize(0, 0))
        self.button_github.setMaximumSize(QSize(360, 16777215))
        self.button_github.setProperty("hasIcon", False)

        self.horizontalLayout_3.addWidget(self.button_github)

        self.button_bilibili = PushButton(self.scrollAreaWidgetContents)
        self.button_bilibili.setObjectName(u"button_bilibili")
        sizePolicy3.setHeightForWidth(self.button_bilibili.sizePolicy().hasHeightForWidth())
        self.button_bilibili.setSizePolicy(sizePolicy3)
        self.button_bilibili.setMinimumSize(QSize(0, 0))
        self.button_bilibili.setMaximumSize(QSize(360, 16777215))

        self.horizontalLayout_3.addWidget(self.button_bilibili)

        self.button_weblate = PushButton(self.scrollAreaWidgetContents)
        self.button_weblate.setObjectName(u"button_weblate")
        sizePolicy3.setHeightForWidth(self.button_weblate.sizePolicy().hasHeightForWidth())
        self.button_weblate.setSizePolicy(sizePolicy3)
        self.button_weblate.setMinimumSize(QSize(0, 0))
        self.button_weblate.setMaximumSize(QSize(360, 16777215))

        self.horizontalLayout_3.addWidget(self.button_weblate)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.button_show_license = PushButton(self.scrollAreaWidgetContents)
        self.button_show_license.setObjectName(u"button_show_license")
        sizePolicy3.setHeightForWidth(self.button_show_license.sizePolicy().hasHeightForWidth())
        self.button_show_license.setSizePolicy(sizePolicy3)
        self.button_show_license.setMinimumSize(QSize(0, 0))
        self.button_show_license.setMaximumSize(QSize(310, 16777215))
        self.button_show_license.setProperty("hasIcon", False)

        self.horizontalLayout_4.addWidget(self.button_show_license)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.button_thanks = PushButton(self.scrollAreaWidgetContents)
        self.button_thanks.setObjectName(u"button_thanks")
        sizePolicy3.setHeightForWidth(self.button_thanks.sizePolicy().hasHeightForWidth())
        self.button_thanks.setSizePolicy(sizePolicy3)
        self.button_thanks.setMinimumSize(QSize(0, 0))
        self.button_thanks.setMaximumSize(QSize(310, 16777215))
        self.button_thanks.setProperty("hasIcon", False)

        self.horizontalLayout_2.addWidget(self.button_thanks)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 12, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.SubtitleLabel_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.CardWidget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.CardWidget_3.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.StrongBodyLabel_5 = StrongBodyLabel(self.CardWidget_3)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")
        self.StrongBodyLabel_5.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.StrongBodyLabel_5)

        self.CaptionLabel_5 = CaptionLabel(self.CardWidget_3)
        self.CaptionLabel_5.setObjectName(u"CaptionLabel_5")
        self.CaptionLabel_5.setWordWrap(False)
        self.CaptionLabel_5.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_5.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_6.addWidget(self.CaptionLabel_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.version_channel = ComboBox(self.CardWidget_3)
        self.version_channel.setObjectName(u"version_channel")
        sizePolicy2.setHeightForWidth(self.version_channel.sizePolicy().hasHeightForWidth())
        self.version_channel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.version_channel)


        self.verticalLayout_5.addWidget(self.CardWidget_3)

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.StrongBodyLabel_14.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_14.setSizePolicy(sizePolicy4)
        self.StrongBodyLabel_14.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.StrongBodyLabel_14)

        self.CaptionLabel_12 = CaptionLabel(self.CardWidget_12)
        self.CaptionLabel_12.setObjectName(u"CaptionLabel_12")
        self.CaptionLabel_12.setWordWrap(True)
        self.CaptionLabel_12.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_12.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_18.addWidget(self.CaptionLabel_12)


        self.horizontalLayout_13.addLayout(self.verticalLayout_18)

        self.auto_check_update = SwitchButton(self.CardWidget_12)
        self.auto_check_update.setObjectName(u"auto_check_update")

        self.horizontalLayout_13.addWidget(self.auto_check_update)


        self.verticalLayout_5.addWidget(self.CardWidget_12)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 106, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.ab_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.ab_scroll)

        self.CaptionLabel_2 = CaptionLabel(Form)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setAlignment(Qt.AlignCenter)
        self.CaptionLabel_2.setProperty("lightColor", QColor(127, 127, 127))
        self.CaptionLabel_2.setProperty("darkColor", QColor(185, 185, 185))
        self.CaptionLabel_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.CaptionLabel_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.label.setText("")
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"Class Widgets", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"Class Widgets \u662f\u4e00\u6b3e\u80fd\u663e\u793a\u5f53\u524d\u8bfe\u7a0b\u7684\u684c\u9762\u7ec4\u4ef6App\u3002\u5176\u63d0\u4f9b\u4e86\u76f4\u89c2\u7684\u56fe\u5f62\u5316\u8bfe\u7a0b\u8868\u7f16\u8f91\u548c\u7f8e\u89c2\u7684\u684c\u9762\u7ec4\u4ef6\u3002", None))
        self.version_number_label.setText(QCoreApplication.translate("Form", u"\u7248\u672c\u53f7:\u83b7\u53d6\u5931\u8d25\uff01", None))
        self.build_date_title_label.setText(QCoreApplication.translate("Form", u"\u7f16\u8bd1\u65e5\u671f", None))
        self.build_date_label.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u5931\u8d25\uff01", None))
        self.build_commit_title_label.setText(QCoreApplication.translate("Form", u"Build Commit", None))
        self.build_commit_label.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u5931\u8d25\uff01", None))
        self.build_uuid_title_label.setText(QCoreApplication.translate("Form", u"Build UUID", None))
        self.build_uuid_label.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u5931\u8d25\uff01", None))
        self.check_update.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.button_github.setText(QCoreApplication.translate("Form", u"\u6b64\u9879\u76ee\u7684 Github", None))
        self.button_bilibili.setText(QCoreApplication.translate("Form", u"\u6211\u7684 \u54d4\u54e9\u54d4\u54e9 \u4e3b\u9875", None))
        self.button_weblate.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u6b64\u5e94\u7528", None))
        self.button_show_license.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u5f00\u653e\u6e90\u4ee3\u7801\u8bb8\u53ef", None))
        self.button_thanks.setText(QCoreApplication.translate("Form", u"\u9e23\u8c22", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u66f4\u65b0\u901a\u9053", None))
        self.CaptionLabel_5.setText(QCoreApplication.translate("Form", u"\u5c06\u4f1a\u83b7\u53d6\u9009\u5b9a\u66f4\u65b0\u901a\u9053\u7684\u7248\u672c", None))
        self.StrongBodyLabel_14.setText(QCoreApplication.translate("Form", u"\u542f\u52a8 Class Widgets \u65f6\u81ea\u52a8\u68c0\u67e5\u66f4\u65b0", None))
        self.CaptionLabel_12.setText(QCoreApplication.translate("Form", u"\u82e5\u542f\u7528\uff0cClass Widgets \u5c06\u5728\u542f\u52a8\u65f6\u8054\u7f51\u68c0\u67e5\u9009\u5b9a\u7684\u66f4\u65b0\u901a\u9053\u4e2d\u662f\u5426\u6709\u6700\u65b0\u7248\u672c\u66f4\u65b0\u3002", None))
        self.auto_check_update.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.auto_check_update.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", u"Copyright \u00a9 2025 RinLit, All Rights Reversed.", None))
    # retranslateUi
