import uuid
from pathlib import Path

import toml

from .basic_path_core import BasicPathCore
from .basic_path_manager import PathManager
from .basic_path_utils import *

__all__ = ['register_path', 'resolve_path', 'user_home', 'app_home', 'create_tmp_folder']

__PATH_MANAGER = PathManager()
__CORE = BasicPathCore(str(uuid.uuid4()))


def app_home():
    return __CORE.app_home


def user_home():
    return __CORE.user_home


def register_path(key: str, path: Path) -> None:
    __PATH_MANAGER.register_path(key, path)


def resolve_path(key: str) -> None:
    return __PATH_MANAGER.resolve_path(key)


def init_from_poetry_toml(toml_file):
    toml_file_path = Path(toml_file)
    if not toml_file_path.exists():
        raise FileNotFoundError(f"{toml_file_path} doesn't exists")

    data = toml.load(toml_file)
    if data == {}:
        raise ValueError(f"{toml_file_path} is empty")

    global __CORE
    __CORE = BasicPathCore(data['tool']['poetry']['name'])


def create_tmp_folder() -> Path:
    return basic_path_utils.create_tmp_folder()
