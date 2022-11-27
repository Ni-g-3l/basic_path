import uuid
from pathlib import Path


__all__ = ['create_tmp_folder']


def create_tmp_folder():
    tmp_folder_path = Path('/tmp') / str(uuid.uuid4())
    if not tmp_folder_path.exists():
        tmp_folder_path.mkdir()
        return tmp_folder_path
    else:
        return create_tmp_folder()
