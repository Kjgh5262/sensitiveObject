import sys

sys.path.append("C:\\Users\\Nocturne\\Desktop\\magister")
from imageDict import imageDict
from sensitiveObject.faceDetection import faceDetection

class test(faceDetection):
	cascade = "C:\Users\Nocturne\Desktop\magister\sensitiveObject\utils\haarcascade_frontalface_default.xml"
	def __init__(self):
		self.testAbba()

	def testAbba(self):
		expectedFaces = 4
		for scale in range(11, 14, 1):
			for neighbor in range(1,5):
				for flag in range (10, 30, 5):
					for size in range (5,30,5):
						faces, image = self.findSensitiveObject(scaleFactor=(scale/10.0), minNeighbors=neighbor, flags=flag, minSize=(size, size+5))
						if expectedFaces < len(faces):
							continue
						for (x, y, w, h) in faces:
							for i in range(4):
								if x >= imageDict["abba"][i]["x1"] and (x+w) <= imageDict["abba"][i]["x2"] and y >= imageDict["abba"][i]["y1"] and (y+h) <= imageDict["abba"][i]["y2"]:
									print i
									print "%s %s %s %s" % (scale, neighbor, flag, size)
						#self.removeSensitiveObject(faces, image)

if __name__ == '__main__':
    test()
