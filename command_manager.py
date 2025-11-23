from actions.record_tasks import RecordTasks, Priotity
from colorama import Fore, Style

class CommandManager:
    def __init__(self):
        self.command: int = None
        self.commands = {
            1: "Agregar una nueva tarea",
            2: "Ver todas las tareas",
            3: "Eliminar una tarea existente",
            4: "Actualizar el estado de una tarea"
        }

    def execute(self):
        self.read_first_level_commands()
        self.handle_command()

    def handle_command(self):
        actions = {
            1: self.add_task,
            2: self.view_tasks,
            3: self.delete_task,
            4: self.update_task
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
        print(Fore.GREEN + "Ejecutando: Ver todas las tareas" + Style.RESET_ALL)

    def delete_task(self):
        print(Fore.GREEN + "Ejecutando: Eliminar una tarea existente" + Style.RESET_ALL)

    def update_task(self):
        print(Fore.GREEN + "Ejecutando: Actualizar el estado de una tarea" + Style.RESET_ALL)

    def invalid_command(self):
        print(Fore.RED + "Comando inválido. Por favor, intente de nuevo." + Style.RESET_ALL)

    def read_first_level_commands(self):
        while True:
            command = input(Fore.CYAN + f"Ingrese una opción a realizar\n" \
            f"1. {self.commands[1]}\n" \
            f"2. {self.commands[2]}\n" \
            f"3. {self.commands[3]}\n" \
            f"4. {self.commands[4]}\n" + Style.RESET_ALL).strip()
            if command and command.isdigit() and int(command) in self.commands:
                self.command = command
                break
            else:
                print(Fore.RED + "Entrada inválida. Por favor, intente de nuevo." + Style.RESET_ALL)

    def load_priorities(self):
        return Priotity.Priotities