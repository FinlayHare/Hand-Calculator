import cv2
from cvzone.HandTrackingModule import HandDetector
from collections import Counter

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=2)

draw_color = (0, 255, 0) 
erase = (0,0,0)
canvas=None

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=False)
    cv2.waitKey(1)
    
    
    h, w, c = img.shape

    # Prepare canvas if not initialized
    if canvas is None:
        canvas = img.copy() * 0
        
    if hands:
        hand1 = hands[0]

        lmList1 = hand1["lmList"]
        hand_detected = True  # A hand is detected
            # print(hand1)

        if len(lmList1) != 0:

            fingers = detector.fingersUp(hand1)

                # Detect specific gestures based on finger pattern
            if fingers == [0, 1, 0, 0, 0]:  # One finger
                #print(lmList1[8][0:3])
                x = int(lmList1[8][0])
                y = int(lmList1[8][1])
                print([x,y])
                cv2.circle(canvas, (x, y), 20, draw_color, -1)
                
            elif fingers == [0, 1, 1, 0, 0]:  # One finger
                #print(lmList1[8][0:3])
                x = int(lmList1[8][0])
                y = int(lmList1[8][1])
                print([x,y])
                cv2.circle(canvas, (x, y), 60, erase, -1)
                
                
    combined = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)
    cv2.imshow('Hand Drawing', combined)
    if cv2.waitKey(1) & 0xFF == 27:
        break