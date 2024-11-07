
from persona import Persona

class Vendedor(Persona):
    def __init__(self, nombre, domicilio, telefono, mail):
        super().__init__(nombre,domicilio, telefono,mail)