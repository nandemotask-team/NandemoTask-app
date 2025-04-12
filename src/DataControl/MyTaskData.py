import json, sys, os

def return_my_work_data():
    if getattr(sys, 'frozen', False):
        account_json_path = os.path.join(sys._MEIPASS, "./data/MyWorkData.json")
        with open(account_json_path, 'r') as file:
            myTaskData = json.load(file)
    else:
        account_json_path = "./data/MyWorkData.json"
        with open(account_json_path, 'r') as file:
            myTaskData = json.load(file)
    
    return myTaskData