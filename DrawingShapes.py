import cv2
import numpy as np


def Draw():
    img = np.full((700, 1000, 3), 255, dtype=np.uint8)


    # Цвета
    yellow = (0, 244, 246)
    green = (0, 130, 0)
    red = (0, 0, 251)
    blue = (251, 0, 0)
    violet = (128, 0, 128)
    aquamarine = (212, 254, 127)
    khaki = (140, 230, 240)
    silver = (192, 192, 192)




    # Равносторонний треугольник
    points = np.array([[[500, 250], [550, 250 + 100 * (np.sqrt(3) / 2)],
                        [450, 250 + 100 * (np.sqrt(3) / 2)]]], dtype=np.int32)
    cv2.fillPoly(img, [points], color=yellow)

    # Произвольный треугольник
    points = np.array([[[300, 590], [400, 550], [500, 660]]], dtype=np.int32)
    cv2.fillPoly(img, [points], color=green)

    # Ромб
    points = np.array([[[850, 310], [900, 410], [850, 510], [800, 410]]], dtype=np.int32)
    cv2.fillPoly(img, [points], color=red)

    # Трапеция
    points = np.array([[[630, 570], [730, 570], [800, 660], [600, 660]]], dtype=np.int32)
    cv2.fillPoly(img, [points], color=blue)

    # Квадрат
    cv2.rectangle(img, (250, 150), (350, 250), violet, -1)

    # Пятиугольник
    points = np.array([[[730, 200], [780, 150], [840, 200], [805, 270], [755, 270]]], dtype=np.int32)
    cv2.fillPoly(img, [points], color=aquamarine)

    # Круг
    cv2.circle(img, (640, 440), 60, khaki, -1)

    # Параллелограмм
    points = np.array([[[100, 500 - 80], [300, 500 - 80], [250, 600 - 80], [50, 600 - 80]]], dtype=np.int32)
    cv2.fillPoly(img, [points], color=silver)


    # Прямоугольный треугольник
    # points = np.array([[[900, 600], [900, 550], [800, 600]]], dtype=np.int32)
    # cv2.fillPoly(img, [points], color=(60, 89, 130))

    # Эллипс
    # cv2.ellipse(img, (320, 390), (100, 50), 45, 0, 360, (72, 207, 45), -1)

    # Прямоугольник
    # cv2.rectangle(img, (460, 140), (660, 230), (120, 8, 85), -1)

    # Шестиугольник
    # points = np.array([[520, 420], [495, 463], [445, 463],
    #                   [420, 420], [445, 376], [495, 376]], np.int32)
    # cv2.fillPoly(img, [points], (172, 10, 252))



    cv2.imwrite('C:\\Users\\koles\\PycharmProjects\\openCV_lab2\\image1.jpg', img)
    output = img.copy()

    return output
