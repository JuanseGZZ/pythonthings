# Implementación de búsqueda binaria para mejorar el rendimiento

def binary_search(word_list, target):
    # Asegurarse de que la lista esté ordenada
    word_list.sort()
    left, right = 0, len(word_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if word_list[mid] == target:
            return word_list[mid]
        elif word_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

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

print(binary_search(palabras, "python"))