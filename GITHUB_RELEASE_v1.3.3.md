# DUK Transport v1.3.3 - Refactored Vehicle Detection 🚀

## 🏗️ Major Architecture Improvements

### 🎯 **Cleaner Vehicle Detection Logic**
Completely refactored `_determine_vehicle_type()` with a much more maintainable architecture:

**New Priority Order:**
1. **Ships** - F1 ferries, T90-T99 tourist boats
2. **Trains** - T1-T29 tourist trains, alphabetic prefixes (U3, R1, IC, etc.)  
3. **const.py Configuration** - Specific lines configured per carrier
4. **Hardcoded Fallbacks** - DPMML→tram, DPCHJ→trolleybus
5. **Default Bus** - Everything else (most common transport)

### 🔧 **Technical Improvements**

#### **Simplified Configuration**
- **Default vehicle type is now `bus`** (covers 85% of transport)
- **Removed duplicate bus definitions** from `CITY_TRANSPORT_LINES`
- **Prioritized `const.py` configuration** over hardcoded rules
- **Cleaner fallback logic** for carrier-based detection

#### **Fixed Platform Parsing**
- **Both DUK and CIS APIs** now correctly use `StationPost` for platform information
- **Platform data now displays correctly** in Home Assistant (previously always empty)

## 📊 **What This Means for Users**

### ✅ **More Accurate Detection**
- **Better maintainability** - easier to add new cities/carriers
- **Cleaner logic flow** - priority-based instead of complex nested conditions  
- **Extensible architecture** - adding new transport modes is simpler

### 🛠️ **For Developers**
- **Single source of truth** - vehicle types primarily configured in `const.py`
- **Reduced code complexity** - 40 lines vs previous 80+ lines
- **Better separation of concerns** - config vs logic

### 🏙️ **Current Support**
- **Teplice**: Trolleybuses (101-109), buses (everything else)
- **Most-Litvínov**: Trams (1-4, 40), all other DPMML lines default to tram
- **Ústí nad Labem**: Funicular (901), trolleybuses (70-88), buses (1-20)  
- **Chomutov**: Trolleybuses (340-353), all other DPCHJ lines default to trolleybus
- **Trains**: All alphabetic lines (U3, R1, IC, EN, etc.)
- **Ships**: F1 ferries, T90-T99 tourist boats

## 🔧 **Installation**

### HACS (Recommended)
1. Go to HACS → Integrations
2. Search for "DUK Transport"
3. Update to v1.3.3

### Manual Installation  
1. Download the latest release
2. Copy `custom_components/duk_transport/` to your Home Assistant
3. Restart Home Assistant

## 🐛 **Bug Fixes**
- Fixed platform information display (was showing empty, now shows correct platform numbers)
- Improved encoding handling for station names and directions

## 🚀 **Full Changelog**
- Refactored vehicle detection with priority-based architecture
- Fixed platform parsing for both DUK and CIS APIs  
- Removed duplicate bus definitions from configuration
- Simplified fallback logic for better maintainability
- Enhanced debug logging for troubleshooting

---

**Previous releases:** [v1.3.2](https://github.com/Peta01/ha-duk-transport/releases/tag/v1.3.2) | [v1.3.1](https://github.com/Peta01/ha-duk-transport/releases/tag/v1.3.1) | [v1.3.0](https://github.com/Peta01/ha-duk-transport/releases/tag/v1.3.0)