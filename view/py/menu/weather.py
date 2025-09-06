# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
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
    QLabel, QLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (CaptionLabel, CardWidget, ComboBox, DisplayLabel,
    ElevatedCardWidget, LineEdit, ProgressBar, PushButton,
    SimpleCardWidget, SmoothScrollArea, SpinBox, StrongBodyLabel,
    SubtitleLabel, TitleLabel, ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(727, 1252)
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

        self.adv_scroll = SmoothScrollArea(Form)
        self.adv_scroll.setObjectName(u"adv_scroll")
        self.adv_scroll.setStyleSheet(u"background: transparent; border: none")
        self.adv_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 679, 1173))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(25, 25))
        self.label.setPixmap(QPixmap(u":/svg/weather/mappin.svg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.teto_x = SubtitleLabel(self.scrollAreaWidgetContents)
        self.teto_x.setObjectName(u"teto_x")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.teto_x.sizePolicy().hasHeightForWidth())
        self.teto_x.setSizePolicy(sizePolicy2)
        self.teto_x.setWordWrap(False)

        self.gridLayout.addWidget(self.teto_x, 0, 0, 1, 1)

        self.weather_re_time = CaptionLabel(self.scrollAreaWidgetContents)
        self.weather_re_time.setObjectName(u"weather_re_time")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.weather_re_time.sizePolicy().hasHeightForWidth())
        self.weather_re_time.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(10)
        font.setBold(False)
        self.weather_re_time.setFont(font)
        self.weather_re_time.setWordWrap(False)
        self.weather_re_time.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.weather_re_time.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.gridLayout.addWidget(self.weather_re_time, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_4 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.ToolButton = ToolButton(self.scrollAreaWidgetContents)
        self.ToolButton.setObjectName(u"ToolButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(50)
        sizePolicy4.setVerticalStretch(50)
        sizePolicy4.setHeightForWidth(self.ToolButton.sizePolicy().hasHeightForWidth())
        self.ToolButton.setSizePolicy(sizePolicy4)
        self.ToolButton.setMinimumSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.ToolButton)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.current_weather_spacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.current_weather_spacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.daily_forecast_layout = QVBoxLayout()
        self.daily_forecast_layout.setSpacing(8)
        self.daily_forecast_layout.setObjectName(u"daily_forecast_layout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(100, 100))
        self.label_2.setPixmap(QPixmap(u":/svg/weather/0.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.current_temperature_4 = DisplayLabel(self.scrollAreaWidgetContents)
        self.current_temperature_4.setObjectName(u"current_temperature_4")
        self.current_temperature_4.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.current_temperature_4)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.current_weather_info_4 = QVBoxLayout()
        self.current_weather_info_4.setSpacing(4)
        self.current_weather_info_4.setObjectName(u"current_weather_info_4")
        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.current_weather_info_4.addItem(self.verticalSpacer_2)

        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setWordWrap(False)

        self.current_weather_info_4.addWidget(self.SubtitleLabel_3, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.current_feels_like_2 = CaptionLabel(self.scrollAreaWidgetContents)
        self.current_feels_like_2.setObjectName(u"current_feels_like_2")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.current_feels_like_2.setFont(font1)
        self.current_feels_like_2.setWordWrap(True)
        self.current_feels_like_2.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.current_feels_like_2.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.current_weather_info_4.addWidget(self.current_feels_like_2)

        self.current_weather_spacer_7 = QSpacerItem(5, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.current_weather_info_4.addItem(self.current_weather_spacer_7)


        self.horizontalLayout_5.addLayout(self.current_weather_info_4)

        self.current_weather_spacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.current_weather_spacer_5)


        self.daily_forecast_layout.addLayout(self.horizontalLayout_5)

        self.details_cards_layout_2 = QHBoxLayout()
        self.details_cards_layout_2.setSpacing(6)
        self.details_cards_layout_2.setObjectName(u"details_cards_layout_2")
        self.details_cards_layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.details_cards_layout_2.setContentsMargins(20, 0, 20, 0)
        self.wind_card = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.wind_card.setObjectName(u"wind_card")
        sizePolicy5.setHeightForWidth(self.wind_card.sizePolicy().hasHeightForWidth())
        self.wind_card.setSizePolicy(sizePolicy5)
        self.wind_card.setMinimumSize(QSize(0, 60))
        self.current_weather_layout_inner_3 = QHBoxLayout(self.wind_card)
        self.current_weather_layout_inner_3.setSpacing(20)
        self.current_weather_layout_inner_3.setObjectName(u"current_weather_layout_inner_3")
        self.current_weather_layout_inner_3.setContentsMargins(24, 24, 24, 24)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.wind_label = QLabel(self.wind_card)
        self.wind_label.setObjectName(u"wind_label")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.wind_label.setFont(font2)
        self.wind_label.setStyleSheet(u"color: rgba(120, 120, 120, 180);\n"
"font-weight: bold;")
        self.wind_label.setTextFormat(Qt.PlainText)
        self.wind_label.setAlignment(Qt.AlignCenter)
        self.wind_label.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.wind_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.progressBar = ProgressBar(self.wind_card)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMinimumSize(QSize(0, 5))
        self.progressBar.setMaximumSize(QSize(50, 5))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setUseAni(True)
        self.progressBar.setVal(0.000000000000000)

        self.verticalLayout_34.addWidget(self.progressBar, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_7.addLayout(self.verticalLayout_34)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.wind_value = StrongBodyLabel(self.wind_card)
        self.wind_value.setObjectName(u"wind_value")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.wind_value.setFont(font3)
        self.wind_value.setWordWrap(False)

        self.verticalLayout_30.addWidget(self.wind_value, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addLayout(self.verticalLayout_30)


        self.current_weather_layout_inner_3.addLayout(self.verticalLayout_7)


        self.details_cards_layout_2.addWidget(self.wind_card)

        self.humidity_card = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.humidity_card.setObjectName(u"humidity_card")
        sizePolicy5.setHeightForWidth(self.humidity_card.sizePolicy().hasHeightForWidth())
        self.humidity_card.setSizePolicy(sizePolicy5)
        self.humidity_card.setMinimumSize(QSize(0, 60))
        self.current_weather_layout_inner_4 = QHBoxLayout(self.humidity_card)
        self.current_weather_layout_inner_4.setSpacing(20)
        self.current_weather_layout_inner_4.setObjectName(u"current_weather_layout_inner_4")
        self.current_weather_layout_inner_4.setContentsMargins(24, 24, 24, 24)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.humidity_label = QLabel(self.humidity_card)
        self.humidity_label.setObjectName(u"humidity_label")
        self.humidity_label.setFont(font2)
        self.humidity_label.setStyleSheet(u"color: rgba(120, 120, 120, 180);\n"
"font-weight: bold;")
        self.humidity_label.setTextFormat(Qt.PlainText)
        self.humidity_label.setAlignment(Qt.AlignCenter)
        self.humidity_label.setWordWrap(True)

        self.verticalLayout_35.addWidget(self.humidity_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.progressBar_2 = ProgressBar(self.humidity_card)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy1.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy1)
        self.progressBar_2.setMinimumSize(QSize(0, 5))
        self.progressBar_2.setMaximumSize(QSize(50, 5))
        self.progressBar_2.setStyleSheet(u"")
        self.progressBar_2.setOrientation(Qt.Horizontal)
        self.progressBar_2.setUseAni(True)
        self.progressBar_2.setVal(0.000000000000000)

        self.verticalLayout_35.addWidget(self.progressBar_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_10.addLayout(self.verticalLayout_35)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.humidity_value = StrongBodyLabel(self.humidity_card)
        self.humidity_value.setObjectName(u"humidity_value")
        self.humidity_value.setFont(font3)
        self.humidity_value.setAlignment(Qt.AlignCenter)
        self.humidity_value.setWordWrap(False)

        self.verticalLayout_15.addWidget(self.humidity_value)


        self.verticalLayout_10.addLayout(self.verticalLayout_15)


        self.current_weather_layout_inner_4.addLayout(self.verticalLayout_10)


        self.details_cards_layout_2.addWidget(self.humidity_card)

        self.visibility_card = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.visibility_card.setObjectName(u"visibility_card")
        sizePolicy5.setHeightForWidth(self.visibility_card.sizePolicy().hasHeightForWidth())
        self.visibility_card.setSizePolicy(sizePolicy5)
        self.visibility_card.setMinimumSize(QSize(0, 60))
        self.current_weather_layout_inner_5 = QHBoxLayout(self.visibility_card)
        self.current_weather_layout_inner_5.setSpacing(20)
        self.current_weather_layout_inner_5.setObjectName(u"current_weather_layout_inner_5")
        self.current_weather_layout_inner_5.setContentsMargins(24, 24, 24, 24)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.visibility_label = QLabel(self.visibility_card)
        self.visibility_label.setObjectName(u"visibility_label")
        self.visibility_label.setFont(font2)
        self.visibility_label.setStyleSheet(u"color: rgba(120, 120, 120, 180);\n"
"font-weight: bold;")
        self.visibility_label.setTextFormat(Qt.PlainText)
        self.visibility_label.setAlignment(Qt.AlignCenter)
        self.visibility_label.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.visibility_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.progressBar_3 = ProgressBar(self.visibility_card)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy1.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy1)
        self.progressBar_3.setMinimumSize(QSize(0, 5))
        self.progressBar_3.setMaximumSize(QSize(50, 5))
        self.progressBar_3.setStyleSheet(u"")
        self.progressBar_3.setOrientation(Qt.Horizontal)
        self.progressBar_3.setUseAni(True)
        self.progressBar_3.setVal(0.000000000000000)

        self.verticalLayout_36.addWidget(self.progressBar_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_17.addLayout(self.verticalLayout_36)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.visibility_value = StrongBodyLabel(self.visibility_card)
        self.visibility_value.setObjectName(u"visibility_value")
        self.visibility_value.setFont(font3)
        self.visibility_value.setAlignment(Qt.AlignCenter)
        self.visibility_value.setWordWrap(False)

        self.verticalLayout_37.addWidget(self.visibility_value)


        self.verticalLayout_17.addLayout(self.verticalLayout_37)


        self.current_weather_layout_inner_5.addLayout(self.verticalLayout_17)


        self.details_cards_layout_2.addWidget(self.visibility_card)

        self.pressure_card = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.pressure_card.setObjectName(u"pressure_card")
        sizePolicy5.setHeightForWidth(self.pressure_card.sizePolicy().hasHeightForWidth())
        self.pressure_card.setSizePolicy(sizePolicy5)
        self.pressure_card.setMinimumSize(QSize(0, 60))
        self.current_weather_layout_inner_7 = QHBoxLayout(self.pressure_card)
        self.current_weather_layout_inner_7.setSpacing(20)
        self.current_weather_layout_inner_7.setObjectName(u"current_weather_layout_inner_7")
        self.current_weather_layout_inner_7.setContentsMargins(24, 24, 24, 24)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.pressure_label_2 = QLabel(self.pressure_card)
        self.pressure_label_2.setObjectName(u"pressure_label_2")
        self.pressure_label_2.setFont(font2)
        self.pressure_label_2.setStyleSheet(u"color: rgba(120, 120, 120, 180);\n"
"font-weight: bold;")
        self.pressure_label_2.setTextFormat(Qt.PlainText)
        self.pressure_label_2.setAlignment(Qt.AlignCenter)
        self.pressure_label_2.setWordWrap(True)

        self.verticalLayout_40.addWidget(self.pressure_label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.progressBar_5 = ProgressBar(self.pressure_card)
        self.progressBar_5.setObjectName(u"progressBar_5")
        sizePolicy1.setHeightForWidth(self.progressBar_5.sizePolicy().hasHeightForWidth())
        self.progressBar_5.setSizePolicy(sizePolicy1)
        self.progressBar_5.setMinimumSize(QSize(0, 5))
        self.progressBar_5.setMaximumSize(QSize(50, 5))
        self.progressBar_5.setStyleSheet(u"")
        self.progressBar_5.setOrientation(Qt.Horizontal)
        self.progressBar_5.setUseAni(True)
        self.progressBar_5.setVal(0.000000000000000)

        self.verticalLayout_40.addWidget(self.progressBar_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_13.addLayout(self.verticalLayout_40)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.pressure_value_2 = StrongBodyLabel(self.pressure_card)
        self.pressure_value_2.setObjectName(u"pressure_value_2")
        self.pressure_value_2.setFont(font3)
        self.pressure_value_2.setAlignment(Qt.AlignCenter)
        self.pressure_value_2.setWordWrap(False)

        self.verticalLayout_41.addWidget(self.pressure_value_2)


        self.verticalLayout_13.addLayout(self.verticalLayout_41)


        self.current_weather_layout_inner_7.addLayout(self.verticalLayout_13)


        self.details_cards_layout_2.addWidget(self.pressure_card)


        self.daily_forecast_layout.addLayout(self.details_cards_layout_2)


        self.verticalLayout_5.addLayout(self.daily_forecast_layout)


        self.verticalLayout_21.addLayout(self.verticalLayout_5)

        self.weather_alerts_section = QVBoxLayout()
        self.weather_alerts_section.setSpacing(10)
        self.weather_alerts_section.setObjectName(u"weather_alerts_section")
        self.alerts_title_label = SubtitleLabel(self.scrollAreaWidgetContents)
        self.alerts_title_label.setObjectName(u"alerts_title_label")
        self.alerts_title_label.setWordWrap(True)
        self.alerts_title_label.setProperty("pixelFontSize", 18)

        self.weather_alerts_section.addWidget(self.alerts_title_label)

        self.alerts_container_widget = QWidget(self.scrollAreaWidgetContents)
        self.alerts_container_widget.setObjectName(u"alerts_container_widget")
        self.alerts_container_widget.setMinimumSize(QSize(0, 100))

        self.weather_alerts_section.addWidget(self.alerts_container_widget)


        self.verticalLayout_21.addLayout(self.weather_alerts_section)

        self.blank = QFrame(self.scrollAreaWidgetContents)
        self.blank.setObjectName(u"blank")
        self.blank.setMinimumSize(QSize(0, 25))
        self.blank.setFrameShape(QFrame.StyledPanel)
        self.blank.setFrameShadow(QFrame.Raised)
        self.blank.setLineWidth(5)

        self.verticalLayout_21.addWidget(self.blank)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SubtitleLabel_5 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_5.setObjectName(u"SubtitleLabel_5")
        self.SubtitleLabel_5.setWordWrap(True)
        self.SubtitleLabel_5.setProperty("pixelFontSize", 18)

        self.verticalLayout_3.addWidget(self.SubtitleLabel_5)

        self.CardWidget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.CardWidget_3.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_14 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.StrongBodyLabel_12 = StrongBodyLabel(self.CardWidget_3)
        self.StrongBodyLabel_12.setObjectName(u"StrongBodyLabel_12")
        self.StrongBodyLabel_12.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.StrongBodyLabel_12)

        self.CaptionLabel_13 = CaptionLabel(self.CardWidget_3)
        self.CaptionLabel_13.setObjectName(u"CaptionLabel_13")
        self.CaptionLabel_13.setWordWrap(True)
        self.CaptionLabel_13.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_13.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_18.addWidget(self.CaptionLabel_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_18)

        self.select_weather_api = ComboBox(self.CardWidget_3)
        self.select_weather_api.setObjectName(u"select_weather_api")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.select_weather_api.sizePolicy().hasHeightForWidth())
        self.select_weather_api.setSizePolicy(sizePolicy6)

        self.horizontalLayout_14.addWidget(self.select_weather_api)


        self.verticalLayout_3.addWidget(self.CardWidget_3)

        self.CardWidget_4 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.CardWidget_4.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_10 = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.StrongBodyLabel_8 = StrongBodyLabel(self.CardWidget_4)
        self.StrongBodyLabel_8.setObjectName(u"StrongBodyLabel_8")
        self.StrongBodyLabel_8.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.StrongBodyLabel_8)

        self.CaptionLabel_9 = CaptionLabel(self.CardWidget_4)
        self.CaptionLabel_9.setObjectName(u"CaptionLabel_9")
        self.CaptionLabel_9.setWordWrap(True)
        self.CaptionLabel_9.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_9.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_16.addWidget(self.CaptionLabel_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_16)

        self.select_city = PushButton(self.CardWidget_4)
        self.select_city.setObjectName(u"select_city")
        sizePolicy6.setHeightForWidth(self.select_city.sizePolicy().hasHeightForWidth())
        self.select_city.setSizePolicy(sizePolicy6)

        self.horizontalLayout_10.addWidget(self.select_city)


        self.verticalLayout_3.addWidget(self.CardWidget_4)

        self.CardWidget_5 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_5.setObjectName(u"CardWidget_5")
        self.CardWidget_5.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_17 = QHBoxLayout(self.CardWidget_5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.StrongBodyLabel_15 = StrongBodyLabel(self.CardWidget_5)
        self.StrongBodyLabel_15.setObjectName(u"StrongBodyLabel_15")
        self.StrongBodyLabel_15.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.StrongBodyLabel_15)

        self.CaptionLabel_17 = CaptionLabel(self.CardWidget_5)
        self.CaptionLabel_17.setObjectName(u"CaptionLabel_17")
        self.CaptionLabel_17.setWordWrap(True)
        self.CaptionLabel_17.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_17.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_22.addWidget(self.CaptionLabel_17)


        self.horizontalLayout_17.addLayout(self.verticalLayout_22)

        self.api_key_edit = LineEdit(self.CardWidget_5)
        self.api_key_edit.setObjectName(u"api_key_edit")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.api_key_edit.sizePolicy().hasHeightForWidth())
        self.api_key_edit.setSizePolicy(sizePolicy7)
        self.api_key_edit.setMaximumSize(QSize(275, 33))

        self.horizontalLayout_17.addWidget(self.api_key_edit)


        self.verticalLayout_3.addWidget(self.CardWidget_5)

        self.CardWidget_6 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_6.setObjectName(u"CardWidget_6")
        self.CardWidget_6.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_16 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.StrongBodyLabel_14 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_14.setObjectName(u"StrongBodyLabel_14")
        self.StrongBodyLabel_14.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.StrongBodyLabel_14)

        self.CaptionLabel_15 = CaptionLabel(self.CardWidget_6)
        self.CaptionLabel_15.setObjectName(u"CaptionLabel_15")
        self.CaptionLabel_15.setWordWrap(True)
        self.CaptionLabel_15.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_15.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_20.addWidget(self.CaptionLabel_15)


        self.horizontalLayout_16.addLayout(self.verticalLayout_20)

        self.alert_exclude = LineEdit(self.CardWidget_6)
        self.alert_exclude.setObjectName(u"alert_exclude")
        sizePolicy7.setHeightForWidth(self.alert_exclude.sizePolicy().hasHeightForWidth())
        self.alert_exclude.setSizePolicy(sizePolicy7)
        self.alert_exclude.setMaximumSize(QSize(275, 33))
        self.alert_exclude.setFrame(True)

        self.horizontalLayout_16.addWidget(self.alert_exclude)


        self.verticalLayout_3.addWidget(self.CardWidget_6)


        self.verticalLayout_21.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SubtitleLabel_4 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")
        self.SubtitleLabel_4.setWordWrap(True)

        self.verticalLayout.addWidget(self.SubtitleLabel_4)

        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel_9.setObjectName(u"StrongBodyLabel_9")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.StrongBodyLabel_9.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_9.setSizePolicy(sizePolicy8)
        self.StrongBodyLabel_9.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.StrongBodyLabel_9)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget)
        self.CaptionLabel_8.setObjectName(u"CaptionLabel_8")
        self.CaptionLabel_8.setWordWrap(False)
        self.CaptionLabel_8.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_8.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_19.addWidget(self.CaptionLabel_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_19)

        self.weather_refresh_picker = SpinBox(self.CardWidget)
        self.weather_refresh_picker.setObjectName(u"weather_refresh_picker")
        self.weather_refresh_picker.setMinimum(0)
        self.weather_refresh_picker.setDisplayIntegerBase(10)

        self.horizontalLayout_8.addWidget(self.weather_refresh_picker)


        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_9 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.StrongBodyLabel_10 = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel_10.setObjectName(u"StrongBodyLabel_10")
        sizePolicy8.setHeightForWidth(self.StrongBodyLabel_10.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_10.setSizePolicy(sizePolicy8)
        self.StrongBodyLabel_10.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.StrongBodyLabel_10)

        self.CaptionLabel_7 = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel_7.setObjectName(u"CaptionLabel_7")
        self.CaptionLabel_7.setWordWrap(False)
        self.CaptionLabel_7.setProperty("lightColor", QColor(0, 0, 0, 150))
        self.CaptionLabel_7.setProperty("darkColor", QColor(255, 255, 255, 200))

        self.verticalLayout_12.addWidget(self.CaptionLabel_7)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)

        self.weather_temperat_unit = ComboBox(self.CardWidget_2)
        self.weather_temperat_unit.setObjectName(u"weather_temperat_unit")
        sizePolicy1.setHeightForWidth(self.weather_temperat_unit.sizePolicy().hasHeightForWidth())
        self.weather_temperat_unit.setSizePolicy(sizePolicy1)
        self.weather_temperat_unit.setMinimumSize(QSize(122, 0))

        self.horizontalLayout_9.addWidget(self.weather_temperat_unit)


        self.verticalLayout.addWidget(self.CardWidget_2)


        self.verticalLayout_21.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer)

        self.adv_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.adv_scroll)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u5929\u6c14", None))
        self.label.setText("")
        self.teto_x.setText(QCoreApplication.translate("Form", u"\u5317\u4eac\u5e02 \u00b7 \u5f53\u524d\u5929\u6c14", None))
        self.weather_re_time.setText(QCoreApplication.translate("Form", u"\u6700\u540e\u66f4\u65b0\u4e8e 00/00/0000 00:00:00", None))
        self.label_2.setText("")
        self.current_temperature_4.setText(QCoreApplication.translate("Form", u"-- \u00b0C", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u5927\u90e8\u6674\u6717", None))
        self.current_feels_like_2.setText(QCoreApplication.translate("Form", u"\u4f53\u611f\u6e29\u5ea6: -- \u00b0C", None))
        self.wind_label.setText(QCoreApplication.translate("Form", u"\u98ce\u901f", None))
        self.wind_value.setText(QCoreApplication.translate("Form", u"-- km/h", None))
        self.humidity_label.setText(QCoreApplication.translate("Form", u"\u6e7f\u5ea6", None))
        self.humidity_value.setText(QCoreApplication.translate("Form", u"-- %", None))
        self.visibility_label.setText(QCoreApplication.translate("Form", u"\u80fd\u89c1\u5ea6", None))
        self.visibility_value.setText(QCoreApplication.translate("Form", u"-- km", None))
        self.pressure_label_2.setText(QCoreApplication.translate("Form", u"\u6c14\u538b", None))
        self.pressure_value_2.setText(QCoreApplication.translate("Form", u"---- hPa", None))
        self.alerts_title_label.setText(QCoreApplication.translate("Form", u"\u5929\u6c14\u9884\u8b66", None))
        self.SubtitleLabel_5.setText(QCoreApplication.translate("Form", u"\u5929\u6c14\u6e90", None))
        self.StrongBodyLabel_12.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5929\u6c14\u6e90", None))
        self.CaptionLabel_13.setText(QCoreApplication.translate("Form", u"\u5c06\u4f1a\u5f71\u54cd\u201c\u5929\u6c14\u201d\u5c0f\u7ec4\u4ef6\u7684\u5929\u6c14\u6570\u636e\u6e90", None))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u57ce\u5e02", None))
        self.CaptionLabel_9.setText(QCoreApplication.translate("Form", u"\u5c06\u4f1a\u7528\u4e8e\u83b7\u5f97\u5929\u6c14\u6570\u636e", None))
        self.select_city.setText(QCoreApplication.translate("Form", u"  \u9009\u62e9\u4e00\u4e2a\u57ce\u5e02  ", None))
        self.StrongBodyLabel_15.setText(QCoreApplication.translate("Form", u"\u5929\u6c14\u6e90 API Key", None))
        self.CaptionLabel_17.setText(QCoreApplication.translate("Form", u"\u90e8\u5206\u5929\u6c14\u6e90\u53ef\u80fd\u9700\u8981\u8bbe\u7f6e Key \u624d\u80fd\u6b63\u5e38\u4f7f\u7528\uff0c\u53ef\u5728\u201c\u5e2e\u52a9\u201d\u9875\u627e\u5230\u5404\u4e2a\u5929\u6c14\u6e90\u83b7\u5f97 Key \u7684\u65b9\u6cd5\u3002", None))
        self.StrongBodyLabel_14.setText(QCoreApplication.translate("Form", u"\u6392\u9664\u7684\u6c14\u8c61\u9884\u8b66", None))
        self.CaptionLabel_15.setText(QCoreApplication.translate("Form", u"\u5305\u542b\u8be5\u5b57\u7b26\u4e32\u5185\u5bb9\u7684\u9884\u8b66\u5c06\u4e0d\u4f1a\u88ab\u663e\u793a\n"
"\u591a\u4e2a\u5185\u5bb9\u4f7f\u7528\u7a7a\u683c\u5206\u9694", None))
        self.alert_exclude.setText("")
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Form", u"\u663e\u793a", None))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate("Form", u"\u8ba1\u65f6\u81ea\u52a8\u5237\u65b0", None))
        self.CaptionLabel_8.setText(QCoreApplication.translate("Form", u"\u6309\u7167\u8bbe\u5b9a\u7684\u5206\u949f\u6570\u5b9a\u65f6\u6267\u884c\u5929\u6c14\u6570\u636e\u5237\u65b0", None))
        self.weather_refresh_picker.setPrefix("")
        self.StrongBodyLabel_10.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u6e29\u5ea6\u5355\u4f4d", None))
        self.CaptionLabel_7.setText(QCoreApplication.translate("Form", u"\u8c03\u6574\u663e\u793a\u7684\u6e29\u5ea6\u5355\u4f4d", None))
        self.weather_temperat_unit.setText(QCoreApplication.translate("Form", u"\u6444\u6c0f\u5ea6 (\u00b0C)", None))
    # retranslateUi
