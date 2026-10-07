# Explicamos Python — Grupo 2

## Integrantes

- Oscar Herreros Cañada
- Laura Soler Úbeda
- Antonio Gabriel Navarro Puig

## Tema

Listas y tuplas.

## Qué demuestra el ejemplo

El programa muestra cómo crear y modificar una lista de productos.

Se añade un producto, se modifica otro y se elimina uno.

También se crea una tupla con el nombre y la ciudad de una tienda.

La diferencia principal es:

- Las listas son mutables: se pueden modificar.
- Las tuplas son inmutables: no se pueden modificar directamente.

## Cómo ejecutarlo

```bash
python main.py
```

## Resultado esperado

```text
Lista inicial: ['portátil', 'ratón', 'teclado']
Lista final: ['portátil', 'ratón inalámbrico', 'monitor']
Primer producto: portátil
Tienda: ('TechStore', 'Valencia')
Ciudad: Valencia

Pregunta: ¿Qué muestra productos[1]?
Respuesta: ratón inalámbrico
```

## Pregunta para la clase

¿Qué mostrará este código?

```python
print(productos[1])
```

Respuesta:

```text
ratón inalámbrico
```

Los índices empiezan en 0, por lo que el índice 1 corresponde al segundo elemento.

## Error típico

Intentar modificar una tupla:

```python
tienda[1] = "Madrid"
```

Esto produce un error porque las tuplas son inmutables.
