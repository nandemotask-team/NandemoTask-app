# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewTask_Form.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_AddNewTask_Form(object):
    def setupUi(self, AddNewTask_Form):
        if not AddNewTask_Form.objectName():
            AddNewTask_Form.setObjectName(u"AddNewTask_Form")
        AddNewTask_Form.resize(550, 475)
        self.WorkType_listWidget = QListWidget(AddNewTask_Form)
        self.WorkType_listWidget.setObjectName(u"WorkType_listWidget")
        self.WorkType_listWidget.setGeometry(QRect(10, 30, 256, 401))
        self.label = QLabel(AddNewTask_Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 121, 21))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.WorkType_lineEdit = QLineEdit(AddNewTask_Form)
        self.WorkType_lineEdit.setObjectName(u"WorkType_lineEdit")
        self.WorkType_lineEdit.setEnabled(False)
        self.WorkType_lineEdit.setGeometry(QRect(280, 50, 261, 21))
        self.label_2 = QLabel(AddNewTask_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 30, 121, 21))
        self.label_2.setFont(font)
        self.TaskName_lineEdit = QLineEdit(AddNewTask_Form)
        self.TaskName_lineEdit.setObjectName(u"TaskName_lineEdit")
        self.TaskName_lineEdit.setGeometry(QRect(280, 100, 261, 21))
        self.label_3 = QLabel(AddNewTask_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 80, 121, 21))
        self.label_3.setFont(font)
        self.TaskInstruction_textEdit = QTextEdit(AddNewTask_Form)
        self.TaskInstruction_textEdit.setObjectName(u"TaskInstruction_textEdit")
        self.TaskInstruction_textEdit.setGeometry(QRect(280, 150, 261, 281))
        self.label_4 = QLabel(AddNewTask_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 130, 151, 21))
        self.label_4.setFont(font)
        self.pushButton = QPushButton(AddNewTask_Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(450, 440, 91, 31))
        self.line = QFrame(AddNewTask_Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(263, 30, 21, 401))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.Create_BT = QPushButton(AddNewTask_Form)
        self.Create_BT.setObjectName(u"Create_BT")
        self.Create_BT.setGeometry(QRect(350, 440, 91, 31))
        self.line_2 = QFrame(AddNewTask_Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 430, 531, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(AddNewTask_Form)
        self.pushButton.clicked.connect(AddNewTask_Form.close)

        QMetaObject.connectSlotsByName(AddNewTask_Form)
    # setupUi

    def retranslateUi(self, AddNewTask_Form):
        AddNewTask_Form.setWindowTitle(QCoreApplication.translate("AddNewTask_Form", u"Add New Task", None))
        self.label.setText(QCoreApplication.translate("AddNewTask_Form", u".Work", None))
        self.label_2.setText(QCoreApplication.translate("AddNewTask_Form", u".Work Type", None))
        self.TaskName_lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("AddNewTask_Form", u".Task Name", None))
        self.label_4.setText(QCoreApplication.translate("AddNewTask_Form", u".My Task Instruction", None))
        self.pushButton.setText(QCoreApplication.translate("AddNewTask_Form", u"Close", None))
        self.Create_BT.setText(QCoreApplication.translate("AddNewTask_Form", u"Create", None))
    # retranslateUi

