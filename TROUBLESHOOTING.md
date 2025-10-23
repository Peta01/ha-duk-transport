# 🔧 Troubleshooting Guide

## ❌ Časté problémy a řešení

### 🚫 "API returned no data"
**Příčina**: Stanice neexistuje nebo je prázdná
**Řešení**: 
- Ověřte ID stanice na https://tabule.portabo.cz/
- Zkuste jiný Post ID (1 nebo 999)
- Zkuste jiný API typ (DUK/CIS)

### 🕐 "Lanovka nejede"
**Příčina**: Lanovka má provozní dobu
**Řešení**:
- Testujte od 9:00 do večera
- Zkontrolujte víkendy a svátky
- Používejte interval 300+ sekund

### 🚌 "Špatný typ vozidla"
**Příčina**: Neznámý dopravce nebo linka
**Řešení**:
- Zkontrolujte správný carrier v logu
- Přidejte issue s detaily stanice
- Použije se fallback (bus/train)

### 🔤 "Divné znaky v názvech"
**Příčina**: Encoding problém
**Řešení**:
- Restartujte HA po updatu
- Problém by měl být opravený ve v1.2.0
- Nahlaste pokud přetrvává

### ⚠️ "Entities neaktualizují"
**Příčina**: API limity nebo network issues
**Řešení**:
- Zvyšte interval aktualizace
- Zkontrolujte network connectivity
- Zkontrolujte HA logs

## 🔍 Debug informace

### Zapnutí logování
```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.duk_transport: debug
```

### Užitečné příkazy pro testování
```bash
# Test API přístupu
curl "https://tabule.portabo.cz/api/v1-tabule/duk/GetStationDeparturesWCount/2950/1/5/0"
curl "https://tabule.portabo.cz/api/v1-tabule/cis/GetStationDeparturesWCount/1578/1/5/0"
```

## 📋 Reporting bugů

Před nahlášením bugu:
1. ✅ Zkontrolujte že používáte nejnovější verzi
2. ✅ Zkuste default konfiguraci 
3. ✅ Zkontrolujte HA logs
4. ✅ Otestujte s mock data (ID: 12345)

Při nahlašování uveďte:
- HA verze
- DUK Transport verze  
- ID stanice
- API typ a Post ID
- Relevantní logy
- Screenshots

## 🚀 Performance tipy

### Optimální nastavení intervalů:
- **Regionální autobusy**: 120-180s
- **Městské trolejbusy/tramvaje**: 60-90s  
- **Vlaky**: 300-600s
- **Lodě**: 1800s (30min)
- **Lanovka**: 300-600s

### Memory/CPU optimalizace:
- Nenastavujte příliš krátké intervaly
- Limitujte max_departures na rozumné číslo (5-15)
- Restartujte HA po velkých updatech

## 🆘 Kontakt

- 🐛 **Bugy**: [GitHub Issues](https://github.com/Peta01/ha-duk-transport/issues)
- 💬 **Otázky**: [GitHub Discussions](https://github.com/Peta01/ha-duk-transport/discussions)  
- 📧 **Direct**: Přes GitHub profil

---
*Pokud vám tento guide nepomohl, neváhejte vytvořit issue! 🤝*

*Troubleshooting guide vytvořen s pomocí GitHub Copilot 🤖*