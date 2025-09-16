# -*- coding: utf-8 -*-

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
        opcion = input("Selecciona una opción: ").strip()
        if opcion in validas:
            return opcion
        else:
            print(f" Entrada inválida. Opciones válidas: {', '.join(validas)}") # Muestra las opciones válidas si la entrada es incorrecta
