"""Sensor platform for DUK Transport integration."""
import logging
from datetime import timedelta
from typing import Any, Dict, List, Optional

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

from .api import DUKTransportAPI
from .const import (
    DOMAIN,
    ATTR_STOP_ID,
    ATTR_STOP_NAME,
    ATTR_LINE,
    ATTR_DESTINATION,
    ATTR_DEPARTURE_TIME,
    ATTR_DELAY,
    ATTR_PLATFORM,
    ATTR_VEHICLE_TYPE,
    DEFAULT_UPDATE_INTERVAL,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up DUK Transport sensor based on a config entry."""
    session = async_get_clientsession(hass)
    api = DUKTransportAPI(session)
    
    stop_id = config_entry.data["stop_id"]
    stop_name = config_entry.data.get("stop_name", f"Zastávka {stop_id}")
    update_interval = config_entry.data.get("update_interval", DEFAULT_UPDATE_INTERVAL)
    max_departures = config_entry.data.get("max_departures", 10)

    coordinator = DUKTransportCoordinator(
        hass, api, stop_id, update_interval, max_departures
    )

    await coordinator.async_config_entry_first_refresh()

    async_add_entities([
        DUKTransportSensor(coordinator, config_entry, stop_name)
    ])

class DUKTransportCoordinator(DataUpdateCoordinator):
    """Class to manage fetching DUK Transport data."""

    def __init__(
        self,
        hass: HomeAssistant,
        api: DUKTransportAPI,
        stop_id: str,
        update_interval: int,
        max_departures: int,
    ) -> None:
        """Initialize."""
        self.api = api
        self.stop_id = stop_id
        self.max_departures = max_departures

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=update_interval),
        )

    async def _async_update_data(self) -> List[Dict[str, Any]]:
        """Fetch data from API endpoint."""
        try:
            return await self.api.get_departures(self.stop_id, self.max_departures)
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

class DUKTransportSensor(CoordinatorEntity, SensorEntity):
    """DUK Transport sensor."""

    def __init__(
        self,
        coordinator: DUKTransportCoordinator,
        config_entry: ConfigEntry,
        stop_name: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._attr_name = f"DUK Transport {stop_name}"
        self._attr_unique_id = f"duk_transport_{config_entry.data['stop_id']}"
        self._stop_id = config_entry.data["stop_id"]
        self._stop_name = stop_name

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        if not self.coordinator.data:
            return "Žádné odjezdy"
        
        next_departure = self.coordinator.data[0] if self.coordinator.data else None
        if next_departure:
            line = next_departure.get('line', 'N/A')
            destination = next_departure.get('destination', 'Neznámý cíl')
            departure_time = next_departure.get('departure_time', 'N/A')
            delay = next_departure.get('delay', 0)
            
            # Format state with delay information
            if delay > 0:
                return f"Linka {line} → {destination} ({departure_time}, +{delay} min)"
            else:
                return f"Linka {line} → {destination} ({departure_time})"
        
        return "Žádné odjezdy"

    @property
    def extra_state_attributes(self) -> Dict[str, Any]:
        """Return the state attributes."""
        if not self.coordinator.data:
            return {
                ATTR_STOP_ID: self._stop_id,
                ATTR_STOP_NAME: self._stop_name,
                "departures": [],
                "count": 0,
            }

        departures = []
        for departure in self.coordinator.data:
            departures.append({
                ATTR_LINE: departure.get("line"),
                ATTR_DESTINATION: departure.get("destination"),
                ATTR_DEPARTURE_TIME: departure.get("departure_time"),
                "scheduled_time": departure.get("scheduled_time"),
                ATTR_DELAY: departure.get("delay", 0),
                "delay_string": departure.get("delay_string", "0:00:00"),
                ATTR_PLATFORM: departure.get("platform", ""),
                ATTR_VEHICLE_TYPE: departure.get("vehicle_type", "bus"),
                "carrier": departure.get("carrier", "Unknown"),
            })

        return {
            ATTR_STOP_ID: self._stop_id,
            ATTR_STOP_NAME: self._stop_name,
            "departures": departures,
            "count": len(departures),
            "next_departure": departures[0] if departures else None,
        }

    @property
    def icon(self) -> str:
        """Return the icon of the sensor."""
        return "mdi:bus-clock"

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self.coordinator.last_update_success