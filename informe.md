# Objetivo

El objetivo del presente trabajo es idear un algoritmo para el Señor del Fuego que logre determinar el orden óptimo en el que debe llevar a cabo un conjunto de batallas. Dicho algoritmo debe implementarse de forma Greedy. Además, se brindará un análisis completo del problema y del algoritmo en cuestión.

## Análisis del Problema

Se nos pide ordenar un total de $n$ batallas, donde cada batalla $B_{i}$ consta de dos atributos:
- $b_{i}$ : la importancia de la batalla. 
- $t_{i}$ : el tiempo necesario para ganar la batalla. 

Además, se define la felicidad producida por la victoria ${j}$ como $F_{j} = F_{i} + t_{j}$ , donde $F_{i}$ corresponde a la batalla anterior ($F_{j} = t_{j}$ para la primera batalla).
Se define como el orden óptimo de batallas a aquel orden tal que minimiza la siguiente suma:

$$
 \sum_{i=1}^{n}b_{i}\cdot F_{i}
$$

Podemos desarrollar esta suma para observar como afecta la magnitud de $b_{i}$ y $t_{i}$:

$$
\sum_{i=1}^{n}b_{i}\cdot F_{i} = b_{1}\cdot F_{1} + b_{2} \cdot F_{2} + b_{3} \cdot F_{3} + ... + b_{n} \cdot F_{n} \newline
=b_{1} \cdot t_{1} + b_{2}\cdot \left(t_{1} + t_{2}\right) + b_{3}\cdot \left(t_{1} + t_{2} + t_{3}\right) + \cdots + b_{n} \cdot \sum_{i=1}^{n}t_{i}
$$

En este punto se puede ver que el término que acompaña a cada $b_{i}$ va *creciendo*, siendo $b_{n}$ (i.e. la importancia de la última batalla), el término mas afectado. 
Ahora, sigamos desarrollando la suma, en esta ocasión distribuyendo $b_{i}$:

$$
\sum_{i=1}^{n}b_{i}\cdot F_{i} =b_{1} \cdot t_{1} + b_{2}\cdot \left(t_{1} + t_{2}\right) + b_{3}\cdot \left(t_{1} + t_{2} + t_{3}\right) + \cdots + b_{n} \cdot \sum_{i=1}^{n}t_{i} \newline
= t_{1}\sum_{i=1}^{n}b_{i} + t_{2}\sum_{i=2}^{n}b_{i} + t_{3}\sum_{i=3}^{n}b_{i} + \cdots + t_{n}\cdot b_{n}
$$

En este caso notamos que los términos que acompañan a cada $t_{i}$ van *disminuyendo*, por ende el $t_{i}$ más afectado será el $t_{1}$ (i.e. el tiempo necesario de la primer batalla). 

Luego, llegamos a dos conclusiones:
- Si obviamos la importancia de las batallas, estas se deben ordenar en forma ascendiente según el tiempo de duración ("las más cortas primero"). 
- Si obviamos la duración de las batallas, debemos ordenarlas de manera descendiente según la importancia ("las más importantes primero").

Si bien esto nos da un indicio de hacia donde debemos encarar el problema, no es suficiente, pues no podemos simplemente ignorar una parte entera del mismo. Entonces, deberíamos buscar una forma que cumpla esta relación lo mejor posible.

# Algoritmo y Complejidad
A continuación expondremos el código de nuestro algoritmo junto con el respectivo análisis de complejidad. Además, analizaremos cómo afecta la variabilidad de los atributos $b_{i}$ y $t_{i}$ a la ejecución del algoritmo planteado.

## Implementación

```python
def ordenarBatallas(batallas):
    return sorted(batallas, key=lambda batalla: batalla[TIEMPO]/batalla[IMPORTANCIA])


def calcular_coeficiente(batallas):
    ordenarBatallas(batallas)
    F = 0
    suma = 0
    for batalla in batallas:
        F += batalla[TIEMPO]
        suma += batalla[IMPORTANCIA]*F
    return suma
```

## Analisis Complejidad
El algoritmo consta de dos partes:

1. Se ordenan las batallas con el criterio planteado. Considerando el uso del sort de Python, esto se hace en O($nlogn$).
2. Se iteran las batallas y se realiza la suma ponderada descrita en el problema, tardando O($n$).

Luego, la complejidad total queda O($n$) + O($nlogn$) = O($nlogn$).