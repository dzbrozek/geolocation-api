from geolocations.clients.ipstack import IPStack, IPStackLookup


class IPStackMock(IPStack):
    def __init__(self, access_key: str):
        pass

    def lookup(self, lookup: str) -> IPStackLookup:
        return {
            "ip": "185.157.15.59",
            "type": "ipv4",
            "continent_code": "EU",
            "continent_name": "Europe",
            "country_code": "PL",
            "country_name": "Poland",
            "region_code": "MA",
            "region_name": "MA",
            "city": "Wieliczka",
            "zip": "32-005",
            "latitude": 49.96186828613281,
            "longitude": 20.173749923706055,
        }
