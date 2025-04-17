import os, shutil
from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui.Extension_Form_ui import Ui_Extension_Form

from src.DataControl.AddressData import return_work_address

class Extension_Form(QMainWindow, Ui_Extension_Form):
    def __init__(self):
        super(Extension_Form, self).__init__()
        self.setupUi(self)

        self.FindFile_BT.clicked.connect(self.FindFile_BT_f)
        self.Add_BT.clicked.connect(self.Add_BT_f)
        self.Delete_BT.clicked.connect(self.Delete_BT_f)

    def FindFile_BT_f(self):
        file_paths, _ = QFileDialog.getOpenFileUrls(self, "Find ZIP File", "", "Find ZIP File (*.zip)")
        for i in file_paths:
            # print(str(i.toLocalFile()))
            self.NewWork_listWidget.addItem(f"{i.toLocalFile()}")
    
    def Add_BT_f(self):
        file_paths = [self.NewWork_listWidget.item(i).text() for i in range(self.NewWork_listWidget.count())]
        ConWorkAdd = return_work_address()
        for i in file_paths:
            shutil.unpack_archive(i, ConWorkAdd, "zip")
        print("ok")
        #####[!!Work 등록 관련!!]#####
        # Work를 zip 형태로 받아와 ConnectedWork 폴더에 등록할때
        # 이 zip 파일이 사용 가능한 Work인지 확인하는 과정과 MyWorkData.json
        # 데이터 파일에 새로운 워크를 등록하는 함수가 필요함#
        #############################
    
    def Delete_BT_f(self):
        self.NewWork_listWidget.takeItem(self.NewWork_listWidget.currentRow())