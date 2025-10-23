# DUK Transport v1.2.0 - Multi-Modal Transport Release 🚀

## 🌟 Major Release - Complete Transport Ecosystem

Největší update od spuštění! Integrace nyní podporuje kompletní spektrum dopravních prostředků v Ústeckém kraji.

## 🚌 Co je nového?

### 🎯 Multi-Modal Transport Support
- **6 typů vozidel**: autobusy, trolejbusy, tramvaje, vlaky, lodě, lanovka
- **Inteligentní detekce** typu vozidla podle dopravce a linky
- **Dynamické ikony** včetně `mdi:gondola` pro lanovku!

### 🏙️ Kompletní pokrytí měst
- **🚎 Teplice** (MD Teplice): Trolejbusy 101-109 + autobusy 110, 119  
- **🚋 Most-Litvínov** (DPMML): Tramvaje 1-4, 40
- **🚠 Ústí nad Labem** (DPMÚL): Trolejbusy 70-88, 43, 46 + **lanovka Větruše 901**
- **🚎 Chomutov-Jirkov** (DPCHJ): Trolejbusy 340-353 + autobusy 302-317

### 🔧 CIS API Integration
- Nové API pro městskou dopravu a vlaky
- Post ID konfigurace pro přesné targetting
- Lepší data quality pro reálný čas

## 🚠 Highlight: Lanovka Větruše!

První integrace lanovky v Home Assistant ČR! 
- **Stanice**: 12140 (Větruše) ↔ 12074 (OC Forum)
- **API typ**: CIS, Post ID: 999
- **Ikona**: mdi:gondola
- **Typ vozidla**: `funicular`

## 🎨 Technické vylepšení

- **Carrier attribute**: Identifikace dopravce (MD Teplice, DPMML, DPMÚL, DPCHJ)
- **Robust parsing**: Lepší handling různých API formátů
- **Encoding fixes**: Správné zobrazení českých znaků
- **Error resilience**: Graceful degradation při výpadcích API

## 📱 Jak upgradovat?

### HACS uživatelé:
1. HACS → Integrations → DUK Transport → Update
2. Restart Home Assistant
3. Enjoy multi-modal transport! 🎉

### Manuální instalace:
1. Stáhněte [v1.2.0 release](https://github.com/Peta01/ha-duk-transport/releases/tag/v1.2.0)
2. Přepište `custom_components/duk_transport/`
3. Restart HA

## 🧪 Testování lanovky

```yaml
# Konfigurace pro lanovku Větruše
ID stanice: 12140
API typ: CIS  
Post ID: 999
Interval: 300 (lanovka nejede často)
```

## 🤝 Poděkování

Speciální poděkování:
- **Wikipedii** za detailní dokumentaci trolejbusů v Ústí n.L.
- **Oficiálním stránkám** všech dopravních podniků
- **API Portabo** za vynikající dokumentaciju a přístupné endpointy
- **GitHub Copilot** 🤖 za neocenitelnou pomoc při vývoji a debugging
- **Home Assistant komunitě** za testování a feedback

## 🔮 Co dále?

- Real-time updates pro lanovku (když bude fungovat)
- Další města v kraji
- Integrační testy s různými verzemi HA
- Performance optimalizace

---

**Užijte si kompletní dopravní ekosystém Ústeckého kraje! 🚌🚎🚋🚆🚢🚠**

*Vytvořeno s 💚 pro Home Assistant komunitu • Powered by GitHub Copilot 🤖*