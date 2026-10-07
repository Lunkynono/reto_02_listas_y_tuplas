# Grupo 2 - Listas y tuplas

# LISTA: se puede modificar
productos = ["portátil", "ratón", "teclado"]

print("Lista inicial:", productos)

# Añadir un producto
productos.append("monitor")

# Modificar un producto
productos[1] = "ratón inalámbrico"

# Eliminar un producto
productos.remove("teclado")

print("Lista final:", productos)
print("Primer producto:", productos[0])


# TUPLA: no se puede modificar
tienda = ("TechStore", "Valencia")

print("Tienda:", tienda)
print("Ciudad:", tienda[1])


# PREGUNTA PARA LA CLASE
print("\nPregunta: ¿Qué muestra productos[1]?")
print("Respuesta:", productos[1])


# ERROR TÍPICO
# Si descomentamos esta línea, dará error porque una tupla es inmutable:
# tienda[1] = "Madrid"
