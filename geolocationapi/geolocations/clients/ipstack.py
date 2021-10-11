from typing import Literal, Optional, TypedDict, cast

import requests


class IPStackLookup(TypedDict):
    ip: str
    type: Literal["ipv4", "ipv6"]
    continent_code: Optional[str]
    continent_name: Optional[str]
    country_code: Optional[str]
    country_name: Optional[str]
    region_code: Optional[str]
    region_name: Optional[str]
    city: Optional[str]
    zip: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]


class IPStackException(Exception):
    def __init__(self, error: dict):
        self.error = error

        super().__init__(error['info'])


class IPStack:
    API_ENDPOINT = 'http://api.ipstack.com/'

    def __init__(self, access_key: str):
        self.s = requests.Session()
        self.s.params = {'access_key': access_key}

    def lookup(self, lookup: str) -> IPStackLookup:
        response = self.s.get(f'{self.API_ENDPOINT}{lookup}', params={'fields': 'main'})
        response.raise_for_status()
        json_response: dict = response.json()
        success = json_response.get('success', True)
        if not success:
            raise IPStackException(json_response['error'])
        return cast(IPStackLookup, json_response)
