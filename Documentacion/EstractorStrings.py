# -*- coding: utf-8 -*-
"""
EstractorStrings.py
==================
Extrae todos los docstrings de los archivos Python del proyecto
y los guarda en Documentacion/DocumentacionProyecto.md
Ignora cualquier caracter que no pueda decodificarse.
"""
import os
import ast

# Carpeta del proyecto
proyecto_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
output_dir = os.path.join(proyecto_dir, "Documentacion")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "DocumentacionProyecto.md")

# Función para extraer docstrings de un archivo
def extraer_docstrings(archivo_path):
    docstrings = []

    # Abrir el archivo ignorando errores de decodificación
    try:
        with open(archivo_path, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
    except Exception:
        return []  # Ignora archivos que no se puedan leer

    try:
        tree = ast.parse(contenido)
    except SyntaxError:
        return []  # Ignora archivos con errores de sintaxis

    # Docstring del módulo
    modulo_doc = ast.get_docstring(tree)
    if modulo_doc:
        docstrings.append(("Modulo", os.path.basename(archivo_path), modulo_doc))

    # Docstrings de funciones y clases
    for nodo in ast.walk(tree):
        if isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(nodo)
            if doc:
                docstrings.append(("Funcion", nodo.name, doc))
        elif isinstance(nodo, ast.ClassDef):
            doc = ast.get_docstring(nodo)
            if doc:
                docstrings.append(("Clase", nodo.name, doc))

    return docstrings

# Recorrer el proyecto y generar documentación
with open(output_file, "w", encoding="utf-8") as f_out:
    f_out.write("# Documentacion del proyecto\n\n")
    for root, _, files in os.walk(proyecto_dir):
        # Ignorar la carpeta Documentacion para no incluir el mismo script
        if "Documentacion" in root:
            continue
        for archivo in files:
            if archivo.endswith(".py"):
                ruta_archivo = os.path.join(root, archivo)
                docs = extraer_docstrings(ruta_archivo)
                if docs:
                    f_out.write(f"## Archivo: {os.path.relpath(ruta_archivo, proyecto_dir)}\n\n")
                    for tipo, nombre, doc in docs:
                        f_out.write(f"### {tipo}: {nombre}\n\n")
                        f_out.write(f"{doc}\n\n")

print(f"Documentacion generada en: {output_file}")
