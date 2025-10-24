# 🚎 DUK Transport v1.2.2 - HACS Compatibility Fix

## 🔧 HACS Validace opravena

### Problém v1.2.1
- HACS validace selhala kvůli chybějícím metadatům
- Repository nebyl správně publikován v HACS store
- Uživatelé nemohli aktualizovat na opravenou verzi

### ✅ Opraveno v1.2.2
- **✅ Repository description** - přidán popis pro HACS
- **✅ GitHub topics** - přidány relevantní tags (home-assistant, hacs, transport, czech-republic)
- **✅ HACS kompatibilita** - release nyní projde validací

### 🚎 Zahrnuje všechny opravy z v1.2.1
- **Opravena detekce trolejbusů** v Teplicích (linky 101-109)
- **Debug logging** pro troubleshooting
- **Zjednodušené dashboard karty**
- **Rozšířená detekce** podle station_id

### 📋 Testování
```yaml
ID stanice: 1578
Název: "Teplice město"
API typ: CIS
Post ID: 1
```

### 🎯 Očekávaný výsledek
- Linka 101-109 = 🚎 trolejbus (místo 🚌 autobus)
- Debug log zobrazí detekci procesu
- Dashboard karty s správnými ikonami

---
*HACS-compatible release - Teplice trolleybus fix now available through HACS* 🚎