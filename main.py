import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE, -4)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    # detect the markers
    corners, ids, rejected = detector.detectMarkers(gray)

    print("Detected markers:", ids)

    if ids is not None:
        cv2.aruco.drawDetectedMarkers(image=frame, corners=corners, ids=ids)

    cv2.imshow("Detected Markers", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
