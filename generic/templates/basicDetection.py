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

if __name__ == "__main__":
	basicDetection()