import math

def promedio(datos):
    return sum(datos) / len(datos)

def desviacion(datos):
    n = len(datos)
    prom = promedio(datos)
    
    suma_cuadrados = sum((x - prom) ** 2 for x in datos)
    
    return math.sqrt(suma_cuadrados / (n - 1))

# ---------------

datos = list(map(float, input("Ingrese los 10 números separados por espacio: ").split()))

print(f"El promedio es {promedio(datos):.2f}")
print(f"La desviacion estándar es {desviacion(datos):.5f}")