import time
import random
from main import get_orden_optimo, calcular_coeficiente
import matplotlib.pyplot as plt  

tamanos_datos = [x for x in range(10, 1000000, 100000)]
tiempos_relacion_cte = []
tiempos_importancia_cte = []
tiempos_duracion_cte = []
tiempos_peor = []

# Calculo los tiempos para el caso de b_i constante
for n in tamanos_datos:
    batallas = [(random.uniform(1, 1000), random.uniform(0, 1000)) for _ in range(n)]
    batallas.sort(key = lambda b: b[1]/b[0])
    start = time.perf_counter()
    solucion = get_orden_optimo(batallas)
    calcular_coeficiente(solucion)
    fin = time.perf_counter()
    tiempo_ms = (fin - start)*1000
    tiempos_peor.append(tiempo_ms)

# Calculo los tiempos para el caso de b_i constante
for n in tamanos_datos:
    batallas = [(random.uniform(1, 1000), 1) for _ in range(n)]
    start = time.perf_counter()
    solucion = get_orden_optimo(batallas)
    calcular_coeficiente(solucion)
    fin = time.perf_counter()
    tiempo_ms = (fin - start)*1000
    tiempos_importancia_cte.append(tiempo_ms)

# Calculo los tiempos para el caso de t_i constante
for n in tamanos_datos:
    batallas = [(1, random.uniform(1, 1000)) for _ in range(n)]
    start = time.perf_counter()
    solucion = get_orden_optimo(batallas)
    calcular_coeficiente(solucion)
    fin = time.perf_counter()
    tiempo_ms = (fin - start)*1000
    tiempos_duracion_cte.append(tiempo_ms)

# Calculo los tiempos para el caso de b_i/t_i constante
for n in tamanos_datos:
    batallas = []
    for i in range(n):
        x = random.uniform(1, 1000)
        y = 2*x
        batallas.append((x,y))
    start = time.perf_counter()
    solucion = get_orden_optimo(batallas)
    calcular_coeficiente(solucion)
    fin = time.perf_counter()
    tiempo_ms = (fin - start)*1000
    tiempos_relacion_cte.append(tiempo_ms)

plt.title("Tiempo de ejecucion en fincion al tamaño del arreglo")
plt.xlabel("tamaño del arreglo")
plt.ylabel("tiempo consumido(en ms)")
plt.plot(tamanos_datos, tiempos_ejecucion)
plt.savefig("grafico complejidad.png")
plt.show()