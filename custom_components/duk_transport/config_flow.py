"""Config flow for DUK Transport integration."""
import logging
import voluptuous as vol
from typing import Any, Dict, Optional

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema({
    vol.Required("stop_id"): cv.string,
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
            # Here you could validate the stop_id by calling the API
            # For now, we'll assume it's valid
            
            title = user_input.get("stop_name") or f"Zastávka {user_input['stop_id']}"
            
            return self.async_create_entry(
                title=title,
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )