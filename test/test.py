import os
import sys
from pprint import pprint
sys.path.append("C:\\Users\\Nocturne\\Desktop\\magister")
from imageDict import imageDict
from sensitiveObject.faceDetection import faceDetection

class test(faceDetection):
	def __init__(self):
		resultDict = self.testAbba()
		pprint(resultDict)

	def testAbba(self):
		filelist = self.listdir_fullpath("C:\Users\Nocturne\Desktop\magister\sensitiveObject\utils\images")

		resultDict = {}
		for scale in range(11, 14, 1):
			for neighbor in range(1,5):
				for flag in range (10, 30, 5):
					for size in range (0,30,5):
						for rotate in range(-30, 30, 10):
							faces, image = self.findSensitiveObject(imageUrl=None, scaleFactor=(scale/10.0), minNeighbors=neighbor, 
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

		return resultDict

	def listdir_fullpath(self, d):
		return [os.path.join(d, f) for f in os.listdir(d)]

if __name__ == '__main__':
    test()
