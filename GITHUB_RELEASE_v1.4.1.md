# DUK Transport v1.4.1 - Universal Emoji Compatibility 🛡️

## 🚨 Critical Compatibility Fix

**Resolved emoji display issues** across all systems and environments! No more broken characters in logs, terminals, or older systems.

## 🛡️ 4-Level Fallback System

Your integration now works **everywhere** with automatic fallback:

### 1. 🚂 Emoji (Modern Systems)
```yaml
{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_emoji'] }}
# Result: 🚂 (Unicode emoji - modern HA, mobile apps)
```

### 2. [STEAM] ASCII Symbols (Universal)
```yaml
{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_symbol'] }}
# Result: [STEAM] (ASCII-safe - logs, terminals, Docker)
```

### 3. S Single Character (Ultra-Compatible)
```yaml
{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_char'] }}
# Result: S (one character - embedded systems, minimal displays)
```

### 4. mdi:steam Icons (Home Assistant UI)
```yaml
{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_icon'] }}
# Result: mdi:steam (Material Design - HA interface)
```

## 🎯 Complete Compatibility Matrix

| Transport Type | Emoji | ASCII Symbol | Char | Icon | Best For |
|----------------|-------|--------------|------|------|----------|
| **Tourist Train** | 🚂 | **[STEAM]** | **S** | **mdi:steam** | Historic railways |
| Trolleybus | 🚎 | [TROL] | T | mdi:bus-electric | City transport |
| Funicular | 🚠 | [CABLE] | C | mdi:gondola | Cable cars |
| Train | 🚆 | [TRAIN] | R | mdi:train | Regular rail |
| Tram | 🚊 | [TRAM] | M | mdi:tram | City rail |
| Ship | ⛴️ | [SHIP] | F | mdi:ferry | Ferries |
| Bus | 🚌 | [BUS] | B | mdi:bus | Everything else |

## ✅ System Compatibility Guaranteed

| Environment | Works With | Recommended Attribute |
|-------------|------------|----------------------|
| **Modern Home Assistant** | All options | `vehicle_emoji` |
| **Docker/Alpine Linux** | ASCII + Char + Icon | `vehicle_symbol` |
| **Windows Terminal** | ASCII + Char + Icon | `vehicle_symbol` |
| **Home Assistant Logs** | ASCII + Char | `vehicle_symbol` |
| **Older Browsers** | Char + Icon | `vehicle_char` |
| **Embedded Systems** | Char only | `vehicle_char` |
| **Mobile Apps** | Emoji + Icon | `vehicle_emoji` |

## 🔧 Migration & Usage

### Recommended Template (Smart Fallback):
```yaml
# This template tries emoji first, falls back to ASCII if needed
name: >
  {% set emoji = state_attr('sensor.duk_transport', 'departures')[0]['vehicle_emoji'] %}
  {% set symbol = state_attr('sensor.duk_transport', 'departures')[0]['vehicle_symbol'] %}
  {% set line = state_attr('sensor.duk_transport', 'departures')[0]['line'] %}
  {{ emoji if emoji != '?' else symbol }} {{ line }}
```

### Safe ASCII-Only (Always Works):
```yaml
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_symbol'] }} {{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"
# Result: "[STEAM] T15", "[TROL] 105", "[CABLE] 901"
```

### Ultra-Minimal (Space-Constrained):
```yaml
name: "{{ state_attr('sensor.duk_transport', 'departures')[0]['vehicle_char'] }}{{ state_attr('sensor.duk_transport', 'departures')[0]['line'] }}"
# Result: "ST15", "T105", "C901"
```

## 🧪 Test Your System

Add this test entity to see which options work in your environment:
```yaml
type: entities
entities:
  - entity: sensor.duk_transport_your_station
    name: "Display Test"
    secondary_info: >
      Emoji: {{ state_attr('sensor.duk_transport_your_station', 'departures')[0]['vehicle_emoji'] }}
      | ASCII: {{ state_attr('sensor.duk_transport_your_station', 'departures')[0]['vehicle_symbol'] }}
      | Char: {{ state_attr('sensor.duk_transport_your_station', 'departures')[0]['vehicle_char'] }}
```

**Expected results:**
- ✅ All work: `Emoji: 🚂 | ASCII: [STEAM] | Char: S`
- ⚠️ Emoji issues: `Emoji: ? | ASCII: [STEAM] | Char: S` → Use ASCII
- 🚨 Major issues: Only `Char: S` works → Use single characters

## 🎯 Perfect For These Issues

### Fixed Problems:
- ❌ "🚂" shows as "?" in Windows Terminal → ✅ Use `[STEAM]`
- ❌ Emoji breaks Docker logs → ✅ ASCII symbols work everywhere  
- ❌ Encoding errors in HA logs → ✅ Fallback system handles all cases
- ❌ Old browsers can't display Unicode → ✅ Single characters always work

### Tourist Train Examples:
```yaml
# Modern display: 🚂 T15 → Jindřichův Hradec
# ASCII safe: [STEAM] T15 → Jindřichův Hradec  
# Minimal: ST15 → Jindřichův Hradec
```

## 📋 What's New in v1.4.1

- **4 display attributes** per departure instead of 1
- **Automatic encoding detection** and fallback
- **Universal compatibility** across all Home Assistant environments
- **Zero breaking changes** - all existing templates still work
- **Complete documentation** with system-specific recommendations

## 🚀 Upgrade Path

1. **Install v1.4.1** - no config changes needed
2. **Test your system** using the test template above
3. **Update templates** to use the best option for your environment
4. **Enjoy reliable symbols** that work everywhere!

---

*No more broken emoji! Universal compatibility guaranteed!* 🛡️✨