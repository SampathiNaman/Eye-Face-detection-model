import os
import cv2
import argparse
import numpy as np

script_dir = os.path.dirname(os.path.realpath(__file__))

face_cascade_path = os.path.join(script_dir, "models/face_cascade.xml")
eye_cascade_path = os.path.join(script_dir, "models/eye_cascade.xml")

def detect_and_display(frame, face_cascade, eye_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, minNeighbors=10, scaleFactor=1.1, minSize=(32,32))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, minNeighbors=10, scaleFactor=1.4, minSize=(30,30), maxSize=(100,100))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
    cv2.imshow('Result', frame)

def detect_faces_and_eyes(input_path=None, input_type='webcam'):
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
    
    if input_type == 'image':
        img = cv2.imread(input_path)
        detect_and_display(img, face_cascade, eye_cascade)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif input_type == 'video' or input_type == 'webcam':
        if input_type == 'webcam':
            input_path = 0  # Use default webcam
        cap = cv2.VideoCapture(input_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                continue
            detect_and_display(frame, face_cascade, eye_cascade)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Face and Eye Detection')
    parser.add_argument('--image', type=str, help='Path to the image file')
    parser.add_argument('--video', type=str, help='Path to the video file')
    args = parser.parse_args()

    if args.image:
        detect_faces_and_eyes(args.image, 'image')
    elif args.video:
        detect_faces_and_eyes(args.video, 'video')
    else:
        detect_faces_and_eyes()