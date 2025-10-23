# 👨‍💻 Developer Documentation

## 🏗️ Architektura

```
custom_components/duk_transport/
├── __init__.py           # Component entry point
├── config_flow.py        # Configuration UI flow  
├── const.py             # Constants & city configs
├── api.py               # API client & vehicle detection
├── sensor.py            # HA sensor implementation
└── manifest.json        # Component metadata
```

## 🔌 API Endpoints

### DUK API (Regional buses)
```
GET https://tabule.portabo.cz/api/v1-tabule/duk/GetStationDeparturesWCount/{node}/{post}/{count}/{line}
```

### CIS API (City transport + trains)
```  
GET https://tabule.portabo.cz/api/v1-tabule/cis/GetStationDeparturesWCount/{node}/{post}/{count}/{line}
```

## 🚌 Vehicle Detection Logic

### 1. Harbor/Port Detection (Ships)
```python
if any(word in station_name for word in ['přístaviště', 'přístav']):
    return 'ship'
```

### 2. Train Line Prefixes
```python
train_prefixes = ['R', 'EX', 'SC', 'IC', 'EC', 'RJ', 'EN', 'OS', 'SP']
```

### 3. City-Specific Configuration
```python
CITY_TRANSPORT_LINES = {
    "teplice_trolleybus": {
        "carrier": "MD Teplice",
        "lines": ["101", "102", "103", "104", "105", "106", "107", "108", "109"],
        "type": TRANSPORT_TYPE_TROLLEYBUS
    },
    # ... more cities
}
```

### 4. Carrier-Based Fallback
```python
if 'md teplice' in carrier_lower:
    if line_name == '901': return 'funicular'
    return 'trolleybus'
```

## 🎨 Icon Mapping

```python  
icon_mapping = {
    'bus': 'mdi:bus-clock' | 'mdi:bus-alert',
    'trolleybus': 'mdi:bus-electric' | 'mdi:bus-electric-alert',
    'tram': 'mdi:tram' | 'mdi:tram-alert', 
    'train': 'mdi:train' | 'mdi:train-alert',
    'ship': 'mdi:ferry' | 'mdi:ferry-alert',
    'funicular': 'mdi:gondola'  # No alert variant
}
```

## 🔄 Data Flow

```
1. ConfigFlow → User Input → Coordinator Setup
2. Coordinator → API Client → HTTP Request  
3. API Response → Vehicle Detection → Data Processing
4. Processed Data → Sensor Entity → HA State
5. HA State → Frontend → User Dashboard
```

## 🧪 Testing

### Mock Data (ID: 12345)
```python
def _get_mock_departures(self, stop_id: str, max_departures: int):
    lines = ['480', '484', '430', '485', '420', '440', '460']
    carriers = ['Doprava Teplice', 'ČSAD Ústí nad Labem', 'ARRIVA']
    # ... generates realistic mock data
```

### API Testing Commands
```bash
# Test DUK endpoint
curl "https://tabule.portabo.cz/api/v1-tabule/duk/GetStationDeparturesWCount/2950/1/10/0"

# Test CIS endpoint  
curl "https://tabule.portabo.cz/api/v1-tabule/cis/GetStationDeparturesWCount/1578/1/10/0"
```

## 🔧 Adding New Cities

### 1. Research Transport System
- Find official transport company website
- Identify line numbering system  
- Determine vehicle types per line

### 2. Update const.py
```python
CITY_TRANSPORT_LINES = {
    # Add new city configuration
    "new_city_trolleybus": {
        "carrier": "New City Transport Co",
        "lines": ["201", "202", "203"],
        "type": TRANSPORT_TYPE_TROLLEYBUS  
    }
}
```

### 3. Test & Validate
- Find working station IDs via API explorer
- Test vehicle detection accuracy
- Verify real-time data quality

### 4. Update Documentation
- Add examples to README.md
- Update configuration_examples.md
- Add troubleshooting notes if needed

## 🏷️ Version Management

### Semantic Versioning
- **MAJOR**: Breaking API changes
- **MINOR**: New features, new cities  
- **PATCH**: Bug fixes, small improvements

### Release Process
1. Update version in `manifest.json`
2. Update CHANGELOG.md
3. Create release notes
4. Test with hassfest & HACS validation
5. Tag release on GitHub

## 🔍 Debug Techniques

### Enable Debug Logging
```yaml
# configuration.yaml
logger:
  logs:
    custom_components.duk_transport: debug
```

### Key Debug Points
- API response structure
- Vehicle detection logic
- Encoding/parsing issues
- Coordinator update cycles

### Common Debug Patterns
```python
_LOGGER.debug(f"API Response: {response.json()}")
_LOGGER.debug(f"Detected vehicle type: {vehicle_type} for line {line_name}")  
_LOGGER.debug(f"Carrier: '{carrier}' → Vehicle: {detected_type}")
```

## 🚀 Performance Considerations

### API Rate Limiting
- Default intervals: 60-300s depending on transport type
- Batch processing when possible
- Graceful degradation on errors

### Memory Management  
- Limit max_departures to reasonable numbers
- Clean up old coordinator data
- Avoid memory leaks in long-running instances

### Error Handling
```python
try:
    # API call
except Exception as e:
    _LOGGER.error(f"API Error: {e}")
    return []  # Empty list, not crash
```

## 🤝 Contributing Guidelines

1. **Fork & Branch**: Create feature branch from master
2. **Code Style**: Follow Home Assistant coding standards
3. **Testing**: Test with real APIs + mock data
4. **Documentation**: Update relevant docs
5. **Pull Request**: Detailed description of changes

---

## 🤖 Development with AI

This project was developed with assistance from **GitHub Copilot**, which helped with:
- 🧠 **API exploration** and endpoint discovery
- 🔍 **Vehicle detection logic** design and implementation  
- 🎯 **City-specific configuration** research and mapping
- 🐛 **Debugging** and error handling patterns
- 📚 **Documentation** writing and examples

*Happy coding! 🚀 • Powered by GitHub Copilot 🤖*