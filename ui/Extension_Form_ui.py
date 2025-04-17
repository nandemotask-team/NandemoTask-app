# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Extension_Form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_Extension_Form(object):
    def setupUi(self, Extension_Form):
        if not Extension_Form.objectName():
            Extension_Form.setObjectName(u"Extension_Form")
        Extension_Form.resize(400, 290)
        self.label = QLabel(Extension_Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 91, 16))
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.Add_BT = QPushButton(Extension_Form)
        self.Add_BT.setObjectName(u"Add_BT")
        self.Add_BT.setGeometry(QRect(300, 100, 91, 31))
        self.Close_BT = QPushButton(Extension_Form)
        self.Close_BT.setObjectName(u"Close_BT")
        self.Close_BT.setGeometry(QRect(300, 250, 91, 31))
        self.FindFile_BT = QPushButton(Extension_Form)
        self.FindFile_BT.setObjectName(u"FindFile_BT")
        self.FindFile_BT.setGeometry(QRect(190, 40, 101, 31))
        self.FindWeb_BT = QPushButton(Extension_Form)
        self.FindWeb_BT.setObjectName(u"FindWeb_BT")
        self.FindWeb_BT.setGeometry(QRect(300, 70, 91, 31))
        self.label_2 = QLabel(Extension_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 10, 81, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setUnderline(True)
        self.label_2.setFont(font1)
        self.NewWork_listWidget = QListWidget(Extension_Form)
        self.NewWork_listWidget.setObjectName(u"NewWork_listWidget")
        self.NewWork_listWidget.setGeometry(QRect(10, 70, 281, 211))
        self.NewWork_listWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.Delete_BT = QPushButton(Extension_Form)
        self.Delete_BT.setObjectName(u"Delete_BT")
        self.Delete_BT.setGeometry(QRect(300, 220, 91, 31))

        self.retranslateUi(Extension_Form)
        self.Close_BT.clicked.connect(Extension_Form.close)

        QMetaObject.connectSlotsByName(Extension_Form)
    # setupUi

    def retranslateUi(self, Extension_Form):
        Extension_Form.setWindowTitle(QCoreApplication.translate("Extension_Form", u"Extension", None))
        self.label.setText(QCoreApplication.translate("Extension_Form", u"Add New Work", None))
        self.Add_BT.setText(QCoreApplication.translate("Extension_Form", u"Add", None))
        self.Close_BT.setText(QCoreApplication.translate("Extension_Form", u"Close", None))
        self.FindFile_BT.setText(QCoreApplication.translate("Extension_Form", u"Find Work File", None))
        self.FindWeb_BT.setText(QCoreApplication.translate("Extension_Form", u"Find in Web", None))
        self.label_2.setText(QCoreApplication.translate("Extension_Form", u"Extension", None))
        self.Delete_BT.setText(QCoreApplication.translate("Extension_Form", u"Delete", None))
    # retranslateUi

