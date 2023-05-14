from pathlib import Path
from typing import Union, Any

T_FILE = Union[str, Path]


class Suppler:

    def get(self) -> Any:
        pass
