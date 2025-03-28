def calc(a, b, op):
    if op == '+':
        if a == a:
            if b == b:
                resultado = a + b
                print("El resultado es:", resultado)
    elif op == '-':
        if a == a:
            if b == b:
                r = a - b
                print("El resultado es:", r)
    elif op == '*':
        if a == a:
            if b == b:
                rr = a * b
                print("El resultado es:", rr)
    elif op == '/':
        if a == a:
            if b != 0:
                rta = a / b
                print("El resultado es:", rta)
            else:
                print("Error: no se puede dividir por cero")
    else:
        print("Operación no reconocida")