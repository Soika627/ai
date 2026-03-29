"""
Запись видео через CV
"""

"""
1. Запись видео с веб-камеры
"""

import cv2
import sys  # системный модуль, операционной системы
import numpy as np

feature_params = {
    "max_corners": 500,
    "quality_level": 0.2,
    "min_distance": 15,
    # "block_size": 9
}

s = 0  # определяю переменную
if len(sys.argv) > 1:  # если есть вебкамера на компьютере
    s = sys.argv[1]

source = cv2.VideoCapture(s)  # source - источник
win_name = "Camera"  # название окошка
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)  # создаем GUI

# cv2.waitKey(1) - как часто мы отслеживаем нажатие клавиши
while cv2.waitKey(1) != 27:  # код клавиши ESCAPE в ASCII
    has_frame, frame = source.read()  # получает видео (True, frame)

    frame = cv2.flip(frame, 1)  # отзеркалить изображение

    # **распаковка словаря
    # *list
    """
    arr = [126,2232,32323,511]
    fucn(*arr) -> распаковка списка   

    """

    #
    result = frame
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    corners = cv2.goodFeaturesToTrack(frame_gray, 500, 0.2, 15.0, 12)
    if corners is not None:
        print(corners)
        for (x, y) in np.float32(corners).reshape(-1, 2):
            cv2.circle(frame, (int(x), int(y)), 10, (0, 255, 0), 1, cv2.LINE_AA)

    # result = cv2.Canny(frame, 80, 150)  # мы применили к фрейму (изображению) фильтр Canny
    # result = cv2.blur(result, (13, 13))  # применяю фильтр blur

    if not has_frame:  # если по какой-то причине мы перестали получать кадры от устройства
        break  # то выходим из цикла
    cv2.imshow(win_name, frame)  # отобразить на нашем GUI

source.release()  # освободили память
