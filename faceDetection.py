import cv2
import sys

from generic.templates.basicDetection import basicDetection

class faceDetection(basicDetection):
	def loadImage(self, picture):
		return cv2.imread(picture)

	def findSensitiveObject(self):
		faceCascade = self._getCascade(sys.argv[2])
		image = self.loadImage(sys.argv[1])
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.3,
			minNeighbors=3,
			flags = 30,
			minSize=(5, 10)
		)

		print "Found {0} faces!".format(len(faces))
		self.removeSensitiveObject(faces, image)

	def removeSensitiveObject(self, faces, image):
		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

		cv2.imshow("Faces found" ,image)
		cv2.waitKey(0)

	def sendImage(self):
		pass

	def _getCascade(self, cascade):
		return cv2.CascadeClassifier(cascade)

if __name__ == "__main__":
	faceDetection()