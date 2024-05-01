import cv2
import numpy as np


class Triangles:
    def __init__(self, approx):
        self.a = approx

    def isEquilateral(self):
        # Является ли треугольник равносторонним

        # a[0] - a[1] является вектором между
        # вершинами треугольника, norm вычисляет его длину
        a = cv2.norm(self.a[0] - self.a[1])
        b = cv2.norm(self.a[1] - self.a[2])
        c = cv2.norm(self.a[2] - self.a[0])

        # Проверка равенства сторон с некоторой погрешностью
        if np.isclose(a, b, rtol=0.04) and np.isclose(b, c, rtol=0.04):  # 4% отклонение (отн. погрешность)
            return True

        return False

    def isIsosceles(self):
        # Является ли треугольник равнобедренным
        a = cv2.norm(self.a[0] - self.a[1])
        b = cv2.norm(self.a[1] - self.a[2])
        c = cv2.norm(self.a[2] - self.a[0])

        # Если две стороны равны, то треугольник равнобедренный
        if (np.isclose(a, b, rtol=0.04) or np.isclose(b, c, rtol=0.04) or
                np.isclose(c, a, rtol=0.04)):
            return True

        return False

    def isRight(self):
        # Является ли треугольник прямоугольным
        a = cv2.norm(self.a[0] - self.a[1])
        b = cv2.norm(self.a[1] - self.a[2])
        c = cv2.norm(self.a[2] - self.a[0])

        # Если квадрат одной стороны равен сумме квадратов двух других,
        # то треугольник прямоугольный
        if (np.isclose(a ** 2, b ** 2 + c ** 2, rtol=0.04) or
                np.isclose(b ** 2, a ** 2 + c ** 2, rtol=0.04) or
                np.isclose(c ** 2, a ** 2 + b ** 2, rtol=0.04)):
            return True

        return False
