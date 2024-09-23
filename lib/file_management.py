import os

def leer_archivo(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("Este archivo ha sido creado automáticamente.\n")
        return "Este archivo ha sido creado automáticamente.\n"
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def escribir_archivo(ruta_archivo, contenido):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)