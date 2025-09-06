# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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

from qfluentwidgets import (CaptionLabel, HyperlinkButton, PushButton, SmoothScrollArea,
    SubtitleLabel, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(721, 817)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.TitleLabel)

        self.CaptionLabel = CaptionLabel(Form)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.CaptionLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.open_by_browser = PushButton(Form)
        self.open_by_browser.setObjectName(u"open_by_browser")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_by_browser.sizePolicy().hasHeightForWidth())
        self.open_by_browser.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.open_by_browser)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.adv_scroll = SmoothScrollArea(Form)
        self.adv_scroll.setObjectName(u"adv_scroll")
        self.adv_scroll.setStyleSheet(u"background: transparent; border: none")
        self.adv_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 673, 691))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_26.setSpacing(12)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(14, 9, 16, -1)
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.SubtitleLabel_5 = SubtitleLabel(self.scrollAreaWidgetContents_2)
        self.SubtitleLabel_5.setObjectName(u"SubtitleLabel_5")
        self.SubtitleLabel_5.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.SubtitleLabel_5)

        self.common_question = QVBoxLayout()
        self.common_question.setSpacing(3)
        self.common_question.setObjectName(u"common_question")
        self.HyperlinkButton = HyperlinkButton(self.scrollAreaWidgetContents_2)
        self.HyperlinkButton.setObjectName(u"HyperlinkButton")
        sizePolicy.setHeightForWidth(self.HyperlinkButton.sizePolicy().hasHeightForWidth())
        self.HyperlinkButton.setSizePolicy(sizePolicy)
        self.HyperlinkButton.setUrl(QUrl(u"https://www.yuque.com/rinlit/class-widgets_help/swg86btkivirtnrl"))

        self.common_question.addWidget(self.HyperlinkButton)

        self.HyperlinkButton_7 = HyperlinkButton(self.scrollAreaWidgetContents_2)
        self.HyperlinkButton_7.setObjectName(u"HyperlinkButton_7")
        sizePolicy.setHeightForWidth(self.HyperlinkButton_7.sizePolicy().hasHeightForWidth())
        self.HyperlinkButton_7.setSizePolicy(sizePolicy)
        self.HyperlinkButton_7.setUrl(QUrl(u"https://www.yuque.com/rinlit/class-widgets_help/lg0p91q2mg4yertn"))

        self.common_question.addWidget(self.HyperlinkButton_7)

        self.HyperlinkButton_6 = HyperlinkButton(self.scrollAreaWidgetContents_2)
        self.HyperlinkButton_6.setObjectName(u"HyperlinkButton_6")
        sizePolicy.setHeightForWidth(self.HyperlinkButton_6.sizePolicy().hasHeightForWidth())
        self.HyperlinkButton_6.setSizePolicy(sizePolicy)
        self.HyperlinkButton_6.setUrl(QUrl(u"https://www.yuque.com/rinlit/class-widgets_help/vlk3plggb8edvub4#mHfUX"))

        self.common_question.addWidget(self.HyperlinkButton_6)

        self.HyperlinkButton_5 = HyperlinkButton(self.scrollAreaWidgetContents_2)
        self.HyperlinkButton_5.setObjectName(u"HyperlinkButton_5")
        sizePolicy.setHeightForWidth(self.HyperlinkButton_5.sizePolicy().hasHeightForWidth())
        self.HyperlinkButton_5.setSizePolicy(sizePolicy)
        self.HyperlinkButton_5.setUrl(QUrl(u"https://www.yuque.com/rinlit/class-widgets_help/gc4epffu7g5bf9os"))

        self.common_question.addWidget(self.HyperlinkButton_5)

        self.HyperlinkButton_4 = HyperlinkButton(self.scrollAreaWidgetContents_2)
        self.HyperlinkButton_4.setObjectName(u"HyperlinkButton_4")
        sizePolicy.setHeightForWidth(self.HyperlinkButton_4.sizePolicy().hasHeightForWidth())
        self.HyperlinkButton_4.setSizePolicy(sizePolicy)
        self.HyperlinkButton_4.setUrl(QUrl(u"https://www.yuque.com/rinlit/cw-docs-dev"))

        self.common_question.addWidget(self.HyperlinkButton_4)

        self.HyperlinkButton_9 = HyperlinkButton(self.scrollAreaWidgetContents_2)
        self.HyperlinkButton_9.setObjectName(u"HyperlinkButton_9")
        sizePolicy.setHeightForWidth(self.HyperlinkButton_9.sizePolicy().hasHeightForWidth())
        self.HyperlinkButton_9.setSizePolicy(sizePolicy)
        self.HyperlinkButton_9.setUrl(QUrl(u"https://github.com/CSES-org/CSES"))

        self.common_question.addWidget(self.HyperlinkButton_9)


        self.verticalLayout_27.addLayout(self.common_question)


        self.verticalLayout_26.addLayout(self.verticalLayout_27)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.SubtitleLabel_6 = SubtitleLabel(self.scrollAreaWidgetContents_2)
        self.SubtitleLabel_6.setObjectName(u"SubtitleLabel_6")
        self.SubtitleLabel_6.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.SubtitleLabel_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.HyperlinkButton_3 = HyperlinkButton(self.scrollAreaWidgetContents_2)
        self.HyperlinkButton_3.setObjectName(u"HyperlinkButton_3")
        sizePolicy.setHeightForWidth(self.HyperlinkButton_3.sizePolicy().hasHeightForWidth())
        self.HyperlinkButton_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.HyperlinkButton_3)

        self.HyperlinkButton_8 = HyperlinkButton(self.scrollAreaWidgetContents_2)
        self.HyperlinkButton_8.setObjectName(u"HyperlinkButton_8")
        sizePolicy.setHeightForWidth(self.HyperlinkButton_8.sizePolicy().hasHeightForWidth())
        self.HyperlinkButton_8.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.HyperlinkButton_8)

        self.HyperlinkButton_2 = HyperlinkButton(self.scrollAreaWidgetContents_2)
        self.HyperlinkButton_2.setObjectName(u"HyperlinkButton_2")
        sizePolicy.setHeightForWidth(self.HyperlinkButton_2.sizePolicy().hasHeightForWidth())
        self.HyperlinkButton_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.HyperlinkButton_2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_2)


        self.verticalLayout_26.addLayout(self.verticalLayout_28)

        self.blank_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.blank_2.setObjectName(u"blank_2")
        self.blank_2.setMinimumSize(QSize(0, 25))
        self.blank_2.setFrameShape(QFrame.StyledPanel)
        self.blank_2.setFrameShadow(QFrame.Raised)
        self.blank_2.setLineWidth(5)

        self.verticalLayout_26.addWidget(self.blank_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_2)

        self.adv_scroll.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.adv_scroll)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u5e2e\u52a9\u6587\u6863", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u9700\u8fde\u63a5\u5230\u4e92\u8054\u7f51", None))
        self.open_by_browser.setText(QCoreApplication.translate("Form", u"\u5728\u6d4f\u89c8\u5668\u4e2d\u6d4f\u89c8", None))
        self.SubtitleLabel_5.setText(QCoreApplication.translate("Form", u"\u731c\u4f60\u60f3\u95ee", None))
        self.HyperlinkButton.setText(QCoreApplication.translate("Form", u"\u5982\u4f55\u8bbe\u7f6e\u8bfe\u7a0b\u8868\uff1f", None))
        self.HyperlinkButton_7.setText(QCoreApplication.translate("Form", u"\u5982\u4f55\u5207\u6362\u4e3b\u9898\uff1f", None))
        self.HyperlinkButton_6.setText(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u7684\u65f6\u95f4\u4e0e\u94c3\u58f0\u4e0d\u7b26\u600e\u4e48\u529e\uff1f\u5982\u4f55\u8bbe\u7f6e\u65f6\u5dee\u504f\u79fb\uff1f", None))
        self.HyperlinkButton_5.setText(QCoreApplication.translate("Form", u"\u600e\u4e48\u5feb\u901f\u8bbe\u7f6e\u8c03\u4f11\u65e5\u548c\u6362\u8bfe\uff1f", None))
        self.HyperlinkButton_4.setText(QCoreApplication.translate("Form", u"\u5982\u4f55\u5f00\u53d1\u63d2\u4ef6\uff1f", None))
        self.HyperlinkButton_9.setText(QCoreApplication.translate("Form", u"\u4ec0\u4e48\u662f CSES\uff1f", None))
        self.SubtitleLabel_6.setText(QCoreApplication.translate("Form", u"\u793e\u533a", None))
        self.HyperlinkButton_3.setText(QCoreApplication.translate("Form", u"\u6211\u4eec\u7684Q\u7fa4", None))
        self.HyperlinkButton_8.setText(QCoreApplication.translate("Form", u"GitHub Discussion", None))
        self.HyperlinkButton_2.setText(QCoreApplication.translate("Form", u"Discord", None))
    # retranslateUi
