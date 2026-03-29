"""
Computer Vision - это область задач,
для анализа изображения в режиме реального времени.
"""

import cv2   # computer vision 2
# нужно установить matplotlib
import matplotlib.pyplot as plt
import numpy as np

# pip install matplotlib

# когда мы считываем изображение, можно использовать дополнительные аргументы
# imread(img, 0)
# По умолчанию число 1, есть варианты 0 и -1
cb_img = cv2.imread("checkerboard_84x84.jpg", 0)
coke_img = cv2.imread("coca-cola-logo.png", 0)  # чёрно-белый режим
cb_18_img = cv2.imread("checkerboard_18x18.png", 0)
nz_img = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)

# 2 способа какие мы будем использовать
# чтобы отобразить изображение

# 1 способ через экран opencv
# window1 = "win1"
# cv2.imshow(window1, coke_img)
# cv2.waitKey(8000)
# cv2.destroyWindow(window1)

# 2 способ это использовать модуль matplotlib
print(cb_img)
# plt.imshow(coke_img)
# plt.title("matplotlib imshow")
# plt.show()

# манипуляции над изображениями
print(cb_img[10,50])
print(cb_img.shape)
cb_img[10:20,50:100] = 10

#               [:, :, ::-1]
#nz_img = nz_img[:,:,::-1]  # перевёл из BGR в RGB (поменял местами B и R)
# RGB (10, 50, 100) BGR (80, 50, 20)
nz_img_center = nz_img[200:600, 200:400]

# перевернуть изображение или какую-то ось изображения
nz_flipped = cv2.flip(nz_img, 1)  # flip(img, ) 0 1 -1

# изменение изображения
nz_resized = cv2.resize(nz_img, dsize=(20, 20))

# Добавление аннотаций
# 1. рисовать линии
cv2.line(nz_img,
        (100, 100),
        (800, 100),
        (0, 255, 255),
        8)
# line(img, point1(x,y), point2(x,y), цвет(rgb), толщина, внешний вид линии)

# нарисовать окружность
#                                   BGR
cv2.circle(nz_img,(400,250), 100, (0,255,255), 3)
# квадрат
cv2.rectangle(nz_img,(500,350),(700,500),(0,255,0),3)

font = cv2.FONT_ITALIC
font_size = 1.3
font_color = (0, 0, 255)
font_thickness = 3
# putText(img, text, coordinate, font_type, font_color, font_thickness)
cv2.putText(nz_img,
            "This is exampe of text",
            (300, 150),
            font,
            font_size,
            font_color,
            font_thickness)


# Математические манипуляции над изображениями
# Изменение яркости изображения
# [(11, 50, 30) 50 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 00 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#
# ]
matrix = np.ones(nz_img.shape, dtype="uint8") * 50
img_rgb_bright = cv2.add(nz_img, matrix)
img_rgb_dark = cv2.subtract(nz_img, matrix)

img_coast = cv2.imread("New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
# манипуляции с контрастностью
matrix1 = np.ones(img_coast.shape) * 0.8   # 80% контрастности
matrix2 = np.ones(img_coast.shape) * 1.2  # 120% контрастности

img_low_cont = np.uint8(cv2.multiply(np.float64(img_coast), matrix1))
img_high_cont = np.uint8(cv2.multiply(np.float64(img_coast), matrix2))

"""
Thresholding
Пороговое значение
"""

img_building = cv2.imread("building-windows.jpg", cv2.IMREAD_GRAYSCALE)

# возвращает пару значений (val1, val2)
retval, dist = cv2.threshold(img_building, 100, 255, cv2.THRESH_BINARY)

img_notes = cv2.imread("Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)

retval, dist1 = cv2.threshold(img_notes, 60, 255, cv2.THRESH_BINARY)
retval, dist2 = cv2.threshold(img_notes, 100, 255, cv2.THRESH_BINARY)
img_notes_adaptive = cv2.adaptiveThreshold(img_notes, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

# plt.figure(figsize=[8, 6])
# plt.subplot(221)
# plt.title("Original")
# plt.imshow(img_notes, cmap="gray")
#
# plt.subplot(222)
# plt.title("Threshold 60")
# plt.imshow(dist1, cmap="gray")
#
# plt.subplot(223)
# plt.title("Threshold 100")
# plt.imshow(dist2, cmap="gray")
#
# plt.subplot(224)
# plt.title("Threshold adaptive [11, 7]")
# plt.imshow(img_notes_adaptive, cmap="gray")
#
# plt.show()

"""
Bitwice операции
"""

img_rect = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
img_circle = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)

# Bitwice - объединение изображений или их частей
# Зачастую есть 4 логические операции: AND OR XOR NOT

result1 = cv2.bitwise_and(img_rect, img_circle, mask=None)
result2 = cv2.bitwise_or(img_rect, img_circle, mask=None)
result3 = cv2.bitwise_xor(img_rect, img_circle, mask=None)

img_coke = cv2.imread("coca-cola-logo.png", cv2.COLOR_BGR2RGB)
img_coke = img_coke[:,:,::-1]  # поменял местами синий и красный цвет для каждого пикселя
img_cb_color = cv2.imread("checkerboard_color.png", cv2.COLOR_BGR2RGB)
print(img_coke.shape, img_cb_color.shape)

logo_w = img_coke.shape[0]  # ширина
logo_h = img_coke.shape[1]  # высота
aspect_ration = logo_w / img_cb_color.shape[1]
dim = (logo_w, int(img_cb_color.shape[0] * aspect_ration))

img_cb_color = cv2.resize(img_cb_color, dim, interpolation=cv2.INTER_AREA)
print(img_coke.shape, img_cb_color.shape)

# создал новое изображение, серого цвета (среднее между белым и чёрным)
#                           размер          цвет
img_gray = cv2.cvtColor(img_coke, cv2.COLOR_RGB2GRAY)

# создание маски оригинального изображения кока-колы
# threshold - он анализирует цвета всех пикселей
# и закрашивает пиксели, которые нам не подошли в определенный цвет
val, img_mask = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
inv_mask = cv2.bitwise_not(img_mask)  # инвертируем маску с помощью bitwice

# результирующее действие, но с чёрным фоном. Сама радужная кола
img_bitmask = cv2.bitwise_and(img_cb_color, img_cb_color, mask=img_mask)

# изолирую красный фон отдельно
img_foreground = cv2.bitwise_and(img_coke, img_coke, mask=inv_mask)

result = cv2.add(img_bitmask, img_foreground)  # радужная-кола с красным фоном

plt.figure(figsize=[15, 8])  # 15, 8 - размер формы в дюймах
plt.subplot(221)  # каждое отдельное изображение на этой форме, но в определенном месте на форме
plt.imshow(img_coke)

plt.subplot(222)
plt.imshow(img_cb_color)

plt.subplot(223)
plt.imshow(img_mask, cmap="gray")

plt.subplot(224)
plt.title("Result")
plt.imshow(result)


plt.show()

# run = True
# while run:
#     # буду отображать что-то до тех  пор, пока не нажал клавишу
#     cv2.imshow("Пример threshold", dist)
#
#     keypress = cv2.waitKey(1) # начинай считывать клавишу с клавиатуры
#     if keypress == ord('q'):  # ASCII, UNICODE  "q" -> 118
#         run = False

