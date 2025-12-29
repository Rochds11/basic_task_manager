import os, uuid, datetime, json

class RecordTasks:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ROOT_DIR = os.path.dirname(self.BASE_DIR)
        self.DATA_DIR = os.path.join(self.ROOT_DIR, "data")
        self.FILE_NAME = os.path.join(self.DATA_DIR, "registers.json")
        self.incoming_data = {}
        self.title:str = None
        self.priority:int = None
        self.status:str = Status.PENDING

    def record_task(self):
        print(f"Tarea creada: Título= '{self.title}', Prioridad= {Priotity.Priotities[self.priority]}, Estado= '{self.status}'")
        self.prepare_task_data()
        data = self.load_tasks()
        data.append(self.incoming_data)
        self.save_task(data)
        print("Tarea guardada exitosamente.")

    
    def prepare_task_data(self):
        self.incoming_data = {
            "_id": uuid.uuid4().hex[:8],
            "title": self.title,
            "priority": self.priority,
            "status": self.status,
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat(),
        }

    def load_tasks(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_task(self, data):
        with open(self.FILE_NAME, 'w') as json_file:
            json.dump(data, json_file)

class Priotity:
    Priotities = {
        1: "Baja",
        2: "Media",
        3: "Alta",
        4: "Urgente"
    }

class Status:
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"