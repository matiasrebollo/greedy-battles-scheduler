# Trabajo Práctico 1: Algoritmos Greedy en la Nación del Fuego

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo Greedy. La fecha de entrega del mismo es el 8/04.
## Introducción

Es el año 10 AG, y somos asesores del Señor del Fuego (líder supremo de la Nación del Fuego). El Señor del Fuego cuenta con un ejército de Maestros Fuego, muy temidos en el mundo. Tiene varias batallas con las cuales lidiar: una contra el Templo Aire del Este, otra en la Tribu del Agua del Norte, otra en la Isla de Kyoshi, una muy importante en Ba Sing Se (capital del Reino de la Tierra), y muchas otras más. Sabemos cuánto tiempo necesita el ejército para ganar cada una de las batallas (ti). El ejército ataca todo junto, no puede ni conviene que se separen en grupos. Es decir, no participan de más de una batalla en simultáneo.

La felicidad que produce saber que se logró una victoria depende del momento en el que ésta se obtenga (es decir, que la batalla termine). Es por esto que podemos definir a Fi como el momento en el que se termina la batalla i. Si la primera batalla es la j, entonces Fj​=tj​, en cambio si la batalla j se realiza justo después de la batalla i, entonces Fj​=Fi​+tj​.

Además del tiempo que consume cada batalla, sabemos que al Señor del Fuego no le da lo mismo el orden en el que se realizan, porque comunicar la victoria a su nación en diferentes batallas genera menos impacto si pasa mucho tiempo. Además, cada batalla tiene una importancia diferente. Vamos a definir que tenemos un peso bi​ que nos define cuán importante es una batalla.

Dadas estas características, se quiere buscar tener el orden de las batallas tales que se logre minimizar la suma ponderada de los tiempos de finalización: ∑​bi​Fi​.

El Señor del Fuego nos pide diseñar un algoritmo que determine aquel orden de las batallas que logre minimizar dicha suma ponderada.
