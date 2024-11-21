import cv2
from cvzone.HandTrackingModule import HandDetector
from collections import Counter

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=2)

buffer = []
buffer_size = 10
string = ""
last_detection = None  # Track the last added character to the string
thumb_processed = False  # Flag to track if thumb gesture has been processed
hand_detected = False  # Track if a hand is currently detected
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    current_detection = None  # Reset for each frame

    if hands:
        hand1 = hands[0]
       
        lmList1 = hand1['lmList']
        hand_detected = True  # A hand is detected
        #print(hand1)

        if len(lmList1) != 0:
            

            fingers = detector.fingersUp(hand1)
            

            
            # Detect specific gestures based on finger patterns
            if hand1['type'] == 'Left':
                if fingers == [0, 0, 0, 0, 0]:  # One finger
                    print(hand1['type'])
                    string = ""
                    print("Delete")
                    
                elif fingers == [0, 1, 0, 0, 0]:  # One finger
                    current_detection = '1'
                elif fingers == [0, 1, 1, 0, 0]:  # Two fingers
                    current_detection = '2'
                elif fingers == [0, 1, 1, 1, 0]:  # Three fingers
                    current_detection = '3'
                elif fingers == [0, 1, 1, 1, 1]:  # Four fingers
                    current_detection = '4'
                elif fingers == [1, 1, 1, 1, 1]:  # Five fingers
                    current_detection = '5'
                
                elif fingers == [0, 1, 0, 0, 1]:  # One finger
                    current_detection = '-'
                
                    
            elif fingers == [0, 1, 0, 0, 0]:  # One finger
                current_detection = '6'
            elif fingers == [0, 1, 1, 0, 0]:  # Two fingers
                current_detection = '7'
            elif fingers == [0, 1, 1, 1, 0]:  # Three fingers
                current_detection = '8'
            elif fingers == [0, 1, 1, 1, 1]:  # Four fingers
                current_detection = '9'
            elif fingers == [1,0,1,1,1]:  # Five fingers
                current_detection = '0'
            elif fingers == [0, 1, 0, 0, 1]:  # Index and pinky (e.g., '+')
                current_detection = '+'
            
            
            # Handle "Thumbs Up" (only trigger result once)
            elif (lmList1[17][1] > lmList1[2][1]) :  # Thumb higher than usual
                if not thumb_processed:  # Process only once
                    print("THUMBS UP!!!")
                    result = eval(string) if string else 0  # Evaluate the string
                    print("Result:", result)
                    buffer.clear()
                    thumb_processed = True  # Mark thumb gesture as processed
                    continue
            
            #print(fingers)
            # Add the current detection to the buffer
            if current_detection is not None:
                buffer.append(current_detection)

            # Process the buffer when full
            if len(buffer) >= buffer_size:
                most_common = Counter(buffer).most_common(1)[0][0]
                
                # Add to string if:
                # - The most common detection is different, OR
                # - The hand was removed and redetected
                if most_common != last_detection or not hand_detected:
                    string += most_common
                    print("Updated String:", string)
                    last_detection = most_common  # Update last added character
                
                buffer.clear()
    else:
        # Reset flags and buffer when no hands are detected
        buffer.clear()
        thumb_processed = False  # Allow thumb gesture to be processed again
        hand_detected = False  # Reset hand detection flag
        last_detection = None  # Allow consecutive same numbers on re-detection
