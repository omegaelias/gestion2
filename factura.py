class Factura:
    def __init__(self, cliente, vendedor, productos):
        self.cliente = cliente
        self.vendedor = vendedor
        self.productos = productos
        
    def imprimir(self):
        print(f"cliente{self.cliente.imprimir()}")
        print(f"vendedor: {self.vendedor.imprimir()}")
        print(f"producto: {self.productos.imprimir()}")