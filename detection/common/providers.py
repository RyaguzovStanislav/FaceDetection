import os
from pathlib import Path
from typing import List, Iterable, Optional

from detection.common.base import Suppler, T_FILE


class FileContentProvider(Suppler):

    def get(self) -> str:
        pass


class OnlyFilesProvider(Suppler):

    def __init__(self, path_in: T_FILE, extentions: Optional[List[str]] = None):
        self.__path_in = path_in
        self.__extentions = extentions or []

    def get(self) -> Iterable[T_FILE]:
        for address, dirs, files in os.walk(self.__path_in):
            for file_name in files:
                if self.__extentions is None or Path(file_name).suffix.lower() in self.__extentions:
                    yield Path(address, file_name).resolve()


class OnlyJpgFilesProvider(OnlyFilesProvider):

    def __init__(self, path_in: T_FILE):
        super().__init__(path_in=path_in, extentions=[".jpg"])
