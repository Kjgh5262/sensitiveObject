import cv2

class basicDetection(object):
	def __init__(self):
		faces, image = self.findSensitiveObject()
		self.removeSensitiveObject(faces, image)
		self.sendImage()

	def loadImage(self):
		raise NotImplementedError

	def findSensitiveObject(self):
		self.loadImage()
		self.removeSensitiveObject()

	def removeSensitiveObject(self, faces, image):
		raise NotImplementedError

	def sendImage(self):
		raise NotImplemetedError

	def rotateImage(self, image, rotate):
		rows, cols, _ = image.shape
		M = cv2.getRotationMatrix2D((cols/2,rows/2),rotate,1)
		return cv2.warpAffine(image,M,(cols,rows))

if __name__ == "__main__":
	basicDetection()