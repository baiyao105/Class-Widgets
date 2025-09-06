# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QSizePolicy, QSpacerItem, QTableWidgetItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (ComboBox, SubtitleLabel, TableWidget, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(715, 636)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.subtitle_file = SubtitleLabel(Form)
        self.subtitle_file.setObjectName(u"subtitle_file")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtitle_file.sizePolicy().hasHeightForWidth())
        self.subtitle_file.setSizePolicy(sizePolicy)
        self.subtitle_file.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.subtitle_file)

        self.pre_week_type_combo = ComboBox(Form)
        self.pre_week_type_combo.setObjectName(u"pre_week_type_combo")

        self.horizontalLayout_5.addWidget(self.pre_week_type_combo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.schedule_view = TableWidget(Form)
        self.schedule_view.setObjectName(u"schedule_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.schedule_view.sizePolicy().hasHeightForWidth())
        self.schedule_view.setSizePolicy(sizePolicy1)
        self.schedule_view.setStyleSheet(u"QTableView {\n"
"    background: transparent;\n"
"    outline: none;\n"
"    border: none;\n"
"    /* font: 13px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    selection-background-color: transparent;\n"
"    alternate-background-color: transparent;\n"
"}\n"
"\n"
"QTableView[isBorderVisible=true] {\n"
"    border: none;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    background: transparent;\n"
"    border: 0px;\n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"\n"
"QTableView::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: transparent;\n"
"    color: rgb(96, 96, 96);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 15);\n"
"    font: 13px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"}\n"
"\n"
"QHe"
                        "aderView::section:horizontal {\n"
"    border-left: none;\n"
"    height: 33px;\n"
"}\n"
"\n"
"QTableView[isBorderVisible=true] QHeaderView::section:horizontal {\n"
"    border-top: none;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:last {\n"
"    border-right: none;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    border-top: none;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;\n"
"    image: url(:/qfluentwidgets/images/table_view/Down_black.svg);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;\n"
"    image: url(:/qfluentwidgets/images/table_view/Up_black.svg);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgba(0, 0, 0, 15);\n"
"}\n"
"\n"
"QTableCornerButton::s"
                        "ection:pressed {\n"
"    background-color: rgba(0, 0, 0, 12);\n"
"}")
        self.schedule_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.schedule_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.schedule_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.schedule_view.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.schedule_view.setTextElideMode(Qt.ElideMiddle)
        self.schedule_view.setWordWrap(False)
        self.schedule_view.verticalHeader().setMinimumSectionSize(50)
        self.schedule_view.verticalHeader().setDefaultSectionSize(50)

        self.verticalLayout_2.addWidget(self.schedule_view)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b\u8868", None))
        self.subtitle_file.setText(QCoreApplication.translate("Form", u"\u9884\u89c8", None))
    # retranslateUi
