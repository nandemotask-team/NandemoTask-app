import sys, os, subprocess, shutil
from PySide6.QtWidgets import QMainWindow, QMenu
from ui.MainWindow_ui import Ui_MainWindow

from src.Forms.Setting_Form import Setting_Form
from src.Forms.AddNewTask_Form import AddNewTask_Form

from src.DataControl.AddressData import return_task_address
from src.DataControl.TaskInfoData import return_task_info_data
from src.DataControl.MyTaskData import return_my_work_data

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 매뉴바 세팅
        self.actionAdd_New_Task.setStatusTip("add new task")
        self.actionAdd_New_Task.triggered.connect(self.actionAdd_New_Task_f)
        self.actionStop_All.setStatusTip('stop all task')
        self.actionExtension.setStatusTip('Extension')
        self.actionAccount.setStatusTip('account management')
        self.actionSetting.setStatusTip('Nandemo Task App Setting')
        self.actionSetting.triggered.connect(self.actionSetting_f)
        self.actionRefresh.setStatusTip('Refresh')
        self.actionRefresh.triggered.connect(self.reset)

        # Task List 세팅
        tasksAddress = return_task_address()
        self.myTaskList = os.listdir(tasksAddress)
        for i in self.myTaskList:
            self.Task_ListWidget.addItem(f"off | {i}")
        self.Task_ListWidget.itemDoubleClicked.connect(self.Task_ListWidget_f)
        self.Task_ListWidget.customContextMenuRequested.connect(self.Task_ListWidget_context_menu_f)
    
    def Task_ListWidget_f(self):
        selectItem = self.Task_ListWidget.currentItem().text()
        selectItem = selectItem.lstrip('off on')
        selectItem = selectItem.lstrip(' | ')

        selectItemInfo = return_task_info_data(selectItem)

        selectItemType = selectItemInfo['Work_Type']

        my_work = return_my_work_data()
        selectItemWorkAdd = my_work[selectItemType][1]     

        ######[간의 코드]######
        taskAdd = return_task_address()
        subprocess.run(args=[sys.executable, f"{selectItemWorkAdd}/app.py", '-s', f"{taskAdd}/{selectItem}/WorkData/data.json"])
        ######################

    def Task_ListWidget_context_menu_f(self, pos):
        item = self.Task_ListWidget.itemAt(pos)

        if item:
            menu = QMenu()
            run_action = menu.addAction("Run")
            setting_action = menu.addAction("Setting")
            information_action = menu.addAction("Information")
            delete_action = menu.addAction("Delete")

            selected_action = menu.exec(self.Task_ListWidget.mapToGlobal(pos))

            #####[Run]######
            if selected_action == run_action:
                selectItem = self.Task_ListWidget.currentItem().text()
                selectItem = selectItem.lstrip('off on')
                selectItem = selectItem.lstrip(' | ')
                selectItemInfo = return_task_info_data(selectItem)

                selectItemType = selectItemInfo['Work_Type']

                my_work = return_my_work_data()
                selectItemWorkAdd = my_work[selectItemType][1]     

                ######[간의 코드]######
                taskAdd = return_task_address()
                subprocess.run(args=[sys.executable, f"{selectItemWorkAdd}/app.py", '-r', f"{taskAdd}/{selectItem}/WorkData/data.json"])
                ######################
            ################
            
            #####[setting]#####
            elif selected_action == setting_action:
                selectItem = self.Task_ListWidget.currentItem().text()
                selectItem = selectItem.lstrip('off on')
                selectItem = selectItem.lstrip(' | ')
                selectItemInfo = return_task_info_data(selectItem)

                selectItemType = selectItemInfo['Work_Type']

                my_work = return_my_work_data()
                selectItemWorkAdd = my_work[selectItemType][1]     

                ######[간의 코드]######
                taskAdd = return_task_address()
                subprocess.run(args=[sys.executable, f"{selectItemWorkAdd}/app.py", '-s', f"{taskAdd}/{selectItem}/WorkData/data.json"])
                ######################

            ###################

            #####[information]#####
            elif selected_action == information_action:
                pass
            #######################

            #####[Delete]#####
            elif selected_action == delete_action:
                selectItem = self.Task_ListWidget.currentItem().text()
                selectItem = selectItem.lstrip('off on')
                selectItem = selectItem.lstrip(' | ')

                # "정말 삭제하시겠습니까?" 의미의 경고문 호출 후 삭제삭제
                #####[삭제 로직]####
                Task_add = return_task_address()
                try:
                    shutil.rmtree(f"{Task_add}/{selectItem}")
                    self.reset()
                except:
                    # 파일 삭제 에러문도 필요
                    print("파일을 찾을 수 없습니다.")
                ####################
            ##################

    def actionAdd_New_Task_f(self):
        ANTForm = AddNewTask_Form()
        ANTForm.show()
        ANTForm.exec_()

    def actionSetting_f(self):
        SettingForm = Setting_Form()
        SettingForm.show()
        SettingForm.exec_()

    def reset(self):
        tasksAddress = return_task_address()
        self.myTaskList = os.listdir(tasksAddress)
        self.Task_ListWidget.clear()
        for i in self.myTaskList:
            self.Task_ListWidget.addItem(f"off | {i}")