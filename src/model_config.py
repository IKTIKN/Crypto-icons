import json
from constants import KEY_API, PATH_CONFIG_JSON, STRING_API_KEY_INPUT, STRING_CONFIG_SAVED
from service_file_handler import FileHandler


class Config:

    def __init__(self) -> None:
        self.api_key = None
        self.fh = FileHandler()
        self.set_api_key()

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    def to_dict(self) -> dict:
        config_dict = self.__dict__.copy()
        config_dict.popitem()
        return config_dict

    def set_api_key(self) -> str:
        config = self.fh.read_file(PATH_CONFIG_JSON)
        if not config or not config.get(KEY_API):
            config = self.save()
        self.api_key = config.get(KEY_API)
    
    def save(self) -> None:
        if not self.api_key:
            self.api_key = self.fh.get_input(STRING_API_KEY_INPUT)
        self.fh.write_file(PATH_CONFIG_JSON, self.to_json())
        print(STRING_CONFIG_SAVED.format(PATH_CONFIG_JSON))
        return self.to_dict()
