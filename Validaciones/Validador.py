# -*- coding: utf-8 -*-

from Formato.config import MARGEN   

"""Valida entradas del usuario."""
def pedir_opcion(validas):
    """
    Solicita al usuario una opción valida de la lista.
    Si la entrada no esta en las opciones, la ignora y vuelve a pedir.

    Args:
        validas (list[str]): Lista de valores permitidos.

    Returns:
        str: La opcion elegida.
    """
    while True:
        opcion =input(" " * int(MARGEN / 4) + "Selecciona una opcion: ").strip() # se agrega espacio x el margen establecido /4 para que sea apenas una sangria
        if opcion in validas:
            return opcion
        else:
            print(f" Entrada invalida. Opciones validas: {', '.join(validas)}") # Muestra las opciones válidas si la entrada es incorrecta
