# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(138, 189)
        Widget.setStyleSheet(u"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(31,31,31);")
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 115, 164))
        self.widget.setMinimumSize(QSize(115, 0))
        self.widget.setMaximumSize(QSize(115, 16777215))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.c_label = QLabel(self.widget)
        self.c_label.setObjectName(u"c_label")
        self.c_label.setMinimumSize(QSize(115, 18))
        self.c_label.setMaximumSize(QSize(115, 18))

        self.gridLayout.addWidget(self.c_label, 0, 0, 1, 1)

        self.g_label = QLabel(self.widget)
        self.g_label.setObjectName(u"g_label")
        self.g_label.setMinimumSize(QSize(115, 18))
        self.g_label.setMaximumSize(QSize(115, 18))

        self.gridLayout.addWidget(self.g_label, 1, 0, 1, 1)

        self.r_label = QLabel(self.widget)
        self.r_label.setObjectName(u"r_label")
        self.r_label.setMinimumSize(QSize(115, 18))
        self.r_label.setMaximumSize(QSize(115, 18))

        self.gridLayout.addWidget(self.r_label, 2, 0, 1, 1)

        self.v_label = QLabel(self.widget)
        self.v_label.setObjectName(u"v_label")
        self.v_label.setMinimumSize(QSize(115, 18))
        self.v_label.setMaximumSize(QSize(115, 18))

        self.gridLayout.addWidget(self.v_label, 3, 0, 1, 1)

        self.p_label = QLabel(self.widget)
        self.p_label.setObjectName(u"p_label")
        self.p_label.setMinimumSize(QSize(115, 18))
        self.p_label.setMaximumSize(QSize(115, 18))

        self.gridLayout.addWidget(self.p_label, 4, 0, 1, 1)

        self.h_label = QLabel(self.widget)
        self.h_label.setObjectName(u"h_label")
        self.h_label.setMinimumSize(QSize(115, 18))
        self.h_label.setMaximumSize(QSize(115, 18))

        self.gridLayout.addWidget(self.h_label, 5, 0, 1, 1)

        self.f_label = QLabel(self.widget)
        self.f_label.setObjectName(u"f_label")
        self.f_label.setMinimumSize(QSize(115, 18))
        self.f_label.setMaximumSize(QSize(115, 18))

        self.gridLayout.addWidget(self.f_label, 6, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.c_label.setText(QCoreApplication.translate("Widget", u"CPU    ", None))
        self.g_label.setText(QCoreApplication.translate("Widget", u"GPU     ", None))
        self.r_label.setText(QCoreApplication.translate("Widget", u"RAM    ", None))
        self.v_label.setText(QCoreApplication.translate("Widget", u"VRAM  ", None))
        self.p_label.setText(QCoreApplication.translate("Widget", u"PWR    ", None))
        self.h_label.setText(QCoreApplication.translate("Widget", u"HEAT   ", None))
        self.f_label.setText(QCoreApplication.translate("Widget", u"FPS      ", None))
    # retranslateUi

