from celery import Celery
import time

# Celery se conecta a Redis
app = Celery(
    'mis_tareas',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'  # 👈 Esto permite usar .get()
)


# Tarea simple
@app.task
def saludar(nombre):
    print(f"Hola {nombre}")
    time.sleep(3)  # simulamos que tarda
    return f"Saludos para {nombre}"

# Tarea encolada en cola específica
@app.task(queue='cola_seleccionada') 
def sumar(a, b):
    print(f"Sumando {a} y {b}...")
    return a + b

@app.task(queue='default')
def multiplicar(a, b):
    print(f"Multiplicando {a} y {b}...")
    return a * b
