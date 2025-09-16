# -*- coding: utf-8 -*-

"""
Archivo de configuracion global.
Contiene constantes y parámetros usados en toda la aplicacion.
"""

from pyfiglet import Figlet # importa la librería pyfiglet para mostrar texto en ASCII art


# Dimensiones y estilo
MARGEN = 15
HEIGHT = 5
WIDTH = 50                       # ancho del recuadro del menu
CARACTER_HORIZONTAL = "─"        # empleado para el recuadro horizontal interno de la app
CARACTER_VERTICAL = "│"          # empleado para el recuadro vertical interno de la app
CARACTER_UNION = "+"             # emleado para las esquinas del recuadro externo de la app
CARACTER_DOBLE_VERTICAL = "││"   # emleado para el recuadro vertical externo de la app
CARACTER_DOBLE_HORIZONTAL = "═"  # emleado para el recuadro horizontal externo de la app
f = Figlet(font='digital')       #tipo dde fuente ASCII art