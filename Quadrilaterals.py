# import cv2
# import numpy as np
#
#
# class Quadrilaterals:
#     def __init__(self, approx):
#         self.a = approx
#
#
#     def isParallelogram(self):
#         # Является ли четырёхугольник параллелограммом
#         # print(self.a)
#         # Вычисляем направляющие коэффициенты сторон
#         k1 = (self.a[0][0][1] - self.a[1][0][1]) / (self.a[0][0][0] - self.a[1][0][0])
#         k2 = (self.a[1][0][1] - self.a[2][0][1]) / (self.a[1][0][0] - self.a[2][0][0])
#         k3 = (self.a[2][0][1] - self.a[3][0][1]) / (self.a[2][0][0] - self.a[3][0][0])
#         k4 = (self.a[3][0][1] - self.a[0][0][1]) / (self.a[3][0][0] - self.a[0][0][0])
#
#         # Если противоположные стороны параллельны, то это параллелограмм
#         if np.isclose(k1, k3, rtol=0.04) and np.isclose(k2, k4, rtol=0.04):
#             return True
#
#         return False
#
#
#     def isRhombus(self):
#         # Является ли параллелограмм ромбом
#
#         a = cv2.norm(self.a[0] - self.a[1])
#         b = cv2.norm(self.a[1] - self.a[2])
#         c = cv2.norm(self.a[2] - self.a[3])
#         d = cv2.norm(self.a[3] - self.a[0])
#
#         if (np.isclose(a, b, rtol=0.08) and
#                 np.isclose(b, c, rtol=0.08) and
#                 np.isclose(c, d, rtol=0.08)):
#             return True
#
#         return False
#
#
#     def isRectangle(self):
#         # Является ли параллелограмм прямоугольником
#
#         # Вычисляем углы между сторонами
#         angles = []
#         for i in range(4):
#             v1 = (self.a[i] - self.a[(i - 1) % 4]).flatten()  # flatten преобразует массив в одномерный
#             v2 = (self.a[i] - self.a[(i + 1) % 4]).flatten()
#             # dot вычисляет скалярное произведение векторов
#             angle = np.arccos(np.dot(v1, v2) / (cv2.norm(v1) * cv2.norm(v2)))  # Вычисление угла между векторами
#             angles.append(angle)
#
#         # Если все углы равны 90 градусам, то это прямоугольник
#         if all(np.isclose(angle, np.pi / 2, rtol=0.08) for angle in angles):  # Проверяем каждый угол из списка
#             return True
#
#         return False
#
#
#     def isSquare(self):
#         # Является ли прямоугольник квадратом
#
#         # Если у прямоугольника смежные стороны равны,
#         # то такой прямоугольник является квадратом
#         if np.isclose(cv2.norm(self.a[0] - self.a[1]),
#                       cv2.norm(self.a[1] - self.a[2]), rtol=0.08):
#             return True
#
#         return False
#
#
#     def isTrapezoid(self):
#         # Является ли фигура трапецией
#
#         # Вычисляем направляющие коэффициенты сторон
#         k1 = (self.a[0][0][1] - self.a[1][0][1]) / (self.a[0][0][0] - self.a[1][0][0])
#         k2 = (self.a[1][0][1] - self.a[2][0][1]) / (self.a[1][0][0] - self.a[2][0][0])
#         k3 = (self.a[2][0][1] - self.a[3][0][1]) / (self.a[2][0][0] - self.a[3][0][0])
#         k4 = (self.a[3][0][1] - self.a[0][0][1]) / (self.a[3][0][0] - self.a[0][0][0])
#
#         # Если противоположные стороны параллельны, то это трапеция
#         if np.isclose(k1, k3, atol=0.05) or np.isclose(k2, k4, atol=0.05):
#             return True
#
#         return False


import cv2
import numpy as np


class Quadrilaterals:
    def __init__(self, approx):
        self.a = approx

    def isParallelogram(self):
        k1 = np.inf if self.a[0][0][0] - self.a[1][0][0] == 0 else (self.a[0][0][1] - self.a[1][0][1]) / (
                    self.a[0][0][0] - self.a[1][0][0])
        k2 = np.inf if self.a[1][0][0] - self.a[2][0][0] == 0 else (self.a[1][0][1] - self.a[2][0][1]) / (
                    self.a[1][0][0] - self.a[2][0][0])
        k3 = np.inf if self.a[2][0][0] - self.a[3][0][0] == 0 else (self.a[2][0][1] - self.a[3][0][1]) / (
                    self.a[2][0][0] - self.a[3][0][0])
        k4 = np.inf if self.a[3][0][0] - self.a[0][0][0] == 0 else (self.a[3][0][1] - self.a[0][0][1]) / (
                    self.a[3][0][0] - self.a[0][0][0])

        if np.isclose(k1, k3, rtol=0.04) and np.isclose(k2, k4, rtol=0.04):
            return True

        return False

    def isRhombus(self):
        a = cv2.norm(self.a[0] - self.a[1])
        b = cv2.norm(self.a[1] - self.a[2])
        c = cv2.norm(self.a[2] - self.a[3])
        d = cv2.norm(self.a[3] - self.a[0])

        if (np.isclose(a, b, rtol=0.08) and
                np.isclose(b, c, rtol=0.08) and
                np.isclose(c, d, rtol=0.08)):
            return True

        return False

    def isRectangle(self):
        angles = []
        for i in range(4):
            v1 = (self.a[i] - self.a[(i - 1) % 4]).flatten()
            v2 = (self.a[i] - self.a[(i + 1) % 4]).flatten()
            angle = np.arccos(np.dot(v1, v2) / (cv2.norm(v1) * cv2.norm(v2)))
            angles.append(angle)

        if all(np.isclose(angle, np.pi / 2, rtol=0.08) for angle in angles):
            return True

        return False

    def isSquare(self):
        if np.isclose(cv2.norm(self.a[0] - self.a[1]),
                      cv2.norm(self.a[1] - self.a[2]), rtol=0.08):
            return True

        return False

    def isTrapezoid(self):
        k1 = np.inf if self.a[0][0][0] - self.a[1][0][0] == 0 else (self.a[0][0][1] - self.a[1][0][1]) / (
                    self.a[0][0][0] - self.a[1][0][0])
        k2 = np.inf if self.a[1][0][0] - self.a[2][0][0] == 0 else (self.a[1][0][1] - self.a[2][0][1]) / (
                    self.a[1][0][0] - self.a[2][0][0])
        k3 = np.inf if self.a[2][0][0] - self.a[3][0][0] == 0 else (self.a[2][0][1] - self.a[3][0][1]) / (
                    self.a[2][0][0] - self.a[3][0][0])
        k4 = np.inf if self.a[3][0][0] - self.a[0][0][0] == 0 else (self.a[3][0][1] - self.a[0][0][1]) / (
                    self.a[3][0][0] - self.a[0][0][0])

        if np.isclose(k1, k3, atol=0.05) or np.isclose(k2, k4, atol=0.05):
            return True

        return False
