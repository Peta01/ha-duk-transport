"""Constants for the DUK Transport integration."""

DOMAIN = "duk_transport"
API_BASE_URL = "https://tabule.portabo.cz/api/v1-tabule"

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