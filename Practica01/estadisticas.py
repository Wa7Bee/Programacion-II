import math

class Estadistica:
    def __init__(self, datos):
        self.__datos = datos  

    def promedio(self):
        return sum(self.__datos) / len(self.__datos)

    def desviacion(self):
        n = len(self.__datos)
        prom = self.promedio()
        
        suma_cuadrados = sum((x - prom) ** 2 for x in self.__datos)
        
        return math.sqrt(suma_cuadrados / (n - 1))


# ---------------

valores = list(map(float, input("Ingrese los 10 números separados por espacio: ").split()))

est = Estadistica(valores)

print(f"El promedio es {est.promedio():.2f}")
print(f"La desviacion estandard es {est.desviacion():.5f}")