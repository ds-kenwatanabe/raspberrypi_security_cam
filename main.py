import cv2


class LiveCamera:
    def __init__(self, http):
        self.http = http

    def start_capture(self):
        cap = cv2.VideoCapture(self.http)

        # Read initial frame for comparison
        ret_init, frame_init = cap.read()
        gray_frame_init = cv2.cvtColor(frame_init, cv2.COLOR_BGR2GRAY)
        gray_frame_init = cv2.GaussianBlur(gray_frame_init, (61, 61), 0)
        cv2.imshow('Win1', frame_init)

        while True:
            ret, frame = cap.read()
            text = "No movement"

            if not ret:
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (61, 61), 0)

            # Compute difference between current and first frame
            frame_delta = cv2.absdiff(gray_frame_init, gray_frame)
            _, threshold = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)
            threshold = cv2.dilate(threshold, None)
            # Find contours on the thresholded image
            contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Loop contours
            for contour in contours:
                if cv2.contourArea(contour) < 700:
                    continue
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Movement"

            cv2.putText(img=frame, text="Status: {}".format(text), org=(30, 20),
                        fontFace=0, fontScale=0.8, color=(0, 0, 255), thickness=3)
            cv2.imshow('Motion Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()  # Release the video capture object


if __name__ == "__main__":
    http_url = 'http://192.168.68.114:8080'

    run = LiveCamera(http_url)
    run.start_capture()
    cv2.destroyAllWindows()
