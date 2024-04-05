from time import perf_counter
from random import uniform
from main import get_orden_optimo, calcular_coeficiente
import matplotlib.pyplot as plt

tamanos_datos = [x for x in range(10, 50000, 500)]
tiempos_ejecucion = []

for n in tamanos_datos:
    batallas = [(uniform(1, 1000), uniform(0, 1000)) for _ in range(n)]
    start = perf_counter()
    solucion = get_orden_optimo(batallas)
    calcular_coeficiente(solucion)
    fin = perf_counter()
    tiempo_ms = (fin - start)*1000
    tiempos_ejecucion.append(tiempo_ms)

plt.title("Tiempo de ejecución en función del tamaño del arreglo")
plt.xlabel("cantidad de batallas")
plt.ylabel("tiempo consumido [ms]")
plt.plot(tamanos_datos, tiempos_ejecucion)
plt.savefig("img/grafico_complejidad.png")
plt.show()