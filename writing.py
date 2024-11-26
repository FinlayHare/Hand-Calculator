import cv2
from cvzone.HandTrackingModule import HandDetector
from collections import Counter
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)  
detector = HandDetector(detectionCon=0.9, maxHands=2)

draw_color = (255, 255, 255) 
erase = (0,0,0)
canvas=None

small_canvas = np.zeros((28, 28, 3), dtype=np.uint8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    hands, img = detector.findHands(img)
    # Could have used the code below to show the correct hand being used, but it greatly reduced the tracking performance.
    #hands, img = detector.findHands(img, flipType=False)
    #cv2.imshow('Hand', img)
    
    cv2.waitKey(1)
        
    
    # Prepare canvas if not initialized
    if canvas is None:
        canvas = img.copy() * 0 #Black canvas, will be overlaid img later
        
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
                cv2.circle(canvas, (x, y), 30, draw_color, -1)
                
            elif fingers == [0, 1, 1, 0, 0]:  # Two fingers
                #print(lmList1[8][0:3])
                x = int(lmList1[8][0])
                y = int(lmList1[8][1])
                print([x,y])
                cv2.circle(canvas, (x, y), 60, erase, -1)
            
            elif fingers == [0, 1, 1, 1, 0]:  # Two fingers
                #print(lmList1[8][0:3])
                x = int(lmList1[8][0])
                y = int(lmList1[8][1])
                print([x,y])
                cv2.circle(canvas, (x, y), 200, erase, -1)
            
            elif fingers == [0, 1, 0, 0, 1]:
                
                small_canvas = cv2.resize(canvas, (28, 28), interpolation=cv2.INTER_AREA)
                #PUT IN YOUR OWN FILE PATH
                file_name = r'C:\OWN\FILE\PATH\openCVpic.jpg'  
                cv2.imwrite(file_name, small_canvas)
                small_canvas_preview = cv2.resize(small_canvas, (200, 200))
                print("saving")
                
                # Next step is to save the img in the correct format
                
    combined = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)
    cv2.imshow('Hand Drawing', combined)
 