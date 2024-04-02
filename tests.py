import unittest, os
from main import cargar_archivo, get_orden_optimo, calcular_coeficiente 

class Test(unittest.TestCase):
    def test_drive_10(self):
        path_archivo = os.path.join(os.getcwd(), 'pruebas_drive/10.txt')
        batallas = cargar_archivo(path_archivo)
        orden_optimo = get_orden_optimo(batallas)
        self.assertEqual(calcular_coeficiente(orden_optimo), 309600)

    def test_drive_50(self):
        path_archivo = os.path.join(os.getcwd(), 'pruebas_drive/50.txt')
        batallas = cargar_archivo(path_archivo)
        orden_optimo = get_orden_optimo(batallas)                     
        self.assertEqual(calcular_coeficiente(orden_optimo), 5218700)
               
    def test_drive_100(self):
        path_archivo = os.path.join(os.getcwd(), 'pruebas_drive/100.txt')
        batallas = cargar_archivo(path_archivo)
        orden_optimo = get_orden_optimo(batallas)    
        self.assertEqual(calcular_coeficiente(orden_optimo), 780025365)

    def test_drive_1000(self):
        path_archivo = os.path.join(os.getcwd(), 'pruebas_drive/1000.txt')
        batallas = cargar_archivo(path_archivo)
        orden_optimo = get_orden_optimo(batallas)
        self.assertEqual(calcular_coeficiente(orden_optimo), 74329021942)

    def test_drive_5000(self):
        path_archivo = os.path.join(os.getcwd(), 'pruebas_drive/5000.txt')
        batallas = cargar_archivo(path_archivo)
        orden_optimo = get_orden_optimo(batallas)        
        self.assertEqual(calcular_coeficiente(orden_optimo), 1830026958236)

    def test_drive_10000(self):
        path_archivo = os.path.join(os.getcwd(), 'pruebas_drive/10000.txt')
        batallas = cargar_archivo(path_archivo)
        orden_optimo = get_orden_optimo(batallas)   
        self.assertEqual(calcular_coeficiente(orden_optimo), 7245315862869)

    def test_drive_100000(self):
        path_archivo = os.path.join(os.getcwd(), 'pruebas_drive/100000.txt')
        batallas = cargar_archivo(path_archivo)
        orden_optimo = get_orden_optimo(batallas)  
        self.assertEqual(calcular_coeficiente(orden_optimo), 728684685661017)

    def test_mismo_tiempo(self):
        path_archivo = os.path.join(os.getcwd(), 'ejemplos/Mismo tiempo.txt')
        batallas = cargar_archivo(path_archivo)
        orden_optimo = get_orden_optimo(batallas)  
        self.assertEqual(calcular_coeficiente(orden_optimo), 167000)

     def test_importancia_decimal1(self):
        path_archivo = os.path.join(os.getcwd(), 'ejemplos/Importancia decimal1.txt')
        batallas = cargar_archivo(path_archivo)
        orden_optimo = get_orden_optimo(batallas)  
        self.assertEqual(calcular_coeficiente(orden_optimo), 128.89)

       
if __name__ == '__main__':
    unittest.main()
