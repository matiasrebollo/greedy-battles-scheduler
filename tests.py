import unittest
from main import cargar_archivo, get_orden_optimo, calcular_coeficiente_de_impacto 

class Test(unittest.TestCase):
    def test_drive_10(self):
        batallas = cargar_archivo('pruebas_drive/10.txt')
        orden_optimo = get_orden_optimo(batallas)
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 309600)

    def test_drive_50(self):
        batallas = cargar_archivo('pruebas_drive/50.txt')
        orden_optimo = get_orden_optimo(batallas)                     
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 5218700)
               
    def test_drive_100(self):
        batallas = cargar_archivo('pruebas_drive/100.txt')
        orden_optimo = get_orden_optimo(batallas)    
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 780025365)

    def test_drive_1000(self):
        batallas = cargar_archivo('pruebas_drive/1000.txt')
        orden_optimo = get_orden_optimo(batallas)
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 74329021942)

    def test_drive_5000(self):
        batallas = cargar_archivo('pruebas_drive/5000.txt')
        orden_optimo = get_orden_optimo(batallas)        
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 1830026958236)

    def test_drive_10000(self):
        batallas = cargar_archivo('pruebas_drive/10000.txt')
        orden_optimo = get_orden_optimo(batallas)   
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 7245315862869)

    def test_drive_100000(self):
        batallas = cargar_archivo('pruebas_drive/100000.txt')
        orden_optimo = get_orden_optimo(batallas)  
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 728684685661017)

    def test_importancia_decimal1(self):
        batallas = cargar_archivo('ejemplos/Importancia decimal1.txt')
        orden_optimo = get_orden_optimo(batallas)  
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 128.89000000000001)

    def test_importancia_decimal2(self):
        batallas = cargar_archivo('ejemplos/Importancia decimal2.txt')
        orden_optimo = get_orden_optimo(batallas)  
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 8390.910000000002)
        
    def test_mismo_tiempo(self):
        batallas = cargar_archivo('ejemplos/Mismo tiempo.txt')
        orden_optimo = get_orden_optimo(batallas)  
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 165000)

    def test_numeros_muy_grandes(self):
        batallas = cargar_archivo('ejemplos/Numeros muy grandes.txt')
        orden_optimo = get_orden_optimo(batallas)  
        self.assertEqual(calcular_coeficiente_de_impacto(orden_optimo), 1.6435902372095263e+20)

       
if __name__ == '__main__':
    unittest.main()
