from pathlib import Path


class BasicPathCore:

    def __init__(self, namespace: str):
        self.__user_home = Path.home()
        self.__app_home = self.__user_home / f".{namespace}"

    @property
    def user_home(self):
        return self.__user_home

    @property
    def app_home(self):
        return self.__app_home



