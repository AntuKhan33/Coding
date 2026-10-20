import cv2
from ultralytics import YOLO
import numpy as np
import math
import cvzone

# Load YOLOv8 model (pretrained, you can fine-tune on basketballs)
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("Videos/vid (4).mp4")

poslistX, poslistY = [], []
xlist = [item for item in range(0, 1300)]
prediction = False

while True:
    success, img = cap.read()
    if not success:
        break
    img = img[0:900, :]

    # Detect objects with YOLO
    results = model(img, verbose=False)
    ball_center = None

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            if cls == 32 and conf > 0.4:  # 'sports ball' in COCO dataset
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                ball_center = ((x1 + x2) // 2, (y1 + y2) // 2)
                cv2.circle(img, ball_center, 10, (0, 255, 0), cv2.FILLED)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # If ball detected, track trajectory
    if ball_center:
        poslistX.append(ball_center[0])
        poslistY.append(ball_center[1])

    if poslistX:
        # Fit trajectory using quadratic regression
        A, B, C = np.polyfit(poslistX, poslistY, 2)

        # Draw trajectory
        for i, (posX, posY) in enumerate(zip(poslistX, poslistY)):
            cv2.circle(img, (posX, posY), 10, (0, 255, 0), cv2.FILLED)
            if i > 0:
                cv2.line(img, (poslistX[i - 1], poslistY[i - 1]), (posX, posY), (0, 255, 0), 2)

        for x in xlist:
            y = int(A * x ** 2 + B * x + C)
            cv2.circle(img, (x, y), 1, (255, 0, 0), cv2.FILLED)

        # Predict final x position at hoop height (y=590)
        a, b, c = A, B, C - 590
        if b**2 - 4*a*c >= 0:  # valid solution
            x_pred = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
            prediction = 330 < x_pred < 430
            print("Prediction:", prediction, "x=", x_pred)

            if prediction:
                cvzone.putTextRect(img, "Basket Ball Shot", (50, 150), scale=5,
                                   thickness=3, colorR=(0, 200, 0), offset=20)
            else:
                cvzone.putTextRect(img, "No Basket Ball Shot", (50, 150),
                                   scale=5, thickness=3, colorR=(0, 0, 200), offset=20)

    cv2.imshow("Shot Detection", img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
