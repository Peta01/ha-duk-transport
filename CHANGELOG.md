# Changelog# Changelog# DUK Transport Integration - Changelog



Všechny změny v DUK Transport integraci jsou zdokumentovány v tomto souboru.



Formát vychází z [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),All notable changes to the DUK Transport integration will be documented in this file.All notable changes to this project will be documented in this file.

verzování podle [Semantic Versioning](https://semver.org/spec/v2.0.0.html).



## [1.0.0] - 2025-11-03

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),

### 🚀 První veřejné vydání

and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Komplexní integrace pro odjezdové tabule veřejné dopravy v České republice.



#### ✨ Hlavní funkce

## [1.0.0] - 2025-01-24 - Initial Release## [1.0.0] - 2025-11-03

- **Multi-modální podpora dopravy** - 6 typů vozidel

  - 🚌 Autobusy (městské i regionální)

  - 🚎 Trolejbusy (včetně parciálních)

  - 🚋 TramvajeWelcome to the first public release of **DUK Transport** integration for Home Assistant! 🎉### 🚀 Initial Release

  - 🚆 Vlaky (automatická detekce)

  - 🚠 Lanovky (např. Větruše v Ústí nad Labem)

  - 🚢 Lodě (Labská plavební)

This integration provides real-time departure information from public transport stations across the Czech Republic using the DUK Transport API. Track buses, trams, trolleybuses, trains, funiculars, and boats with intelligent vehicle detection and multi-modal transport support.**Komplexní integrace pro odjezdové tabule v Ústeckém kraji**

- **Inteligentní detekce vozidel** podle dopravce a čísla linky

- **Dynamické ikony** pro každý typ vozidla

- **7 122 zastávek** po celé České republice v [STATIONS.md](STATIONS.md)

### ✨ Core Features#### ✨ Features

#### 🏙️ Pokrytí měst

- **Multi-modal transport support** - autobusy, trolejbusy, tramvaje, vlaky, lodě, lanovka 🚌🚎🚋🚆🚢🚠

- **Teplice** (MD Teplice) - trolejbusy 101-109, autobusy 110, 119

- **Most-Litvínov** (DPMML) - tramvaje 1-4, 40#### 🚌 Multi-Modal Transport Support- **Real-time departure data** - aktuální odjezdy s informacemi o zpožděních

- **Ústí nad Labem** (DPMÚL) - trolejbusy 70-88, 43, 46 + lanovka Větruše 901

- **Chomutov-Jirkov** (DPCHJ) - trolejbusy 340-353, autobusy 302-317- **6 vehicle types supported:**- **Dual API support** - DUK (regionální) + CIS (městská doprava + vlaky)



#### 🔌 Možnosti konfigurace  - 🚌 Buses (standard and regional)- **Intelligent vehicle detection** - automatická detekce typu vozidla podle dopravce a čísla linky



- Snadná konfigurace přes UI Home Assistantu  - 🚎 Trolleybuses (including partial trolleybuses)- **Dynamic icons** - ikony pro každý typ dopravního prostředku

- Nastavitelný interval aktualizace (minimum 60 sekund)

- Nastavitelný počet zobrazených odjezdů  - 🚋 Trams- **Emoji fallback system** - 4-úrovňový fallback systém (emoji → ASCII → char → icon)

- Bohaté atributy senzoru: dopravce, zpoždění, nástupiště, typ vozidla

- Dual API: DUK (regionální doprava) + CIS (městská doprava a vlaky)  - 🚆 Trains (automatic detection)- **7000+ stations** - kompletní seznam všech zastávek v STATIONS.md



#### 📋 Co je součástí  - 🚠 Funiculars (e.g., Větruše cable car)



- Home Assistant custom component s plnou async/await architekturou  - 🚢 Boats (e.g., Labská plavební)#### 🏙️ Coverage

- UI configuration flow pro snadné nastavení

- Kompletní dokumentace a rychlý návod- **Intelligent vehicle type detection** based on carrier and line number- **Teplice** - trolejbusy MD Teplice (linky 101-109)

- Příklady dashboardů a hotové karty

- Úplný seznam 7 122 zastávek podle regionů- **Dynamic icons** that change automatically based on vehicle type- **Most-Litvínov** - tramvaje DPMML (linky 1-4, 40)

- Troubleshooting průvodce

- **Ústí nad Labem** - trolejbusy DPMÚL (linky 70-88, 43, 46) + lanovka Větruše (901)

#### 🏙️ Comprehensive Coverage- **Chomutov-Jirkov** - trolejbusy DPCHJ (linky 340-353)

- **Teplice** (MD Teplice) - trolleybuses 101-109, buses 110, 119- **Labská plavební** - lodě (linky F1, T90-T99)

- **Most-Litvínov** (DPMML) - trams 1-4, 40- **Tourist trains** - turistické vlaky T1-T29 s parní lokomotivou 🚂

- **Ústí nad Labem** (DPMÚL) - trolleybuses 70-88, 43, 46 + Větruše funicular 901

- **Chomutov-Jirkov** (DPCHJ) - trolleybuses 340-353, buses 302-317#### 🎨 Display Features

- **7,122 stations** available across the Czech Republic- **Vehicle emoji** - 🚌 (modern systems)

- **Vehicle symbol** - [BUS] (ASCII-safe for logs)

#### 🔌 Integration Features- **Vehicle char** - B (single character for minimal displays)

- **Easy configuration** through Home Assistant UI- **Vehicle icon** - mdi:bus (Material Design for HA UI)

- **Station search** - find station IDs in [STATIONS.md](STATIONS.md)

- **Configurable update interval** (minimum 60 seconds)#### 🔧 Technical

- **Configurable departure count** (how many departures to show)- Config flow pro snadnou konfiguraci přes UI

- **Rich sensor attributes:** carrier name, delays, platform info, vehicle types- Konfigurovatelný interval aktualizace

- **CIS API integration** for urban transport and trains- Konfigurovatelný počet odjezdů

- Mock data pro testování

### 📋 What's Included- Kompletní dokumentace včetně dashboard příkladů

- Home Assistant custom component with full async/await architecture- HACS kompatibilita

- UI configuration flow for easy sensor setup

- Comprehensive documentation and quick start guide#### 📋 Documentation

- Dashboard examples and ready-to-use card templates- README.md s kompletním průvodcem

- Complete station list with 7,122 stations grouped by region- STATIONS.md se seznamem 7000+ zastávek

- Troubleshooting guide and developer documentation- QUICK_START.md pro rychlou instalaci

- Dashboard příklady v examples/

### 🎯 Planned Features- Troubleshooting guide

- 🌐 Multi-language support (Czech/English)

- 📍 GPS-based stop discovery---

- 🔔 Advanced notification options

- 📈 Historical data tracking## [Unreleased]

- 🎨 Enhanced dashboard cards

- 🚀 Performance optimizations### Planned Features

- 🌐 Multi-language support (Czech/English)
- 📍 GPS-based stop discovery
- 🔔 Advanced notification options
- 📈 Historical data tracking
- 🎨 Enhanced dashboard cards
- 🚀 Performance optimizations

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