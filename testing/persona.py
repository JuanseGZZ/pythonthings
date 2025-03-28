import cuenta as c

class Persona:
    __personas = []

    def __init__(self,nombre,apellido,estatura,edad,Cuenta = None):
        self.nombre = nombre
        self.apellido = apellido
        self.estatura = estatura
        self.edad = edad


    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Estatura: {self.estatura}, Edad: {self.edad}"

    def crear_cuenta(self):
        usuario = input("Agregar un nombre de usuario: ")
        contrasenia = input("Agregar una contraseña: ")
        dni = input("Agregue su dni: ")
        self.Cuenta = c.Cuenta(usuario, contrasenia, dni)

    def mostrar_datos_cuenta(self):
        return f"{self.Cuenta.usuario} | {self.Cuenta.mostrar_contrasenia()} | {self.Cuenta.dni}"
    
    @classmethod
    def add_persona(cls,persona):
        if isinstance(persona, Persona):
            cls.__personas.append(persona)
        else:
            return ValueError("Agrega solo instancias de persona")
        
    @classmethod
    def get_personas(cls):
        return cls.__personas.copy()