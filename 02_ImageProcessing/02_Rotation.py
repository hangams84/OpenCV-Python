import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    height, width, channel = frame.shape
    matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
    dst = cv2.warpAffine(frame, matrix, (width, height))
    cv2.imshow("Rotation", dst)

capture.release()
cv2.destroyAllWindows()