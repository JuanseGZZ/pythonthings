# registro_perfiles.py

import os

def cargar_nombres(path_txt: str) -> set:
    nombres = set()
    if os.path.exists(path_txt):
        with open(path_txt, "r", encoding="utf-8") as f:
            for linea in f:
                if "|" in linea:
                    nombre, _ = linea.strip().split("|", 1)
                    nombres.add(nombre.strip())
    return nombres

def guardar_si_nuevo(path_txt: str, nombre: str, url: str) -> bool:
    nombre = nombre.strip()
    url = url.strip()
    nombres_existentes = cargar_nombres(path_txt)

    if nombre in nombres_existentes:
        return False  # Ya registrado

    with open(path_txt, "a", encoding="utf-8") as f:
        f.write(f"{nombre} | {url}\n")
    return True  # Nuevo registro agregado
