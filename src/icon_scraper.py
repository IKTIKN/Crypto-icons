import datetime
import time
from constants import (
    EXCEPTION_CMC_MAP,
    EXCEPTION_DEFAULT,
    HEADER_BITCOIN,
    PATH_ICON_MAP_JSON,
    STRING_EXIT,
    STRING_NO_ICON,
    STRING_PERCENT,
    STRING_PROGRESS,
    STRING_SCRAPE_TITLE,
    STRING_SCRAPER_STATS,
    STRING_SKIPPED_ICONS
)
from model_config import Config
from model_icon import Icon
from service_file_handler import FileHandler
from service_http import HttpService


class IconScraper:

    def __init__(self) -> None:
        self.fh = FileHandler()
        self.http = HttpService(Config().api_key)
        self.icon_map = []
        self.cmc_id_map = self.http.get_cmc_id_map()
        self.no_icon_messages = []
        self.start_time = None

    def print_stats(self) -> None:
            runtime_seconds = time.time() - self.start_time
            runtime_string = datetime.timedelta(seconds=runtime_seconds)
            icons_per_second = len(self.icon_map) / runtime_seconds
            print(STRING_SCRAPER_STATS.format(len(self.icon_map), icons_per_second, runtime_string))
            if self.no_icon_messages:
                percent = STRING_PERCENT.format((len(self.no_icon_messages) / len(self.cmc_id_map)) * 100)
                print(STRING_SKIPPED_ICONS.format(len(self.no_icon_messages), percent))
                for message in self.no_icon_messages:
                    print(message)

    def print_progress(self, icon: Icon) -> None:
        percent = STRING_PERCENT.format((len(self.icon_map) / len(self.cmc_id_map)) * 100)
        print(STRING_PROGRESS.format(percent, icon.id, icon.symbol, icon.name))

    def scrape_icons(self) -> None:
        if self.cmc_id_map:
            try:
                print(STRING_SCRAPE_TITLE)
                self.fh.set_output_dirs()
                self.start_time = time.time()
                for map in self.cmc_id_map:
                    icon_bytes_response = self.http.download_icon(map.id)
                    if icon_bytes_response:
                        icon = map.to_icon(icon_bytes_response)
                        self.icon_map.append(icon.to_icon_map())
                        self.print_progress(icon)
                        icon.save()
                    else:
                        no_icon_message = STRING_NO_ICON.format(map.name, map.symbol, self.http.format_icon_url(map.id))
                        self.no_icon_messages.append(no_icon_message.strip())
            except KeyboardInterrupt:
                pass
            self.fh.write_file(PATH_ICON_MAP_JSON, self.icon_map, write_json=True)
            self.print_stats()
        else:
            raise Exception(EXCEPTION_CMC_MAP)


if __name__ == "__main__":
    print(HEADER_BITCOIN)
    try: 
        scraper = IconScraper()
        scraper.scrape_icons()
    except KeyboardInterrupt:
        print(STRING_EXIT)
    except Exception as e:
        print(EXCEPTION_DEFAULT.format(e))
