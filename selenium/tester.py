from registro_perfiles import guardar_si_nuevo

nombre = "María Fernández dosela"
url = "https://linkedin.com/in/mariafernandez"

archivo = "reclutadores.txt"

if guardar_si_nuevo(archivo, nombre, url):
    print("✅ Registro guardado.")
else:
    print("⚠️ Ya estaba registrado.")
