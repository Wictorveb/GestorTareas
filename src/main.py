#Importamos la clase principal que gestiona las tareas
from task_manager import TaskManager

def show_menu():
    #Muestra el menu en la consola, no hace nada
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    #Funcion principal del programa

    #Creamos una instancia del gestor de tareas
    #Aquí se cargaran las tareas desde el archivo JSON
    manager = TaskManager

    #Bucle infinito, el programa se seguirá ejecutando hasta que el usuario eliga salir
    while True:
        show_menu()

        #Leemos la opción elegida por el usuario
        option=input("Elige una opción (1-5): ").strip()

        #Opcion 1: Añadir una nueva tarea
        if option=="1":
            title=input("Introduce el nombre de la tarea")

            #Validamos que el titulo no esté vacío
            if title:
                manager.ad_task(title)
                print("Tarea añadida correctamente")
            else:
                print("El título no puede estar vacío!")

        #Opcion 2: listar todas las tareas
        if option=="2":
            manager.list_tasks()

        #Opcion 3: Marcar una actividad como realizada
        if option=="3":
            manager.list_tasks()
            try:
                index = int(input("Número de tarea a completar: "))
                manager.complete_task(index - 1)
                print("Tarea marcada como completada")
            except ValueError:
                print("Debes introducir un número válido")

        #Opcion 4: Eliminar una tarea
        if option=="4":
            manager.list_tasks()
            try:
                index = int(input("Número de la tarea a eliminar: "))
                manager.delete_task(index - 1)
                print("Tarea eliminada correctamente")
            except ValueError:
                print("Debes introducir un número válido")

        #Opcion 5: Salir del programa
        if option=="5":
            print("Has decidido salir del programa")
            break

#Esta condición asegura que el main solo se ejecute cuando este archivo es ejecutado directamente y no cuando se importa desde otro archivo
if __name__ == "__main__":
    main()