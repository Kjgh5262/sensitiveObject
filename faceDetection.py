from generic.templates.basicDetection import basicDetection

class faceDetection(basicDetection):
	def __init__(self):
		pass

	def loadImage(self):
		raise NotImplementedError

	def findSensitiveObject(self):
		raise NotImplementedError

	def removeSensitiveObject(self):
		raise NotImplementedError

	def sendImage(self):
		raise NotImplemetedError

if __name__ == "__main__":
	faceDetection()