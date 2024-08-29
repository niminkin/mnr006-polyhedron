from math import sin, cos, sqrt


class R3:
    """ Вектор (точка) в R3 """

    # Конструктор
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    # Сумма векторов
    def __add__(self, other):
        return R3(self.x + other.x, self.y + other.y, self.z + other.z)

    # Разность векторов
    def __sub__(self, other):
        return R3(self.x - other.x, self.y - other.y, self.z - other.z)

    # Умножение на число
    def __mul__(self, k):
        return R3(k * self.x, k * self.y, k * self.z)

    # Поворот вокруг оси Oz
    def rz(self, fi):
        return R3(
            cos(fi) * self.x - sin(fi) * self.y,
            sin(fi) * self.x + cos(fi) * self.y, self.z)

    # Поворот вокруг оси Oy
    def ry(self, fi):
        return R3(cos(fi) * self.x + sin(fi) * self.z,
                  self.y, -sin(fi) * self.x + cos(fi) * self.z)

    # Скалярное произведение
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Векторное произведение
    def cross(self, other):
        return R3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x)

    # Является ли точка "хорошей" для квадрата с центром в (0; 0; 0)
    # и произвольной длиной ребра 2t
    def vertex_is_not_good(self, t):
        if (abs(self.x) < t and
            abs(self.y) < t and
            abs(self.z) < t):
            return False
        else:
            return True

    # Расстояние между двумя точками в R3
    def length(self, other):
        return (sqrt((self.x - other.x)**2 + (self.y - other.y)**2
                + (self.z - other.z)**2))

    # Точка посередине между двумя заданными
    def mid_dot(self, other):
        return R3((self.x + other.x) / 2, (self.y + other.y) / 2,
                  (self.z + other.z) / 2)

    # Точки совпадают
    def is_equal(self, other):
        if (self.x != other.x or self.y != other.y or
            self.z != other.z):
            return False
        else:
            return True

if __name__ == "__main__":  # pragma: no cover
    x = R3(1.0, 1.0, 1.0)
    print("x", type(x), x.__dict__)
    y = x + R3(1.0, -1.0, 0.0)
    print("y", type(y), y.__dict__)
    y = y.rz(1.0)
    print("y", type(y), y.__dict__)
    u = x.dot(y)
    print("u", type(u), u)
    v = x.cross(y)
    print("v", type(v), v.__dict__)
