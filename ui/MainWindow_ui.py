# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowHKirJQ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(290, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionAdd_New_Task = QAction(MainWindow)
        self.actionAdd_New_Task.setObjectName(u"actionAdd_New_Task")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.actionAdd_New_Task.setIcon(icon)
        self.actionStop_All = QAction(MainWindow)
        self.actionStop_All.setObjectName(u"actionStop_All")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.actionStop_All.setIcon(icon1)
        self.actionAccount = QAction(MainWindow)
        self.actionAccount.setObjectName(u"actionAccount")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.CameraWeb))
        self.actionAccount.setIcon(icon2)
        self.actionExtension = QAction(MainWindow)
        self.actionExtension.setObjectName(u"actionExtension")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaFlash))
        self.actionExtension.setIcon(icon3)
        self.actionSetting = QAction(MainWindow)
        self.actionSetting.setObjectName(u"actionSetting")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.actionSetting.setIcon(icon4)
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemReboot))
        self.actionRefresh.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.Task_ListWidget = QListWidget(self.centralwidget)
        self.Task_ListWidget.setObjectName(u"Task_ListWidget")
        self.Task_ListWidget.setGeometry(QRect(10, 40, 270, 541))
        sizePolicy.setHeightForWidth(self.Task_ListWidget.sizePolicy().hasHeightForWidth())
        self.Task_ListWidget.setSizePolicy(sizePolicy)
        self.Task_ListWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 30, 271, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 580, 271, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.Department_label = QLabel(self.centralwidget)
        self.Department_label.setObjectName(u"Department_label")
        self.Department_label.setGeometry(QRect(170, 10, 111, 21))
        self.Niknam_label = QLabel(self.centralwidget)
        self.Niknam_label.setObjectName(u"Niknam_label")
        self.Niknam_label.setGeometry(QRect(10, 10, 151, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 290, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionAdd_New_Task)
        self.menu.addAction(self.actionStop_All)
        self.menu.addAction(self.actionExtension)
        self.menu.addAction(self.actionAccount)
        self.menu.addAction(self.actionSetting)
        self.menu.addAction(self.actionRefresh)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NandemoTask", None))
        self.actionAdd_New_Task.setText(QCoreApplication.translate("MainWindow", u"Add New Task", None))
        self.actionStop_All.setText(QCoreApplication.translate("MainWindow", u"Stop All", None))
        self.actionAccount.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.actionExtension.setText(QCoreApplication.translate("MainWindow", u"Extension", None))
        self.actionSetting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.Department_label.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.Niknam_label.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ub9e4\ub274", None))
    # retranslateUi

