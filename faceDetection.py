import cv2
import sys

from generic.templates.basicDetection import basicDetection

class faceDetection(basicDetection):
	cascade = "utils\haarcascade_frontalface_default.xml"
	def loadImage(self, picture):
		return cv2.imread(picture)

	def getGrayColor(self, image):
		return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	def findSensitiveObject(self, scaleFactor=1.3, minNeighbors=1, flags=10, minSize=(5, 10)):
		faceCascade = self._getCascade(self.cascade)
		image = self.loadImage(sys.argv[1])

		faces = faceCascade.detectMultiScale(
			self.getGrayColor(image),
			scaleFactor=scaleFactor,
			minNeighbors=minNeighbors,
			flags = flags,
			minSize=minSize
		)

		print "Found {0} faces!".format(len(faces))
		return faces, image

	def removeSensitiveObject(self, faces, image):
		#result_image = image.copy()
		for f in faces:
			x, y, w, h = [ v for v in f ]

			cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 1)
			#sub_face = image[y:y+h, x:x+w]
			#sub_face = cv2.GaussianBlur(sub_face,(23, 23), 30)
			#result_image[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
		cv2.imshow("Faces found" ,image)
		cv2.waitKey(0)

	def sendImage(self):
		pass

	def _getCascade(self, cascade):
		return cv2.CascadeClassifier(cascade)

if __name__ == "__main__":
	faceDetection()