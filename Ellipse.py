import cv2
import numpy as np


def isEllipse(self, approx, dictContours, keyId):
    # Вычисляем площадь контура
    area1 = cv2.contourArea(approx)

    # Вычисляем параметры эллипса, наилучшим образом приближающего контур
    (x, y), (MA, ma), angle = cv2.fitEllipse(approx)

    # Если большая и малая оси близки, то это окружность
    if np.isclose(MA, ma, rtol=0.1):
        self.shape = " circle"
        self.dictShapes["Эллипсы"]["Окружность: "]["count"] += 1
        self.dictShapes["Эллипсы"]["Окружность: "]["details"].append(dictContours[keyId])
        return True

    # Вычисляем площадь этого эллипса
    area2 = np.pi * (MA / 2) * (ma / 2)

    # Если площади близки, то это эллипс
    if np.isclose(area1, area2, rtol=0.1):
        self.shape = " ellipse"
        self.dictShapes["Эллипсы"]["Эллипс: "]["count"] += 1
        self.dictShapes["Эллипсы"]["Эллипс: "]["details"].append(dictContours[keyId])
        return True

    return False
