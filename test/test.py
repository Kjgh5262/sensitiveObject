import os
import sys

sys.path.append("C:\\Users\\Nocturne\\Desktop\\magister")
from imageDict import imageDict
from sensitiveObject.faceDetection import faceDetection

class test(faceDetection):
	cascade = "C:\Users\Nocturne\Desktop\magister\sensitiveObject\utils\haarcascade_frontalface_default.xml"
	def __init__(self):
		self.testAbba()

	def testAbba(self):
		filelist = self.listdir_fullpath("C:\Users\Nocturne\Desktop\magister\sensitiveObject\utils\images")#os.listdir("C:\Users\Nocturne\Desktop\magister\sensitiveObject\utils\images")
		for url in filelist:
			basename = os.path.basename(url)
			print basename
			for scale in range(11, 14, 1):
				for neighbor in range(1,5):
					for flag in range (10, 30, 5):
						for size in range (5,30,5):
							counter = 0
							faces, image = self.findSensitiveObject(imageUrl=url, scaleFactor=(scale/10.0), minNeighbors=neighbor, flags=flag, minSize=(size, size+5), rotate=0)
							if imageDict[basename]["expFace"] < len(faces):
								print "%s != %s" % (imageDict[basename]["expFace"], len(faces))
								continue
							elif imageDict[basename]["expFace"] == len(faces):
								print "%s %s %s %s" % (scale/10.0, neighbor, flag, size)
								self.removeSensitiveObject(faces, image)
							for (x, y, w, h) in faces:
								for i in range(imageDict[basename]["expFace"]):
									if x >= imageDict[basename][i]["x1"] and (x+w) <= imageDict[basename][i]["x2"] and y >= imageDict[basename][i]["y1"] and (y+h) <= imageDict[basename][i]["y2"]:
										print i
										counter = counter + 1
							print (counter / len(faces)) * 100
							#	self.removeSensitiveObject(faces, image)

	def listdir_fullpath(self, d):
		return [os.path.join(d, f) for f in os.listdir(d)]

if __name__ == '__main__':
    test()
