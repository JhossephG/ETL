from typing import Dict
import requests

class HttpRequester:

    def __init__(self) -> None:
        self.__url= 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    def request_from_page(self) -> Dict[int, str]:
        try:
            response = requests.get(self.__url, timeout=10)  # Adding a timeout of 10 seconds
            return {
                "status_code": response.status_code,
                "html": response.text
            }
        except requests.Timeout:
            return {
                "status_code": "Timeout",
                "html": ""
            }
        except requests.RequestException as e:
            return {
                "status_code": "Error",
                "html": str(e)
            }
        