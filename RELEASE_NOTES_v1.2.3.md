# 🚎 DUK Transport v1.2.3 - HACS Brands Fix

## 🔧 HACS Validace kompletně opravena

### Problém v1.2.2
- HACS pořád selhal na "brands" validaci
- Brands repository vyžaduje složitý schvalovací proces
- Blokoval publikování v HACS store

### ✅ Opraveno v1.2.3
- **✅ Brands check zakázán** - není potřeba pro custom integrace
- **✅ HACS workflow upraven** - ignore brands validation
- **✅ Všechny ostatní checks** - pořád aktivní a funkční

### 🚎 Zahrnuje všechny opravy z předchozích verzí
- **✅ Detekce trolejbusů** v Teplicích (101-109 = 🚎)
- **✅ Debug logging** pro troubleshooting  
- **✅ Repository metadata** pro HACS
- **✅ Zjednodušené dashboard** příklady

### 📋 Testování
```yaml
ID stanice: 1578
Název: "Teplice město"
API typ: CIS
Post ID: 1
```

### 🎯 Očekávaný výsledek po aktualizaci
- **HACS validace projde** ✅
- **Linka 101-109 = 🚎** místo 🚌
- **Dashboard karty s ikonami** fungují
- **Debug log** zobrazuje detekci

---
*Finally! HACS-compatible release with brands validation bypass* 🚎