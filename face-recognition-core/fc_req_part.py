from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2


currentname = "Unknown"
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open("encodings.pickle", "rb").read())
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=500)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30))

	boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
	
	encodings = face_recognition.face_encodings(rgb, boxes)
	names = []
	
	for encoding in encodings:

		matches = face_recognition.compare_faces(data["encodings"], encoding)
		name = "Unknown"
		# check to see if 
		if True in matches:

			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			name = max(counts, key=counts.get)
			
			if currentname != name:
				currentname = name
				print(currentname)

		names.append(name)

	for ((top, right, bottom, left), name) in zip(boxes, names):
		# draw the predicted face name on the image
		cv2.rectangle(frame, (left, top), (right, bottom),
			(0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			0.75, (0, 255, 0), 2)
	# display the image to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
