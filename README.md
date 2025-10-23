# 🚌 DUK Transport - Home Assistant Integration

<p align="center">
  <img src="https://github.com/Peta01/ha-duk-transport/raw/master/custom_components/duk_transport/assets/logo.png" alt="DUK Logo" width="200"/>
</p>

**Komplexní integrace pro odjezdové tabule v Ústeckém kraji** - podporuje autobusy, trolejbusy, tramvaje, vlaky, lodě i lanovku! 🚌🚎🚋🚆🚢🚠

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/Peta01/ha-duk-transport.svg)](https://github.com/Peta01/ha-duk-transport/releases)

## 🌟 Funkce

- 🚌 **Multi-modal transport** - autobusy, trolejbusy, tramvaje, vlaky, lodě, lanovka
- ⏰ **Aktuální odjezdy** s informacemi o zpožděních v reálném čase
- 🏙️ **Pokrytí celého kraje** - Teplice, Most, Litvínov, Ústí n.L., Chomutov, Jirkov
- � **Inteligentní detekce** typu vozidla podle dopravce a linky
- � **Duální API podpora** - DUK (regionální) + CIS (městské + vlaky)
- 🎨 **Dynamické ikony** pro každý typ dopravního prostředku
- 🧪 **Mock data** pro testování bez API připojení

## 🚀 Rychlá instalace

### Přes HACS (doporučeno)

1. Otevřete HACS v Home Assistant
2. Přejděte na "Integrations"
3. Klikněte na "..." → "Custom repositories"
4. Přidejte URL: `https://github.com/Peta01/ha-duk-transport`
5. Kategorie: "Integration"
6. Klikněte "Add"
7. Restartujte Home Assistant
8. Přidejte integraci: Nastavení → Zařízení a služby → + Přidat → "DUK Transport"

### Manuální instalace

1. Stáhněte soubory z [releases](https://github.com/Peta01/ha-duk-transport/releases)
2. Zkopírujte složku `custom_components/duk_transport` do vaší HA config složky
3. Restartujte Home Assistant
4. Přidejte integraci přes UI

## ⚙️ Konfigurace

Po instalaci přidejte integraci:

1. **Nastavení** → **Zařízení a služby** → **+ PŘIDAT INTEGRACI**
2. Vyhledejte **"DUK Transport"**
3. Zadejte konfiguraci:
   - **ID zastávky**: Číselné ID zastávky
   - **Název zastávky**: Volitelný popisný název
   - **Typ API**: `DUK` (regionální) nebo `CIS` (městská doprava + vlaky)
   - **Post ID**: Pro CIS API (obvykle `1` nebo `999`)
   - **Interval aktualizace**: Jak často aktualizovat data (sekundy)
   - **Maximální počet odjezdů**: Kolik odjezdů zobrazit

### 🚌 Příklady stanic

#### DUK API (regionální autobusy)
- **2950**: Krupka, ke Kateřině 
- **2957**: Krupka, Bohosudov, Lindnerova

#### CIS API (městská doprava)
- **1578**: Teplice (trolejbusy MD Teplice)
- **1967**: Most-Litvínov (tramvaje DPMML) 
- **12140**: Ústí n.L., Větruše (lanovka DPMÚL)
- **2427**: Labská plavební (lodě)

### Testovací konfigurace

Pro testování použijte:
- **ID zastávky**: `12345`
- **Název**: `Test zastávka`
- **API typ**: `DUK`
- **Interval**: `60` sekund
- **Max odjezdy**: `10`

## 📱 Dashboard

### Základní karta

```yaml
type: entities
title: 🚌 Odjezdy DUK
entities:
  - entity: sensor.duk_transport_test_zastavka
    name: Aktuální stav
```

### Odjezdová tabulka

```yaml
type: markdown
title: 📋 Seznam odjezdů
content: |
  {% set departures = state_attr('sensor.duk_transport_test_zastavka', 'departures') or [] %}
  {% if departures %}
  | Linka | Směr | Čas | Zpoždění |
  |-------|------|-----|----------|
  {% for departure in departures %}
  | **{{ departure.line }}** | {{ departure.destination }} | {{ departure.departure_time }} | {% if departure.delay > 0 %}+{{ departure.delay }} min{% else %}načas{% endif %} |
  {% endfor %}
  {% endif %}
```

## 🔍 Dostupné entity

### Senzory
- `sensor.duk_transport_[nazev_zastavky]` - Hlavní senzor s odjezdy

### Atributy
- `stop_id` - ID zastávky
- `stop_name` - Název zastávky  
- `departures` - Seznam všech odjezdů
- `count` - Počet dostupných odjezdů
- `next_departure` - Detail nejbližšího odjezdu

### Struktura odjezdu
- `line` - Číslo linky
- `destination` - Cílová stanice
- `departure_time` - Čas odjezdu (HH:MM)
- `delay` - Zpoždění v minutách
- `platform` - Nástupiště
- `vehicle_type` - Typ vozidla (`bus`, `trolleybus`, `tram`, `train`, `ship`, `funicular`)
- `carrier` - Název dopravce (MD Teplice, DPMML, DPMÚL, DPCHJ)

## 🚌 Podporované dopravní systémy

### 🚎 Trolejbusy
- **Teplice** (MD Teplice): Linky 101-109 (parciální trolejbusy), 110+119 (autobusy)
- **Ústí nad Labem** (DPMÚL): Linky 70-88, 43, 46
- **Chomutov-Jirkov** (DPCHJ): Linky 340-353 (trolejbusy), 302-317 (autobusy)

### 🚋 Tramvaje  
- **Most-Litvínov** (DPMML): Linky 1-4 (denní), 40 (noční)

### 🚠 Speciální doprava
- **Lanovka Větruše** (DPMÚL): Linka 901 (funicular)
- **Labská plavební**: Lodní spoje po Labi

### 🚆 Vlaky
- **Automatická detekce** vlakových linek (R, EX, SC, IC, EC, RJ, EN, OS, SP)

## 🤝 Přispívání

1. Forkněte repozitář
2. Vytvořte feature branch (`git checkout -b feature/amazing-feature`)
3. Commitujte změny (`git commit -m 'Add amazing feature'`)
4. Pushněte branch (`git push origin feature/amazing-feature`)
5. Otevřete Pull Request

## 📄 Licence

Tento projekt je licencován pod MIT licencí - viz [LICENSE](LICENSE) soubor.

## 🙋 Podpora

- 🐛 **Chyby**: [GitHub Issues](https://github.com/Peta01/ha-duk-transport/issues)
- 💬 **Diskuze**: [GitHub Discussions](https://github.com/Peta01/ha-duk-transport/discussions)
- 📖 **Dokumentace**: [Wiki](https://github.com/Peta01/ha-duk-transport/wiki)

## 🏆 Poděkování

- [Home Assistant](https://www.home-assistant.io/) za úžasnou platformu
- [Doprava Ústeckého kraje](https://www.duk.cz/) za poskytnutí API
- [GitHub Copilot](https://github.com/features/copilot) 🤖 za asistenci při vývoji
- Všem přispěvovatelům a testerům ❤️

---

**Vytvořeno s 💚 pro Home Assistant komunitu • Powered by GitHub Copilot 🤖**