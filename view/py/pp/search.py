# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, SearchLineEdit, SmoothScrollArea, StrongBodyLabel)

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
        self.search_scroll = SmoothScrollArea(Form)
        self.search_scroll.setObjectName(u"search_scroll")
        self.search_scroll.setStyleSheet(u"background: transparent; border: none")
        self.search_scroll.setWidgetResizable(True)
        self.search_scroll.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 688, 713))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(24, 24, 24, -1)
        self.search_plugin = SearchLineEdit(self.scrollAreaWidgetContents)
        self.search_plugin.setObjectName(u"search_plugin")

        self.verticalLayout_9.addWidget(self.search_plugin)

        self.suggestions_layout = QVBoxLayout()
        self.suggestions_layout.setSpacing(3)
        self.suggestions_layout.setObjectName(u"suggestions_layout")
        self.StrongBodyLabel = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setWordWrap(True)

        self.suggestions_layout.addWidget(self.StrongBodyLabel)

        self.tags_layout = QGridLayout()
        self.tags_layout.setObjectName(u"tags_layout")
        self.tags_layout.setContentsMargins(12, 6, 12, -1)

        self.suggestions_layout.addLayout(self.tags_layout)


        self.verticalLayout_9.addLayout(self.suggestions_layout)

        self.search_plugin_grid = QGridLayout()
        self.search_plugin_grid.setObjectName(u"search_plugin_grid")

        self.verticalLayout_9.addLayout(self.search_plugin_grid)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.blank = QFrame(self.scrollAreaWidgetContents)
        self.blank.setObjectName(u"blank")
        self.blank.setMinimumSize(QSize(0, 25))
        self.blank.setFrameShape(QFrame.StyledPanel)
        self.blank.setFrameShadow(QFrame.Raised)
        self.blank.setLineWidth(5)

        self.verticalLayout_9.addWidget(self.blank)

        self.search_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.search_scroll)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_plugin.setPlaceholderText(QCoreApplication.translate("Form", u"\u641c\u7d22\u4f60\u5e0c\u671b\u67e5\u627e\u7684\u63d2\u4ef6\u3001Tag\u7b49", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u63a2\u7d22\u66f4\u591a", None))
    # retranslateUi
