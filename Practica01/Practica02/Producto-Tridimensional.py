import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def suma(self, otro):
        return Vector3D(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def multiplicar_escalar(self, r):
        return Vector3D(r * self.x, r * self.y, r * self.z)

    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normal(self):
        l = self.longitud()
        if l == 0:
            return "No se puede normalizar el vector nulo"
        return Vector3D(self.x / l, self.y / l, self.z / l)

    def producto_escalar(self, otro):
        return (self.x * otro.x) + (self.y * otro.y) + (self.z * otro.z)

    def producto_vectorial(self, otro):
        rx = (self.y * otro.z) - (self.z * otro.y)
        ry = (self.z * otro.x) - (self.x * otro.z)
        rz = (self.x * otro.y) - (self.y * otro.x)
        return Vector3D(rx, ry, rz)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)

print("a =", a)
print("b =", b)
print("a) Suma (a + b):", a.suma(b))
print("b) Multiplicación por escalar (3 * a):", a.multiplicar_escalar(3))
print("c) Longitud de a:", a.longitud())
print("d) Normal de a:", a.normal())
print("e) Producto escalar (a . b):", a.producto_escalar(b))
print("f) Producto vectorial (a x b):", a.producto_vectorial(b))