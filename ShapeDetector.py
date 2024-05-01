import cv2
import numpy as np
from Quadrilaterals import Quadrilaterals
from Triangles import Triangles
from Ellipse import isEllipse


class ShapeDetector:
    def __init__(self):
        self.shape = " unidentified"

        self.keyId = 0

        self.dictTriangles = {"Общее количество: ": 0,
                              "Равносторонний: ": {"count": 0, "details": []},
                              "Равнобедренный: ": {"count": 0, "details": []},
                              "Прямоугольный: ": {"count": 0, "details": []},
                              "Произвольный: ": {"count": 0, "details": []}}

        self.dictQuadrilaterals = {"Общее количество: ": 0,
                                   "Произвольный: ": {"count": 0, "details": []},
                                   "Трапеция: ": {"count": 0, "details": []},
                                   "Параллелограмм: ": {"count": 0, "details": []},
                                   "Ромб: ": {"count": 0, "details": []},
                                   "Прямоугольник: ": {"count": 0, "details": []},
                                   "Квадрат: ": {"count": 0, "details": []}}

        self.dictPentagons = {"Общее количество: ": 0,
                              "Пятиугольник: ": {"count": 0, "details": []}}

        self.dictHexagons = {"Общее количество: ": 0,
                             "Шестиугольник: ": {"count": 0, "details": []}}

        self.dictEllipse = {"Общее количество: ": 0,
                            "Эллипс: ": {"count": 0, "details": []},
                            "Окружность: ": {"count": 0, "details": []}}


        self.dictShapes = {"Треугольники": self.dictTriangles,
                           "Четырёхугольники": self.dictQuadrilaterals,
                           "Пятиугольники": self.dictPentagons,
                           "Шестиугольники": self.dictHexagons,
                           "Эллипсы": self.dictEllipse}

    def detect(self, cnt, dictContours, IdContours):



        for key, value in IdContours.items():
            if np.array_equal(cnt, value):
                self.keyId = key





        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)

        # Определение формы по числу вершин

        if len(approx) == 3:  # Если у фигуры 3 вершины, это треугольник
            self.dictShapes["Треугольники"]["Общее количество: "] += 1
            Triangle = Triangles(approx)
            if Triangle.isEquilateral():  # Равносторонний
                self.shape = " equilateral triangle"
                self.dictShapes["Треугольники"]["Равносторонний: "]["count"] += 1
                self.dictShapes["Треугольники"]["Равносторонний: "]["details"].append(dictContours[self.keyId])

            elif Triangle.isIsosceles():  # Равнобедренный
                self.shape = " isosceles triangle"
                self.dictShapes["Треугольники"]["Равнобедренный: "]["count"] += 1
                self.dictShapes["Треугольники"]["Равнобедренный: "]["details"].append(dictContours[self.keyId])


            elif Triangle.isRight():  # Прямоугольный
                self.shape = " right triangle"
                self.dictShapes["Треугольники"]["Прямоугольный: "]["count"] += 1
                self.dictShapes["Треугольники"]["Прямоугольный: "]["details"].append(dictContours[self.keyId])

            else:  # Произвольный
                self.shape = " random triangle"
                self.dictShapes["Треугольники"]["Произвольный: "]["count"] += 1
                self.dictShapes["Треугольники"]["Произвольный: "]["details"].append(dictContours[self.keyId])


        elif len(approx) == 4:  # Если у фигуры 4 вершины, это четырёхугольник
            self.dictShapes["Четырёхугольники"]["Общее количество: "] += 1
            Quad = Quadrilaterals(approx)

            if Quad.isParallelogram():
                if Quad.isRectangle():
                    if Quad.isSquare():
                        self.shape = " square"
                        self.dictShapes["Четырёхугольники"]["Квадрат: "]["count"] += 1
                        self.dictShapes["Четырёхугольники"]["Квадрат: "]["details"].append(dictContours[self.keyId])
                    else:
                        self.shape = " rectangle"
                        self.dictShapes["Четырёхугольники"]["Прямоугольник: "]["count"] += 1
                        self.dictShapes["Четырёхугольники"]["Прямоугольник: "]["details"].append(dictContours[self.keyId])

                elif Quad.isRhombus():
                    self.shape = " rhombus"
                    self.dictShapes["Четырёхугольники"]["Ромб: "]["count"] += 1
                    self.dictShapes["Четырёхугольники"]["Ромб: "]["details"].append(dictContours[self.keyId])

                else:
                    self.shape = " parallelogram"
                    self.dictShapes["Четырёхугольники"]["Параллелограмм: "]["count"] += 1
                    self.dictShapes["Четырёхугольники"]["Параллелограмм: "]["details"].append(dictContours[self.keyId])

            elif Quad.isTrapezoid():
                self.shape = " trapezoid"
                self.dictShapes["Четырёхугольники"]["Трапеция: "]["count"] += 1
                self.dictShapes["Четырёхугольники"]["Трапеция: "]["details"].append(dictContours[self.keyId])

            else:
                self.shape = " random quadrilateral"
                self.dictShapes["Четырёхугольники"]["Произвольный: "]["count"] += 1
                self.dictShapes["Четырёхугольники"]["Произвольный: "]["details"].append(dictContours[self.keyId])

        elif len(approx) == 5:
            self.shape = " pentagon"
            self.dictShapes["Пятиугольники"]["Общее количество: "] += 1
            self.dictShapes["Пятиугольники"]["Пятиугольник: "]["count"] += 1
            self.dictShapes["Пятиугольники"]["Пятиугольник: "]["details"].append(dictContours[self.keyId])

        elif len(approx) == 6:
            self.shape = " hexagon"
            self.dictShapes["Шестиугольники"]["details"].append(dictContours[self.keyId])
        else:
            # Определение круга или эллипса
            if isEllipse(self, cnt, dictContours, self.keyId):
                self.dictShapes["Эллипсы"]["Общее количество: "] += 1
            else:
                self.shape = " unidentified"

        return self.shape
