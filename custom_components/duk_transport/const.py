"""Constants for the DUK Transport integration."""

DOMAIN = "duk_transport"
API_BASE_URL = "https://tabule.portabo.cz/api/v1-tabule"

# API endpoints
DUK_ENDPOINT = "duk"  # Buses
CIS_ENDPOINT = "cis"  # Trains and ships

# Transport types
TRANSPORT_TYPE_BUS = "bus"
TRANSPORT_TYPE_TROLLEYBUS = "trolleybus"
TRANSPORT_TYPE_TRAM = "tram"
TRANSPORT_TYPE_TRAIN = "train"
TRANSPORT_TYPE_SHIP = "ship"
TRANSPORT_TYPE_FUNICULAR = "funicular"  # Cable car / lanovka

# Default values
DEFAULT_UPDATE_INTERVAL = 60  # seconds
DEFAULT_MAX_DEPARTURES = 10

# Attributes
ATTR_STOP_ID = "stop_id"
ATTR_STOP_NAME = "stop_name"
ATTR_LINE = "line"
ATTR_DESTINATION = "destination"
ATTR_DEPARTURE_TIME = "departure_time"
ATTR_SCHEDULED_TIME = "scheduled_time"
ATTR_DELAY = "delay"
ATTR_DELAY_STRING = "delay_string"
ATTR_PLATFORM = "platform"
ATTR_VEHICLE_TYPE = "vehicle_type"
ATTR_CARRIER = "carrier"

# Well-known DUK station IDs for examples
EXAMPLE_STATIONS = {
    "2950": "Krupka,ke Kateřině",
    "2957": "Krupka,Bohosudov,Lindnerova",
    "12345": "Test Station (Mock Data)"
}

# City-specific transport line definitions
# To be updated with real line numbers from each city
CITY_TRANSPORT_LINES = {
    # Teplice - trolejbusy (MD Teplice) - podle oficiálního schéma 2025
    "teplice_trolleybus": {
        "carrier": "MD Teplice",
        "lines": ["101", "102", "103", "104", "105", "106", "107", "108", "109"],  # Všechny parciální trolejbusy
        "type": TRANSPORT_TYPE_TROLLEYBUS
    },
    # Teplice - autobusy (MD Teplice)
    "teplice_bus": {
        "carrier": "MD Teplice",
        "lines": ["110", "119"],  # 110 běžná linka, 119 noční flamendr
        "type": TRANSPORT_TYPE_BUS
    },
    # Most-Litvínov - tramvaje (DPMML) - podle oficiálního schématu DPmML
    "most_tram": {
        "carrier": "DPMML", 
        "lines": ["1", "2", "3", "4", "40"],  # Denní linky 1-4, noční linka 40
        "type": TRANSPORT_TYPE_TRAM
    },
    # Ústí nad Labem - lanovka (DPMÚL)
    "usti_funicular": {
        "carrier": "DPMÚL",
        "lines": ["901"],  # Lanovka Větruše - OC Forum
        "type": TRANSPORT_TYPE_FUNICULAR
    },
    # Ústí nad Labem - trolejbusy (DPMÚL) - podle Wikipedie k 2.9.2024
    "usti_trolleybus": {
        "carrier": "DPMÚL",
        "lines": ["70", "71", "72", "73", "76", "80", "84", "87", "88", "43", "46"],  # Denní + noční linky
        "type": TRANSPORT_TYPE_TROLLEYBUS
    },
    # Chomutov - trolejbusy (DPCHJ) - podle visit.chomutov.cz
    "chomutov_trolleybus": {
        "carrier": "DPCHJ",
        "lines": ["340", "341", "350", "351", "352", "353"],  # Trolejbusové linky 340-359
        "type": TRANSPORT_TYPE_TROLLEYBUS
    },
    # Chomutov - autobusy (DPCHJ)
    "chomutov_bus": {
        "carrier": "DPCHJ", 
        "lines": ["302", "303", "304", "306", "307", "308", "309", "310", "312", "314", "316", "317"],  # Autobusové linky 300-319
        "type": TRANSPORT_TYPE_BUS
    }
}