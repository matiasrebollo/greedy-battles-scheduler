from time import perf_counter
from random import uniform
from main import get_orden_optimo, calcular_coeficiente
import matplotlib.pyplot as plt

tamanos_datos = [x for x in range(10, 50000, 500)]
tiempos_importancia_cte = []
tiempos_duracion_cte = []
tiempos_relacion_cte = []

for n in tamanos_datos:
    batallas = [(uniform(1, 1000), 1) for _ in range(n)]
    start = perf_counter()
    solucion = get_orden_optimo(batallas)
    calcular_coeficiente(solucion)
    fin = perf_counter()
    tiempo_ms = (fin - start)*1000
    tiempos_importancia_cte.append(tiempo_ms)

for n in tamanos_datos:
    batallas = [(1, uniform(0, 1000)) for _ in range(n)]
    start = perf_counter()
    solucion = get_orden_optimo(batallas)
    calcular_coeficiente(solucion)
    fin = perf_counter()
    tiempo_ms = (fin - start)*1000
    tiempos_duracion_cte.append(tiempo_ms)

for n in tamanos_datos:
    batallas = []
    for _ in range(n):
        t = uniform(1, 1000)
        b = 2*t
        batallas.append((t, b))

    start = perf_counter()
    solucion = get_orden_optimo(batallas)
    calcular_coeficiente(solucion)
    fin = perf_counter()
    tiempo_ms = (fin - start)*1000
    tiempos_relacion_cte.append(tiempo_ms)

plt.title("Analisis de variabilidad")
plt.xlabel("cantidad de batallas")
plt.ylabel("tiempo consumido [ms]")
plt.plot(tamanos_datos, tiempos_importancia_cte, label='importancia constante')
plt.plot(tamanos_datos, tiempos_duracion_cte, label='duracion constante')
plt.plot(tamanos_datos, tiempos_relacion_cte, label='relacion b/t constante')
plt.legend()
plt.savefig("img/grafico_variabilidad.png")
plt.show()