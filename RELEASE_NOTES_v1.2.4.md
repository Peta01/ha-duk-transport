# 🔍 DUK Transport v1.2.4 - Debug Release

## 🐛 Rozšířený debug pro Teplice problém

### Objevený problém
- **Linky 101-108 jsou v datech** ✅
- **Dopravce "MD Teplice"** je správný ✅  
- **Ale `vehicle_type: bus`** místo `trolleybus` ❌
- **Debug log se nespouštěl** - potřebujeme víc informací

### 🔍 Rozšířený debug v1.2.4
- **Debug pro VŠECHNY linky** z Teplice (ne jen 101-109)
- **Ukáže přesně** jaká data se zpracovávají
- **Odhalí** proč selže detekce trolejbusu
- **Zachová** původní debug pro linky 101-109

### 📊 Debug výstup po aktualizaci
```
DEBUG [custom_components.duk_transport.api] Teplice analysis - Linka: 106, Dopravce: 'MD Teplice', Stanice: 'teplice,benešovo náměstí', ID: 1578
DEBUG [custom_components.duk_transport.api] Teplice trolejbus detection - Linka: 106, Dopravce: 'MD Teplice', Stanice: 'teplice,benešovo náměstí', ID: 1578
```

### 🎯 Očekávané zjištění
- Uvidíme **přesná data** která kód dostává
- Zjistíme **proč se nespouští** teplice detekce
- **Opravíme logiku** na základě skutečných dat

---
*Debug release to track down Teplice trolleybus detection issue* 🔍