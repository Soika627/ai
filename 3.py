"""
1. Как обрабатывать видео-файл
2. Как записывать экран и обрабатывать его?
"""

import cv2
import numpy as np
import mss  # для скриншотов
from PIL import Image  # разные манипуляции над картинками

# размеры экрана и точка захвата
monitor = {
    "top": 0,
    "left": 0,
    "width": 1600,
    "height": 900,
}

fps = 30
output_file = "video.mp4"

# объект для mss для захвата экрана
sct = mss.mss()  # модуль.класс -> объект

# настройка видеозаписи
# кодек
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (1600, 900))

run = True
while run:
    frame = sct.grab(monitor)
    img = Image.frombytes("RGB", frame.size, frame.rgb)
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # записывать с какими-то фильтрамиq
    #frame = cv2.Canny(frame, 80, 150)

    out.write(frame)
    #cv2.imshow("Desktop capture", frame)

    if cv2.waitKey(1) == ord("q"):
        run = False

out.release()  #
