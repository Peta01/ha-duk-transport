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
TRANSPORT_TYPE_TOURIST_TRAIN = "tourist_train"  # Turistické vlaky T1-T29
TRANSPORT_TYPE_SHIP = "ship"
TRANSPORT_TYPE_FUNICULAR = "funicular"  # Cable car / lanovka

# Transport emojis for UI display (with fallback support)
TRANSPORT_EMOJIS = {
    TRANSPORT_TYPE_BUS: "🚌",
    TRANSPORT_TYPE_TROLLEYBUS: "🚎", 
    TRANSPORT_TYPE_TRAM: "🚊",
    TRANSPORT_TYPE_TRAIN: "🚆",
    TRANSPORT_TYPE_TOURIST_TRAIN: "🚂",  # Parní lokomotiva pro turistické vlaky
    TRANSPORT_TYPE_SHIP: "⛴️",
    TRANSPORT_TYPE_FUNICULAR: "🚠"
}

# ASCII fallback symbols (for systems without emoji support)
TRANSPORT_SYMBOLS = {
    TRANSPORT_TYPE_BUS: "[BUS]",
    TRANSPORT_TYPE_TROLLEYBUS: "[TROL]", 
    TRANSPORT_TYPE_TRAM: "[TRAM]",
    TRANSPORT_TYPE_TRAIN: "[TRAIN]",
    TRANSPORT_TYPE_TOURIST_TRAIN: "[STEAM]",  # Steam train indicator
    TRANSPORT_TYPE_SHIP: "[SHIP]",
    TRANSPORT_TYPE_FUNICULAR: "[CABLE]"
}

# Unicode-safe short symbols (single char, widely supported)
TRANSPORT_CHARS = {
    TRANSPORT_TYPE_BUS: "B",
    TRANSPORT_TYPE_TROLLEYBUS: "T", 
    TRANSPORT_TYPE_TRAM: "M",  # Metro/tram
    TRANSPORT_TYPE_TRAIN: "R",  # Rail
    TRANSPORT_TYPE_TOURIST_TRAIN: "S",  # Steam
    TRANSPORT_TYPE_SHIP: "F",  # Ferry
    TRANSPORT_TYPE_FUNICULAR: "C"  # Cable
}

# Material Design Icons for Home Assistant
TRANSPORT_ICONS = {
    TRANSPORT_TYPE_BUS: "mdi:bus",
    TRANSPORT_TYPE_TROLLEYBUS: "mdi:bus-electric", 
    TRANSPORT_TYPE_TRAM: "mdi:tram",
    TRANSPORT_TYPE_TRAIN: "mdi:train",
    TRANSPORT_TYPE_TOURIST_TRAIN: "mdi:steam",  # Parní lokomotiva pro turistické vlaky
    TRANSPORT_TYPE_SHIP: "mdi:ferry",
    TRANSPORT_TYPE_FUNICULAR: "mdi:gondola"
}

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
ATTR_VEHICLE_EMOJI = "vehicle_emoji"
ATTR_VEHICLE_SYMBOL = "vehicle_symbol"
ATTR_VEHICLE_CHAR = "vehicle_char"
ATTR_VEHICLE_ICON = "vehicle_icon"
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
        "lines": ["70", "71", "72", "73", "76", "79", "80", "81", "83", "84", "85", "87", "88", "89", "43", "46"],  # Denní + noční linky
        "type": TRANSPORT_TYPE_TROLLEYBUS
    },
    # Chomutov - trolejbusy (DPCHJ) - podle visit.chomutov.cz
    "chomutov_trolleybus": {
        "carrier": "DPCHJ",
        "lines": ["340", "341", "350", "351", "352", "353"],  # Trolejbusové linky 340-359
        "type": TRANSPORT_TYPE_TROLLEYBUS
    },

}