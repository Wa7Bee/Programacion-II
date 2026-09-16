import math

class AlgebraVectorial:
    def __init__(self, ax=0.0, ay=0.0, bx=0.0, by=0.0):
        self.ax = float(ax)
        self.ay = float(ay)
        self.bx = float(bx)
        self.by = float(by)

    def _magnitud_b(self):
        return math.sqrt(self.bx**2 + self.by**2)

    def _producto_escalar(self):
        return (self.ax * self.bx) + (self.ay * self.by)


    def perpendicular(self, criterio="c"):
        if criterio == "a":
            suma = math.sqrt((self.ax + self.bx)**2 + (self.ay + self.by)**2)
            resta = math.sqrt((self.ax - self.bx)**2 + (self.ay - self.by)**2)
            return math.isclose(suma, resta)
            
        elif criterio == "d": 
            suma_cuadrado = (self.ax + self.bx)**2 + (self.ay + self.by)**2
            mag_a_sq = self.ax**2 + self.ay**2
            mag_b_sq = self.bx**2 + self.by**2
            return math.isclose(suma_cuadrado, mag_a_sq + mag_b_sq)
            
        else:
            return math.isclose(self._producto_escalar(), 0.0)

    def paralela(self, criterio="f"):
        if criterio == "e": 
            if self.bx != 0 and self.by != 0:
                return math.isclose(self.ax / self.bx, self.ay / self.by)
            return False
        else:
            producto_cruz = (self.ax * self.by) - (self.ay * self.bx)
            return math.isclose(producto_cruz, 0.0)

    def componente(self):
        if self._magnitud_b() == 0:
            return "No se puede calcular (el vector b es nulo)"
        return self._producto_escalar() / self._magnitud_b()

    def proyeccion(self):
        mag_b_cuadrado = self.bx**2 + self.by**2
        if mag_b_cuadrado == 0:
            return "No se puede calcular (el vector b es nulo)"
            
        factor = self._producto_escalar() / mag_b_cuadrado
        return (factor * self.bx, factor * self.by)




v = AlgebraVectorial(3, 4, 1, 0)

print("¿Son perpendiculares?:", v.perpendicular())
print("¿Son paralelas?:", v.paralela())
print("Componente de a en b:", v.componente())
print("Proyección de a sobre b:", v.proyeccion())