import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()
smoothening = 5
scroll_sensitivity = 100 # Adjust scrolling speed

prev_x, prev_y = 0, 0
prev_scroll_y = 0
scroll_mode = False

def is_finger_extended(landmarks, tip_idx, pip_idx):
    tip = landmarks.landmark[tip_idx]
    pip = landmarks.landmark[pip_idx]
    return tip.y < pip.y  # Lower y value means higher position on screen

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_extended = is_finger_extended(hand_landmarks, 8, 6)
            middle_extended = is_finger_extended(hand_landmarks, 12, 10)
            
            # Scroll mode (two fingers extended)
            if index_extended and middle_extended:
                index_y = hand_landmarks.landmark[8].y
                middle_y = hand_landmarks.landmark[12].y
                current_avg_y = (index_y + middle_y) / 2

                if not scroll_mode:
                    scroll_mode = True
                    prev_scroll_y = current_avg_y
                else:
                    delta_y = prev_scroll_y - current_avg_y
                    scroll_amount = delta_y * scroll_sensitivity
                    pyautogui.scroll(int(scroll_amount))
                
                prev_scroll_y = current_avg_y
            else:
                scroll_mode = False
                # Cursor movement
                index_finger = hand_landmarks.landmark[8]
                x, y = int(index_finger.x * screen_width), int(index_finger.y * screen_height)
                curr_x = prev_x + (x - prev_x) / smoothening
                curr_y = prev_y + (y - prev_y) / smoothening
                pyautogui.moveTo(curr_x, curr_y)
                prev_x, prev_y = curr_x, curr_y

            # Right-click (ring finger close to thumb)
            ring_tip = hand_landmarks.landmark[16]
            thumb = hand_landmarks.landmark[4]
            distance_right = ((ring_tip.x - thumb.x)**2 + (ring_tip.y - thumb.y)**2)**0.5
            if distance_right < 0.03:
                pyautogui.rightClick()
                pyautogui.sleep(0.2)
            # Left-click (index finger close to thumb)
            else:
                index_finger = hand_landmarks.landmark[8]
                distance_left = ((index_finger.x - thumb.x)**2 + (index_finger.y - thumb.y)**2)**0.5
                if distance_left < 0.03:
                    pyautogui.click()
                    pyautogui.sleep(0.2)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()