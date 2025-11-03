# 🚀 Rychlá instalace DUK Transport

## 📦 Co potřebujete

- Home Assistant 2023.1 nebo novější
- Přístup k internetu pro API volání
- ID zastávky DUK - najděte v [seznamu stanic](../STATIONS.md) nebo použijte `12345` pro testování

## 🏠 Pro Synology NAS (VM)

**👉 Pokud máte HA na Synology, použijte:** `SYNOLOGY_INSTALL.md`

## ⚡ Rychlé kroky (standardní instalace)

### 1. Instalace (2 minuty)

```bash
# Zkopírujte složku do Home Assistant
cp -r custom_components/duk_transport /config/custom_components/

# Restartujte Home Assistant
```

### 2. Konfigurace (1 minuta)

1. **Nastavení** → **Zařízení a služby** → **+ PŘIDAT INTEGRACI**
2. Vyhledejte **"Doprava Ústeckého kraje"**
3. Zadejte:
   - ID zastávky: Najděte v [seznamu stanic](../STATIONS.md) nebo použijte `12345` pro test
   - Název: `Moje zastávka`
   - Interval: `60` sekund

### 3. Dashboard (3 minuty)

Přidejte do Lovelace:

```yaml
# Základní karta
- type: entities
  title: "🚌 Odjezdy DUK"
  entities:
    - sensor.duk_transport_moje_zastávka

# Tabulka odjezdů  
- type: markdown
  content: |
    {% set deps = state_attr('sensor.duk_transport_moje_zastávka', 'departures') or [] %}
    | Linka | Kam | Čas | Zpoždění |
    |-------|-----|-----|----------|
    {% for d in deps[:5] %}
    | {{d.line}} | {{d.destination}} | {{d.departure_time}} | {{d.delay}}min |
    {% endfor %}
```

## ✅ Test

Po instalaci byste měli vidět:
- Senzor `sensor.duk_transport_moje_zastávka`
- Mock data s testovacími odjezdy
- Funkční dashboard s odjezdovou tabulí

## 🆘 Problémy?

- **Nevidím integraci**: Restartujte HA a zkontrolujte složku `custom_components`
- **Žádná data**: Zkontrolujte ID zastávky nebo použijte mock data
- **Chyby**: Zapněte debug logy v `configuration.yaml`

## 📞 Podpora

- GitHub Issues pro chyby
- Home Assistant Community Forum pro otázky
- README.md pro detailní dokumentaci

---
**Hotovo za 6 minut! 🎉**