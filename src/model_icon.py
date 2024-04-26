import json
from constants import DIR_ICONS_ID, DIR_ICONS_NAME, DIR_ICONS_SYMBOL, PATH_ICON_PNG
from service_file_handler import FileHandler


class Icon():

    def __init__(self, id, name, symbol, png_bytes=b'') -> None:
        self.fh = FileHandler()
        self.id = str(id)
        self.name = self.fh.sanitize(name)
        self.symbol = self.fh.sanitize(symbol)
        self.id_png_path = PATH_ICON_PNG.format(DIR_ICONS_ID, self.id)
        self.name_png_path = PATH_ICON_PNG.format(DIR_ICONS_NAME, self.name)
        self.symbol_png_path = PATH_ICON_PNG.format(DIR_ICONS_SYMBOL, self.symbol)
        self.hex_bytes = png_bytes.hex()

    def __str__(self) -> str:
        slice_dict = self._slice_dict(1, 6)
        return self._format_dict(slice_dict, True)

    def _slice_dict(self, start_index, end_index) -> dict:
        slice_dict = self.__dict__.copy()
        for index, key in enumerate(list(slice_dict)):
            if not start_index <= index <= end_index:
                slice_dict.pop(key)
        return slice_dict

    def _format_dict(self, icon_dict, json_format) -> dict:
        if json_format:
            icon_dict = json.dumps(icon_dict, indent=4)
        return icon_dict

    def to_json(self) -> dict:
        return self._format_dict(self._slice_dict(1, 7), True)

    def to_icon_map(self, json_format=False) -> dict:
        return self._format_dict(self._slice_dict(1, 3), json_format)

    def to_bytes(self) -> bytes:
        return bytes.fromhex(self.hex_bytes)

    def get_output_paths(self) -> list[str]:
        return [self.id_png_path, self.name_png_path, self.symbol_png_path]

    def save(self, path=None) -> None:
        if path:
            output_paths = [path]
        else: 
            output_paths = self.get_output_paths()
        for path in output_paths:
            self.fh.write_file(path, self.to_bytes(), "wb", False)
