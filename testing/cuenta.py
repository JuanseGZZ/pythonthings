class Cuenta:
    def __init__(self, usuario, contrasenia,dni):
        self.usuario = usuario
        self.__contrasenia = contrasenia
        self.dni = dni

    def mostrar_contrasenia(self):
        return self.__contrasenia