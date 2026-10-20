import cv2
from ultralytics import YOLO
import numpy as np
import math
import cvzone
import pickle

# -----------------------------
# Load YOLOv8 model
# -----------------------------
model = YOLO("yolov8n.pt")  # pretrained COCO model

# -----------------------------
# Load Random Forest classifier
# -----------------------------
clf = pickle.load(open("shot_classifier.pkl", "rb"))

# -----------------------------
# Video capture
# -----------------------------
cap = cv2.VideoCapture("1.mov")

# -----------------------------
# Tracking variables
# -----------------------------
poslistX, poslistY = [], []
xlist = [item for item in range(0, 1300)]

while True:
    success, img = cap.read()
    if not success:
        break
    img = img[0:900, :]  # crop if needed

    # -----------------------------
    # Detect ball with YOLO
    # -----------------------------
    results = model(img, verbose=False)
    ball_center = None

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            if cls == 32 and conf > 0.4:  # COCO 'sports ball'
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                ball_center = ((x1 + x2) // 2, (y1 + y2) // 2)
                cv2.circle(img, ball_center, 10, (0, 255, 0), cv2.FILLED)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # -----------------------------
    # Track trajectory
    # -----------------------------
    if ball_center:
        poslistX.append(ball_center[0])
        poslistY.append(ball_center[1])

    if poslistX:
        # Quadratic regression
        A, B, C = np.polyfit(poslistX, poslistY, 2)

        # Draw trajectory points
        for i, (posX, posY) in enumerate(zip(poslistX, poslistY)):
            cv2.circle(img, (posX, posY), 10, (0, 255, 0), cv2.FILLED)
            if i > 0:
                cv2.line(img, (poslistX[i - 1], poslistY[i - 1]), (posX, posY), (0, 255, 0), 2)

        # Draw predicted trajectory
        for x in xlist:
            y = int(A * x ** 2 + B * x + C)
            cv2.circle(img, (x, y), 1, (255, 0, 0), cv2.FILLED)

        # Predict landing x at hoop height y=590
        a, b, c_new = A, B, C - 590
        if b**2 - 4*a*c_new >= 0:
            x_pred = int((-b - math.sqrt(b**2 - 4*a*c_new)) / (2 * a))

            # -----------------------------
            # Use ML classifier
            # -----------------------------
            features = [[A, B, C, x_pred, 590]]
            prediction = clf.predict(features)[0]  # 1 = made, 0 = missed

            if prediction:
                cvzone.putTextRect(img, "Basket Ball Shot", (50, 150), scale=5,
                                   thickness=3, colorR=(0, 200, 0), offset=20)
            else:
                cvzone.putTextRect(img, "No Basket Ball Shot", (50, 150),
                                   scale=5, thickness=3, colorR=(0, 0, 200), offset=20)

    # -----------------------------
    # Show image
    # -----------------------------
    cv2.imshow("Basket Shot Detection", img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
