import cv2
import sys
import math
from pprint import pprint
from generic.templates.basicDetection import basicDetection

class faceDetection(basicDetection):
	cascade = "utils\haarcascade_frontalface_default.xml"

	def __init__(self):
		resultDict, numberOfFaces = self.getCorrectParameters(sys.argv[1])
		pprint(resultDict)
		print numberOfFaces
		for x in numberOfFaces:
			print resultDict[x]["total"]
		scale = self.getAvgNumber(resultDict[4]["scale"] / resultDict[4]["total"])
		neighbor = int(self.getAvgNumber(resultDict[4]["neighbor"] / resultDict[4]["total"]))
		flag = int(self.getAvgNumber(resultDict[4]["flag"] / resultDict[4]["total"]))
		size = int(self.getAvgNumber(resultDict[4]["size"] / resultDict[4]["total"]))
		rotate = int(self.getAvgNumber(resultDict[4]["rotate"] / resultDict[4]["total"]))
		print "scale=%s\nneighbor=%s\nflag=%s\nsize=%s\nrotate=%s\n" % (scale, neighbor, flag, size, rotate)
		faces, image = self.findSensitiveObject(imageUrl=sys.argv[1], scaleFactor=scale, minNeighbors=neighbor, flags=flag, minSize=(size, size + 5), rotate=rotate)
		self.removeSensitiveObject(faces, image, rotate)

	def getAvgNumber(self, number):
		return round(number * 100, -1) / 100

	def loadImage(self, picture):
		return cv2.imread(picture)

	def getGrayColor(self, image):
		return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	def findSensitiveObject(self, imageUrl=None, scaleFactor=1.2, minNeighbors=3, flags=17, minSize=(13, 18), rotate=0):
		faceCascade = self._getCascade(self.cascade)
		if imageUrl is not None:
			url = imageUrl
		else:
			url = sys.argv[1]
		image = self.loadImage(url)
		imageTemp = image
		image = self.rotateImage(image, rotate)
		faces = faceCascade.detectMultiScale(
			self.getGrayColor(image),
			scaleFactor=scaleFactor,
			minNeighbors=minNeighbors,
			flags = flags,
			minSize=minSize
		)
		print "Found {0} faces!".format(len(faces))
		return faces, imageTemp

	def removeSensitiveObject(self, faces, image, rotate):
		result_image = image.copy()
		rows, cols, _ = image.shape
		for f in faces:
			x1, y1, w, h = [ v for v in f ]
			x2, y2 = x1 + w, y1 + h
			x1r, y1r = self.rotateCoords(x1, y1, cols/2, rows/2, rotate)
			x2r, y2r = self.rotateCoords(x2, y2, cols/2, rows/2, rotate)
			cv2.rectangle(result_image, (x1r, y1r), (x2r, y2r), (0, 255, 0), 2)
			#xr = xr - w
			#yr = yr - h
			#sub_face = image[y1r:y2r, x2r:x1r]
			#sub_face = cv2.GaussianBlur(sub_face,(23, 23), 30)
			#print sub_face
			#result_image[y1r:y2r, x1r:x2r] = sub_face

		cv2.imshow("Faces found" ,result_image)
		cv2.waitKey(0)

	def sendImage(self):
		pass

	def _getCascade(self, cascade):
		return cv2.CascadeClassifier(cascade)

	def rotateCoords(self, x, y, xm, ym, a):
		a = a * math.pi /180
		xr = (x - xm) * math.cos(a) - (y - ym) * math.sin(a) + xm
		yr = (x - xm) * math.sin(a) + (y - ym) * math.cos(a) + ym

		return [int(xr), int(yr)]

	def getCorrectParameters(self, url):
		resultDict = {}
		numberOfFaces = []
		for scale in range(11, 13, 1):
			for neighbor in range(1,3):
				for flag in range (10, 30, 10):
					for size in range (5,30,5):
						for rotate in range(-90, 90, 90):
							faces, image = self.findSensitiveObject(imageUrl=url, scaleFactor=(scale/10.0), minNeighbors=neighbor, 
																	flags=flag, minSize=(size, size+5), rotate=rotate)

							try:
								resultDict[len(faces)]["total"] = resultDict[len(faces)]["total"] + 1
								resultDict[len(faces)]["scale"] = resultDict[len(faces)]["scale"] + (scale / 10.0)
								resultDict[len(faces)]["neighbor"] = resultDict[len(faces)]["neighbor"] + neighbor
								resultDict[len(faces)]["flag"] = resultDict[len(faces)]["flag"] + flag
								resultDict[len(faces)]["size"] = resultDict[len(faces)]["size"] + size
								resultDict[len(faces)]["rotate"] = resultDict[len(faces)]["rotate"] + rotate
							except KeyError:
								resultDict.update({
									len(faces): {
										"total": 1,
										"scale": (scale / 10.0),
										"neighbor": neighbor,
										"flag": flag,
										"size": size,
										"rotate": rotate
									}
								})
								numberOfFaces.append(len(faces))

		return resultDict, numberOfFaces

if __name__ == "__main__":
	faceDetection()