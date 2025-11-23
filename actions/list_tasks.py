import os, json

class ListTasks:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ROOT_DIR = os.path.dirname(self.BASE_DIR)
        self.DATA_DIR = os.path.join(self.ROOT_DIR, "data")
        self.FILE_NAME = os.path.join(self.DATA_DIR, "registers.json")

    def search_all_task(self):
        tasks = self.get_all_tasks()
        for task in tasks:
            print(f"Task ID: {task["_id"]}, Titulo: {task["title"]}, Status: {task["status"]}, Priority: {task["priority"]}")

    def get_all_tasks(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
        
    def search_task_by_title(self, title: str):
        result = self.search_engine(1, title)
        for task in result:
            print(f"Task ID: {task['_id']}, Titulo: {task['title']}, Status: {task['status']}, Priority: {task['priority']}")
        
    def list_tasks_by_priority(self, priority: int):
        result = self.search_engine(2, priority)
        for task in result:
            print(f"Task ID: {task['_id']}, Titulo: {task['title']}, Status: {task['status']}, Priority: {task['priority']}")

    def search_engine(self, search_type: int, value):
        tasks = self.get_all_tasks()
        if search_type == 1:
            return [task for task in tasks if value.lower() in task["title"].lower()]
        elif search_type == 2:
            return [task for task in tasks if task["priority"] == value]
        else:
            return []