"""
.exe

Tracking
Отслеживание объекта
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys  # системный модуль
import os  # системный модуль для файловой системы

video_file = "race_car.mp4"  # путь до файла

def draw_rect(frame, bbox):  # border box
    """ нарисовать прямоугольник """
    # (x1=50, y1=30, x2=80, y2=150)
    pt1 = (int(bbox[0]), int(bbox[1]))
    pt2 = (int(bbox[0] + bbox[2]), int(bbox[1]+bbox[3]))
    cv2.rectangle(frame,
                  pt1=pt1,
                  pt2=pt2,
                  color=(30, 20, 255),
                  thickness=2)



# API - интерфейс
tracking_types = ['BOOSTING', # 0
                  'MIL',  # 1
                  'KCF',  # 2
                  'CSRT',  # 3
                  'TLD',  # 4
                  'MEDIANFLOW',  # 5
                  'GOTURN',  # 6
                  'MOSSE']

tracker_type = tracking_types[6]

# legacy code - python 2.7

if tracker_type == tracking_types[0]:
    tracker = cv2.legacy_TrackerBoosting.create()
elif tracker_type == tracking_types[1]:
    tracker = cv2.TrackerMIL.create()
elif tracker_type == tracking_types[2]:
    tracker = cv2.legacy_TrackerKCF.create()
elif tracker_type == "GOTURN":
    tracker = cv2.TrackerGOTURN.create()


bbox = (1300, 405, 160, 120)

cap = cv2.VideoCapture(video_file)
ok, frame = cap.read()
tracker.init(frame, bbox)

run = True
while run:
    if not cap.isOpened():  # если не удалось получить видеопоток
        print("Не удалось открыть видео!")
        sys.exit()  # закрыть приложение
    else:  # если видеопоток получить удалось
        width = cap.get(int(cv2.CAP_PROP_FRAME_WIDTH))
        height = cap.get(int(cv2.CAP_PROP_FRAME_HEIGHT))
        # [frame, frame, frame, frame, frame, frame, frame, frame, frame, frame, frame, frame]

    val, frame = cap.read()  # получить фрейм и возвращаемое значение
    #frame_width = 800
    #frame_height = frame.shape[1]
    #aspect_ratio = frame_width / frame_height
    #frame = cv2.resize(frame, dsize=(frame_width, int(frame_height * aspect_ratio)))
    if cv2.waitKey(1) == 27:  # 27 -> ESC
        break
    # АЛГОРИТМ ТРЕКИНГА

    ok, bbox = tracker.update(frame)
    if ok:
        draw_rect(frame, bbox)

    #draw_rect(frame, bbox)
    cv2.imshow("Car tracking", frame)
