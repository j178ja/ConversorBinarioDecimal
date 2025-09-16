# -*- coding: utf-8 -*-

"""
Main.py
========
Este archivo es el punto de entrada del conversor.
Muestra un menu de opciones y llama a las funciones correspondientes.
"""                     # comentarios para docstring se ven reflejados en archivo Documentacion.md



#Importa desde los archivos necesarios las funciones que se van a utilizar

from Formato.clear import limpiar_resultado, pausar_tecla, limpiar_pantalla # se importa la función limpiar_pantalla y pausar_tecla del archivo clear.py de la carpeta formato
from Formato.finalizacion import salir # se importa la funcion salir del archivo finalizacion.py de la carpeta formato
from Formato.menu import mostrar_menu # se importa la funcion mostrar_menu del archivo menu.py de la carpeta formato
from Conversores.ConvertAbinario import decimal_a_binario #llama a la funcion decimal_a_binario para convertir de decimal a binario
from Conversores.ConvertAdecimal import binario_a_decimal #llama a la funcion binario_a_decimal para convertir de binario a decimal
from Validaciones.Validador import pedir_opcion # se importa de la carpeta validaciones el archivo validador la función pedir_opcion para poder verificar la entrada del usuario



def main():  
    """
    Funcion principal que ejecuta el menu del conversor.

    - Muestra opciones al usuario.
    - Llama a la funcion correspondiente según la eleccion.
    - Permite salir del programa.
    """
    # Diccionario que mapea opciones a funciones
    opciones = {
        "1": decimal_a_binario, #llama a la funcion decimal_a_binario 
        "2": binario_a_decimal, #llama a la funcion binario_a_decimal 
        "*": salir              #llama a la funcion salir 
    }
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = pedir_opcion(list(opciones.keys()))   # Llama a la funcion para pedir opción válida
        opciones[opcion]()                             # Ejecuta la funcion correspondiente
        altura_resultado = 20                          # limpia toda la pnatlla y muestra nuevamente el menu
        pausar_tecla()                                 # espera que el usuario lea el resultado
        limpiar_resultado(altura_resultado)            # borra solo el resultado

if __name__ == "__main__":
    main()
