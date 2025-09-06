# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plugin_detail.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, HyperlinkLabel, ImageLabel,
    PrimarySplitPushButton, SmoothScrollArea, SplitPushButton, TitleLabel,
    ToolButton, TransparentToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(688, 713)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background: transparent; border: none")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 688, 713))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(24, 24, 24, 24)
        self.detailLayout = QHBoxLayout()
        self.detailLayout.setObjectName(u"detailLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.detailLayout.addItem(self.horizontalSpacer_5)

        self.closeButton = TransparentToolButton(self.scrollAreaWidgetContents)
        self.closeButton.setObjectName(u"closeButton")

        self.detailLayout.addWidget(self.closeButton)


        self.verticalLayout_9.addLayout(self.detailLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, -1, 12, -1)
        self.pluginIcon = ImageLabel(self.scrollAreaWidgetContents)
        self.pluginIcon.setObjectName(u"pluginIcon")
        self.pluginIcon.setMinimumSize(QSize(128, 128))
        self.pluginIcon.setMaximumSize(QSize(128, 128))
        self.pluginIcon.setWordWrap(True)

        self.horizontalLayout.addWidget(self.pluginIcon)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setSpacing(12)
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLabel = TitleLabel(self.scrollAreaWidgetContents)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy1)
        self.titleLabel.setWordWrap(False)

        self.titleLayout.addWidget(self.titleLabel)

        self.versionLabel = BodyLabel(self.scrollAreaWidgetContents)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setProperty("lightColor", QColor(153, 153, 153))
        self.versionLabel.setProperty("darkColor", QColor(153, 153, 153))
        self.versionLabel.setWordWrap(True)

        self.titleLayout.addWidget(self.versionLabel)


        self.verticalLayout.addLayout(self.titleLayout)

        self.authorLayout = QHBoxLayout()
        self.authorLayout.setSpacing(12)
        self.authorLayout.setObjectName(u"authorLayout")
        self.authorButton = HyperlinkLabel(self.scrollAreaWidgetContents)
        self.authorButton.setObjectName(u"authorButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.authorButton.sizePolicy().hasHeightForWidth())
        self.authorButton.setSizePolicy(sizePolicy2)

        self.authorLayout.addWidget(self.authorButton)

        self.BodyLabel_2 = BodyLabel(self.scrollAreaWidgetContents)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        self.BodyLabel_2.setProperty("lightColor", QColor(153, 153, 153))
        self.BodyLabel_2.setProperty("darkColor", QColor(153, 153, 153))
        self.BodyLabel_2.setWordWrap(True)

        self.authorLayout.addWidget(self.BodyLabel_2)

        self.tagButton = HyperlinkLabel(self.scrollAreaWidgetContents)
        self.tagButton.setObjectName(u"tagButton")
        sizePolicy2.setHeightForWidth(self.tagButton.sizePolicy().hasHeightForWidth())
        self.tagButton.setSizePolicy(sizePolicy2)

        self.authorLayout.addWidget(self.tagButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.authorLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.authorLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(18, -1, 18, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(24)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.descLabel = CaptionLabel(self.scrollAreaWidgetContents)
        self.descLabel.setObjectName(u"descLabel")
        self.descLabel.setMaximumSize(QSize(425, 16777215))
        self.descLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.descLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.installButton = PrimarySplitPushButton(self.scrollAreaWidgetContents)
        self.installButton.setObjectName(u"installButton")
        icon = QIcon()
        iconThemeName = u"UPDATE"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.installButton.setProperty("icon_", icon)

        self.horizontalLayout_3.addWidget(self.installButton)

        self.openGitHub = TransparentToolButton(self.scrollAreaWidgetContents)
        self.openGitHub.setObjectName(u"openGitHub")

        self.horizontalLayout_3.addWidget(self.openGitHub)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleLabel.setText(QCoreApplication.translate("Form", u"PluginName", None))
        self.versionLabel.setText(QCoreApplication.translate("Form", u"1.1.0", None))
        self.authorButton.setText(QCoreApplication.translate("Form", u"Author", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"|", None))
        self.tagButton.setText(QCoreApplication.translate("Form", u"Tag", None))
        self.descLabel.setText(QCoreApplication.translate("Form", u"Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description Plugin Description ", None))
        self.installButton.setProperty("text_", QCoreApplication.translate("Form", u"Install", None))
    # retranslateUi
