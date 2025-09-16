# -*- coding: utf-8 -*-

"""Convierte un numero decimal a binario."""

from Formato.finalizacion import salir # se importa la función salir del archivo finalizacion.py de la carpeta formato
from Formato.menu import MARGEN # se importa la variable margen del archivo menu.py de la carpeta formato


def es_decimal(cadena: str) -> bool:
    """Verifica si una cadena representa un numero decimal (entero positivo)."""
    return cadena.isdigit() # metodo de python devuelve True si todos los caracteres de la cadena son dígitos (0-9) y la cadena no está vacía.

def decimal_a_binario():
    """Convierte un numero decimal a binario.""" 
    print("\nConvertir de DECIMAL a BINARIO ( Presione * para salir)")
    valor = input(" " * MARGEN + "\nIngrese un valor DECIMAL: ")
    # Verificar si el usuario desea salir
    if valor == "*":
       salir() #llama a la función salir para finalizar el programa

    if not es_decimal(valor): # se llama a la bandera que verifica si el valor es binario, si no lo es, muestra el mensaje de error
        print(" " * MARGEN + "\nError: El valor ingresado no es un numero decimal.")
        return  
   # convertir a entero
    valor = int(valor)

    # convertir a binario y mostrar resultado
    binario = bin(valor)[2:]  # [2:] elimina el prefijo '0b' que agrega Python
    print(" " * MARGEN + f"\nEl numero decimal {valor} en binario es: {binario}")

