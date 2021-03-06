import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

thr_min = 128
thr_max = 128

def on_thresold_min_change(pos):
    global thr_min
    thr_min = np.clip(pos * 2, 0, 255)

def on_thresold_max_change(pos):
    global thr_max 
    thr_max = np.clip(pos * 2, 0, 255)

cv2.namedWindow('Binary')


cv2.createTrackbar('thresold min', 'Binary', 102, 128, on_thresold_min_change)
cv2.createTrackbar('thresold max', 'Binary', 128, 128, on_thresold_max_change)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(gray, thr_min, thr_max, cv2.THRESH_BINARY)
    binary = cv2.bitwise_not(binary)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

    for contour in contours:
        epsilon = cv2.arcLength(contour, True) * 0.02
        approx_poly = cv2.approxPolyDP(contour, epsilon, True)

        for approx in approx_poly:
            cv2.circle(frame, tuple(approx[0]), 3, (255, 0, 0), -1)

    cv2.imshow('Binary', binary)
    cv2.imshow('Result', frame)



capture.release()
cv2.destroyAllWindows()