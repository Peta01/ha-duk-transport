# 🚌 DUK Transport - Home Assistant Integration

<p align="center">
  <img src="https://github.com/Peta01/ha-duk-transport/raw/master/custom_components/duk_transport/assets/logo.png" alt="DUK Logo" width="200"/>
</p>

Integrace pro zobrazení odjezdových tabulí Dopravy Ústeckého kraje v Home Assistant.

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/Peta01/ha-duk-transport.svg)](https://github.com/Peta01/ha-duk-transport/releases)

## 🌟 Funkce

- 🚌 **Aktuální odjezdy** z libovolné zastávky DUK
- ⏰ **Informace o zpožděních** v reálném čase
- 🔄 **Automatické aktualizace** s konfigurovatelným intervalem
- 🎨 **Přizpůsobitelný dashboard** s odjezdovou tabulí
- 🔔 **Notifikace** při větších zpožděních
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
   - **ID zastávky**: Číselné ID zastávky DUK
   - **Název zastávky**: Volitelný popisný název
   - **Interval aktualizace**: Jak často aktualizovat data (sekundy)
   - **Maximální počet odjezdů**: Kolik odjezdů zobrazit

### Testovací konfigurace

Pro testování použijte:
- **ID zastávky**: `12345`
- **Název**: `Test zastávka`
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
- `vehicle_type` - Typ vozidla

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
- [Doprava Ústeckého kraje](https://www.duk.cz/) za API
- Všem přispěvovatelům ❤️

---

**Vytvořeno s 💚 pro Home Assistant komunitu**