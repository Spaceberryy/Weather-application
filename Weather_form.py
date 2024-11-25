# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Weather_form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Weather_form(object):
    def setupUi(self, Weather_form):
        if not Weather_form.objectName():
            Weather_form.setObjectName(u"Weather_form")
        Weather_form.resize(400, 400)
        self.enter_city_name = QLabel(Weather_form)
        self.enter_city_name.setObjectName(u"enter_city_name")
        self.enter_city_name.setGeometry(QRect(10, 10, 381, 31))
        self.enter_city_name.setFrameShape(QFrame.Shape.StyledPanel)
        self.enter_city_name.setFrameShadow(QFrame.Shadow.Sunken)
        self.enter_city_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pb_getweather = QPushButton(Weather_form)
        self.pb_getweather.setObjectName(u"pb_getweather")
        self.pb_getweather.setGeometry(QRect(10, 90, 381, 31))
        self.city_name = QLineEdit(Weather_form)
        self.city_name.setObjectName(u"city_name")
        self.city_name.setGeometry(QRect(10, 50, 381, 31))
        self.city_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_val = QLabel(Weather_form)
        self.temp_val.setObjectName(u"temp_val")
        self.temp_val.setGeometry(QRect(10, 130, 381, 41))
        font = QFont()
        font.setPointSize(20)
        self.temp_val.setFont(font)
        self.temp_val.setFrameShape(QFrame.Shape.StyledPanel)
        self.temp_val.setFrameShadow(QFrame.Shadow.Sunken)
        self.temp_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.feels_like = QLabel(Weather_form)
        self.feels_like.setObjectName(u"feels_like")
        self.feels_like.setGeometry(QRect(10, 340, 381, 51))
        self.feels_like.setFrameShape(QFrame.Shape.StyledPanel)
        self.feels_like.setFrameShadow(QFrame.Shadow.Sunken)
        self.feels_like.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label = QLabel(Weather_form)
        self.emoji_label.setObjectName(u"emoji_label")
        self.emoji_label.setGeometry(QRect(130, 180, 150, 150))
        font1 = QFont()
        font1.setPointSize(72)
        self.emoji_label.setFont(font1)
        self.emoji_label.setFrameShape(QFrame.Shape.StyledPanel)
        self.emoji_label.setFrameShadow(QFrame.Shadow.Sunken)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Weather_form)

        QMetaObject.connectSlotsByName(Weather_form)
    # setupUi

    def retranslateUi(self, Weather_form):
        Weather_form.setWindowTitle(QCoreApplication.translate("Weather_form", u"Widget", None))
        self.enter_city_name.setText(QCoreApplication.translate("Weather_form", u"Enter City name:", None))
        self.pb_getweather.setText(QCoreApplication.translate("Weather_form", u"Get Weather!", None))
        self.temp_val.setText("")
        self.feels_like.setText("")
        self.emoji_label.setText("")
    # retranslateUi

