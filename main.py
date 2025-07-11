import sys, csv

TIEMPO = 0
IMPORTANCIA = 1

def cargar_archivo(archivo):
    with open(archivo) as f:
        r = csv.DictReader(f)
        batallas = [tuple(float(x) for x in linea.values()) for linea in r]
    return batallas

def get_orden_optimo(batallas):
    return sorted(batallas, reverse=True, key=lambda batalla: batalla[IMPORTANCIA]/batalla[TIEMPO])

def calcular_coeficiente_de_impacto(batallas):
    felicidad = 0
    suma = 0
    for batalla in batallas:
        felicidad += batalla[TIEMPO]
        suma += batalla[IMPORTANCIA]*felicidad
    return suma

def main():
    batallas = cargar_archivo(sys.argv[1])
    orden_optimo = get_orden_optimo(batallas)
    print("Orden optimo:", orden_optimo)
    print("Coeficiente de impacto:", calcular_coeficiente_de_impacto(orden_optimo))

if __name__ == "__main__":
    main()
