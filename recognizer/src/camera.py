import threading
import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set frame width
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set frame height
        self.video.set(cv2.CAP_PROP_FPS, 15)  # Set frame rate
        self.lock = threading.Lock()
        self.grabbed, self.frame = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        with self.lock:
            return self.frame

    def update(self):
        while True:
            grabbed, frame = self.video.read()
            if grabbed:
                with self.lock:
                    self.frame = frame

def gen(camera):
    while True:
        frame = camera.get_frame()
        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
