# DUK Transport Integration - Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-10-23

### 🚀 Added
- **Multi-modal transport support** - podpora 6 typů dopravních prostředků
- **CIS API integrace** - nové API pro městskou dopravu a vlaky  
- **Inteligentní detekce vozidel** podle dopravce a čísla linky
- **Nové typy vozidel:**
  - 🚎 Trolejbusy (včetně parciálních)
  - 🚋 Tramvaje  
  - 🚠 Funicular/lanovka (Větruše)
  - 🚢 Lodě (Labská plavební)
  - 🚆 Vlaky (automatická detekce)
- **Comprehensive city coverage:**
  - Teplice (MD Teplice) - trolejbusy 101-109, autobusy 110, 119
  - Most-Litvínov (DPMML) - tramvaje 1-4, 40
  - Ústí nad Labem (DPMÚL) - trolejbusy 70-88, 43, 46 + lanovka 901
  - Chomutov-Jirkov (DPCHJ) - trolejbusy 340-353, autobusy 302-317
- **Dynamické ikony** pro každý typ vozidla (`mdi:gondola` pro lanovku!)
- **Carrier attribute** v odjezdech pro identifikaci dopravce
- **Post ID konfigurace** pro CIS API endpoint

### 🔧 Improved
- Robustnější parsing API odpovědí
- Lepší error handling pro různé API endpointy
- Optimalizovaná detekce typu vozidla
- Aktualizovaná dokumentace s příklady stanic
- Komprehensivní dokumentace včetně troubleshootingu

### 🐛 Fixed
- Encoding issues s českými znaky
- Parsing časů z různých formátů API
- Handling prázdných odpovědí API

### 🤖 Development
- Projekt vyvinut s asistencí GitHub Copilot pro rychlejší a kvalitnější vývoj

## [1.1.5] - 2025-10-23

### Added
- 🎨 **Integration logo display** - DUK logo now shows in HA integrations list
- 📋 Brand configuration file for proper logo recognition
- 🖼️ Multiple icon formats for better HA compatibility

### Fixed
- 🔧 Integration logo display in Home Assistant interface
- 📱 Brand recognition and visual identity

## [1.1.4] - 2025-10-23

### Fixed
- 🎨 Fixed icon display issues in Home Assistant
- 🔧 Improved sensor icon selection and visibility
- 📊 Better default icons for bus entities

## [1.1.3] - 2025-10-23

### Added
- 📋 HACS configuration file (hacs.json) for proper HACS validation
- 🔧 HACS compatibility improvements

### Fixed
- 🔄 HACS validation errors and compatibility issues

## [1.1.2] - 2025-10-23

### Fixed
- 🔄 HACS version detection and release management
- 📦 GitHub release tagging for proper distribution

## [1.1.1] - 2025-10-23

### Added
- 🎨 Official DUK logo integration with brand assets
- 🌐 Real DUK API integration with live departure data
- 🔧 Improved encoding handling for Czech characters
- 📊 Enhanced error handling and fallback mechanisms
- 🚌 Dynamic icons based on vehicle type and delays

### Changed
- 🔄 Switched from mock data to real DUK API endpoint
- ⚡ Improved API response parsing and error handling
- 🎯 Enhanced sensor attributes with carrier information
- 🔍 Better logging for debugging and monitoring

### Fixed
- 🐛 Character encoding issues with Czech text
- 🛠️ API timeout and connection error handling
- 📝 Proper time formatting for Home Assistant

## [1.0.0] - 2025-10-22

### Added
- ✨ Initial release of DUK Transport integration
- 🚌 Support for departure board data from DUK API
- ⚙️ UI configuration flow for easy setup
- 🔄 Automatic data updates with configurable interval
- 📊 Rich sensor data with departure information
- 🧪 Mock data support for testing
- 📱 Dashboard examples and templates
- 📖 Comprehensive documentation

### Features
- Real-time departure information
- Delay notifications
- Customizable update intervals
- Multiple departure display
- Platform and vehicle type information
- Template sensors for enhanced display

### Technical
- Async/await architecture
- Proper error handling
- Debug logging support
- Home Assistant 2023.1+ compatibility
- HACS integration ready

## [Unreleased]

### Planned
- 🌐 Multi-language support (Czech/English)
- 📍 GPS-based stop discovery
- 🔔 Advanced notification options
- 📈 Historical data tracking
- 🎨 Enhanced dashboard cards
- 🚀 Performance optimizations