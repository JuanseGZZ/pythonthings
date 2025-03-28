from tasks import *

# Ejecutar la tarea en segundo plano
resultado = saludar.delay("Mundo")

# Podés consultar el resultado más tarde
print("Esperando resultado...")
print(resultado.get(timeout=10))  # Bloquea hasta que termine o se agote el tiempo

resultado = multiplicar.delay(2, 3)

print("Esperando resultado...")

print(resultado.get(timeout=10))  # Bloquea hasta que termine o se agote el tiempo