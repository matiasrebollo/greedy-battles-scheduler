import sys
import csv
TIEMPO = 0
IMPORTANCIA = 1

def cargar_archivo(archivo):
    with open(archivo) as f:
        r = csv.DictReader(f)
        batallas = [tuple(int(x) for x in linea.values()) for linea in r]
    return batallas

def get_orden_optimo(batallas):
    return sorted(batallas, key=lambda batalla: batalla[0]/batalla[1])

def calcular_coeficiente(batallas):
    felicidad = 0
    suma = 0
    for batalla in batallas:
        felicidad += batalla[0]
        suma += batalla[1]*felicidad
    return suma

def main():
    batallas = cargar_archivo(sys.argv[1])
    orden_optimo = get_orden_optimo(batallas)
    print(orden_optimo)
    print(calcular_coeficiente(orden_optimo))

if __name__ == "__main__":
    main()