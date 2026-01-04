"""
task.py
Define la clase task, que representa a una tarea individual
"""

class Task:
    """
    Clase que representa una tarea
    Cada instancia de esta clase es de una tarea concreta
    """

    def __init__(self, title, completed=False):
        """

        Constructor de la clase task, se ejecuta automaticamente cuando creamos una tarea
        
            task=Task("Comprar pan")

        title: Nombre que describe la tarea
        completed: Indica si esta completada o no, por defecto es False
        """

        #Titulo o descripcion de la tarea
        self.title = title

        #Estado de la tarea (True = completada, False = Penediente)
        self.completed = completed

    def __repr__(self): #Solamente sirve que para cuando se imrima una tarea lo puedas ver en debug
        """

        Representacion interna del objeto Task. Se usa principalmente para depuracion (debug)
        Ejemplo:
            Task(title='Comprar pan', completed=False)
        """
        return f"Task(title={self.title!r}, completed={self.completed})"

    def mark_completed(self):
        # Marca la tarea como completada

        self.completed = True
