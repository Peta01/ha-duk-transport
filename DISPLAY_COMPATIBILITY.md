# Vehicle Symbol Display Guide

## Problem Statement
Emoji (🚌🚂🚠) may not display correctly in all environments:
- **Windows terminals** with CP1250/ASCII encoding
- **Home Assistant logs** in ASCII mode
- **Older browsers** without emoji support
- **Docker containers** without font packages
- **Embedded systems** with limited Unicode support

## Solution: Multi-Level Fallback System

Each departure now includes **4 different display options**:

### 1. `vehicle_emoji` - Modern Systems (Preferred)
```yaml
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_emoji'] }} {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"
# Result: "🚂 T15" (tourist train)
```

### 2. `vehicle_symbol` - ASCII Fallback (Safe)
```yaml
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_symbol'] }} {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"
# Result: "[STEAM] T15" (works in all logs)
```

### 3. `vehicle_char` - Minimal (Ultra-compatible)
```yaml
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_char'] }} {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"
# Result: "S T15" (single character)
```

### 4. `vehicle_icon` - Material Design (UI Icons)
```yaml
icon: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_icon'] }}"
# Result: "mdi:steam" (for Home Assistant UI)
```

## Complete Symbol Mapping

| Transport | Emoji | Symbol | Char | Icon | Use Case |
|-----------|-------|--------|------|------|----------|
| Bus | 🚌 | [BUS] | B | mdi:bus | Regional transport |
| Trolleybus | 🚎 | [TROL] | T | mdi:bus-electric | City electric bus |
| Tram | 🚊 | [TRAM] | M | mdi:tram | City rail |
| Train | 🚆 | [TRAIN] | R | mdi:train | Regular railway |
| **Tourist Train** | **🚂** | **[STEAM]** | **S** | **mdi:steam** | **Historic/scenic** |
| Ship | ⛴️ | [SHIP] | F | mdi:ferry | Ferry/boat |
| Funicular | 🚠 | [CABLE] | C | mdi:gondola | Cable car |

## Recommended Usage Patterns

### Smart Template (Auto-fallback)
```yaml
# Try emoji first, fallback to symbol if encoding fails
name: >
  {% set emoji = state_attr('sensor.duk_transport', 'departures')[0]['vehicle_emoji'] %}
  {% set symbol = state_attr('sensor.duk_transport', 'departures')[0]['vehicle_symbol'] %}
  {% set line = state_attr('sensor.duk_transport', 'departures')[0]['line'] %}
  {% if emoji and emoji != '?' %}
    {{ emoji }} {{ line }}
  {% else %}
    {{ symbol }} {{ line }}
  {% endif %}
```

### Safe ASCII-Only
```yaml
# For systems known to have encoding issues
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_symbol'] }} {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"
```

### Ultra-Minimal
```yaml
# For space-constrained displays
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_char'] }}{{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"
# Result: "ST15", "B123", "R456"
```

## System Compatibility

| Environment | Recommended | Fallback | Notes |
|-------------|-------------|----------|-------|
| Modern HA (2023+) | `vehicle_emoji` | `vehicle_symbol` | Full Unicode support |
| Docker/Alpine | `vehicle_symbol` | `vehicle_char` | Limited fonts |
| Windows Terminal | `vehicle_symbol` | `vehicle_char` | CP1250 encoding |
| HA Logs | `vehicle_symbol` | `vehicle_char` | ASCII-safe logging |
| Mobile Apps | `vehicle_emoji` | `vehicle_icon` | Native emoji support |
| Old Browsers | `vehicle_char` | `vehicle_icon` | Minimal fallback |

## Testing Your System

Add this to your Lovelace for testing:
```yaml
type: entities
entities:
  - entity: sensor.duk_transport_your_station
    name: "Emoji Test"
    secondary_info: >
      {{ state_attr('sensor.duk_transport_your_station', 'departures')[0]['vehicle_emoji'] }}
      {{ state_attr('sensor.duk_transport_your_station', 'departures')[0]['vehicle_symbol'] }}
      {{ state_attr('sensor.duk_transport_your_station', 'departures')[0]['vehicle_char'] }}
```

If you see "🚂 [STEAM] S" - all options work!
If you see "? [STEAM] S" - use symbol or char fallback.

## Migration from v1.3.x

**No breaking changes!** All existing templates continue to work.

Old way (still works):
```yaml
# Complex template mapping
icon: >
  {% if state_attr('sensor.duk', 'departures')[0]['vehicle_type'] == 'tourist_train' %}
    mdi:steam
  {% else %}
    mdi:bus
  {% endif %}
```

New way (simpler):
```yaml
# Direct attribute access
icon: "{{ state_attr('sensor.duk', 'departures')[0]['vehicle_icon'] }}"
```