# -*- coding: utf-8 -*-


""" Da formato a menu de aplicacion"""

from Formato.config import MARGEN,HEIGHT,WIDTH,CARACTER_VERTICAL ,CARACTER_DOBLE_HORIZONTAL, CARACTER_HORIZONTAL,CARACTER_UNION # importa la constante MARGEN del archivo config.py
from Formato.clear import limpiar_pantalla # importa la función para limpiar contenido de pantalla
from Formato.config import f  # importa la instancia de Figlet desde config.py

def imprimir_centrada_lineas(texto, WIDTH):
    """
    Imprime varias lineas centradas.
    """
    for linea in texto.splitlines():
        print(linea.center(WIDTH))

def imprimir_lineaVertical(texto="", ancho=70):
    """
    Imprime una linea con bordes '|' a los lados.
    - texto: contenido de la linea
    - ancho: ancho total del recuadro
    """
    contenido = texto.ljust(WIDTH - 2)  # deja espacio para los bordes
    print(CARACTER_VERTICAL + contenido + CARACTER_VERTICAL)


def mostrar_menu():
    limpiar_pantalla()  # borra todo lo anterior
    titulo = f.renderText("CONVERSOR DE NUMEROS").splitlines() # Se le aplica el formato ASCII art al título y se divide en líneas

    # Línea superior
    print(CARACTER_UNION + CARACTER_HORIZONTAL * (WIDTH - 2) + CARACTER_UNION)

    # Altura disponible
    contenido = []

    # Agregar título centrado
    for linea in titulo:
        contenido.append(linea.center(WIDTH - 2))

    # Agregar espacio antes de opciones
    contenido.append("")

    # Opciones
    contenido.append(" " * MARGEN + "1. Decimal a Binario")
    contenido.append(" " * MARGEN + "2. Binario a Decimal")
    contenido.append(" " * MARGEN + "*. Salir")

    # Calcular espacio vacío para altura
    while len(contenido) < HEIGHT:
        contenido.append("")

    # Imprimir cada línea con borde lateral
    for linea in contenido:
        imprimir_lineaVertical(linea, WIDTH)

    # Línea inferior
    print(CARACTER_UNION + CARACTER_HORIZONTAL  * (WIDTH - 2) + CARACTER_UNION)
    
