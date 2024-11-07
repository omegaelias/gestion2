from persona import Persona



class Proveedor(Persona):
    def __init__(self, nombre, domicilio, telefono, mail):
        super().__init__(nombre, domicilio, telefono, mail)

def imprimir(self):
    print(self.nombre)
    print(self.domicilio)
    print(self.telefono)
    print(self.mail)

p1 = Proveedor('Josue','Alvear 980','3549780919','enigmaonewin@gmail.com')