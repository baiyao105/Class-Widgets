# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (CaptionLabel, DisplayLabel, IndeterminateProgressRing, ProgressBar)

class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(445, 189)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Splash.sizePolicy().hasHeightForWidth())
        Splash.setSizePolicy(sizePolicy)
        Splash.setStyleSheet(u"QWidget{ background:#ffffff; }\n"
"#logoBox{ background:#f7f7f9; border:1px solid #e9e9ec; border-radius:12px; }\n"
"#logo{ background:transparent; }")
        self.rootLayout = QVBoxLayout(Splash)
        self.rootLayout.setSpacing(12)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(18, 18, 18, 16)
        self.rightExpander_4 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.rootLayout.addItem(self.rightExpander_4)

        self.frame = QFrame(Splash)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 8px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rightExpander_3 = QSpacerItem(6, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.rightExpander_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topRow = QHBoxLayout()
        self.topRow.setSpacing(12)
        self.topRow.setObjectName(u"topRow")
        self.topRow.setContentsMargins(0, 0, -1, 0)
        self.logoBox = QFrame(self.frame)
        self.logoBox.setObjectName(u"logoBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logoBox.sizePolicy().hasHeightForWidth())
        self.logoBox.setSizePolicy(sizePolicy1)
        self.logoBox.setMinimumSize(QSize(66, 66))
        self.logoBox.setMaximumSize(QSize(66, 66))
        self.logoBox.setFrameShape(QFrame.NoFrame)
        self.logoLayout = QVBoxLayout(self.logoBox)
        self.logoLayout.setObjectName(u"logoLayout")
        self.logoLayout.setContentsMargins(8, 8, 8, 8)
        self.appInitials = QLabel(self.logoBox)
        self.appInitials.setObjectName(u"appInitials")
        self.appInitials.setMinimumSize(QSize(50, 50))
        self.appInitials.setMaximumSize(QSize(50, 50))
        self.appInitials.setPixmap(QPixmap(u":/img/logo/favicon.ico"))
        self.appInitials.setScaledContents(True)
        self.appInitials.setAlignment(Qt.AlignCenter)

        self.logoLayout.addWidget(self.appInitials)


        self.topRow.addWidget(self.logoBox)

        self.titleGrid = QGridLayout()
        self.titleGrid.setSpacing(0)
        self.titleGrid.setObjectName(u"titleGrid")
        self.titleGrid.setContentsMargins(0, 6, 0, 0)
        self.title = DisplayLabel(self.frame)
        self.title.setObjectName(u"title")
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setBold(True)
        font.setKerning(True)
        self.title.setFont(font)
        self.title.setText(u"Class Widgets")
        self.title.setWordWrap(False)
        self.title.setIndent(-1)
        self.title.setProperty("lightColor", QColor(38, 38, 38))
        self.title.setProperty("pixelFontSize", 25)

        self.titleGrid.addWidget(self.title, 0, 0, 1, 1)

        self.versionLabel = CaptionLabel(self.frame)
        self.versionLabel.setObjectName(u"versionLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.versionLabel.sizePolicy().hasHeightForWidth())
        self.versionLabel.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setBold(False)
        self.versionLabel.setFont(font1)
        self.versionLabel.setText(u"v0.0.0.0")
        self.versionLabel.setWordWrap(False)
        self.versionLabel.setProperty("lightColor", QColor(112, 112, 112, 150))
        self.versionLabel.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.versionLabel.setProperty("pixelFontSize", 12)

        self.titleGrid.addWidget(self.versionLabel, 1, 0, 1, 1)


        self.topRow.addLayout(self.titleGrid)

        self.rightExpander = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topRow.addItem(self.rightExpander)


        self.verticalLayout.addLayout(self.topRow)

        self.ringbow = QVBoxLayout()
        self.ringbow.setSpacing(4)
        self.ringbow.setObjectName(u"ringbow")
        self.progressRow = QHBoxLayout()
        self.progressRow.setSpacing(8)
        self.progressRow.setObjectName(u"progressRow")
        self.progressRow.setContentsMargins(0, 0, 0, 0)
        self.ring = IndeterminateProgressRing(self.frame)
        self.ring.setObjectName(u"ring")
        self.ring.setMinimumSize(QSize(18, 18))
        self.ring.setMaximumSize(QSize(18, 18))
        self.ring.setTextVisible(False)
        self.ring.setStrokeWidth(3)

        self.progressRow.addWidget(self.ring)

        self.statusLabel = CaptionLabel(self.frame)
        self.statusLabel.setObjectName(u"statusLabel")

        self.progressRow.addWidget(self.statusLabel)


        self.ringbow.addLayout(self.progressRow)

        self.statusBar = ProgressBar(self.frame)
        self.statusBar.setObjectName(u"statusBar")

        self.ringbow.addWidget(self.statusBar)


        self.verticalLayout.addLayout(self.ringbow)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.rightExpander_2 = QSpacerItem(20, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.rightExpander_2)


        self.rootLayout.addWidget(self.frame)

        self.rightExpander_5 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.rootLayout.addItem(self.rightExpander_5)


        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QCoreApplication.translate("Splash", u"Splash", None))
        self.statusLabel.setText(QCoreApplication.translate("Splash", u"\u6b63\u5728\u542f\u52a8...", None))
    # retranslateUi
