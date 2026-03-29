"""
Computer Vision

Ultra Realistics - это надстройка (модуль) на основе
модуля cv2, который предоставляет доступ к дообученным модулям
для решения множества прикладных задач по определению объектов на экране


python -m pip install opencv-python
pip install opencv-python

ultra realistic yolo docs

pip install -U ultralytics
"""

import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("Source/race_car.mp4")
assert cap.isOpened(), "Error reading video file"


# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

region_points = [(0, h), (w, h), (w, 0), (0, 0)]  # rectangular region

# Initialize object counter object
counter = solutions.ObjectCounter(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo26n.pt",  # model="yolo26n-obb.pt" for object counting with OBB model.
    classes=[0, 2],  # count specific classes, e.g., person and car with the COCO pretrained model.
    # tracker="botsort.yaml",  # choose trackers, e.g., "bytetrack.yaml"
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = counter(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows

