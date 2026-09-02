import math

class EcuacionLineal:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return (self.__b**2) - (4*self.__a*self.__c)

    def getRaiz1(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
        
        return (-self.__b + math.sqrt(d))/(2*self.__a)

    def getRaiz2(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
                
        return (-self.__b - math.sqrt(d))/(2*self.__a)


#---------------

a, b, c = map(float, input("Ingrese a, b, c (separado por espacios): ").split())

ecuacion = EcuacionLineal(a, b, c)

discriminante = ecuacion.getDiscriminante()

if discriminante > 0:
    print(f"La ecuacion tiene dos raices {ecuacion.getRaiz1():.6g} y {ecuacion.getRaiz2():.6g}")
elif discriminante == 0:
    print(f"La ecuación tiene una raíz {ecuacion.getRaiz1():.6g}")
else:
    print("La ecuación no tiene raíces reales")