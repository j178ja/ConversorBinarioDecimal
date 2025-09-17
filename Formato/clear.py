# -*- coding: utf-8 -*-

"""clase para limpiar el contenido de la pantalla"""
import msvcrt
import os




def limpiar_pantalla():
    """Limpia la consola segun el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def limpiar_resultado(height_resultado: int) -> None:
    """Borra lineas del resultado sin tocar el menu"""
    for _ in range(height_resultado):
        print("\033[F" + " " * 80 + "\r", end="")  # mueve cursor arriba y borra l�nea
                                                   #  se puso 80 pero deberia ser WIDTH o el ancho de la consola, pero con WIDTH texto que sobresale se ve.


"""clase para pausar hasta que el usuario presiona cualquier tecla"""
def pausar_tecla() -> None:
    print("\nPresiona cualquier tecla para continuar...")
    msvcrt.getch()  # espera hasta que se presione cualquier tecla
