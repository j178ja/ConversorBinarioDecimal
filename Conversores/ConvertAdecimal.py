"""Convierte un número binario a decimal."""

def binario_a_decimal(binario):
    decimal = 0
    binario = binario[::-1]  # Se invierte la cadena para recorrerla de derecha a izquierda
    for i in range(len(binario)):
        if binario[i] == '1':
            decimal += 2**i
    return decimal