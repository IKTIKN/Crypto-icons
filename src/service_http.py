import json
from constants import (
    CMC_BASE_URL,
    CMC_ICON_URL,
    CMC_MAP_ENDPOINT,
    CMC_PRO_API_KEY,
    EXCEPTION_HTTP,
    EXCEPTION_HTTP_401,
    EXCEPTION_NETWORK,
    HTTP_SESSION_HEADER,
    KEY_DATA,
    STRING_DOWNLOAD_MAP
)
from enum_icon_size import IconSize
from http import HTTPStatus
from model_cmc_id_map import CmcIdMap
from requests import Response, Session, Timeout, TooManyRedirects


class HttpService:

    def __init__(self, api_key) -> None:
        HTTP_SESSION_HEADER.update({CMC_PRO_API_KEY: api_key})
        self.session = Session()
        self.session.headers.update(HTTP_SESSION_HEADER)
    
    def _http_get(self, url) -> Response | None:
        try:
            response = self.session.get(url)
            if not response.ok:
                if response.status_code == HTTPStatus.UNAUTHORIZED:
                    error_message = EXCEPTION_HTTP_401.format(self.session.headers.get(CMC_PRO_API_KEY))
                else:
                    error_message = EXCEPTION_HTTP.format(response.status_code, url)
                response = None
                print(error_message)
            return response
        except (ConnectionError, Timeout, TooManyRedirects) as error:
            raise Exception(EXCEPTION_NETWORK.format(error))

    def format_icon_url(self, icon_id, icon_size=IconSize.HUGE) -> str:
        return CMC_ICON_URL.format(size=icon_size.value, id=icon_id)
    
    def download_icon(self, icon_id) -> bytes | None:
        for size in IconSize:
            request_url = self.format_icon_url(icon_id, size)
            icon_response = self._http_get(request_url)
            if icon_response and icon_response.content:
                return icon_response.content
        return None

    def get_cmc_id_map(self) -> list[CmcIdMap]:
        print(STRING_DOWNLOAD_MAP)
        request_url = CMC_BASE_URL.format(CMC_MAP_ENDPOINT)
        response = self._http_get(request_url)
        cmc_id_map_list = []
        if response:
            response_json: dict = json.loads(response.text)
            response_data = response_json.get(KEY_DATA)
            for data in response_data:
                cmc_id_map_list.append(CmcIdMap(data))
        return cmc_id_map_list
