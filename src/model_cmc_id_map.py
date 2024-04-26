import json
from constants import (
    KEY_FIRST_HIST_DATA,
    KEY_ID,
    KEY_IS_ACTIVE,
    KEY_LAST_HIST_DATA,
    KEY_NAME,
    KEY_PLATFORM,
    KEY_RANK,
    KEY_SLUG,
    KEY_SYMBOL
)
from model_icon import Icon


class CmcIdMap:

    def __init__(self, cmc_id_map: dict) -> None:
        self.id = str(cmc_id_map.get(KEY_ID))
        self.rank = cmc_id_map.get(KEY_RANK)
        self.name = cmc_id_map.get(KEY_NAME)
        self.symbol = cmc_id_map.get(KEY_SYMBOL)
        self.slug = cmc_id_map.get(KEY_SLUG)
        self.is_active = cmc_id_map.get(KEY_IS_ACTIVE)
        self.first_historical_data = cmc_id_map.get(KEY_FIRST_HIST_DATA)
        self.last_historical_data = cmc_id_map.get(KEY_LAST_HIST_DATA)
        self.platform = cmc_id_map.get(KEY_PLATFORM)

    def to_json(self) -> str:
        return json.dumps(self.__dict__, indent=4)

    def to_icon(self, hex_bytes) -> Icon:
        return Icon(self.id, self.name, self.symbol, hex_bytes)
