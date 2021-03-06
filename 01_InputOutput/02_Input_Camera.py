import cv2

capture = cv2.VideoCapture(1, cv2.CAP_DSHOW)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(10) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()