# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plugin_mgr.ui'
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

from qfluentwidgets import (CaptionLabel, CardWidget, ComboBox, LineEdit,
    PushButton, SearchLineEdit, SmoothScrollArea, SpinBox,
    StrongBodyLabel, SubtitleLabel, SwitchButton, TitleLabel,
    ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(791, 982)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.pm_scroll = SmoothScrollArea(Form)
        self.pm_scroll.setObjectName(u"pm_scroll")
        self.pm_scroll.setStyleSheet(u"background: transparent; border: none")
        self.pm_scroll.setWidgetResizable(True)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 743, 876))
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SubtitleLabel = SubtitleLabel(self.widget)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.SubtitleLabel)

        self.plugin_count_label = CaptionLabel(self.widget)
        self.plugin_count_label.setObjectName(u"plugin_count_label")
        self.plugin_count_label.setAlignment(Qt.AlignCenter)
        self.plugin_count_label.setProperty("lightColor", QColor(96, 96, 96))
        self.plugin_count_label.setProperty("darkColor", QColor(210, 210, 210))
        self.plugin_count_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.plugin_count_label)

        self.CaptionLabel_3 = CaptionLabel(self.widget)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.CaptionLabel_3.setWordWrap(True)
        self.CaptionLabel_3.setProperty("lightColor", QColor(96, 96, 96))
        self.CaptionLabel_3.setProperty("darkColor", QColor(210, 210, 210))

        self.horizontalLayout.addWidget(self.CaptionLabel_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.CardWidget_10 = CardWidget(self.widget)
        self.CardWidget_10.setObjectName(u"CardWidget_10")
        self.CardWidget_10.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_10 = QHBoxLayout(self.CardWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.StrongBodyLabel_7 = StrongBodyLabel(self.CardWidget_10)
        self.StrongBodyLabel_7.setObjectName(u"StrongBodyLabel_7")
        self.StrongBodyLabel_7.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.StrongBodyLabel_7)

        self.CaptionLabel_9 = CaptionLabel(self.CardWidget_10)
        self.CaptionLabel_9.setObjectName(u"CaptionLabel_9")
        self.CaptionLabel_9.setWordWrap(True)
        self.CaptionLabel_9.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_9.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_12.addWidget(self.CaptionLabel_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_12)

        self.open_plugin_plaza_2 = PushButton(self.CardWidget_10)
        self.open_plugin_plaza_2.setObjectName(u"open_plugin_plaza_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_plugin_plaza_2.sizePolicy().hasHeightForWidth())
        self.open_plugin_plaza_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.open_plugin_plaza_2)


        self.verticalLayout_3.addWidget(self.CardWidget_10)

        self.verticalSpacer_for_note_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_for_note_2)

        self.CardWidget_search = CardWidget(self.widget)
        self.CardWidget_search.setObjectName(u"CardWidget_search")
        self.CardWidget_search.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_search = QHBoxLayout(self.CardWidget_search)
        self.horizontalLayout_search.setObjectName(u"horizontalLayout_search")
        self.horizontalLayout_search.setContentsMargins(16, 16, 16, 16)
        self.plugin_search = SearchLineEdit(self.CardWidget_search)
        self.plugin_search.setObjectName(u"plugin_search")

        self.horizontalLayout_search.addWidget(self.plugin_search)

        self.filter_combo = ComboBox(self.CardWidget_search)
        self.filter_combo.setObjectName(u"filter_combo")
        sizePolicy.setHeightForWidth(self.filter_combo.sizePolicy().hasHeightForWidth())
        self.filter_combo.setSizePolicy(sizePolicy)
        self.filter_combo.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_search.addWidget(self.filter_combo)

        self.refresh_btn = ToolButton(self.CardWidget_search)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout_search.addWidget(self.refresh_btn)


        self.verticalLayout_3.addWidget(self.CardWidget_search)

        self.plugin_card_layout = QVBoxLayout()
        self.plugin_card_layout.setSpacing(3)
        self.plugin_card_layout.setObjectName(u"plugin_card_layout")
        self.plugin_card_layout.setProperty("minimumSize", QSize(0, 200))
        self.plugin_card_layout.setContentsMargins(16, -1, 16, -1)
        self.tips_plugin_empty = CaptionLabel(self.widget)
        self.tips_plugin_empty.setObjectName(u"tips_plugin_empty")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tips_plugin_empty.sizePolicy().hasHeightForWidth())
        self.tips_plugin_empty.setSizePolicy(sizePolicy1)
        self.tips_plugin_empty.setMinimumSize(QSize(0, 150))
        self.tips_plugin_empty.setStyleSheet(u"FluentLabelBase {\n"
"\n"
"    color: black;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"HyperlinkLabel {\n"
"\n"
"    color: #009faa;\n"
"\n"
"    border: none;\n"
"\n"
"    background-color: transparent;\n"
"\n"
"    text-align: left;\n"
"\n"
"    padding: 0;\n"
"\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"\n"
"    text-decoration: underline;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"\n"
"    text-decoration: none;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"HyperlinkLabel:hover {\n"
"\n"
"    color: #007780;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"HyperlinkLabel:pressed {\n"
"\n"
"    color: #00a7b3;\n"
"\n"
"}\n"
"FluentLabelBase{color:#7d000000}")
        self.tips_plugin_empty.setAlignment(Qt.AlignCenter)
        self.tips_plugin_empty.setProperty("lightColor", QColor(0, 0, 0, 125))
        self.tips_plugin_empty.setProperty("darkColor", QColor(255, 255, 255, 155))
        self.tips_plugin_empty.setProperty("pixelFontSize", 14)
        self.tips_plugin_empty.setWordWrap(True)

        self.plugin_card_layout.addWidget(self.tips_plugin_empty)


        self.verticalLayout_3.addLayout(self.plugin_card_layout)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SubtitleLabel_2 = SubtitleLabel(self.widget)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.SubtitleLabel_2)

        self.CardWidget_8 = CardWidget(self.widget)
        self.CardWidget_8.setObjectName(u"CardWidget_8")
        self.CardWidget_8.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.StrongBodyLabel_5 = StrongBodyLabel(self.CardWidget_8)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")
        self.StrongBodyLabel_5.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.StrongBodyLabel_5)

        self.CaptionLabel_7 = CaptionLabel(self.CardWidget_8)
        self.CaptionLabel_7.setObjectName(u"CaptionLabel_7")
        self.CaptionLabel_7.setWordWrap(True)
        self.CaptionLabel_7.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_7.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_10.addWidget(self.CaptionLabel_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.open_plugin_folder = PushButton(self.CardWidget_8)
        self.open_plugin_folder.setObjectName(u"open_plugin_folder")
        sizePolicy.setHeightForWidth(self.open_plugin_folder.sizePolicy().hasHeightForWidth())
        self.open_plugin_folder.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.open_plugin_folder)


        self.verticalLayout_4.addWidget(self.CardWidget_8)

        self.CardWidget_7 = CardWidget(self.widget)
        self.CardWidget_7.setObjectName(u"CardWidget_7")
        self.CardWidget_7.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.CardWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.StrongBodyLabel_4 = StrongBodyLabel(self.CardWidget_7)
        self.StrongBodyLabel_4.setObjectName(u"StrongBodyLabel_4")
        self.StrongBodyLabel_4.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.StrongBodyLabel_4)

        self.CaptionLabel_6 = CaptionLabel(self.CardWidget_7)
        self.CaptionLabel_6.setObjectName(u"CaptionLabel_6")
        self.CaptionLabel_6.setWordWrap(True)
        self.CaptionLabel_6.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_6.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_8.addWidget(self.CaptionLabel_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.open_plugin_plaza = PushButton(self.CardWidget_7)
        self.open_plugin_plaza.setObjectName(u"open_plugin_plaza")
        sizePolicy.setHeightForWidth(self.open_plugin_plaza.sizePolicy().hasHeightForWidth())
        self.open_plugin_plaza.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.open_plugin_plaza)


        self.verticalLayout_4.addWidget(self.CardWidget_7)

        self.CardWidget_import = CardWidget(self.widget)
        self.CardWidget_import.setObjectName(u"CardWidget_import")
        self.CardWidget_import.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_import = QHBoxLayout(self.CardWidget_import)
        self.horizontalLayout_import.setObjectName(u"horizontalLayout_import")
        self.horizontalLayout_import.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_import = QVBoxLayout()
        self.verticalLayout_import.setSpacing(0)
        self.verticalLayout_import.setObjectName(u"verticalLayout_import")
        self.StrongBodyLabel_import = StrongBodyLabel(self.CardWidget_import)
        self.StrongBodyLabel_import.setObjectName(u"StrongBodyLabel_import")
        self.StrongBodyLabel_import.setWordWrap(True)

        self.verticalLayout_import.addWidget(self.StrongBodyLabel_import)

        self.CaptionLabel_import = CaptionLabel(self.CardWidget_import)
        self.CaptionLabel_import.setObjectName(u"CaptionLabel_import")
        self.CaptionLabel_import.setWordWrap(True)
        self.CaptionLabel_import.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_import.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_import.addWidget(self.CaptionLabel_import)


        self.horizontalLayout_import.addLayout(self.verticalLayout_import)

        self.import_plugin_btn = PushButton(self.CardWidget_import)
        self.import_plugin_btn.setObjectName(u"import_plugin_btn")
        sizePolicy.setHeightForWidth(self.import_plugin_btn.sizePolicy().hasHeightForWidth())
        self.import_plugin_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_import.addWidget(self.import_plugin_btn)


        self.verticalLayout_4.addWidget(self.CardWidget_import)


        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SubtitleLabel_3 = SubtitleLabel(self.widget)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.SubtitleLabel_3)

        self.CardWidget_2 = CardWidget(self.widget)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        self.StrongBodyLabel_2.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.StrongBodyLabel_2)

        self.CaptionLabel_4 = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel_4.setObjectName(u"CaptionLabel_4")
        self.CaptionLabel_4.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_4.setProperty("darkColor", QColor(255, 255, 255, 200))
        self.CaptionLabel_4.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.CaptionLabel_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.switch_safe_plugin = SwitchButton(self.CardWidget_2)
        self.switch_safe_plugin.setObjectName(u"switch_safe_plugin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.switch_safe_plugin.sizePolicy().hasHeightForWidth())
        self.switch_safe_plugin.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.switch_safe_plugin)


        self.verticalLayout_5.addWidget(self.CardWidget_2)

        self.CardWidget_9 = CardWidget(self.widget)
        self.CardWidget_9.setObjectName(u"CardWidget_9")
        self.CardWidget_9.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_9 = QHBoxLayout(self.CardWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_9)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        self.StrongBodyLabel_6.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.StrongBodyLabel_6)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_9)
        self.CaptionLabel_8.setObjectName(u"CaptionLabel_8")
        self.CaptionLabel_8.setWordWrap(True)
        self.CaptionLabel_8.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_8.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_11.addWidget(self.CaptionLabel_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_11)

        self.auto_delay = SpinBox(self.CardWidget_9)
        self.auto_delay.setObjectName(u"auto_delay")
        sizePolicy.setHeightForWidth(self.auto_delay.sizePolicy().hasHeightForWidth())
        self.auto_delay.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.auto_delay)


        self.verticalLayout_5.addWidget(self.CardWidget_9)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.pm_scroll.setWidget(self.widget)

        self.verticalLayout_2.addWidget(self.pm_scroll)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u63d2\u4ef6", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u63d2\u4ef6\u7ba1\u7406", None))
        self.plugin_count_label.setText(QCoreApplication.translate("Form", u"\u5df2\u5b89\u88c5 0 \u4e2a\u63d2\u4ef6", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"*\u5bf9\u63d2\u4ef6\u7684\u4efb\u610f\u64cd\u4f5c\u5c06\u5728\u91cd\u542f\u540e\u751f\u6548\u3002", None))
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("Form", u"\u5728\u201c\u63d2\u4ef6\u5e7f\u573a\u201d\u4e2d\u68c0\u67e5\u66f4\u65b0", None))
        self.CaptionLabel_9.setText(QCoreApplication.translate("Form", u"\u5c06\u8df3\u8f6c\u81f3\u201c\u63d2\u4ef6\u5e7f\u573a\u201d\u4ee5\u68c0\u67e5\u63d2\u4ef6\u7684\u66f4\u65b0\u72b6\u6001", None))
        self.open_plugin_plaza_2.setText(QCoreApplication.translate("Form", u"\u5728\u201c\u63d2\u4ef6\u5e7f\u573a\u201d\u68c0\u67e5", None))
        self.plugin_search.setPlaceholderText(QCoreApplication.translate("Form", u"\u641c\u7d22\u63d2\u4ef6\u540d\u79f0\u3001\u4f5c\u8005\u6216\u63cf\u8ff0...", None))
#if QT_CONFIG(tooltip)
        self.refresh_btn.setToolTip(QCoreApplication.translate("Form", u"\u5237\u65b0\u63d2\u4ef6\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_btn.setText("")
        self.tips_plugin_empty.setText(QCoreApplication.translate("Form", u"\u8fd8\u672a\u6dfb\u52a0\u4efb\u4f55\u63d2\u4ef6", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u63d2\u4ef6", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", u"\u7ba1\u7406\u63d2\u4ef6\u6587\u4ef6\u5939", None))
        self.CaptionLabel_7.setText(QCoreApplication.translate("Form", u"\u53ef\u5728\u6b64\u6587\u4ef6\u5939\u6dfb\u52a0\u3001\u5220\u9664\u548c\u4fee\u6539\u60a8\u6240\u5b89\u88c5\u7684\u63d2\u4ef6", None))
        self.open_plugin_folder.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u201c\u8d44\u6e90\u7ba1\u7406\u5668\u201d\u6253\u5f00", None))
        self.StrongBodyLabel_4.setText(QCoreApplication.translate("Form", u"\u5728\u201c\u63d2\u4ef6\u5e7f\u573a\u201d\u4e2d\u5bfb\u627e", None))
        self.CaptionLabel_6.setText(QCoreApplication.translate("Form", u"\u5c06\u8df3\u8f6c\u81f3\u201c\u63d2\u4ef6\u5e7f\u573a\u201d", None))
        self.open_plugin_plaza.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u201c\u63d2\u4ef6\u5e7f\u573a\u201d", None))
        self.StrongBodyLabel_import.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165\u672c\u5730\u63d2\u4ef6", None))
        self.CaptionLabel_import.setText(QCoreApplication.translate("Form", u"\u4ece\u672c\u5730\u6587\u4ef6\u5bfc\u5165\u63d2\u4ef6\u5305 (\u652f\u6301.zip\u683c\u5f0f\u4e0e\u89e3\u538b\u540e\u7684\u63d2\u4ef6)", None))
        self.import_plugin_btn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5bfc\u5165", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u5176\u4ed6", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"\u5b89\u5168\u6a21\u5f0f\u52a0\u8f7d\u63d2\u4ef6", None))
        self.CaptionLabel_4.setText(QCoreApplication.translate("Form", u"\u5f53\u63d2\u4ef6\u51fa\u73b0\u9519\u8bef\u65f6\u81ea\u52a8\u7981\u7528\u63d2\u4ef6\u52a0\u8f7d", None))
        self.switch_safe_plugin.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.switch_safe_plugin.setOnText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.switch_safe_plugin.setOffText(QCoreApplication.translate("Form", u"\u5173", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"\u63d2\u4ef6\u81ea\u52a8\u5316\u6267\u884c\u5ef6\u8fdf", None))
        self.CaptionLabel_8.setText(QCoreApplication.translate("Form", u"\u5f53\u63d2\u4ef6\u6267\u884c\u81ea\u52a8\u5316\u64cd\u4f5c\u65f6\uff0c\u9700\u7b49\u5f85\u7684\u65f6\u95f4\uff08\u5355\u4f4d\uff1a\u79d2\uff09", None))
    # retranslateUi
