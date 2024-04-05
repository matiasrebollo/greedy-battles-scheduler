import time
import random
from main import get_orden_optimo, calcular_coeficiente
import matplotlib.pyplot as plt

tamanos_datos = [x for x in range(10, 50000, 50)]
tiempos_ejecucion = []

for n in tamanos_datos:
    batallas = [(random.randint(1, 1000), random.randint(0, 1000)) for _ in range(n)]
    start = time.perf_counter()
    solucion = get_orden_optimo(batallas)
    calcular_coeficiente(solucion)
    fin = time.perf_counter()
    tiempo_ms = (fin - start)*1000
    tiempos_ejecucion.append(tiempo_ms)

plt.title("Tiempo de ejecución en función del tamaño del arreglo")
plt.xlabel("cantidad de batallas")
plt.ylabel("tiempo consumido [ms]")
plt.plot(tamanos_datos, tiempos_ejecucion)
plt.savefig("img/grafico_complejidad.png")
plt.show()