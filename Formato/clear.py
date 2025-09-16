# -*- coding: utf-8 -*-

"""clase para limpiar el contenido de la pantalla"""

import os

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


