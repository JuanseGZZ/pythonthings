#v1
def calc(numero1, numero2, operacion):
    if operacion == '+':
        if numero1 == numero1:
            if numero2 == numero2:
                resultado_suma = numero1 + numero2
                print("El resultado es:", resultado_suma)
    elif operacion == '-':
        if numero1 == numero1:
            if numero2 == numero2:
                resultado_resta = numero1 - numero2
                print("El resultado es:", resultado_resta)
    elif operacion == '*':
        if numero1 == numero1:
            if numero2 == numero2:
                resultado_multiplicacion = numero1 * numero2
                print("El resultado es:", resultado_multiplicacion)
    elif operacion == '/':
        if numero1 == numero1:
            if numero2 != 0:
                resultado_division = numero1 / numero2
                print("El resultado es:", resultado_division)
            else:
                print("Error: no se puede dividir por cero")
    else:
        print("Operación no reconocida")

#v2
def calcular(numero1, numero2, operacion):
    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '*':
        resultado = numero1 * numero2
    elif operacion == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Error: no se puede dividir por cero")
            return
    else:
        print("Operación no reconocida")
        return

    print("El resultado es:", resultado)

#v3

def sumar(numero1, numero2):
    return numero1 + numero2

def restar(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        print("Error: no se puede dividir por cero")
        return None

def calcular(numero1, numero2, operacion):
    if operacion == '+':
        resultado = sumar(numero1, numero2)
    elif operacion == '-':
        resultado = restar(numero1, numero2)
    elif operacion == '*':
        resultado = multiplicar(numero1, numero2)
    elif operacion == '/':
        resultado = dividir(numero1, numero2)
        if resultado is None:
            return
    else:
        print("Operación no reconocida")
        return

    print("El resultado es:", resultado)

    #v4
    # Constantes para los operadores
OPERADOR_SUMA = '+'
OPERADOR_RESTA = '-'
OPERADOR_MULTIPLICACION = '*'
OPERADOR_DIVISION = '/'

# Funciones para cada operación
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: no se puede dividir por cero")
        return None

# Diccionario de operaciones
OPERACIONES = {
    OPERADOR_SUMA: sumar,
    OPERADOR_RESTA: restar,
    OPERADOR_MULTIPLICACION: multiplicar,
    OPERADOR_DIVISION: dividir,
}

def calcular(a, b, op):
    operacion = OPERACIONES.get(op)
    if operacion:
        resultado = operacion(a, b)
        if resultado is not None:
            print("El resultado es:", resultado)
    else:
        print("Operación no reconocida")

#v5

# Constantes para los operadores
OPERADOR_SUMA = '+'
OPERADOR_RESTA = '-'
OPERADOR_MULTIPLICACION = '*'
OPERADOR_DIVISION = '/'

# Funciones para cada operación
def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números, manejando la división por cero."""
    if b == 0:
        raise ValueError("Error: no se puede dividir por cero")
    return a / b

# Diccionario de operaciones
OPERACIONES = {
    OPERADOR_SUMA: sumar,
    OPERADOR_RESTA: restar,
    OPERADOR_MULTIPLICACION: multiplicar,
    OPERADOR_DIVISION: dividir,
}

def calcular(a, b, op):
    """
    Realiza una operación matemática entre dos números.

    :param a: Primer número.
    :param b: Segundo número.
    :param op: Operador matemático (por ejemplo, '+', '-', '*', '/').
    """
    operacion = OPERACIONES.get(op)
    if not operacion:
        raise ValueError(f"Operación no reconocida: {op}")
    return operacion(a, b)

# Ejecución principal (separada de la lógica de cálculo)
if __name__ == "__main__":
    try:
        # Ejemplo de entrada
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        op = input("Ingrese la operación (+, -, *, /): ")

        resultado = calcular(a, b, op)
        print("El resultado es:", resultado)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Ocurrió un error inesperado:", e)


#v6 

# Funciones para cada operación
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Error: no se puede dividir por cero")
        return None
    return a / b

# Diccionario de operaciones
OPERACIONES = {
    '+': sumar,
    '-': restar,
    '*': multiplicar,
    '/': dividir,
}

def calcular(a, b, op):
    """
    Realiza una operación matemática entre dos números.

    :param a: Primer número.
    :param b: Segundo número.
    :param op: Operador matemático (por ejemplo, '+', '-', '*', '/').
    """
    operacion = OPERACIONES.get(op)
    if operacion:
        resultado = operacion(a, b)
        if resultado is not None:
            print("El resultado es:", resultado)
    else:
        print("Operación no reconocida")


#v7
# Funciones para cada operación
def sumar(numero1, numero2):
    return numero1 + numero2

def restar(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(dividendo, divisor):
    if divisor == 0:
        print("Error: no se puede dividir por cero")
        return None
    return dividendo / divisor

# Diccionario de operaciones
OPERACIONES = {
    '+': sumar,
    '-': restar,
    '*': multiplicar,
    '/': dividir,
}

def calcular(numero1, numero2, operador):
    """
    Realiza una operación matemática entre dos números.

    :param numero1: Primer número.
    :param numero2: Segundo número.
    :param operador: Operador matemático (por ejemplo, '+', '-', '*', '/').
    """
    operacion = OPERACIONES.get(operador)
    if operacion:
        resultado = operacion(numero1, numero2)
        if resultado is not None:
            print("El resultado es:", resultado)
    else:
        print("Operación no reconocida")