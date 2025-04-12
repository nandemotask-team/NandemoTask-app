import sys, os, subprocess, json
from PySide6.QtWidgets import QMainWindow
from ui.AddNewTask_Form_ui import Ui_AddNewTask_Form

from src.DataControl.MyTaskData import return_my_work_data
from src.DataControl.AddressData import return_task_address

class AddNewTask_Form(QMainWindow, Ui_AddNewTask_Form):
    def __init__(self):
        super(AddNewTask_Form, self).__init__()
        self.setupUi(self)

        myTaskData = return_my_work_data()
        myTaskDatatoList = list(myTaskData.keys())
        for i in myTaskDatatoList:
            self.WorkType_listWidget.addItem(i)
        self.WorkType_listWidget.itemDoubleClicked.connect(self.TaskType_listWidget_f)

        # Click Create Button
        self.Create_BT.clicked.connect(self.Create_BT_f)
    
    def TaskType_listWidget_f(self):
        SelectedItem = self.WorkType_listWidget.currentItem().text()
        self.WorkType_lineEdit.setText(SelectedItem)

    def Create_BT_f(self):
        task_add = return_task_address()
        task_name = self.TaskName_lineEdit.text()
        work_name = self.WorkType_lineEdit.text()
        work_instruction = self.TaskInstruction_textEdit.toPlainText()
        
        # get Work info
        my_work_data = return_my_work_data()
        work_info = my_work_data[work_name]
        work_add = work_info[1]

        # New Task 워크 레파지토리 생성
        os.mkdir(f"{task_add}/{task_name}")
        
        # New Task 워크 데이터 레파지토리 생성성
        os.mkdir(f"{task_add}/{task_name}/WorkData")

        # New Task Task info json 파일 생성
        taskInfo = {
            "Work_Type": work_name,
            "Work_V": work_info[0],
            "Work_Add": work_info[1],
            "Instruction" : work_instruction
        }
        if getattr(sys, 'frozen', False):
            account_json_path = os.path.join(sys._MEIPASS, f"{task_add}/{task_name}/info.json")
            with open(account_json_path, 'w', encoding='utf-8') as file:
                json.dump(taskInfo, file, indent="\t")
        else:
            account_json_path = f"{task_add}/{task_name}/info.json"
            with open(account_json_path, 'w', encoding='utf-8') as file:
                json.dump(taskInfo, file, indent="\t")

        # print(work_add)
        #######[간의 코드]####### (특수부호로 인한 에러 22([Error 22]) 해결 필요)
        subprocess.run(args=[sys.executable, f"{work_add}/app.py", '-c', f"{task_add}/{task_name}/WorkData"])
        ########################
        self.close()
        