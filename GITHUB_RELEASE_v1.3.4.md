# DUK Transport v1.3.4 - Critical Platform Fix 🚨

## 🐛 **CRITICAL BUG FIX: Platform Information**

### **Problem Solved**
**Platform information was incorrectly showing all departures on platform 1**, even when vehicles were actually departing from different platforms.

### **Root Cause Discovered** 
The API `post` parameter has a **crucial impact** on platform data accuracy:

```
post=1  → All departures show as "platform 1" ❌
post=999 → All departures show as "platform 999" ❌  
post=0  → Correct platform numbers ✅
```

## 🔧 **Technical Fix**

### **API Parameter Changes**
- **DUK API**: Changed from `post=1` to `post=0` 
- **CIS API**: Changed default from `post=999` to `post=0`
- **Station Info**: Updated to use `post=0` for consistency

### **Code Changes**
```python
# BEFORE (incorrect)
endpoint = f"/duk/GetStationDeparturesWCount/{stop_id}/1/{max_departures}/0"
get_cis_departures(stop_id: str, post_id: str = "999", ...)

# AFTER (correct)  
endpoint = f"/duk/GetStationDeparturesWCount/{stop_id}/0/{max_departures}/0"
get_cis_departures(stop_id: str, post_id: str = "0", ...)
```

## 📊 **Real-World Results**

### **Station 1591 (Teplice, Hlavní nádraží) - BEFORE vs AFTER**

#### **❌ Before (v1.3.3 and earlier):**
```
All departures: platform "1"
```

#### **✅ After (v1.3.4):**
```
Line 103 (MD Teplice trolleybus): platform "1"
Line 110 (MD Teplice trolleybus): platform "2"  
Line U3 (ČD train): platform "92"
Line 488 (Doprava Teplice bus): platform "2"
```

### **Platform Diversity Now Working:**
- **Platform 1**: Trolleybuses (some MD Teplice lines)
- **Platform 2**: Trolleybuses and buses (MD Teplice, Doprava Teplice)
- **Platform 92**: Trains (ČD railway platform)

## 🎯 **Impact for Users**

### **✅ What's Fixed**
- **Accurate platform information** in Home Assistant UI
- **Proper train platform numbers** (showing 92 instead of 1)
- **Correct bus/trolleybus platforms** (1, 2, etc.)
- **Better transit planning** with real platform data

### **🏙️ Affected Locations**
This fix improves platform accuracy for **all supported stations**:
- Teplice (verified working correctly)
- Most-Litvínov  
- Ústí nad Labem
- Chomutov
- All railway stations with CIS data

## 🔧 **Installation**

### HACS (Recommended)
1. Go to HACS → Integrations
2. Search for "DUK Transport"
3. Update to v1.3.4

### Manual Installation
1. Download the latest release
2. Copy `custom_components/duk_transport/` to your Home Assistant
3. Restart Home Assistant

## 📝 **Additional Notes**

- **Breaking Change**: None - this is a pure bug fix
- **Performance Impact**: None - same API calls, just different parameter
- **Backward Compatibility**: Full - all existing configurations work unchanged

## 🚀 **Technical Details**

### **API Documentation Discovery**
Through extensive testing, we discovered the undocumented behavior:
- `post=0`: Returns actual platform/post numbers from station infrastructure
- `post=1`: Filters to specific post but shows all as platform 1
- `post=999`: Shows long-distance departures but assigns platform 999

### **Testing Methodology**
Comprehensive testing across multiple `post` parameter values revealed the correct approach for accurate platform data extraction.

---

**Previous releases:** [v1.3.3](https://github.com/Peta01/ha-duk-transport/releases/tag/v1.3.3) | [v1.3.2](https://github.com/Peta01/ha-duk-transport/releases/tag/v1.3.2) | [v1.3.1](https://github.com/Peta01/ha-duk-transport/releases/tag/v1.3.1) | [v1.3.0](https://github.com/Peta01/ha-duk-transport/releases/tag/v1.3.0)