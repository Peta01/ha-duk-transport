"""Config flow for DUK Transport integration."""
import logging
import voluptuous as vol
from typing import Any, Dict, Optional

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, EXAMPLE_STATIONS

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema({
    vol.Required("stop_id", description={"suggested_value": "2950"}): cv.string,
    vol.Optional("stop_name", default=""): cv.string,
    vol.Optional("update_interval", default=60): cv.positive_int,
    vol.Optional("max_departures", default=10): cv.positive_int,
})

class DUKTransportConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for DUK Transport."""

    VERSION = 1

    async def async_step_user(
        self, user_input: Optional[Dict[str, Any]] = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            stop_id = user_input["stop_id"]
            
            # Validate stop_id format (should be numeric)
            if not stop_id.isdigit():
                errors["stop_id"] = "invalid_stop_id"
            else:
                # Use predefined station name if available, otherwise use user input or default
                if stop_id in EXAMPLE_STATIONS:
                    station_name = EXAMPLE_STATIONS[stop_id]
                    if not user_input.get("stop_name"):
                        user_input["stop_name"] = station_name
                
                title = user_input.get("stop_name") or f"Zastávka {stop_id}"
                
                return self.async_create_entry(
                    title=title,
                    data=user_input,
                )

        # Add description with examples
        description_placeholders = {
            "examples": "Příklady: 2950 (Krupka,ke Kateřině), 2957 (Krupka,Bohosudov,Lindnerova)"
        }

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
            description_placeholders=description_placeholders,
        )