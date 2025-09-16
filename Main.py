"""
Main.py
========
Este archivo es el punto de entrada del conversor.
Muestra un menú de opciones y llama a las funciones correspondientes.
"""
from Conversores import ConvertAbinario, ConvertAdecimal # se importan las funciones de los archivos binario.py y decimal.py de la carpeta conversores
from Validaciones.Validador import pedir_opcion # se importa de la carpeta validaciones el archivo validador la función pedir_opcion para poder verificar la entrada del usuario

def decimal_a_binario():
    """Convierte un número decimal a binario.""" # comentarios para docstring se ven reflejados en archivo Documentacion.md
    print("Convertir de decimal a binario")

def binario_a_decimal():
    """Convierte un número binario a decimal."""
    print("Convertir de binario a decimal")

def salir():
    """Finaliza la ejecución del programa."""
    print("Saliendo del programa...")
    exit()

def main():
    """
    Función principal que ejecuta el menú del conversor.

    - Muestra opciones al usuario.
    - Llama a la función correspondiente según la elección.
    - Permite salir del programa.
    """
    # Diccionario que mapea opciones a funciones
    opciones = {
        "1": decimal_a_binario,
        "2": binario_a_decimal,
        "3": salir
    }
    while True:
            print("\n--- CONVERSOR DE NÚMEROS ---")
            print("1. Decimal a Binario")
            print("2. Binario a Decimal")
            print("3. Salir")

            opcion = pedir_opcion(list(opciones.keys()))  # Llama a la función para pedir opción válida
            opciones[opcion]()  # Ejecuta la función correspondiente


if __name__ == "__main__":
    main()
