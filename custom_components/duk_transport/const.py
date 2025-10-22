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
ATTR_DELAY = "delay"
ATTR_PLATFORM = "platform"
ATTR_VEHICLE_TYPE = "vehicle_type"