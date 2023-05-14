import os

import cv2

from detection.main.run import MainRunner

if __name__ == '__main__':
    dir_in = "./in"

    detect_image = MainRunner(dir_in=dir_in).run()
    path = 'C:/Users/Stas/Desktop/django project/FaceDetection/detection/demo/out'
    detect_image_path = os.path.join(path, 'detect_img.jpg')
    cv2.imwrite(detect_image_path, cv2.cvtColor(detect_image, cv2.COLOR_RGB2BGR))
    print(detect_image)
