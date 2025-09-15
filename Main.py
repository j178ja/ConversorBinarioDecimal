"""
Main.py
========
Este archivo es el punto de entrada del conversor.
Muestra un menú de opciones y llama a las funciones correspondientes.
"""

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

        opcion = input("Selecciona una opción: ")

        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print(" Opción no válida.")

if __name__ == "__main__":
    main()
