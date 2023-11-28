import cv2


class LiveCamera:
    def __init__(self, http):
        self.http = http

    def start_capture(self):
        cap = cv2.VideoCapture(self.http)

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (61, 61), 0)
            _, threshold = cv2.threshold(gray_frame, 30, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                if cv2.contourArea(contour) < 700:
                    continue
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow('Motion Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()  # Release the video capture object


if __name__ == "__main__":
    http_url = 'http://192.168.68.100:8080'

    run = LiveCamera(http_url)
    run.start_capture()
    cv2.destroyAllWindows()
