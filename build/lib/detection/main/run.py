from typing import Any

from detection.common.base import T_FILE
from detection.common.providers import OnlyJpgFilesProvider
from detection.detect.faces import DetectFaces


class Runner:

    def run(self) -> Any:
        pass


class MainRunner(Runner):

    def __init__(self, dir_in: T_FILE):
        self.__dir_in = dir_in

    def run(self):
        for file_path in OnlyJpgFilesProvider(path_in=self.__dir_in).get():
            detect_image = DetectFaces().detect_faces(file_path)
        return detect_image
