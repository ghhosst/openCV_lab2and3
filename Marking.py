import cv2
from ShapeDetector import ShapeDetector
from ColorAndAreaDetector import ColorAndAreaDetector


def fMarking(img):

    CA_detect = ColorAndAreaDetector()
    dictContours, IdContours = CA_detect.whatIsColorAndArea(img)
    sDetector = ShapeDetector()



    textFIO = "1141, Колесников Егор Вячеславович"
    cv2.putText(img, textFIO, (20, 35), cv2.FONT_HERSHEY_COMPLEX,
                0.4, (0, 0, 0), 0)

    textContours = "Количество найденных контуров: {}".format(len(dictContours))
    cv2.putText(img, textContours, (20, 55), cv2.FONT_HERSHEY_COMPLEX,
                0.4, (0, 0, 0), 0)

    print("\n1141, Колесников Егор Вячеславович")
    print("Количество найденных контуров: ", len(dictContours))
    print()


    for c in IdContours.values():
        # Вычисляем центр фигуры
        center = cv2.moments(c)
        centerX = int(center["m10"] / center["m00"])
        centerY = int(center["m01"] / center["m00"])

        # Определяем форму
        shape = sDetector.detect(c, dictContours, IdContours)

        # Рисуем контуры у фигур
        cv2.drawContours(img, [c], -1, (0, 0, 0), 2)
        cv2.circle(img, (centerX, centerY), 3, (0, 0, 0), -1)
        cv2.putText(img, shape, (centerX, centerY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)


    # for shape, details in sDetector.dictShapes.items():
    #     total = 0
    #     if isinstance(details, dict):
    #         for subtype, count in details.items():
    #             if subtype == "Общее количество: ":
    #                 total = count
    #
    #         if total != 0:
    #             print(shape)
    #             for subtype, count in details.items():
    #                 if count != 0:
    #                     print(f'    {subtype:<20} {count}')
    #     else:
    #         print(f'    Общее количество: {details}')
    #
    #     if total != 0:
    #         print()

    for shape, details in sDetector.dictShapes.items():
        total = details.get("Общее количество: ", 0)
        if total > 0:
            print(f"{shape}: \nОбщее количество: {total}")
            if isinstance(details, dict):
                for subtype, info in details.items():
                    if subtype != "Общее количество: " and isinstance(info, dict) and info['count'] != 0:
                        print(f'    {subtype:<20} {info["count"]}', end=' ')
                        for detail in info['details']:
                            print(f'{detail}', end=' ')
                        print()
            print()

    cv2.imshow("ResultImage", img)
    cv2.waitKey(0)
