# -*- coding: utf-8 -*-

"""Programa para mostrar una animacion al finalizar el programa"""

import time
import sys
from Formato.config import MARGEN  # importa la constante MARGEN del archivo config.py

def salir() -> None:
    """Finaliza la ejecucion del programa con una animacion."""
    mensaje = "Saliendo del programa"
    print(" " * MARGEN + mensaje, end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()
    sys.exit(0)