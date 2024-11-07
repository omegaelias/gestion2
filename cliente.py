class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.historial_compras = []
    
    def agregar_compra(self, compra):
        self.historial_compras.append(compra)
    
    def mostrar_info(self):
        return f"ID: {self.id_cliente} | Cliente: {self.nombre} | Email: {self.email} | Compras realizadas: {len(self.historial_compras)}"
