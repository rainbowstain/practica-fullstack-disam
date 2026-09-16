# Sesión 16 — `len()` y el `if` en Python

Notas de apoyo escritas por Claude a pedido de Eduardo, porque estaba
programando en otro dispositivo y necesitaba la referencia por escrito.
No reemplazan las notas de Eduardo.

---

## 1. `len()`

`len` viene de *length*: largo. Le pasas algo y te dice **cuántos elementos tiene**.

```python
solicitudes = ["Tóner", "Permiso", "Aire acondicionado"]
print(len(solicitudes))   # 3
```

### Es una función, no una propiedad

Esta es la diferencia con JS y es pregunta de prueba:

| JS | Python |
|---|---|
| `solicitudes.length` | `len(solicitudes)` |

En JS el largo es un **atributo** que cuelga de la lista: se lee con punto.
En Python es una **función global**: la lista va adentro del paréntesis.

Escribir `solicitudes.len()` en Python es `AttributeError`.
Escribir `len` sin paréntesis te imprime la función misma, no el número.

### Sirve para más que listas

```python
len("Eduardo")              # 7  (cantidad de caracteres)
len([10, 20, 30])           # 3  (elementos de la lista)
len([])                     # 0  (lista vacía)
```

### El uso que importa: el último elemento

Los índices arrancan en **0**. Entonces en una lista de 3 elementos las
posiciones válidas son 0, 1 y 2. La última posición es siempre `len(lista) - 1`.

```python
solicitudes[len(solicitudes) - 1]   # "Aire acondicionado"
```

Si escribes `solicitudes[len(solicitudes)]` te da `IndexError`, porque esa
posición no existe. Ese error tiene nombre: *off-by-one*, error por uno.

(Python además permite `solicitudes[-1]` para el último, que JS no tiene.
Anótalo, pero primero acostúmbrate a la forma larga: es la que se entiende
igual en todos los lenguajes.)

### Por qué `range(len(lista))` funciona

```python
for i in range(len(solicitudes)):
    print(f"{i + 1}. {solicitudes[i]}")
```

`len(solicitudes)` da `3`.
`range(3)` da `0, 1, 2`.
Esas son exactamente las posiciones válidas de la lista.

Por eso `range(len(...))` es el calco del `for (let i = 0; i < arr.length; i++)`
de JS. Y por eso `range` excluye el último número: está hecho para que calce
con los índices.

---

## 2. El `if`

Un `if` ejecuta un bloque **solo si** una condición es verdadera.

```python
monto = 30000

if monto > 10000:
    print("Requiere visto bueno")
```

Tres partes obligatorias:

1. La palabra `if`
2. Una condición que da `True` o `False`
3. Dos puntos `:` al final
4. El bloque indentado debajo (4 espacios)

Si la condición da `False`, Python **se salta todo el bloque indentado** y sigue.

### La indentación es la que manda

Python no tiene llaves. Lo que está corrido hacia adentro pertenece al `if`.

```python
if monto > 10000:
    print("A")
    print("B")
print("C")
```

Si `monto` es 30000 imprime A, B y C.
Si `monto` es 400 imprime solo C.

`print("C")` está pegado al margen, así que está **fuera** del `if`.
Mover una línea 4 espacios cambia el programa. No es estilo, es sintaxis.

### `else` y `elif`

`else` es "si no":

```python
if monto > 10000:
    print("Requiere visto bueno")
else:
    print("Compra menor")
```

`elif` es "si no, pero si...". Es la contracción de *else if*, y en Python
se escribe pegado, `elif`, no `else if`:

```python
if monto > 50000:
    print("Requiere aprobación del director")
elif monto > 10000:
    print("Requiere visto bueno del jefe")
else:
    print("Compra menor")
```

Se evalúan **en orden y se detiene en la primera que se cumple**. Con
`monto = 60000` imprime solo la primera línea, aunque también sea mayor
que 10000.

Por eso el orden importa. Si pones `elif monto > 10000` arriba de
`if monto > 50000`, la segunda nunca se ejecuta. Error clásico de prueba:
te muestran las condiciones desordenadas y preguntan qué imprime.

`else` no lleva condición y nunca lleva paréntesis. Solo `else:`.

### Los comparadores

| Operador | Significa |
|---|---|
| `==` | igual a |
| `!=` | distinto de |
| `>` | mayor que |
| `<` | menor que |
| `>=` | mayor o igual |
| `<=` | menor o igual |

**`=` y `==` no son lo mismo.** `=` asigna, `==` compara.

```python
monto = 30000      # asigna: mete 30000 en monto
monto == 30000     # compara: da True
```

En Python escribir `if monto = 30000:` es `SyntaxError` directo. Es una de
las pocas cosas donde Python te protege mejor que JS.

Dato para la prueba: Python **no tiene `===`**. Eso es solo de JS y PHP.
En Python `==` ya compara valor y no hace conversiones raras: `1 == "1"`
da `False`.

### Combinar condiciones: `and`, `or`, `not`

Python usa palabras donde JS usa símbolos:

| JS | Python |
|---|---|
| `&&` | `and` |
| `\|\|` | `or` |
| `!` | `not` |

```python
if monto > 10000 and monto < 50000:
    print("Visto bueno del jefe")
```

`and` exige que las dos se cumplan. `or` con una basta.

Python además permite encadenar, cosa que JS no:

```python
if 10000 < monto < 50000:
    print("Visto bueno del jefe")
```

Las dos versiones hacen lo mismo. Usa la que entiendas mejor.

### Preguntar si algo está en una lista

```python
if "Tóner" in solicitudes:
    print("Ya está pedido")
```

`in` recorre la lista y devuelve `True` o `False`. Es el equivalente a
`includes()` de JS.

Ojo: `in` tiene dos usos distintos según dónde aparezca. En un `for`
(`for x in lista:`) significa "recorre". En un `if` (`if x in lista:`)
significa "pertenece". Es la misma palabra haciendo dos trabajos.

---

## 3. Los dos juntos: el patrón de filtrado

Este es el molde que se repite en todo el temario:

```python
montos = [30000, 20000, 10001, 400, 500]
mayores = []

for monto in montos:
    if monto > 10000:
        mayores.append(monto)

print(len(mayores))
```

Lo que pasa, vuelta por vuelta:

| Vuelta | `monto` | ¿`> 10000`? | `mayores` queda |
|---|---|---|---|
| 1 | 30000 | sí | `[30000]` |
| 2 | 20000 | sí | `[30000, 20000]` |
| 3 | 10001 | sí | `[30000, 20000, 10001]` |
| 4 | 400 | no | sin cambios |
| 5 | 500 | no | sin cambios |

Al final `mayores` tiene 3 elementos y `montos` sigue teniendo 5: el `for`
**no modifica** la lista que recorre.

Fíjate en los tres niveles de indentación:

- `for` al margen
- `if` a 4 espacios, dentro del `for`
- `append` a 8 espacios, dentro del `if`

Si dejas el `append` a 4 espacios, queda dentro del `for` pero **fuera del
`if`**, y se copian los 5 montos. Es el error más común de este ejercicio.

---

## 4. Lo que hay que retener para la prueba

- `len(lista)` es función, `lista.length` es JS. No se mezclan.
- Última posición: `len(lista) - 1`. Índices desde 0.
- `range(n)` llega hasta `n - 1`, nunca incluye `n`.
- `=` asigna, `==` compara. Python no tiene `===`.
- `and` / `or` / `not`, no `&&` / `||` / `!`.
- `elif`, no `else if`. `else` sin condición.
- La cadena `if/elif/else` para en la primera verdadera: el orden decide.
- La indentación define el bloque. Cuatro espacios por nivel.
- `append` modifica la lista y no devuelve nada. Nunca
  `lista = lista.append(x)`.

---

## 5. Pendiente

Aplicar esto en `01-fundamentos-comparados/py/listas.py`: filtrar montos
sobre 10000, calcular IVA, imprimir numerado con f-string y totalizar.
