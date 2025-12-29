from actions.record_tasks import RecordTasks, Priotity
from actions.list_tasks import ListTasks
from colorama import Fore, Style
import os, platform

class CommandManager:
    def __init__(self):
        self.running: bool = True
        self.command: int = None
        self.commands = {
            1: "Agregar una nueva tarea",
            2: "Listar tareas",
            3: "Eliminar una tarea existente",
            4: "Actualizar el estado de una tarea",
            5: "Salir"
        }

    def execute(self):
        while self.running:
            self.read_first_level_commands()
            self.handle_command()
            self.clean_screen()

    def handle_command(self):
        actions = {
            1: self.add_task,
            2: self.view_tasks,
            3: self.delete_task,
            4: self.update_task,
            5: self.finish_program
        }

        action = actions.get(int(self.command), self.invalid_command)
        action()

    def add_task(self):
        print(Fore.GREEN + "Ejecutando: Agregar una nueva tarea" + Style.RESET_ALL)
        register = RecordTasks()
        register.title = input("Ingrese el título de la tarea: ")
        register.priority = int(input("Ingrese la prioridad de la tarea \n" + \
                                        Fore.CYAN + f"{self.load_priorities()}\n" + Style.RESET_ALL + \
                                        Fore.YELLOW + "(número entero): " + Style.RESET_ALL))
        register.record_task()
        
    def view_tasks(self):
        print(Fore.GREEN + "Ejecutando: Listar tareas" + Style.RESET_ALL)
        input_action = self.read_search_options()
        list_tasks = ListTasks()
        list_actions = {
            1: list_tasks.search_all_task,
            2: list_tasks.search_task_by_title,
            3: list_tasks.list_tasks_by_priority,
            4: list_tasks.search_all_tasks_by_priority
        }
        list_action = list_actions.get(int(input_action), self.invalid_command)
        list_action() if input_action == 1 or input_action == 4 else \
        list_action(input("Ingrese el valor de búsqueda: ") if input_action == 2 else\
        int(input("Ingrese la prioridad (número entero): ")))

    def delete_task(self):
        print(Fore.GREEN + "Ejecutando: Eliminar una tarea existente" + Style.RESET_ALL)

    def update_task(self):
        print(Fore.GREEN + "Ejecutando: Actualizar el estado de una tarea" + Style.RESET_ALL)

    def invalid_command(self):
        print(Fore.RED + "Comando inválido. Por favor, intente de nuevo." + Style.RESET_ALL)

    def finish_program(self):
        self.running = False
    
    def clean_screen(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def read_first_level_commands(self):
        while True:
            command = input(Fore.CYAN + f"Ingrese una opción a realizar\n" \
            f"1. {self.commands[1]}\n" \
            f"2. {self.commands[2]}\n" \
            f"3. {self.commands[3]}\n" \
            f"4. {self.commands[4]}\n" \
            f"5. {self.commands[5]}\n" + Style.RESET_ALL).strip()
            if command and command.isdigit() and int(command) in self.commands:
                self.command = command
                break
            else:
                print(Fore.RED + "Entrada inválida. Por favor, intente de nuevo." + Style.RESET_ALL)

    def load_priorities(self):
        return Priotity.Priotities
    
    def read_search_options(self):
        while True:
            option = input(Fore.CYAN + f"Seleccione una opción de búsqueda:\n" \
            f"1. Ver todas las tareas\n" \
            f"2. Buscar por título\n" \
            f"3. Listar por prioridad\n" \
            f"4. Listar todas las tareas por prioridad\n" + Style.RESET_ALL).strip()
            if option and option.isdigit() and int(option) in [1, 2, 3, 4]:
                return int(option)
            else:
                print(Fore.RED + "Entrada inválida. Por favor, intente de nuevo." + Style.RESET_ALL)