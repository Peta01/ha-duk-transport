# 🔧 Troubleshooting Guide

## ❓ Co to znamená? Co mám dělat?

### 📖 Průvodce chybovými hláškami

Tato sekce vysvětluje všechny chybové hlášky, které můžete v DUK Transport integraci potkat, a poskytuje jasná řešení.

---

#### 🔴 "Error communicating with API: [error details]"

**Co to znamená:**
Integrace se nemůže připojit k API serveru nebo server neodpovídá správně.

**Příčiny:**
1. Problémy se síťovým připojením
2. API server je dočasně nedostupný
3. Nesprávné ID zastávky
4. Nesprávný typ API (DUK vs CIS)
5. Nesprávný Post ID pro CIS API

**Co mám dělat:**
1. ✅ **Zkontrolujte internetové připojení** - Ujistěte se, že Home Assistant má přístup k internetu
2. ✅ **Ověřte ID zastávky** - Zkontrolujte, že vaše ID zastávky existuje v [seznamu stanic](STATIONS.md)
3. ✅ **Vyzkoušejte správný API typ:**
   - **DUK API** - pro regionální autobusy (linky 400+)
   - **CIS API** - pro městskou dopravu (trolejbusy, tramvaje, vlaky, lodě, lanovku)
4. ✅ **Pro CIS API zkuste jiný Post ID:**
   - Vyzkoušejte `1` nebo `999`
   - Některé stanice vyžadují specifický Post ID
5. ✅ **Zkuste testovací konfiguraci** s ID `12345` (mock data) - pokud funguje, problém je s vaší stanicí
6. ✅ **Zvyšte interval aktualizace** - zkuste nastavit na 120-180 sekund
7. ✅ **Počkejte 5-10 minut** - API může být dočasně nedostupné
8. ✅ **Zkontrolujte logy** - zapněte debug logging (viz níže)

**Příklad řešení:**
```yaml
# Pokud máte chybu s CIS API, zkuste:
stop_id: "1578"
api_type: "CIS"
post_id: "1"  # nebo zkuste "999"
update_interval: 120
```

---

#### 🟠 "DUK API returned status [kód] for stop [ID]"
#### 🟠 "CIS API returned status [kód]"

**Co to znamená:**
API server odpověděl, ale vrátil chybový kód místo dat.

**Běžné chybové kódy:**
- **404** - Zastávka neexistuje nebo nemá žádné odjezdy
- **500** - Chyba na straně serveru
- **503** - Server je přetížený nebo v údržbě

**Co mám dělat:**

**Pro kód 404:**
1. ✅ **Ověřte správné ID zastávky** - zkontrolujte [STATIONS.md](STATIONS.md)
2. ✅ **Zkuste jiný Post ID** (pro CIS) - `1` nebo `999`
3. ✅ **Zkuste druhý typ API** - pokud máte DUK, zkuste CIS a naopak
4. ✅ **Testujte API ručně:**
   ```bash
   # DUK API test
   curl "https://tabule.portabo.cz/api/v1-tabule/duk/GetStationDeparturesWCount/2950/0/5/0"
   
   # CIS API test
   curl "https://tabule.portabo.cz/api/v1-tabule/cis/GetStationDeparturesWCount/1578/1/5/0"
   ```

**Pro kód 500/503:**
1. ✅ **Počkejte a zkuste znovu** - server může být dočasně nedostupný
2. ✅ **Zvyšte interval aktualizace** na 180-300 sekund
3. ✅ **Nahlaste problém** pokud přetrvává dlouhodobě

---

#### 🟡 "Invalid DUK API response format"

**Co to znamená:**
API vrátilo data, ale nejsou ve správném formátu, který integrace očekává.

**Co mám dělat:**
1. ✅ **Restartujte Home Assistant**
2. ✅ **Zkontrolujte, že máte nejnovější verzi** integrace
3. ✅ **Zkuste jinou zastávku** - některé stanice mohou mít nekonzistentní data
4. ✅ **Zapněte debug logging** a nahlaste issue s konkrétní stanicí

---

#### 🟢 "Žádné odjezdy"

**Co to znamená:**
Integrace funguje, ale pro danou zastávku nejsou aktuálně žádné odjezdy.

**Příčiny:**
1. Stanice skutečně nemá žádné odjezdy v tuto chvíli
2. Je noc nebo časný ranní čas
3. Víkend nebo svátek (omezený provoz)
4. Lanovka nebo loď (specifická provozní doba)

**Co mám dělat:**
1. ✅ **Zkontrolujte čas** - zkuste testovat během provozní doby (6:00 - 22:00)
2. ✅ **Pro lanovku testujte 9:00-20:00** ve všední den
3. ✅ **Pro lodě testujte během turistické sezóny** (květen-září)
4. ✅ **Počkejte na další aktualizaci** - data se aktualizují podle nastaveného intervalu
5. ✅ **Zkuste nižší max_departures** - začněte s hodnotou 5

---

#### 🔵 "invalid_stop_id"

**Co to znamená:**
Zadali jste neplatné ID zastávky při konfiguraci.

**Co mám dělat:**
1. ✅ **ID zastávky musí být číselné** - např. `2950`, `1578`
2. ✅ **Najděte správné ID** v [STATIONS.md](STATIONS.md)
3. ✅ **Nepoužívejte písmena nebo speciální znaky**

**Správně:** ✅ `2950`, `1578`, `12140`  
**Špatně:** ❌ `Krupka`, `2950a`, `teplice`

---

#### ⚪ "Error parsing departure: [details]"

**Co to znamená:**
Jeden odjezd ze seznamu má špatný formát dat, ale ostatní fungují.

**Co mám dělat:**
1. ✅ **Ignorujte** - integrace přeskočí špatný odjezd a zobrazí ostatní
2. ✅ **Není třeba nic měnit** - běžná situace při problémech s daty od dopravce
3. ✅ **Pokud je to časté**, nahlaste issue s ID stanice

---

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
- Ujistěte se, že máte nejnovější verzi integrace
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