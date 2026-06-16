# utils/data_reader.py
import csv
import json
from pathlib import Path

def leer_csv_login(nombre_archivo="users.csv"):
    ruta = Path(__file__).parent.parent / "data" / nombre_archivo
    datos = []
    
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            usuario = fila['username'].strip()
            clave = fila['password'].strip()
            es_valido = fila['valid'].strip().lower() == 'true'
            datos.append((usuario, clave, es_valido))
            
    return datos

def leer_json_productos(nombre_archivo="productos.json"):
    """Lee el archivo JSON de productos utilizando rutas dinámicas."""
    ruta = Path(__file__).parent.parent / "data" / nombre_archivo
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)