class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
    
    def mostrar_info(self):
        return f"ID: {self.id_producto} | Producto: {self.nombre} | Precio: {self.precio} | Stock: {self.cantidad} | Categoría: {self.categoria}"
    
    def actualizar_stock(self, cantidad_vendida):
        if self.cantidad >= cantidad_vendida:
            self.cantidad -= cantidad_vendida
            return True
        else:
            print(f"Error: No hay suficiente stock de {self.nombre}. Solo quedan {self.cantidad} unidades.")
            return False

