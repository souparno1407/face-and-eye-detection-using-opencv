import cv2
import numpy as np

# Creating cascade classifiers for face and eye
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Capturing video. 0 is passed to set it to the default webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Multi-scale is used to analyze the image with various scales so that it can succesfully detect small faces as well
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.25, # You may play around with this scaling factor to obtain better results
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
    # Do the same thing for eyes
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    #Press q to terminate the program or else go on detecting
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture after pressing the quit button and destroy the windows
video_capture.release()
cv2.destroyAllWindows()
