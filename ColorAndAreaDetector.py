import cv2


class ColorAndAreaDetector:
    def __init__(self):
        self.dictContours = {}
        self.IdContours = {}


        self.colors = [
            "Желтый",
            "Зеленый",
            "Красный",
            "Синий",
            "Фиолетовый",
            "Аквамарин",
            "Хаки",
            "Серебряный"
        ]

        self.masks = {
            "Желтый": ((20, 240, 240), (30, 255, 255)),
            "Зеленый": ((45, 100, 100), (75, 255, 255)),
            "Красный": ((0, 70, 50), (10, 255, 255)),
            "Синий": ((110, 50, 50), (130, 255, 255)),
            "Фиолетовый": ((149, 50, 50), (150, 255, 255)),
            "Аквамарин": ((70, 100, 100), (80, 128, 255)),
            "Хаки": ((15, 100, 200), (27, 110, 245)),
            "Серебряный": ((0, 0, 180), (5, 5, 192))
        }

    def whatIsColorAndArea(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        i = 0
        for color in self.colors:
            # Наложение маски поверх исходного изображения с заданным
            # диапазоном цветов, если пиксель в заданном диапазоне, то он
            # закрашивается в белый, остальные в чёрный
            mask = cv2.inRange(hsv, self.masks[color][0], self.masks[color][1])

            # Поиск контуров
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

            for cnt in contours:

                self.IdContours[i] = cnt

                area = cv2.contourArea(cnt)

                self.dictContours[i] = ", " + color + " площадью " + str(area)
                i = i + 1

                if area > 10:
                    # Вычисляем координаты центра масс
                    M = cv2.moments(cnt)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])

                    # Пишем цвет фигуры рядом с её центром
                    cv2.putText(img, color, (cX, cY + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

                    # Нарисуем линии для вывода значения площади фигуры
                    point1 = (cX - 70, cY + 70)
                    point2 = (cX - 70 - 30, cY + 70)
                    point3 = (cX - 70 - 65, cY + 70 - 5)

                    cv2.line(img, (cX, cY), point1, (0, 0, 0), 1)
                    cv2.line(img, point1, point2, (0, 0, 0), 1)
                    cv2.putText(img, str(area), point3, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

        return self.dictContours, self.IdContours
