import shutil
from os import mkdir
from pathlib import Path

class TempDir:
    def __init__(self, path):
        self._path = Path(path + r"/" + ".temp")
        mkdir(self._path)

    @property
    def path(self):
        return self._path

    def __del__(self):
        shutil.rmtree(self.path)