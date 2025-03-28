import random

palabras = [
    "python", "programacion", "inteligencia", "artificial", "juego", "computadora", "teclado", "raton", "pantalla",
    "internet", "red", "servidor", "cliente", "base", "datos", "algoritmo", "variable", "funcion", "clase", "objeto",
    "metodo", "herencia", "polimorfismo", "encapsulamiento", "modulo", "paquete", "sintaxis", "compilador", "interprete",
    "debugger", "error", "excepcion", "bucle", "condicional", "logica", "binario", "decimal", "hexadecimal", "octal",
    "cadena", "lista", "tupla", "diccionario", "conjunto", "archivo", "sistema", "operativo", "memoria", "procesador",
    "disco", "almacenamiento", "redes", "seguridad", "criptografia", "hash", "encriptacion", "desencriptacion", "token",
    "autenticacion", "autorizacion", "usuario", "contraseña", "sesion", "cookie", "dominio", "host", "puerto", "protocolo",
    "http", "https", "ftp", "ssh", "dns", "ip", "tcp", "udp", "socket", "firewall", "vpn", "proxy", "servidorweb",
    "servidorftp", "servidordns", "servidorcorreo", "html", "css", "javascript", "framework", "biblioteca", "frontend",
    "backend", "fullstack", "desarrollador", "ingeniero", "software", "hardware", "robotica", "automatizacion"
]

def obtener_palabra_aleatoria():
    return random.choice(palabras)
