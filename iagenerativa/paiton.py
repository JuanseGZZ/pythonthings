def sumar_numeros(a, b):
    return a + b

def dividir_numeros(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except TypeError:
        return "Error: Ambos valores deben ser números."

def sumarydividir_numeros(a, b):
    suma = sumar_numeros(a, b)
    division = dividir_numeros(a, b)
    return suma, division