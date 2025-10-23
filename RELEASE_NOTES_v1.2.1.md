# 🚎 DUK Transport v1.2.1 - Teplice Trolleybus Fix

## 🐛 Oprava chyby detekce typu vozidla

### Problém
- Linka 101 v Teplicích se zobrazovala jako autobus (🚌) místo trolejbus (🚎)
- API vrací nesprávný vehicle_type pro trolejbusy MD Teplice

### ✅ Oprava
- **Rozšířena detekce typu vozidla** pro Teplice stanici (ID: 1578)
- **Přidána detekce podle ID stanice** kromě carrier
- **Debug logging** pro troubleshooting

### 🔧 Technické změny
- Metoda `_determine_vehicle_type()` nyní používá stop_id
- Logika pro Teplice: linky 101-109 = trolejbus, 110+119 = autobus
- Fallback detekce podle názvu stanice

### 🚎 Co je opraveno
- **Linka 101-109** v Teplicích = 🚎 trolejbus
- **Linka 110, 119** v Teplicích = 🚌 autobus  
- **Dashboard karty** nyní zobrazí správné ikony

### 📋 Testování
Použijte konfiguraci:
```yaml
ID stanice: 1578
Název: "Teplice město"
API typ: CIS
Post ID: 1
```

### 🎯 Další vylepšení
- Zjednodušené příklady dashboard karet
- Odstraněné duplicitní MD soubory
- Univerzální Flex Table karta pro všechny typy vozidel

---
*Fix #trolejbus-detection - Teplice trolleybus lines now correctly identified* 🚎