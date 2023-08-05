import cv2 as cv

# img=cv.imread("Photos\cat_large2.jpg")
# cv.imshow()


open

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeres(width, height):
    capture.set(3, width)
    capture.set(4, width)

capture = cv.VideoCapture("Videos\dog.mp4")
while True:
    isTrue,    frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow("Video", frame)
    cv.imshow("video resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
capture.destroyAllWindows()
