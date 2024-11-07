import cv2
import numpy as np

# Open the video file
cap = cv2.VideoCapture('D:/Movies/@WMR_Laila.Majnu.2018.Hindi.1080p.HQ.HDRip.x265.Hevc.mkv')

while True:
    ret, frame = cap.read()
    
    # Check if the frame was successfully read
    if not ret:
        break
    
    # Define the points for perspective transformation
    pts1 = np.float32([[200, 300], [5, 2], [0, 4], [6, 0]])
    pts2 = np.float32([[0, 0], [400, 0], [0, 300], [400, 300]])
    
    # Get the transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    
    # Apply the perspective transformation
    height, width = frame.shape[:2]
    result = cv2.warpPerspective(frame, matrix, (width, height))
    
    # Display the original and transformed frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Transformed Frame', result)
    
    # Break the loop if the 'Esc' key is pressed
    if cv2.waitKey(24) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
