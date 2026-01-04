"""
storage.py, Gestiona la persistencia de las tareas

Se encarga de:
- Guardar las tareas en un archivo JSON
- Cargar las tareas desde ese archivo
"""
import json
import os

from task import Task

#Ruta del archivo donde se guardan las tareas
FILE_PATH = "data/tareas.json"

def load_tasks():
    #Carga las tareas desde el archivo JSON
    #Return lista de objetos tasks

    #Si el archivo no existe, devolvemos la lista vacia
    if not os.path.exists(FILE_PATH):
        return []
    
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file: #Con with open abrimos el archivo en modo lectura y con with nos aseguramos de que se va a cerrar solo
            data = json.load(file) # Aqui leemos el json y data sera una lista de diccionarios

            #Convertimos cada diccionario en un objeto task
            tasks = []
            for item in data:
                task = Task(
                    title=item["title"],
                    completed=item["completed"]
                )
                tasks.append(task)

            return tasks

    except (json.JSONDecodeError, KeyError):
        #Si el archivo esta corrupto o mal formado
        print("Error al leer el archivo de tareas, se iniciara vacio")
        return []

def save_tasks(tasks):
    #Guardar la lista de tareas en el archivo json, el parametro task es la lista de objetos Task

    #Aseguramos que la carpeta 'data' existe
    os.makedirs(os.path.dirname(FILE_PATH), exists_ok=True)

    #Convertimos las tareas en diccionarios
    data = []
    for task in tasks:
        data.append({
            "title": task.title,
            "completed": task.completed
        })

    #Escribimos el archivo json
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=2, #Esto sirve para que sea legible (es para guardarlo en formato bonito)
            ensure_ascii=False #Esto sirve para que soporte acentos
        )
