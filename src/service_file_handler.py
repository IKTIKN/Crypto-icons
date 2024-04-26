import json
import os
import shutil
from constants import (
    DIR_ICONS_ID,
    DIR_ICONS_NAME,
    DIR_ICONS_SYMBOL,
    DIR_OUTPUT
)


class FileHandler:

    def __init__(self) -> None:
        self.output_dirs = []

    def _create_dir(self, path) -> None:
        if not os.path.isdir(path):
            os.makedirs(path) 

    def _delete_dir(self, path) -> None:
        if os.path.isdir(path):
            shutil.rmtree(path)

    def _file_exists(self, path) -> bool:
        return os.path.isfile(path)
    
    def _read(self, path, read_mode):
        with open(path, read_mode) as r:
            content = r.read()
        r.close()
        return content
    
    def _write(self, path, data, write_mode):
        with open(path, write_mode) as w:
            w.write(data)
        w.close()

    def write_file(self, path, data, write_mode="w", overwrite=True, write_json=False) -> bool:
        if not overwrite and os.path.isfile(path):
            return False
        if write_json:
            data = json.dumps(data, indent=4)
        self._write(path, data, write_mode)
        return True

    def read_file(self, path, read_mode="r", read_json=True) -> dict | None:
        try:
            file_content = self._read(path, read_mode)
            if read_json:
                file_content = json.loads(file_content)
                if isinstance(file_content, str):
                    return None
            return file_content
        except (FileNotFoundError, ValueError, TypeError) as e:
            return None

    def set_output_dirs(self) -> None:
        self._delete_dir(DIR_OUTPUT)
        for dir in [DIR_ICONS_ID, DIR_ICONS_SYMBOL, DIR_ICONS_NAME]:
            self._create_dir(dir)

    def get_input(self, text, default_value="") -> str:
        user_input = ""
        while not user_input:
            raw_input = input(text)
            if not raw_input and default_value:
                user_input = default_value
            else:
                user_input = raw_input
        return user_input

    def sanitize(self, filename: str) -> str:
        return filename.strip().replace("/", "-")
