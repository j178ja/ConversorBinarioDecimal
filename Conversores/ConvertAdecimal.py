# -*- coding: utf-8 -*-

"""Convierte numeros de Binario a Decimal"""

from Formato.finalizacion import salir # se importa la funci�n salir del archivo finalizacion.py de la carpeta formato
from Formato.menu import MARGEN # se importa la variable margen del archivo menu.py de la carpeta formato


def es_binario(cadena: str) -> bool:  #se establece una bandera para verificar si el numero es binario
    """Verifica si una cadena representa un n�mero binario."""
    return set(cadena).issubset({"0", "1"})# verifica que los componentes de la cadena sean 0 o 1 (n�meros binarios))

def binario_a_decimal():
    """Convierte un n�mero binario a decimal."""
    print(" " * MARGEN + "\nConvertir de BINARIO a DECIMAL ( Presione * para salir)")
    valor = input(" " * MARGEN + "\nIngrese un valor BINARIO: ")
    # Verificar si el usuario desea salir
    if valor == "*":
       salir() #llama a la funci�n salir para finalizar el programa
     
    if not es_binario(valor): # se llama a la bandera que verifica si el valor es binario, si no lo es, muestra el mensaje de error
        print(" " * MARGEN + "\nError: El valor ingresado no es un n�mero binario.")
        return

    decimal = int(valor, 2)
    print(" " * MARGEN + f"\nEl n�mero binario {valor} equivale a {decimal} en decimal.")
