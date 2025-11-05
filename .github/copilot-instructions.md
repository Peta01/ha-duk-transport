# DUK Transport - AI Coding Guidelines

## Architecture Overview

This is a Home Assistant custom component for public transport departure boards in the Ústí nad Labem region (Czech Republic). The component integrates with two APIs:

- **DUK API**: Regional bus services (`/duk/GetStationDeparturesWCount/{node}/{post}/{count}/{line}`)
- **CIS API**: City transport + trains (`/cis/GetStationDeparturesWCount/{node}/{post}/{count}/{line}`)

### Core Components (`custom_components/duk_transport/`)

- **`__init__.py`**: Component entry point, forwards setup to sensor platform
- **`config_flow.py`**: UI configuration flow with validation
- **`sensor.py`**: Main sensor implementation using DataUpdateCoordinator pattern
- **`api.py`**: API client with vehicle type detection logic
- **`const.py`**: Constants, transport types, icon mappings, city configurations
- **`manifest.json`**: Component metadata and dependencies

### Data Flow

```
ConfigFlow → Coordinator → API Client → HTTP Request → Vehicle Detection → Sensor Entity → HA State
```

## Vehicle Type Detection Logic

Use the complex detection patterns in `api.py` and `const.py`. Key rules:

### Primary Detection (in order of precedence)

1. **Ships**: Station names containing 'přístaviště'/'přístav', or lines T90-T99
2. **Cable Cars**: Line 901 in Teplice, station names with 'lanovka'
3. **Trains**: Lines starting with R, EX, SC, IC, EC, RJ, EN, OS, SP, or T1-T29 (tourist)
4. **City-Specific**: Check `CITY_TRANSPORT_LINES` in `const.py` for carrier/line matches
5. **Trolleybuses**: MD Teplice carrier with specific line ranges
6. **Replacement Buses**: Lines starting with 'X'

### Icon Mapping Priority

Always provide all icon variants from `const.py`:
```python
# Example for a detected bus
{
    ATTR_VEHICLE_TYPE: TRANSPORT_TYPE_BUS,
    ATTR_VEHICLE_EMOJI: "🚌",
    ATTR_VEHICLE_SYMBOL: "[BUS]",
    ATTR_VEHICLE_CHAR: "B", 
    ATTR_VEHICLE_ICON: "mdi:bus"
}
```

## Testing & Development

### Mock Data Testing

Use stop_id `12345` for mock data testing - returns realistic sample departures without API calls.

### API Testing Commands

```bash
# Test DUK endpoint (regional buses)
curl "https://tabule.portabo.cz/api/v1-tabule/duk/GetStationDeparturesWCount/2950/0/10/0"

# Test CIS endpoint (city transport)  
curl "https://tabule.portabo.cz/api/v1-tabule/cis/GetStationDeparturesWCount/1578/1/10/0"
```

### Validation Workflows

- **hassfest**: Validates Home Assistant component structure
- **HACS**: Validates for HACS store compatibility
- Both run on push/PR and daily schedule

## Configuration Examples

### Well-Known Stations

- **2950**: Krupka, ke Kateřině (DUK buses)
- **1578**: Teplice trolleybuses (CIS)
- **1967**: Most-Litvínov trams (CIS)
- **12140**: Ústí n.L. cable car (CIS)

### City Transport Lines

Reference `CITY_TRANSPORT_LINES` in `const.py` for accurate line classifications per city.

## Code Patterns

### Error Handling

Always fallback to mock data on API failures:
```python
try:
    # API call
    return parsed_data
except Exception as e:
    _LOGGER.error(f"API error: {e}")
    return self._get_mock_departures(stop_id, max_departures)
```

### Logging

Use appropriate log levels:
- `debug`: API request URLs and parameters
- `info`: Successful data fetches with counts
- `warning`: API status errors, fallback to mock
- `error`: Exceptions and parsing failures

### Async Patterns

Follow Home Assistant async patterns:
- Use `async_get_clientsession(hass)` for HTTP clients
- Implement proper timeouts (`ClientTimeout(total=10)`)
- Use `DataUpdateCoordinator` for polling sensors

## File Structure Conventions

- Keep transport type constants in `const.py`
- API logic in `api.py`, sensor logic in `sensor.py`
- Test scripts in root directory as `test_*.py`
- Documentation in `docs/`, examples in `examples/`
- Dashboard configs in `dashboards/`</content>
<parameter name="filePath">c:\Users\admin\Documents\HomeAssistant\DUK\.github\copilot-instructions.md