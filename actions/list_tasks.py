import os, json

class ListTasks:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ROOT_DIR = os.path.dirname(self.BASE_DIR)
        self.DATA_DIR = os.path.join(self.ROOT_DIR, "data")
        self.FILE_NAME = os.path.join(self.DATA_DIR, "registers.json")

    def execute(self):
        tasks = self.get_all_tasks()
        for task in tasks:
            print(f"Task ID: {task["_id"]}, Titulo: {task["title"]}, Status: {task["status"]}")

    def get_all_tasks(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)