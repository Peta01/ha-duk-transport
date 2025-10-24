# DUK Transport v1.4.0 - Tourist Trains & Direct Emoji Support 🚂

## ✨ New Features

### 🚂 Tourist Train Detection
- **Tourist trains (T1-T29)** now get special **steam locomotive icon** 🚂 (`mdi:steam`)
- Differentiated from regular trains for authentic historic transport experience
- Perfect for scenic railway routes and heritage transport

### 📱 Universal Display Support with Smart Fallbacks
- **4 display options** for maximum compatibility across all systems
- **Automatic fallback** from emoji → ASCII symbols → single chars
- **Works everywhere**: Modern HA, Docker, Windows terminals, logs, old browsers
- New sensor attributes: `vehicle_emoji`, `vehicle_symbol`, `vehicle_char`, `vehicle_icon`

## 🚍 Complete Transport Type Coverage

| Transport | Type | Emoji | Icon | Lines |
|-----------|------|--------|------|--------|
| Bus | `bus` | 🚌 | `mdi:bus` | Most lines |
| Trolleybus | `trolleybus` | 🚎 | `mdi:bus-electric` | 340-359, 70-89, 101-109 |
| Tram | `tram` | 🚊 | `mdi:tram` | 1-4, 40 |
| Train | `train` | 🚆 | `mdi:train` | R, Ex, Os, IC, etc. |
| **Tourist Train** | `tourist_train` | **🚂** | **`mdi:steam`** | **T1-T29** |
| Ship | `ship` | ⛴️ | `mdi:ferry` | F1, T90-T99 |
| Funicular | `funicular` | 🚠 | `mdi:gondola` | 901 |

## 🎨 UI Improvements

### Before (complex templates):
```yaml
# Old way - complex mapping
icon: >
  {% if state_attr('sensor.duk_transport', 'departures')[0]['vehicle_type'] == 'train' %}
    mdi:train
  {% elif state_attr('sensor.duk_transport', 'departures')[0]['vehicle_type'] == 'tram' %}
    mdi:tram
  {% endif %}
```

### After (multiple options):
```yaml
# Modern systems (emoji)
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_emoji'] }} {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"

# Safe ASCII fallback (works everywhere)  
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_symbol'] }} {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"

# Minimal (ultra-compatible)
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_char'] }} {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"

# Direct icon access
icon: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_icon'] }}"
```

## 📋 New Sensor Attributes

Each departure in the `departures` attribute now includes **4 display options**:
- `vehicle_emoji`: Unicode emoji (🚌🚎🚊🚆🚂⛴️🚠) - for modern systems
- `vehicle_symbol`: ASCII fallback ([BUS], [STEAM], [CABLE]) - for logs/terminals  
- `vehicle_char`: Single character (B, S, C) - ultra-compatible
- `vehicle_icon`: Material Design icon (mdi:bus, mdi:steam) - for HA UI
- `vehicle_type`: Transport type string (backward compatible)

## 🛡️ Compatibility Guarantee
- **Emoji issues?** Use `vehicle_symbol` instead
- **Encoding problems?** Use `vehicle_char`  
- **Old systems?** All ASCII variants work everywhere
- **Docker/Alpine?** No font dependencies for fallbacks

## 🔧 Technical Details

### Vehicle Type Detection Logic
1. **Ships**: F1 ferries, T90-T99 tourist boats → ⛴️
2. **Tourist Trains**: T1-T29 historic railways → 🚂 (NEW!)
3. **Regular Trains**: Letter prefixes (R, Ex, Os, IC, etc.) → 🚆
4. **City Transport**: Based on carrier and line configuration → 🚎🚊🚠
5. **Default**: Regional buses and replacement services → 🚌

### Backward Compatibility
- All existing functionality preserved
- `vehicle_type` attribute still available
- No breaking changes to existing configurations

## 🚂 Perfect for Historic Railways
This update is ideal for regions with tourist and heritage railways:
- **Jindřichův Hradec narrow gauge railway** (T15)
- **Šumava forest railway** (T1-T29 range)
- **Czech heritage steam trains**
- Any tourist railway using T1-T29 line numbers

## 📖 Example Usage

```yaml
# Modern systems with emoji support
type: custom:template-entity-row
name: >
  {{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_emoji'] }}
  {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}
# Result: "🚂 T15"

# Safe ASCII for all systems (recommended)
type: custom:template-entity-row  
name: >
  {{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_symbol'] }}
  {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}
# Result: "[STEAM] T15"

# Ultra-minimal for space-constrained displays
type: custom:template-entity-row
name: >
  {{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_char'] }}{{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}
# Result: "ST15"
```

## 🧪 Test Your System Compatibility
Add this entity to test which display option works best:
```yaml
type: entities
entities:
  - entity: sensor.duk_transport_your_station
    secondary_info: >
      Emoji: {{ state_attr('sensor.duk_transport_your_station', 'departures')[0]['vehicle_emoji'] }}
      ASCII: {{ state_attr('sensor.duk_transport_your_station', 'departures')[0]['vehicle_symbol'] }}
      Char: {{ state_attr('sensor.duk_transport_your_station', 'departures')[0]['vehicle_char'] }}
```

## 🎯 Migration Guide
No migration needed! This is a **purely additive update**:
- Install v1.4.0
- Optionally simplify your Lovelace templates using new emoji attributes
- Enjoy steam locomotive icons for tourist trains! 🚂

---
*Ready to experience the charm of historic railways with proper steam locomotive representation!* 🚂✨