# -*- coding: utf-8 -*-

"""
Main.py
========
Este archivo es el punto de entrada del conversor.
Muestra un menú de opciones y llama a las funciones correspondientes.
"""                     # comentarios para docstring se ven reflejados en archivo Documentacion.md



#Importa desde los archivos necesarios las funciones que se van a utilizar

from Formato.finalizacion import salir # se importa la función salir del archivo finalizacion.py de la carpeta formato
from Formato.menu import mostrar_menu # se importa la función mostrar_menu del archivo menu.py de la carpeta formato
from Conversores.ConvertAbinario import decimal_a_binario #llama a la función decimal_a_binario para convertir de decimal a binario
from Conversores.ConvertAdecimal import binario_a_decimal #llama a la función binario_a_decimal para convertir de binario a decimal
from Validaciones.Validador import pedir_opcion # se importa de la carpeta validaciones el archivo validador la función pedir_opcion para poder verificar la entrada del usuario



def main():  
    """
    Función principal que ejecuta el menú del conversor.

    - Muestra opciones al usuario.
    - Llama a la función correspondiente según la elección.
    - Permite salir del programa.
    """
    # Diccionario que mapea opciones a funciones
    opciones = {
        "1": decimal_a_binario, #llama a la función decimal_a_binario 
        "2": binario_a_decimal, #llama a la función binario_a_decimal 
        "*": salir              #llama a la función salir 
    }
    while True:
        mostrar_menu()
        opcion = pedir_opcion(list(opciones.keys()))   # Llama a la función para pedir opción válida
        opciones[opcion]()                             # Ejecuta la función correspondiente

if __name__ == "__main__":
    main()
