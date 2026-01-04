"""

task_manager.py
Contiene la clase TaskManager, responsable de:
- Gestionar la lista de tareas en memoria
- Anadir, Completar, Listar y eliminar tareas
- Guardar los cambios usando el sistema de almacenamiento
"""

#Importamos la calse Task (Modelo de datos)
from task import Task

#Importamos las funciones de persistencia
from storage import load_tasks, save_tasks

class TaskManager:
	#Clase que centraliza toda la logica del gestor de tareas

	def __init__(self):
		"""

		Constructor de la clase, se ejecuta automaticamente al crear una instancia:

			manager = TaskManager()

		Aqui cargamos las tareas desde el archivo (JSON)
		y las guardamos en memoria.
		"""

		self.tasks = load_tasks()

	def add_task(self, title):
		#Anade una tarea al sistema, title es el texto que define la tarea

		#Creamos una nueva tarea (por defecto no viene completada)
		task = Task(title)

		#La anadimos a la lista en memoria
		self.tasks.append(task)

		#Guardamos los cambios en el achivo
		save_tasks(self.tasks)

	def list_tasks(self):
		#Muestra todas las tareas por pantalla

		#Si no hay tareas informamos al usuario
		if not self.tasks:
			print("\nNo hay tareas registradas.")
			return

		print("\nLISTA DE TAREAS")
		#enumerate nos da indice + objeto
		#start=1 para que el usuario vea indices con numeros naturales
		for index, task in enumerate(self.tasks, start=1):

			#Estado visual de la tarea
			status = "Hecha" if task.completed else "Pendiente"

			#Imprimimos cada tarea
			print(f"{index}. [{status}] {task.title}")

	def complete_tasks(self, index):
		#Marca una tarea como completada, index es el indice de la tarea en la lista (base 0) creo que quiere decir que empieza en 0

		#Comprobamos que el indice sea valido
		if 0 <= index <= len(self.tasks):

			#Marcamos la tarea como completada
			self.tasks[index].completed = True

			#Guardamos los cambios
			save_tasks(self.tasks)

		else:
			print("Indice de tarea no valido")

	def delete_task(self, index):
		#Elimina una tarea del sistema, index es el indice en la lista

		#validamos el indice
		if 0 <= index <= len(self.tasks):
			#Eliminamos la tarea
			self.tasks.pop(index)
			#Guardamos los cambios
			save_tasks(self.tasks)
		
		else:
			print("Indice de tarea no valido")
