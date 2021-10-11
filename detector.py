#!/bin/env python3
import cv2
from tensorflow.keras.models import load_model
from src.models.stream.stream import Stream

class detector(Stream) :

	def __init__ (self) :

		# load our serialized face detector model from disk
		self.prototxtPath = r"src\models\detector_models\deploy.prototxt"
		self.weightsPath  = r"src\models\detector_models\res10_300x300_ssd_iter_140000.caffemodel"
		self.faceNet      = cv2.dnn.readNet(self.prototxtPath, self.weightsPath)

		# load the face mask detector model from disk
		self.maskNet = load_model("mask_detector.model")

		super().__init__()

	def running(self) :

		self.video_stream(

			face_net = self.faceNet,

			mask_net = self.maskNet

		)

if __name__ == "__main__" :

	detector = detector()
	detector.running()












	