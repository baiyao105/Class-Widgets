# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
    QListWidgetItem, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, HorizontalFlipView, HorizontalPipsPager, IndeterminateProgressRing,
    SmoothScrollArea, SubtitleLabel, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(688, 777)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.home_scroll = SmoothScrollArea(Form)
        self.home_scroll.setObjectName(u"home_scroll")
        self.home_scroll.setStyleSheet(u"background: transparent; border: none")
        self.home_scroll.setWidgetResizable(True)
        self.home_scroll.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 688, 818))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(24, 24, 24, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TitleLabel = TitleLabel(self.scrollAreaWidgetContents)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.TitleLabel)

        self.time_today_label = TitleLabel(self.scrollAreaWidgetContents)
        self.time_today_label.setObjectName(u"time_today_label")
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(18)
        font.setBold(True)
        self.time_today_label.setFont(font)
        self.time_today_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.time_today_label.setProperty("lightColor", QColor(93, 93, 93))
        self.time_today_label.setProperty("darkColor", QColor(209, 209, 209))
        self.time_today_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.time_today_label)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.banner_view = HorizontalFlipView(self.scrollAreaWidgetContents)
        self.banner_view.setObjectName(u"banner_view")
        self.banner_view.setMinimumSize(QSize(480, 450))
        self.banner_view.setMaximumSize(QSize(16777215, 450))

        self.verticalLayout_9.addWidget(self.banner_view)

        self.pagerLayout = QHBoxLayout()
        self.pagerLayout.setObjectName(u"pagerLayout")
        self.banner_pager = HorizontalPipsPager(self.scrollAreaWidgetContents)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        QListWidgetItem(self.banner_pager)
        self.banner_pager.setObjectName(u"banner_pager")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.banner_pager.sizePolicy().hasHeightForWidth())
        self.banner_pager.setSizePolicy(sizePolicy1)

        self.pagerLayout.addWidget(self.banner_pager)


        self.verticalLayout_9.addLayout(self.pagerLayout)

        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.SubtitleLabel_3)

        self.rec_plugin_grid = QGridLayout()
        self.rec_plugin_grid.setObjectName(u"rec_plugin_grid")

        self.verticalLayout_9.addLayout(self.rec_plugin_grid)

        self.progressRingLayout = QHBoxLayout()
        self.progressRingLayout.setObjectName(u"progressRingLayout")
        self.progressRingLayout.setContentsMargins(0, 12, -1, 12)
        self.load_plugin_progress = IndeterminateProgressRing(self.scrollAreaWidgetContents)
        self.load_plugin_progress.setObjectName(u"load_plugin_progress")
        self.load_plugin_progress.setMinimumSize(QSize(45, 45))
        self.load_plugin_progress.setMaximumSize(QSize(45, 45))

        self.progressRingLayout.addWidget(self.load_plugin_progress)


        self.verticalLayout_9.addLayout(self.progressRingLayout)

        self.tips = BodyLabel(self.scrollAreaWidgetContents)
        self.tips.setObjectName(u"tips")
        self.tips.setAlignment(Qt.AlignCenter)
        self.tips.setWordWrap(True)
        self.tips.setProperty("lightColor", QColor(125, 125, 125))
        self.tips.setProperty("darkColor", QColor(211, 211, 211))

        self.verticalLayout_9.addWidget(self.tips)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.blank = QFrame(self.scrollAreaWidgetContents)
        self.blank.setObjectName(u"blank")
        self.blank.setMinimumSize(QSize(0, 25))
        self.blank.setFrameShape(QFrame.StyledPanel)
        self.blank.setFrameShadow(QFrame.Raised)
        self.blank.setLineWidth(5)

        self.verticalLayout_9.addWidget(self.blank)

        self.home_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.home_scroll)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u4eca\u5929", None))
        self.time_today_label.setText(QCoreApplication.translate("Form", u"11\u670845\u65e5 \u5468\u65e5", None))

        __sortingEnabled = self.banner_pager.isSortingEnabled()
        self.banner_pager.setSortingEnabled(False)
        self.banner_pager.setSortingEnabled(__sortingEnabled)

        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u63a8\u8350\u63d2\u4ef6", None))
        self.tips.setText(QCoreApplication.translate("Form", u"\u8fd9\u5c31\u5230\u5e95\u4e86\u5417\u2026\u2026(\u3063 \u00b0\u0414 \u00b0;)\u3063", None))
    # retranslateUi
