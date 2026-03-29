"""
Загрузка видео и обработка видео через cv2
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# относительный путь до файла
source = "race_car.mp4"  # путь до файла

cap = cv2.VideoCapture(source)
"""
ТАБЛИЦА СИМВОЛОВ ASCII
a -> 100101010101 -> 1FF2 -> 15
b -> 110101101011 -> 1DE2 -> 16
*ESC* -> 11010101111 -> 11FF -> 27
"""
mode = 0
while cv2.waitKey(1) != 27:  # код клавиши ESCAPE
# not cap.isOpened()
    if cap.isOpened() == False:
        print("Не удалось открыть видеофайл")
    key = cv2.waitKey(10) # возвращет число, соответствующее текущей нажатой клавише

    if key == 113:  # 'q' -> 55
        mode = 1
    elif key == 119:
        mode = 2
    elif key == 120:  # ord()
        mode = 0

    val, frame = cap.read()  # читаем видеофайл покадрово
    if val == False:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # начни с фрейма 0
        continue
    if mode == 1:
        result = cv2.Canny(frame, 80, 150)
    elif mode == 2:
        result = cv2.blur(frame, (13, 13))
    elif mode == 0:
        result = frame



    cv2.imshow("Видео", result)
