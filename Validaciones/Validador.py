# -*- coding: utf-8 -*-

from Formato.config import MARGEN   

"""Valida entradas del usuario."""
def pedir_opcion(validas):
    """
    Solicita al usuario una opción válida de la lista.
    Si la entrada no está en las opciones, la ignora y vuelve a pedir.

    Args:
        validas (list[str]): Lista de valores permitidos.

    Returns:
        str: La opción elegida.
    """
    while True:
        opcion =input(" " * int(MARGEN / 4) + "Selecciona una opción: ").strip() # se agrega espacio x el margen establecido /4 para que sea apenas una sangria
        if opcion in validas:
            return opcion
        else:
            print(f" Entrada inválida. Opciones válidas: {', '.join(validas)}") # Muestra las opciones válidas si la entrada es incorrecta
