Python Grupo 2: Listas y tuplas

Integrantes: - Oscar Herreros Cañada - Laura Soler Úbeda - Antonio Gabriel Navarro Puig

¿Qué demuestra el ejemplo?

El programa muestra cómo crear y modificar una lista de productos.

Se añade un producto, se modifica otro y se elimina uno.

También se crea una tupla con el nombre y la ciudad de una tienda.

Diferencia principal es:

Las listas son mutables: se pueden modificar.
Las tuplas son inmutables: no se pueden modificar directamente.
Resultado esperado

Lista inicial: ['portátil', 'ratón', 'teclado']
Lista final: ['portátil', 'ratón inalámbrico', 'monitor']
Primer producto: portátil
Tienda: ('TechStore', 'Valencia')
Ciudad: Valencia
Pregunta: ¿Qué muestra productos[1]? Respuesta: ratón inalámbrico

Pregunta para la clase: ¿Qué mostrará este código?

print(productos[1])
Respuesta: ratón inalámbrico

Hay que recordar que los índices empiezan en 0, por lo que el índice 1 corresponde al segundo elemento.
Otro error típico

Intentar modificar una tupla: tienda[1] = "Madrid"

Esto produce un error porque las tuplas son inmutables.
