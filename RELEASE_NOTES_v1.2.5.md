# DUK Transport v1.2.5 - Trolleybus Detection Fix

## 🚎 Trolleybus Detection Fixed!

This release fixes the critical issue where Teplice trolleybus lines (101-109) were showing as "bus" instead of "trolleybus" in Home Assistant sensors and dashboard cards.

## 🔧 Technical Changes 

**Root Cause Fixed:**
- The `_parse_duk_response` method was using hardcoded `'vehicle_type': 'bus'` instead of calling the `_determine_vehicle_type` logic
- Our trolleybus detection code was implemented in `_parse_cis_response` but DUK API uses `_parse_duk_response`

**Changes Made:**
- ✅ Updated `_parse_duk_response` to use `_determine_vehicle_type` method
- ✅ Added `stop_id` parameter to `_parse_duk_response` method signature
- ✅ Modified `get_departures` to pass `stop_id` to the parser
- ✅ Ensured consistent vehicle type detection across all API endpoints

## 🚌 What This Fixes

**Before v1.2.5:**
```yaml
sensor.teplice_benesovo_namesti:
  linky:
    - line: "101"
      vehicle_type: "bus"  # ❌ Wrong!
      carrier: "MD Teplice"
```

**After v1.2.5:**
```yaml
sensor.teplice_benesovo_namesti:
  linky:
    - line: "101" 
      vehicle_type: "trolleybus"  # ✅ Correct!
      carrier: "MD Teplice"
```

## 📍 Affected Lines

Teplice trolleybus lines that will now show correct `vehicle_type`:
- **101, 102, 103, 104, 105, 106, 107, 108, 109**

## 🏠 Dashboard Impact

Dashboard cards using the provided templates will now display:
- ✅ Correct trolleybus icons (🚎) for lines 101-109
- ✅ Proper color coding for trolleybus vs bus routes
- ✅ Accurate vehicle type information in entity attributes

## 🔄 Installation

Update through HACS or download v1.2.5 from releases. After updating:
1. Restart Home Assistant 
2. Check your Teplice sensor - trolleybus lines should now show `vehicle_type: "trolleybus"`
3. Dashboard cards will automatically display correct icons

## 🐛 Debug Information

The fix includes comprehensive debug logging that will show in logs:
```
Teplice analysis - Linka: 101, Dopravce: 'MD Teplice', Stanice: 'Teplice,Benešovo náměstí', ID: 1578
```

---

**Previous versions:** [v1.2.4](./RELEASE_NOTES_v1.2.4.md) | [v1.2.3](./RELEASE_NOTES_v1.2.3.md) | [v1.2.2](./RELEASE_NOTES_v1.2.2.md) | [v1.2.1](./RELEASE_NOTES_v1.2.1.md) | [v1.2.0](./RELEASE_NOTES_v1.2.0.md)