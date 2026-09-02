import time
import random


class Cronometro:
    def __init__(self, inicia=0, finaliza=0):
        self.inicia = inicia
        self.finaliza = finaliza

    def getInicia(self):
        return self.inicia

    def getFinaliza(self):
        return self.finaliza

    def Comienza(self):
        self.inicia = time.time()

    def Detener(self):
        self.finaliza = time.time()

    def lapsoDeTiempo(self):
        return self.finaliza - self.inicia


class Ordenacion:

    def selection_sort(self, lista):
        n = len(lista)

        for i in range(n):
            idx_minimo = i

            for j in range(i + 1, n):
                if lista[j] < lista[idx_minimo]:
                    idx_minimo = j

            lista[i], lista[idx_minimo] = lista[idx_minimo], lista[i]

        return lista



CANTIDAD = 100000

print(f"Generando {CANTIDAD:,} los números aleatorios...")

numeros = [random.randint(1, 1000000) for _ in range(CANTIDAD)]




cronometro = Cronometro()
ordenacion = Ordenacion()




cronometro.Comienza()

ordenacion.selection_sort(numeros)

cronometro.Detener()



tiempo = cronometro.lapsoDeTiempo()

print(f"Tiempo de ejecución: {tiempo:.4f} segundos")