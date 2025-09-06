# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'latests.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, SmoothScrollArea, SubtitleLabel, TitleLabel)

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
        self.latest_scroll = SmoothScrollArea(Form)
        self.latest_scroll.setObjectName(u"latest_scroll")
        self.latest_scroll.setStyleSheet(u"background: transparent; border: none")
        self.latest_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 688, 713))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(24, 24, 24, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TitleLabel = TitleLabel(self.scrollAreaWidgetContents)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.TitleLabel)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.SubtitleLabel_3)

        self.all_plugin_grid = QGridLayout()
        self.all_plugin_grid.setObjectName(u"all_plugin_grid")

        self.verticalLayout_9.addLayout(self.all_plugin_grid)

        self.BodyLabel = BodyLabel(self.scrollAreaWidgetContents)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setAlignment(Qt.AlignCenter)
        self.BodyLabel.setProperty("lightColor", QColor(125, 125, 125))
        self.BodyLabel.setProperty("darkColor", QColor(211, 211, 211))
        self.BodyLabel.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.BodyLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.blank = QFrame(self.scrollAreaWidgetContents)
        self.blank.setObjectName(u"blank")
        self.blank.setMinimumSize(QSize(0, 25))
        self.blank.setFrameShape(QFrame.StyledPanel)
        self.blank.setFrameShadow(QFrame.Raised)
        self.blank.setLineWidth(5)

        self.verticalLayout_9.addWidget(self.blank)

        self.latest_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.latest_scroll)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u5206\u7c7b", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u6240\u6709\u63d2\u4ef6", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"Coming Soon~", None))
    # retranslateUi
