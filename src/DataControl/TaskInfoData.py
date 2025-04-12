import json, sys, os
from src.DataControl.AddressData import return_task_address

def return_task_info_data(my_task_name):
    taskAdd = return_task_address()

    if getattr(sys, 'frozen', False):
        json_path = os.path.join(sys._MEIPASS, f"{taskAdd}/{my_task_name}/info.json")
        with open(json_path, 'r') as file:
            taskData = json.load(file)
    else:
        json_path = f"{taskAdd}/{my_task_name}/info.json"
        with open(json_path, 'r') as file:
            taskData = json.load(file)
    return taskData