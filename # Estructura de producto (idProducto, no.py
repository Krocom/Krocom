# Estructura de producto (idProducto, nombre, stockCritico):

from ClaseProducto import *

producto = Producto(1, "Chipa", 0, 252, 0, 0)
dicStock = {'chipa' : producto}

# producto = Producto(2, "Empanada", 0, 48, 0, 0)		Pensar como incluir los distintos tipos de empanada.
# dicStock['empanada'] = producto

producto = Producto(3, "Tarta", 0, 8, 0, 0)
dicStock['tarta'] = producto

producto = Producto(4, "Mini-Tarta", 0, 0, 0, 0)
dicStock['mini'] = producto

producto = Producto(5, "Panini", 0, 24, 0, 0)
dicStock['panini'] = producto

producto = Producto(6, "Tostable", 0, 40, 0, 0)
dicStock['tostable'] = producto

producto = Producto(7, "Medialuna", 0, 288, 0, 0)
dicStock['medialuna'] = producto

producto = Producto(8, "Churro", 0, 40, 0, 0)
dicStock['churro'] = producto

# producto = Producto(9, "Panales", 0, 0, 0, 0)		IDEM empanadas
# dicStock['panales'] = producto

producto = Producto(10, "Criollito", 0, 0, 0, 0)
dicStock['criollito'] = producto


for key in dicStock:
	print(key)
	pass

print()
dicStock['medialuna'].mostrarProducto()
print()