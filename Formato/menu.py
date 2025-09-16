# -*- coding: utf-8 -*-


""" Da formato a menu de aplicacion"""

from config import MARGEN # importa la constante MARGEN del archivo config.py
from clear import limpiar_pantalla # importa la funci�n para limpiar contenido de pantalla
from pyfiglet import Figlet # importa la librer�a pyfiglet para mostrar texto en ASCII art
from config import f  # importa la instancia de Figlet desde config.py

def imprimir_centrada_lineas(texto, ancho=50):
    """
    Imprime varias l�neas centradas.
    """
    for linea in texto.splitlines():
        print(linea.center(ancho))

def imprimir_lineaVertical(texto="", ancho=70):
    """
    Imprime una l�nea con bordes '|' a los lados.
    - texto: contenido de la l�nea
    - ancho: ancho total del recuadro
    """
    contenido = texto.ljust(ancho - 2)  # deja espacio para los bordes
    print("|" + contenido + "|")


def mostrar_menu(ancho=70, MARGEN=15, height=20):
    limpiar_pantalla()  # borra todo lo anterior
    titulo = f.renderText("CONVERSOR DE N�MEROS").splitlines()

    # L�nea superior
    print("+" + "-" * (ancho - 2) + "+")

    # Altura disponible
    contenido = []

    # Agregar t�tulo centrado
    for linea in titulo:
        contenido.append(linea.center(ancho - 2))

    # Agregar espacio antes de opciones
    contenido.append("")

    # Opciones
    contenido.append(" " * MARGEN + "1. Decimal a Binario")
    contenido.append(" " * MARGEN + "2. Binario a Decimal")
    contenido.append(" " * MARGEN + "*. Salir")

    # Calcular espacio vac�o para altura
    while len(contenido) < height:
        contenido.append("")

    # Imprimir cada l�nea con borde lateral
    for linea in contenido:
        imprimir_lineaVertical(linea, ancho)

    # L�nea inferior
    print("+" + "-" * (ancho - 2) + "+")
