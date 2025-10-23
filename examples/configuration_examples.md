# 📋 Příklady konfigurace DUK Transport

## 🚎 Trolejbusy MD Teplice
```yaml
# Konfigurace přes UI:
ID stanice: 1578
Název: "Teplice město" 
API typ: CIS
Post ID: 1  
Interval: 60
Max odjezdy: 10

# Očekávané linky: 101-109 (trolejbusy), 110+119 (autobusy)
# Dopravce: MD Teplice
```

## 🚋 Tramvaje Most-Litvínov  
```yaml
# Konfigurace přes UI:
ID stanice: 1967
Název: "Most-Litvínov"
API typ: CIS
Post ID: 999
Interval: 120
Max odjezdy: 8

# Očekávané linky: 1-4 (denní tramvaje), 40 (noční)
# Dopravce: DPMML
```

## 🚠 Lanovka Větruše
```yaml
# Konfigurace přes UI:
ID stanice: 12140
Název: "Ústí n.L. - Větruše"  
API typ: CIS
Post ID: 999
Interval: 300  # Lanovka nejede často
Max odjezdy: 5

# Očekávaná linka: 901 (funicular)
# Dopravce: DPMÚL
# Pozn: Funguje od 9:00!
```

## 🚎 Trolejbusy Ústí nad Labem
```yaml  
# Konfigurace přes UI:
ID stanice: [najít vhodnou stanici]
Název: "Ústí n.L. centrum"
API typ: CIS  
Post ID: 999
Interval: 90
Max odjezdy: 10

# Očekávané linky: 70-88 (denní), 43+46 (noční)
# Dopravce: DPMÚL
```

## 🚎 Trolejbusy Chomutov-Jirkov
```yaml
# Konfigurace přes UI:
ID stanice: [najít vhodnou stanici]
Název: "Chomutov centrum"
API typ: CIS
Post ID: 999
Interval: 90  
Max odjezdy: 10

# Očekávané linky: 340-353 (trolejbusy), 302-317 (autobusy)
# Dopravce: DPCHJ
```

## 🚢 Labská plavební
```yaml
# Konfigurace přes UI:
ID stanice: 2427
Název: "Labská plavební"
API typ: CIS
Post ID: 999
Interval: 1800  # Lodě jezdí zřídka
Max odjezdy: 3

# Očekávaná linka: 891 (ship)
# Dopravce: Labská plavební linka
```

## 🚌 Regionální autobusy (DUK)
```yaml
# Konfigurace přes UI:
ID stanice: 2950
Název: "Krupka, ke Kateřině"
API typ: DUK
Post ID: 1
Interval: 120
Max odjezdy: 10

# Očekávané linky: 480, 484, 430, 485 atd. (autobusy)
# Různí dopravci: Doprava Teplice, ČSAD atd.
```

## 🧪 Test konfigurace
```yaml
# Konfigurace přes UI:
ID stanice: 12345
Název: "Test stanice"
API typ: DUK
Post ID: 1
Interval: 60
Max odjezdy: 10

# Vygeneruje mock data pro testování
```

## 📱 Dashboard příklady

### Základní karta
```yaml
type: entities
title: 🚎 Teplice trolejbusy
entities:
  - entity: sensor.duk_transport_teplice_mesto
    name: Aktuální stav
```

### Odjezdová tabula
```yaml
type: markdown
title: 📋 Odjezdy - {{ states('sensor.duk_transport_teplice_mesto') }}
content: |
  {% set departures = state_attr('sensor.duk_transport_teplice_mesto', 'departures') or [] %}
  {% if departures %}
  | 🚎 | Linka | Směr | Čas | ⏱️ |
  |---|-------|------|-----|-----|
  {% for dep in departures %}
  | {% if dep.vehicle_type == 'trolleybus' %}🚎{% elif dep.vehicle_type == 'tram' %}🚋{% elif dep.vehicle_type == 'funicular' %}🚠{% elif dep.vehicle_type == 'ship' %}🚢{% else %}🚌{% endif %} | **{{ dep.line }}** | {{ dep.destination }} | {{ dep.departure_time }} | {% if dep.delay > 0 %}+{{ dep.delay }}m{% else %}⏰{% endif %} |
  {% endfor %}
  
  *Aktualizováno: {{ as_timestamp(states.sensor.duk_transport_teplice_mesto.last_updated) | timestamp_custom('%H:%M') }}*
  {% else %}
  Žádné odjezdy k dispozici
  {% endif %}
```

### Conditional card podle typu vozidla
```yaml
type: conditional
conditions:
  - entity: sensor.duk_transport_vetruse_lanovka
    state_not: "unavailable"
card:
  type: entities
  title: 🚠 Lanovka Větruše
  entities:
    - entity: sensor.duk_transport_vetruse_lanovka
      icon: mdi:gondola
```