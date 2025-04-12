# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setting_Form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_Setting_Form(object):
    def setupUi(self, Setting_Form):
        if not Setting_Form.objectName():
            Setting_Form.setObjectName(u"Setting_Form")
        Setting_Form.resize(570, 450)
        Setting_Form.setStyleSheet(u"background-color: rgb(236, 236, 236);")
        self.Setting_tabWidget = QTabWidget(Setting_Form)
        self.Setting_tabWidget.setObjectName(u"Setting_tabWidget")
        self.Setting_tabWidget.setGeometry(QRect(10, 30, 551, 381))
        self.Setting_tabWidget.setStyleSheet(u"")
        self.TaskSetting_tab = QWidget()
        self.TaskSetting_tab.setObjectName(u"TaskSetting_tab")
        self.label = QLabel(self.TaskSetting_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 17, 81, 21))
        self.TasksAddres_lineEdit = QLineEdit(self.TaskSetting_tab)
        self.TasksAddres_lineEdit.setObjectName(u"TasksAddres_lineEdit")
        self.TasksAddres_lineEdit.setGeometry(QRect(90, 17, 421, 21))
        self.TasksAddres_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.FindTasksAddress_BT = QPushButton(self.TaskSetting_tab)
        self.FindTasksAddress_BT.setObjectName(u"FindTasksAddress_BT")
        self.FindTasksAddress_BT.setGeometry(QRect(510, 10, 31, 31))
        self.FindTasksAddress_BT.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.FindTasksAddress_BT.setIcon(icon)
        self.line = QFrame(self.TaskSetting_tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 37, 531, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.Setting_tabWidget.addTab(self.TaskSetting_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.Setting_tabWidget.addTab(self.tab_2, "")
        self.Ok_BT = QPushButton(Setting_Form)
        self.Ok_BT.setObjectName(u"Ok_BT")
        self.Ok_BT.setGeometry(QRect(390, 410, 91, 31))
        self.Ok_BT.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Close_BT = QPushButton(Setting_Form)
        self.Close_BT.setObjectName(u"Close_BT")
        self.Close_BT.setGeometry(QRect(484, 410, 81, 31))
        self.Close_BT.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Setting_Form)
        self.Close_BT.clicked.connect(Setting_Form.close)

        self.Setting_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setting_Form)
    # setupUi

    def retranslateUi(self, Setting_Form):
        Setting_Form.setWindowTitle(QCoreApplication.translate("Setting_Form", u"Setting", None))
        self.label.setText(QCoreApplication.translate("Setting_Form", u"Tasks Address", None))
        self.FindTasksAddress_BT.setText("")
        self.Setting_tabWidget.setTabText(self.Setting_tabWidget.indexOf(self.TaskSetting_tab), QCoreApplication.translate("Setting_Form", u"TaskSetting", None))
        self.Setting_tabWidget.setTabText(self.Setting_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Setting_Form", u"Tab 2", None))
        self.Ok_BT.setText(QCoreApplication.translate("Setting_Form", u"\ud655\uc778", None))
        self.Close_BT.setText(QCoreApplication.translate("Setting_Form", u"\ucde8\uc18c", None))
    # retranslateUi

