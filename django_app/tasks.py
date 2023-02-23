from celery import shared_task
import cv2


@shared_task
def process_video():
    video_path = 'static/YouTube.mp4'
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            cv2.imwrite('static/faces/face_{}.jpg'.format(len(faces)), face)

    cap.release()
