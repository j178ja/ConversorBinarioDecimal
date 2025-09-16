"""
Main.py
========
Este archivo es el punto de entrada del conversor.
Muestra un menú de opciones y llama a las funciones correspondientes.
"""                     # comentarios para docstring se ven reflejados en archivo Documentacion.md
from Conversores import ConvertAbinario, ConvertAdecimal # se importan las funciones de los archivos binario.py y decimal.py de la carpeta conversores
from Validaciones.Validador import pedir_opcion # se importa de la carpeta validaciones el archivo validador la función pedir_opcion para poder verificar la entrada del usuario

# Region DECIMAL A BINARIO

def decimal_a_binario():
    """Convierte un número decimal a binario.""" 
    print("Convertir de DECIMAL a BINARIO ( Presione * para salir)")
    valor = int(input("Ingrese un valor DECIMAL: "))
    if valor == "*":
       salir()
     
  
#end Region

# Region BINARIO A DECIMAL

def es_binario(cadena: str) -> bool:  #se establece una bandera para verificar si el numero es binario
    """Verifica si una cadena representa un número binario."""
    return set(cadena).issubset({"0", "1"})# verifica que los componentes de la cadena sean 0 o 1 (números binarios))

def binario_a_decimal():
    """Convierte un número binario a decimal."""
    print("Convertir de BINARIO a DECIMAL ( Presione * para salir)")
    valor = int(input("Ingrese un valor BINARIO: "))
    if valor == "*":
       salir()
     
    if not es_binario(valor): # se llama a la bandera que verifica si el valor es binario, si no lo es, muestra el mensaje de error
        print(" Error: El valor ingresado no es un número binario.")
        return

    decimal = int(valor, 2)
    print(f" El número binario {valor} equivale a {decimal} en decimal.")

   #end Region   
def salir():
    """Finaliza la ejecución del programa."""
    print("Saliendo del programa...") # mensaje de salida
    exit()    # Fin y salida del programa

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
        "*": salir
    }
    while True:
            print("\n--- CONVERSOR DE NÚMEROS ---")
            print("1. Decimal a Binario")
            print("2. Binario a Decimal")
            print("*. Salir")

            opcion = pedir_opcion(list(opciones.keys()))  # Llama a la función para pedir opción válida
            opciones[opcion]()  # Ejecuta la función correspondiente


if __name__ == "__main__":
    main()
