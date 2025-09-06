# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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

from qfluentwidgets import (CaptionLabel, CardWidget, ComboBox, SmoothScrollArea,
    StrongBodyLabel, SubtitleLabel, SwitchButton, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(688, 806)
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

        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background: transparent; border: none")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 640, 725))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.SubtitleLabel_4 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")
        self.SubtitleLabel_4.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.SubtitleLabel_4)

        self.CardWidget_4 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.CardWidget_4.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_4)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        self.StrongBodyLabel_6.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.StrongBodyLabel_6)

        self.CaptionLabel_3 = CaptionLabel(self.CardWidget_4)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setWordWrap(True)
        self.CaptionLabel_3.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_3.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_8.addWidget(self.CaptionLabel_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.auto_enable_plugin = SwitchButton(self.CardWidget_4)
        self.auto_enable_plugin.setObjectName(u"auto_enable_plugin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.auto_enable_plugin.sizePolicy().hasHeightForWidth())
        self.auto_enable_plugin.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.auto_enable_plugin)


        self.verticalLayout_7.addWidget(self.CardWidget_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.SubtitleLabel_3)

        self.CardWidget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.CardWidget_3.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.StrongBodyLabel_5 = StrongBodyLabel(self.CardWidget_3)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")
        self.StrongBodyLabel_5.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.StrongBodyLabel_5)

        self.CaptionLabel_2 = CaptionLabel(self.CardWidget_3)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setWordWrap(True)
        self.CaptionLabel_2.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_2.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_6.addWidget(self.CaptionLabel_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.select_proxy = ComboBox(self.CardWidget_3)
        self.select_proxy.setObjectName(u"select_proxy")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.select_proxy.sizePolicy().hasHeightForWidth())
        self.select_proxy.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.select_proxy)


        self.verticalLayout_5.addWidget(self.CardWidget_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.blank = QFrame(self.scrollAreaWidgetContents)
        self.blank.setObjectName(u"blank")
        self.blank.setMinimumSize(QSize(0, 25))
        self.blank.setFrameShape(QFrame.StyledPanel)
        self.blank.setFrameShadow(QFrame.Raised)
        self.blank.setLineWidth(5)

        self.verticalLayout_9.addWidget(self.blank)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Form", u"\u63d2\u4ef6", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u540e\u81ea\u52a8\u542f\u7528\u63d2\u4ef6", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"\u5728\u4e0b\u8f7d\u63d2\u4ef6\u540e\uff0c\u5c06\u4e3a\u60a8\u81ea\u52a8\u542f\u7528\u63d2\u4ef6\u4ee5\u4fbf\u60a8\u91cd\u542f\u53ef\u4ee5\u7acb\u5373\u4f7f\u7528\u3002\n"
"\u4f46\u8bf7\u786e\u4fe1\u60a8\u5728\u201c\u63d2\u4ef6\u5e7f\u573a\u201d\u4e2d\u9700\u8981\u7684\u63d2\u4ef6\u662f\u5b89\u5168\u7684\u3002", None))
        self.auto_enable_plugin.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.auto_enable_plugin.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u7f51\u7edc", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u955c\u50cf\u6e90", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", u"\u82e5\u9700\u8981\u5728\u4e2d\u56fd\u5927\u9646\u6b63\u5e38\u4f7f\u7528\u201c\u63d2\u4ef6\u5e7f\u573a\u201d\uff0c\u6700\u597d\u4e3a\u5176\u8bbe\u7f6e\u4e00\u4e2a\u955c\u50cf\u6e90\u3002", None))
    # retranslateUi
