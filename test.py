import cv2

cap = cv2.VideoCapture(0)

height = 720
width = 1280
frame_rate = 30.0

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter("Video.mp4", fourcc, frame_rate, (width, height))
recording = False

while True:
	ret, frame = cap.read()
	if ret:
		cv2.imshow("Video", frame)
		if recording:
			writer.write(frame)

	key = cv2.waitKey(1)
	if key == ord('r'):
		recording = not recording
		if recording:
			print("Recording")
		else:
			print("Stopped")
			break

cap.release()
writer.release()
cv2.destroyAllWindows()