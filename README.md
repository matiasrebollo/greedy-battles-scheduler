# Trabajo Práctico 1: Algoritmos Greedy en la Nación del Fuego

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo Greedy. La fecha de entrega del mismo es el 8/04.
## Introducción

Es el año 10 AG, y somos asesores del Señor del Fuego (líder supremo de la Nación del Fuego). El Señor del Fuego cuenta con un ejército de Maestros Fuego, muy temidos en el mundo. Tiene varias batallas con las cuales lidiar: una contra el Templo Aire del Este, otra en la Tribu del Agua del Norte, otra en la Isla de Kyoshi, una muy importante en Ba Sing Se (capital del Reino de la Tierra), y muchas otras más. Sabemos cuánto tiempo necesita el ejército para ganar cada una de las batallas (ti). El ejército ataca todo junto, no puede ni conviene que se separen en grupos. Es decir, no participan de más de una batalla en simultáneo.

La felicidad que produce saber que se logró una victoria depende del momento en el que ésta se obtenga (es decir, que la batalla termine). Es por esto que podemos definir a Fi como el momento en el que se termina la batalla i. Si la primera batalla es la j, entonces Fj​=tj​, en cambio si la batalla j se realiza justo después de la batalla i, entonces Fj​=Fi​+tj​.

Además del tiempo que consume cada batalla, sabemos que al Señor del Fuego no le da lo mismo el orden en el que se realizan, porque comunicar la victoria a su nación en diferentes batallas genera menos impacto si pasa mucho tiempo. Además, cada batalla tiene una importancia diferente. Vamos a definir que tenemos un peso bi​ que nos define cuán importante es una batalla.

Dadas estas características, se quiere buscar tener el orden de las batallas tales que se logre minimizar la suma ponderada de los tiempos de finalización: ∑​bi​Fi​.

El Señor del Fuego nos pide diseñar un algoritmo que determine aquel orden de las batallas que logre minimizar dicha suma ponderada.

## Consigna

1. Hacer un análisis del problema, y proponer un algoritmo greedy que obtenga la solución óptima al problema planteado: Dados los nn valores de todos los ti​ y bi​, determinar cuál es el orden óptimo para realizar las batallas en el cuál se minimiza ∑​bi​Fi​.
2. Demostrar que el algoritmo planteado obtiene siempre la solución óptima.
3. Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. Analizar si (y cómo) afecta la variabilidad de los valores de ti​ y bi​ a los tiempos del algoritmo planteado.
4. Analizar si (y cómo) afecta la variabilidad de los valores de titi​ y bibi​ a la optimalidad del algoritmo planteado.
5. Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente, el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también.
6. Hacer mediciones de tiempos para corroborar la complejidad teórica indicada. Agregar los casos de prueba necesarios para dicha corroboración. Realizar gráficos correspondientes.
7. Agregar cualquier conclusión que les parezca relevante.

