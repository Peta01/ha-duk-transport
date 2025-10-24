# v1.3.2: Complete DPMÚL Ústí nad Labem Line Classification

## ✨ New Features
- **Precise DPMÚL vehicle detection** based on official transport map
- **Blue lines** (70,71,72,73,76,80,82,84,87,88) → trolleybuses  
- **Green/orange/other lines** → buses
- **Funicular line 901** → funicular

## 🔧 Improvements
- Accurate classification replaces generic "all trolleybuses" approach
- Based on official DPMÚL network map analysis
- Tourist lines (10,20,21) correctly identified as buses
- Mixed-service lines properly categorized

## 📊 DPMÚL Classification
- 🟣 **Funicular**: 901
- 🔵 **Trolleybuses**: 70,71,72,73,76,80,82,84,87,88
- 🟢🟠 **Buses**: All other lines (79,81,83,85,89,90,10,20,21, etc.)

## 🎯 Completion
This completes the research item "DPMÚL bus vs trolleybus distinction" from v1.3.0 future enhancements.

---

**Previous releases:**
- v1.3.1: Fix CONFIG_SCHEMA validation warning
- v1.3.0: Major vehicle detection logic overhaul

**Full Changelog**: https://github.com/Peta01/ha-duk-transport/compare/v1.3.1...v1.3.2