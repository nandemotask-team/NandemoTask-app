import sys, os
from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui.Setting_Form_ui import Ui_Setting_Form

from src.DataControl.AddressData import return_task_address, write_task_address

class Setting_Form(QMainWindow, Ui_Setting_Form):
    def __init__(self):
        super(Setting_Form, self).__init__()
        self.setupUi(self)

        # 기본정보 세팅
        TaskAddress = return_task_address()
        self.TasksAddres_lineEdit.setText(TaskAddress)
        
        # 세팅 옵션션
        self.FindTasksAddress_BT.clicked.connect(self.FindTasksAddress_BT_f)
    
        self.Ok_BT.clicked.connect(self.Ok_BT_f)
    def FindTasksAddress_BT_f(self):
        NewTaskAddress = QFileDialog.getExistingDirectory(self, self.tr("Open Data files"), "./", QFileDialog.ShowDirsOnly)
        # write_task_address(NewTaskAddress)
        self.TasksAddres_lineEdit.setText(NewTaskAddress)

    def Ok_BT_f(self):
        TaskAddress = self.TasksAddres_lineEdit.text()
        write_task_address(TaskAddress)
        self.close()
        # TasksAddres_lineEdit 에 TaskAddress 업데이트 하는 코드 제작 필요