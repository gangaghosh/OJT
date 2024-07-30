import cv2
import numpy as np
import pygame

# Initialize Pygame mixer for playing the alert sound
pygame.mixer.init()
alert_sound = pygame.mixer.Sound('Fire_Detection/sound/siren-alert.mp3')  # Replace 'alert.wav' with your alert sound file

def play_alert_sound():
    pygame.mixer.Sound.play(alert_sound)

# Function to detect fire in the frame
def detect_fire(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the lower and upper bounds for the color of fire in HSV space
    lower_fire = np.array([18, 50, 50])
    upper_fire = np.array([35, 255, 255])
    
    # Create a mask to isolate fire-like regions in the frame
    mask = cv2.inRange(hsv, lower_fire, upper_fire)
    
    # Perform morphological operations to remove noise from the mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    fire_detected = False
    
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Adjust the contour area threshold as needed
            fire_detected = True
            # Draw a rectangle around the detected fire region
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    return fire_detected

# Start capturing video from the camera (or a video file)
cap = cv2.VideoCapture(0)  # Use 0 for webcam or provide a video file path

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect fire in the current frame
    if detect_fire(frame):
        play_alert_sound()
    
    # Display the frame
    cv2.imshow('Fire Detection', frame)
    
    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()
