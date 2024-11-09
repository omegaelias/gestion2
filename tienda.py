from datetime import date
from tkinter import Tk, Label, Text, END, Button, PhotoImage, Frame
from tabulate import tabulate

class Entidad:
    def agregar(self):
        print(f"{self.__class__.__name__} agregado correctamente.")
    
    def modificar(self):
        print(f"{self.__class__.__name__} modificado correctamente.")
    
    def eliminar(self):
        print(f"{self.__class__.__name__} eliminado correctamente.")
        
    def listar(self):
        print(f"Listado de {self.__class__.__name__}.")

# Clase Producto
class Producto(Entidad):
    def __init__(self, idProducto: str, nombre: str, precio: float, descripcion: str, cantidadEnInventario: int):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidadEnInventario = cantidadEnInventario
    
    def actualizarInventario(self, cantidadVendida: int):
        if cantidadVendida <= self.cantidadEnInventario:
            self.cantidadEnInventario -= cantidadVendida
            print(f"Inventario actualizado. Quedan {self.cantidadEnInventario} unidades de {self.nombre}.")
        else:
            print("No hay suficiente inventario.")
    
    def calcularPrecioConImpuesto(self, impuesto: float = 0.15):
        precioFinal = self.precio * (1 + impuesto)
        return precioFinal

# Clase Cliente
class Cliente(Entidad):
    def __init__(self, idCliente: str, nombre: str, correo: str, telefono: str, direccion: str):
        self.idCliente = idCliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
    
    def hacerPedido(self, pedido):
        print(f"{self.nombre} ha realizado el pedido con ID {pedido.idPedido}.")
    
    def actualizarDatos(self, nuevoTelefono: str, nuevaDireccion: str):
        self.telefono = nuevoTelefono
        self.direccion = nuevaDireccion
        print(f"Datos del cliente {self.nombre} actualizados.")

# Clase Proveedor
class Proveedor(Entidad):
    def __init__(self, idProveedor: str, nombre: str, contacto: str, telefono: str, direccion: str):
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono
        self.direccion = direccion

# Clase Pedido
class Pedido(Entidad):
    def __init__(self, idPedido: str, cliente: Cliente, productos: list, proveedor: Proveedor, fecha: date):
        self.idPedido = idPedido
        self.cliente = cliente
        self.productos = productos
        self.proveedor = proveedor
        self.fecha = fecha
        self.total = 0
    
    def calcularTotal(self):
        self.total = sum([producto.precio for producto in self.productos])
        print(f"El total del pedido {self.idPedido} es {self.total}.")

    def generarFactura(self):
        factura = Factura(self.idPedido, self.cliente, self.proveedor, self.productos, self.total)
        factura.mostrarFactura()

# Clase Factura
class Factura(Entidad):
    def __init__(self, idPedido: str, cliente: Cliente, proveedor: Proveedor, productos: list, total: float):
        self.idPedido = idPedido
        self.cliente = cliente
        self.proveedor = proveedor
        self.productos = productos
        self.total = total
    
    def mostrarFactura(self):
        # Crear ventana de Tkinter
        ventana = Tk()
        ventana.title("Factura")
        ventana.geometry("700x700")
        ventana.configure(bg="#e0f7fa")

        # Agregar fondo de imagen
        try:
            fondo = PhotoImage(file="background.png")
            fondo_label = Label(ventana, image=fondo)
            fondo_label.place(relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error al cargar la imagen de fondo: {e}")

        # Frame principal
        frame = Frame(ventana, bg="#ffffff", bd=5)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Etiqueta de título
        titulo = Label(frame, text="Factura", font=("Arial", 24, "bold"), fg="#007acc", bg="#ffffff")
        titulo.pack(pady=10)

        # Información del pedido
        info_texto = f"Pedido ID: {self.idPedido}\n"
        info_texto += f"Cliente: {self.cliente.nombre}\n"
        info_texto += f"Proveedor: {self.proveedor.nombre} (Contacto: {self.proveedor.contacto})\n"
        info_texto += f"Teléfono del proveedor: {self.proveedor.telefono}\nFecha: {date.today()}\n\n"

        # Mostrar productos
        productos_info = [[producto.nombre, f"${producto.precio:.2f}"] for producto in self.productos]
        headers = ["Producto", "Precio"]
        tabla_productos = tabulate(productos_info, headers=headers, tablefmt="fancy_grid")

        info_texto += "Productos:\n"
        info_texto += tabla_productos
        info_texto += f"\n\nTotal: ${self.total:.2f}"

        # Mostrar información en un cuadro de texto
        texto_factura = Text(frame, wrap="word", bg="#e0f2f1", fg="#000000", font=("Courier", 12), borderwidth=0)
        texto_factura.insert(END, info_texto)
        texto_factura.config(state="disabled")
        texto_factura.pack(expand=True, fill="both", padx=10, pady=10)

        # Botón de cerrar
        boton_cerrar = Button(frame, text="Cerrar", command=ventana.destroy, bg="#007acc", fg="#ffffff", font=("Arial", 12, "bold"))
        boton_cerrar.pack(pady=10)

        ventana.mainloop()

# Ejemplo de uso
producto1 = Producto("PR001", "Laptop", 1200.0, "Laptop de 15 pulgadas", 10)
producto2 = Producto("PR002", "Teclado", 50.0, "Teclado mecánico", 20)

cliente1 = Cliente("C001", "Carlos Martínez", "carlos@email.com", "555-6789", "Av. Principal 123")
proveedor1 = Proveedor("P001", "Tech Supplies", "Jorge Rivera", "555-4321", "Calle del Comercio 456")

pedido1 = Pedido("P001", cliente1, [producto1, producto2], proveedor1, date.today())

# Uso de métodos
producto1.actualizarInventario(3)
pedido1.calcularTotal()
pedido1.generarFactura()