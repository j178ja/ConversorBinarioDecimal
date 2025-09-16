# -*- coding: utf-8 -*-

"""
Main.py
========
Este archivo es el punto de entrada del conversor.
Muestra un menú de opciones y llama a las funciones correspondientes.
"""                     # comentarios para docstring se ven reflejados en archivo Documentacion.md
#from Conversores import ConvertAbinario, ConvertAdecimal # se importan las funciones de los archivos binario.py y decimal.py de la carpeta conversores
from Validaciones.Validador import pedir_opcion # se importa de la carpeta validaciones el archivo validador la función pedir_opcion para poder verificar la entrada del usuario
from pyfiglet import Figlet # importa la librería pyfiglet para mostrar texto en ASCII art
import os


f = Figlet(font='digital')  #tipo dde fuente ASCII art

margen = 15 #margen para centrar las opciones del menú

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


# Region DECIMAL A BINARIO

def es_decimal(cadena: str) -> bool:
    """Verifica si una cadena representa un número decimal (entero positivo)."""
    return cadena.isdigit() # metodo de python devuelve True si todos los caracteres de la cadena son dígitos (0-9) y la cadena no está vacía.

def decimal_a_binario():
    """Convierte un número decimal a binario.""" 
    print("\nConvertir de DECIMAL a BINARIO ( Presione * para salir)")
    valor = input(" " * margen + "\nIngrese un valor DECIMAL: ")
    # Verificar si el usuario desea salir
    if valor == "*":
       salir() #llama a la función salir para finalizar el programa

    if not es_decimal(valor): # se llama a la bandera que verifica si el valor es binario, si no lo es, muestra el mensaje de error
        print(" " * margen + "\nError: El valor ingresado no es un número decimal.")
        return  
   # convertir a entero
    valor = int(valor)

    # convertir a binario y mostrar resultado
    binario = bin(valor)[2:]  # [2:] elimina el prefijo '0b' que agrega Python
    print(" " * margen + f"\nEl número decimal {valor} en binario es: {binario}")
#end Region

# Region BINARIO A DECIMAL

def es_binario(cadena: str) -> bool:  #se establece una bandera para verificar si el numero es binario
    """Verifica si una cadena representa un número binario."""
    return set(cadena).issubset({"0", "1"})# verifica que los componentes de la cadena sean 0 o 1 (números binarios))

def binario_a_decimal():
    """Convierte un número binario a decimal."""
    print(" " * margen + "\nConvertir de BINARIO a DECIMAL ( Presione * para salir)")
    valor = input(" " * margen + "\nIngrese un valor BINARIO: ")
    # Verificar si el usuario desea salir
    if valor == "*":
       salir() #llama a la función salir para finalizar el programa
     
    if not es_binario(valor): # se llama a la bandera que verifica si el valor es binario, si no lo es, muestra el mensaje de error
        print(" " * margen + "\nError: El valor ingresado no es un número binario.")
        return

    decimal = int(valor, 2)
    print(" " * margen + f"\nEl número binario {valor} equivale a {decimal} en decimal.")

   #end Region   


def salir():
    """Finaliza la ejecución del programa."""
    print(" " * margen + "Saliendo del programa...") # mensaje de salida
    exit()    # Fin y salida del programa



def imprimir_centrada_lineas(texto, ancho=50):
    """
    Imprime varias líneas centradas.
    """
    for linea in texto.splitlines():
        print(linea.center(ancho))

def imprimir_lineaVertical(texto="", ancho=70):
    """
    Imprime una línea con bordes '|' a los lados.
    - texto: contenido de la línea
    - ancho: ancho total del recuadro
    """
    contenido = texto.ljust(ancho - 2)  # deja espacio para los bordes
    print("|" + contenido + "|")

    # Funcion MOSTRAR MENU 
# def mostrar_menu(ancho=70, margen=15, height=20):
#     ancho = 70  #variable de ancho del menú
   
#     print("+" + "-" * (ancho - 2) + "+")
#     titulo = f.renderText("CONVERSOR DE NÚMEROS")
    

#     imprimir_centrada_lineas(titulo, ancho - 2)
#     print("+" + "-" * (ancho - 2) + "+")
#     # Opciones del menú alineadas 
#     print(" " * margen + "1. Decimal a Binario")
#     print(" " * margen + "2. Binario a Decimal")
#     print(" " * margen + "*. Salir")

#     print("+" + "-" * (ancho - 2) + "+") #linea separadora inferior
def mostrar_menu(ancho=70, margen=15, height=20):
    limpiar_pantalla()  # borra todo lo anterior
    titulo = f.renderText("CONVERSOR DE NÚMEROS").splitlines()

    # Línea superior
    print("+" + "-" * (ancho - 2) + "+")

    # Altura disponible
    contenido = []

    # Agregar título centrado
    for linea in titulo:
        contenido.append(linea.center(ancho - 2))

    # Agregar espacio antes de opciones
    contenido.append("")

    # Opciones
    contenido.append(" " * margen + "1. Decimal a Binario")
    contenido.append(" " * margen + "2. Binario a Decimal")
    contenido.append(" " * margen + "*. Salir")

    # Calcular espacio vacío para altura
    while len(contenido) < height:
        contenido.append("")

    # Imprimir cada línea con borde lateral
    for linea in contenido:
        imprimir_lineaVertical(linea, ancho)

    # Línea inferior
    print("+" + "-" * (ancho - 2) + "+")

def main():  
    """
    Función principal que ejecuta el menú del conversor.

    - Muestra opciones al usuario.
    - Llama a la función correspondiente según la elección.
    - Permite salir del programa.
    """
    # Diccionario que mapea opciones a funciones
    opciones = {
        "1": decimal_a_binario, #llama a la función decimal_a_binario def mas arriba
        "2": binario_a_decimal, #llama a la función binario_a_decimal def mas arriba
        "*": salir              #llama a la función salir def mas arriba
    }
    while True:
        mostrar_menu()
        opcion = pedir_opcion(list(opciones.keys()))   # Llama a la función para pedir opción válida
        opciones[opcion]()                             # Ejecuta la función correspondiente

if __name__ == "__main__":
    main()
