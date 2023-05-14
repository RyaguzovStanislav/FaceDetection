import cv2
from PIL import Image as PImage
from mtcnn.mtcnn import MTCNN
from numpy import asarray


class DetectFaces:

    def detect_faces(self, file_path):
        image = PImage.open(file_path)
        pixels = asarray(image)
        detector = MTCNN()
        results = detector.detect_faces(pixels)
        for counter in range(len(results)):
            bounding_box = results[counter]['box']
            cv2.rectangle(pixels,
                          (bounding_box[0], bounding_box[1]),
                          (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                          (0, 155, 255), 2)
        return pixels
