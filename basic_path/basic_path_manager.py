from pathlib import Path

__all__ = ['PathManager']


class PathManager:

    def __init__(self):
        self.__paths = dict()

    def register_path(self, key: str, path: Path):
        self.__paths[key] = path

    def resolve_path(self, key):
        if key not in self.__paths.keys():
            raise KeyError(f"{key} path hasn't be registered in PathManager")

        return self.__paths[key]
