import json, sys, os

def return_task_address():
    if getattr(sys, 'frozen', False):
        json_path = os.path.join(sys._MEIPASS, "./data/Address_set.json")
        with open(json_path, 'r') as file:
            address_data = json.load(file)
    else:
        json_path = "./data/Address_set.json"
        with open(json_path, 'r') as file:
            address_data = json.load(file)
    
    return address_data['Task_Address']

# Write Task Address
def write_task_address(new_address):
    if getattr(sys, 'frozen', False):
        json_path = os.path.join(sys._MEIPASS, "./data/Address_set.json")
        with open(json_path, 'r') as file:
            address_data = json.load(file)
    else:
        json_path = "./data/Address_set.json"
        with open(json_path, 'r') as file:
            address_data = json.load(file)
    
    address_data['Task_Address'] = new_address

    if getattr(sys, 'frozen', False):
        json_path = os.path.join(sys._MEIPASS, "./data/Address_set.json")
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(address_data, file, indent="\t")
    else:
        json_path = "./data/Address_set.json"
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(address_data, file, indent="\t")


def return_work_address():
    if getattr(sys, 'frozen', False):
        json_path = os.path.join(sys._MEIPASS, "./data/Address_set.json")
        with open(json_path, 'r') as file:
            address_data = json.load(file)
    else:
        json_path = "./data/Address_set.json"
        with open(json_path, 'r') as file:
            address_data = json.load(file)
    
    return address_data['Work_Address']

# Write Work Address
def write_work_address(new_address):
    if getattr(sys, 'frozen', False):
        json_path = os.path.join(sys._MEIPASS, "./data/Address_set.json")
        with open(json_path, 'r') as file:
            address_data = json.load(file)
    else:
        json_path = "./data/Address_set.json"
        with open(json_path, 'r') as file:
            address_data = json.load(file)
    
    address_data['Work_Address'] = new_address

    if getattr(sys, 'frozen', False):
        json_path = os.path.join(sys._MEIPASS, "./data/Address_set.json")
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(address_data, file, indent="\t")
    else:
        json_path = "./data/Address_set.json"
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(address_data, file, indent="\t")