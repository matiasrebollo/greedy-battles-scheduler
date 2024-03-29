# Objetivo

El objetivo de nuestro trabajo es idear un algoritmo para el Señor del Fuego que determine el orden óptimo en el que debe llevar a cabo una lista de batallas. Dicho algoritmo debe implementarse de forma Greedy. Además se brindara un análisis completo del problema y del algoritmo.

## Análisis del Problema

Se nos pide ordenar un total de $n$ batallas,  cada batalla $B_{i}$ consta de dos atributos:
- $b_{i}$ : la importancia de la batalla. 
- $t_{i}$ : el tiempo necesario para ganar la batalla. 

Además se define la felicidad producida por la victoria ${j}$ como $F_{j} = F_{i} + t_{j}$ , donde $F_{i}$ corresponde a la batalla anterior ($F_{j} = t_{j}$ para la primera batalla).
Se define como el orden óptimo de batallas, aquel orden tal que minimiza la siguiente suma:

$$
 \sum_{i=1}^{n}b_{i}\cdot F_{i}
$$

Podemos desarrollar esta suma para observar como afecta la magnitud de $b_{i}$ y $t_{i}$:

$$
\sum_{i=1}^{n}b_{i}\cdot F_{i} = b_{1}\cdot F_{1} + b_{2} \cdot F_{2} + b_{3} \cdot F_{3} + ... + b_{n} \cdot F_{n} \newline
=b_{1} \cdot t_{1} + b_{2}\cdot \left(t_{1} + t_{2}\right) + b_{3}\cdot \left(t_{1} + t_{2} + t_{3}\right) + \cdots + b_{n} \cdot \sum_{i=1}^{n}t_{i}
$$

En este punto se puede ver que el termino que acompaña a cada $b_{i}$ va *creciendo*, siendo $b_{n}$ (i.e. la importancia de la ultima batalla), el termino mas afectado. 
Ahora, sigamos desarrollando la suma, en esta ocasión distribuyendo $b_{i}$:

$$
\sum_{i=1}^{n}b_{i}\cdot F_{i} =b_{1} \cdot t_{1} + b_{2}\cdot \left(t_{1} + t_{2}\right) + b_{3}\cdot \left(t_{1} + t_{2} + t_{3}\right) + \cdots + b_{n} \cdot \sum_{i=1}^{n}t_{i} \newline
= t_{1}\sum_{i=1}^{n}b_{i} + t_{2}\sum_{i=2}^{n}b_{i} + t_{3}\sum_{i=3}^{n}b_{i} + \cdots + t_{n}\cdot b_{n}
$$

En este caso notamos que los términos que acompañan a cada $t_{i}$ van *disminuyendo*, por ende el $t_{i}$ más afectado será el $t_{1}$ (i.e. el tiempo necesario de la primer batalla). 

Luego, llegamos a dos conclusiones:
- Si obviamos la importancia de las batallas, estas se deben ordenar en forma ascendiente según el tiempo de duración. 
- Si obviamos la duración de las batallas, debemos ordenarlas de manera descendiente según la importancia.

Si bien esto nos da un indicio de hacia donde debemos encarar el problema, no es suficiente, pues no podemos simplemente ignorar una parte del problema. Entonces deberíamos buscar una forma que cumpla esta relacion lo mejor posible
