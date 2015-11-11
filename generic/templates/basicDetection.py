class basicDetection(object):
	def __init__(self):
		self.findSensitiveObject()
		self.sendImage()

	def loadImage(self):
		raise NotImplementedError

	def findSensitiveObject(self):
		self.loadImage()
		self.removeSensitiveObject()

	def removeSensitiveObject(self):
		raise NotImplementedError

	def sendImage(self):
		raise NotImplemetedError

if __name__ == "__main__":
	basicDetection()