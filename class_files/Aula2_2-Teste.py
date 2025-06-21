import numpy as np
import cv2

VIDEO = "dados/Arco.mp4"

cap = cv2.VideoCapture(VIDEO)
framesIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

frames = []
for fid in framesIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    hasFrame, frame = cap.read()
    frames.append(frame)

medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)
cv2.imwrite('median_frame_cinza.jpg',grayMedianFrame)

while (True):
    hasFrame, frame = cap.read()

    if not hasFrame:
        print('Acabou os frames')
        break

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frameGray)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()