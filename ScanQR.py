import cv2
import numpy as np
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines()

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        flag = False
        if myData in myDataList:
            print('Access Granted')
            myColor = (0, 255, 0)
            flag = True
        else:
            print('Access Denied')
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape(-1, 1, 2)
        cv2.polylines(img, [pts], True, (0, 255, 0) if flag else (0, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(img, "Access Granted" if flag else "Access denied", (pts2[0], pts2[1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0) if flag else (0, 0, 255), 2)

    cv2.imshow('Scan your QR Code here', img)
    cv2.waitKey(1)