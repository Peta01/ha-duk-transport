# 🎨 Complete Dashboard Layout

Kompletní dashboard layout pro DUK Transport, který můžete rovnou použít jako nový dashboard v Home Assistant.

## 📋 Dashboard YAML (kompletní)

```yaml
title: 🚌 Doprava Ústeckého kraje
path: duk-transport
icon: mdi:bus-multiple
badges: []
cards:
  # Hlavní header
  - type: markdown
    content: |
      # 🚌 Doprava Ústeckého kraje
      **Multi-modal transport integration pro Home Assistant**
      
      ---

  # Rychlý přehled všech stanic
  - type: horizontal-stack
    cards:
      - type: custom:button-card
        entity: sensor.duk_transport_teplice_mesto
        name: "🚎 Teplice"
        show_state: true
        state_display: |
          [[[
            const count = entity.attributes.count || 0;
            return `${count} odjezdů`;
          ]]]
        styles:
          card:
            - background: "#1976d2"
            - color: white
            - border-radius: 10px
            - height: 80px
          name:
            - font-size: 14px
            - font-weight: bold
        tap_action:
          action: navigate
          navigation_path: "#teplice"

      - type: custom:button-card
        entity: sensor.duk_transport_most_litvínov
        name: "🚋 Most"
        show_state: true
        state_display: |
          [[[
            const count = entity.attributes.count || 0;
            return `${count} odjezdů`;
          ]]]
        styles:
          card:
            - background: "#388e3c"
            - color: white
            - border-radius: 10px
            - height: 80px
          name:
            - font-size: 14px
            - font-weight: bold

      - type: custom:button-card
        entity: sensor.duk_transport_vetruse_lanovka
        name: "🚠 Ústí"
        show_state: true
        state_display: |
          [[[
            const count = entity.attributes.count || 0;
            return `${count} odjezdů`;
          ]]]
        styles:
          card:
            - background: "#f57c00"
            - color: white
            - border-radius: 10px
            - height: 80px
          name:
            - font-size: 14px
            - font-weight: bold

      - type: custom:button-card
        entity: sensor.duk_transport_chomutov_centrum
        name: "🚎 Chomutov"
        show_state: true
        state_display: |
          [[[
            const count = entity.attributes.count || 0;
            return `${count} odjezdů`;
          ]]]
        styles:
          card:
            - background: "#7b1fa2"
            - color: white
            - border-radius: 10px
            - height: 80px
          name:
            - font-size: 14px
            - font-weight: bold

  # Separator
  - type: divider

  # Main transport cards
  - type: vertical-stack
    cards:
      # Teplice trolejbusy
      - type: anchor
        anchor: teplice
      - type: markdown
        content: |
          # 🚎 Teplice - MD Teplice
          **Trolejbusy a autobusy**
      
      - type: conditional
        conditions:
          - entity: sensor.duk_transport_teplice_mesto
            state_not: "Žádné odjezdy"
        card:
          type: markdown
          content: |
            {% set departures = state_attr('sensor.duk_transport_teplice_mesto', 'departures') or [] %}
            {% set trolley_deps = departures | selectattr('vehicle_type', 'equalto', 'trolleybus') | list %}
            {% set bus_deps = departures | selectattr('vehicle_type', 'equalto', 'bus') | list %}
            
            ## 🚎 Trolejbusy (parciální linky 101-109)
            {% if trolley_deps %}
            | Linka | Směr | Čas | Status | Nástupiště |
            |-------|------|-----|--------|------------|
            {% for dep in trolley_deps[:5] %}
            | **{{ dep.line }}** | {{ dep.destination }} | {{ dep.departure_time }} | {% if dep.delay > 0 %}🟡 +{{ dep.delay }}m{% else %}🟢 načas{% endif %} | {{ dep.platform or '-' }} |
            {% endfor %}
            {% else %}
            *Momentálně žádné trolejbusy*
            {% endif %}
            
            ## 🚌 Autobusy (linky 110, 119)
            {% if bus_deps %}
            | Linka | Směr | Čas | Status | Nástupiště |
            |-------|------|-----|--------|------------|
            {% for dep in bus_deps[:3] %}
            | **{{ dep.line }}** | {{ dep.destination }} | {{ dep.departure_time }} | {% if dep.delay > 0 %}🟡 +{{ dep.delay }}m{% else %}🟢 načas{% endif %} | {{ dep.platform or '-' }} |
            {% endfor %}
            {% else %}
            *Momentálně žádné autobusy*
            {% endif %}
            
            ---
            *Aktualizováno: {{ as_timestamp(states['sensor.duk_transport_teplice_mesto'].last_updated) | timestamp_custom('%H:%M:%S') }}*

      - type: conditional
        conditions:
          - entity: sensor.duk_transport_teplice_mesto
            state: "Žádné odjezdy"
        card:
          type: markdown
          content: |
            ## ⚠️ Teplice - žádné ofjezdy
            **Konfigurace:** API typ: CIS, Post ID: 1, Stanice: 1578

  # Divider
  - type: divider

  # Most-Litvínov tramvaje  
  - type: vertical-stack
    cards:
      - type: markdown
        content: |
          # 🚋 Most-Litvínov - DPMML
          **Tramvajová síť**
      
      - type: conditional
        conditions:
          - entity: sensor.duk_transport_most_litvínov
            state_not: "Žádné ofjezdy"
        card:
          type: markdown
          content: |
            {% set departures = state_attr('sensor.duk_transport_most_litvínov', 'departures') or [] %}
            {% if departures %}
            ## 🚋 Aktuální odjezdy tramvají
            | Linka | Směr | Čas | Status | Dopravce |
            |-------|------|-----|--------|----------|
            {% for dep in departures[:6] %}
            | **{{ dep.line }}** | {{ dep.destination }} | {{ dep.departure_time }} | {% if dep.delay > 0 %}🟡 +{{ dep.delay }}m{% else %}🟢 načas{% endif %} | {{ dep.carrier }} |
            {% endfor %}
            
            **Legenda linek:**
            - **1-4**: Denní tramvajové linky
            - **40**: Noční tramvajová linka
            
            ---
            *Aktualizováno: {{ as_timestamp(states['sensor.duk_transport_most_litvínov'].last_updated) | timestamp_custom('%H:%M:%S') }}*
            {% endif %}

  # Divider
  - type: divider

  # Ústí nad Labem - speciální sekce pro lanovku
  - type: vertical-stack
    cards:
      - type: markdown
        content: |
          # 🚠 Ústí nad Labem - DPMÚL
          **Lanovka Větruše a trolejbusy**

      # Lanovka highlight card
      - type: picture-elements
        image: /local/images/transparent.png
        elements:
          - type: custom:button-card
            entity: sensor.duk_transport_vetruse_lanovka
            name: "🚠 LANOVKA VĚTRUŠE"
            show_state: true
            state_display: |
              [[[
                const deps = entity.attributes.departures || [];
                const next = deps[0];
                if (next) {
                  const delay = next.delay > 0 ? ` (+${next.delay}m)` : '';
                  return `${next.destination} • ${next.departure_time}${delay}`;
                }
                return 'Momentálně nejede - zkontrolujte provozní dobu';
              ]]]
            styles:
              card:
                - background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
                - border-radius: 20px
                - color: white
                - height: 120px
                - box-shadow: "0 8px 16px rgba(0,0,0,0.3)"
                - font-size: 16px
              name:
                - font-size: 20px
                - font-weight: bold
                - margin-bottom: 10px
              state:
                - font-size: 14px
                - opacity: 0.9
                - white-space: pre-line
            tap_action:
              action: more-info
            style:
              top: 50%
              left: 50%
              width: 90%
              height: 90%

      # Trolejbusy Ústí
      - type: conditional
        conditions:
          - entity: sensor.duk_transport_usti_centrum
            state_not: "unavailable"
        card:
          type: markdown
          content: |
            ## 🚎 Trolejbusy DPMÚL
            {% set departures = state_attr('sensor.duk_transport_usti_centrum', 'departures') or [] %}
            {% if departures %}
            | Linka | Směr | Čas | Status |
            |-------|------|-----|--------|
            {% for dep in departures[:5] %}
            | **{{ dep.line }}** | {{ dep.destination }} | {{ dep.departure_time }} | {% if dep.delay > 0 %}🟡 +{{ dep.delay }}m{% else %}🟢 načas{% endif %} |
            {% endfor %}
            
            **Trolejbusové linky:** 70-88 (denní), 43+46 (noční)
            {% else %}
            *Momentálně žádné trolejbusy*
            {% endif %}

  # Divider  
  - type: divider

  # Chomutov-Jirkov
  - type: vertical-stack
    cards:
      - type: markdown
        content: |
          # 🚎 Chomutov-Jirkov - DPCHJ
          **Trolejbusy a autobusy**
      
      - type: conditional
        conditions:
          - entity: sensor.duk_transport_chomutov_centrum
            state_not: "unavailable"
        card:
          type: markdown
          content: |
            {% set departures = state_attr('sensor.duk_transport_chomutov_centrum', 'departures') or [] %}
            {% set trolley_deps = departures | selectattr('vehicle_type', 'equalto', 'trolleybus') | list %}
            {% set bus_deps = departures | selectattr('vehicle_type', 'equalto', 'bus') | list %}
            
            ## 🚎 Trolejbusy DPCHJ (340-353)
            {% if trolley_deps %}
            | Linka | Směr | Čas | Status |
            |-------|------|-----|--------|
            {% for dep in trolley_deps[:4] %}
            | **{{ dep.line }}** | {{ dep.destination }} | {{ dep.departure_time }} | {% if dep.delay > 0 %}🟡 +{{ dep.delay }}m{% else %}🟢 načas{% endif %} |
            {% endfor %}
            {% else %}
            *Momentálně žádné trolejbusy*
            {% endif %}
            
            ## 🚌 Autobusy DPCHJ (302-317)
            {% if bus_deps %}
            | Linka | Směr | Čas | Status |
            |-------|------|-----|--------|
            {% for dep in bus_deps[:3] %}
            | **{{ dep.line }}** | {{ dep.destination }} | {{ dep.departure_time }} | {% if dep.delay > 0 %}🟡 +{{ dep.delay }}m{% else %}🟢 načas{% endif %} |
            {% endfor %}
            {% else %}
            *Momentálně žádné autobusy*
            {% endif %}

  # Divider
  - type: divider

  # Regionální spojení a speciální doprava
  - type: horizontal-stack
    cards:
      # Regionální autobusy
      - type: markdown
        content: |
          ## 🚌 Regionální autobusy
          **DUK API - mezi městy**
          
          {% set departures = state_attr('sensor.duk_transport_krupka_katerina', 'departures') or [] %}
          {% if departures %}
          ### Aktuální spoje:
          {% for dep in departures[:3] %}
          **{{ dep.line }}** → {{ dep.destination }}  
          ⏰ {{ dep.departure_time }} {% if dep.delay > 0 %}(+{{ dep.delay }}m){% endif %}
          {% endfor %}
          {% else %}
          *Žádné regionální spoje*
          {% endif %}

      # Labská plavební
      - type: markdown
        content: |
          ## ⛴️ Labská plavební
          **Lodní doprava po Labi**
          
          {% set departures = state_attr('sensor.duk_transport_labska_plavebni', 'departures') or [] %}
          {% if departures %}
          ### Aktuální spoje:
          {% for dep in departures[:2] %}
          **{{ dep.line }}** → {{ dep.destination }}  
          ⏰ {{ dep.departure_time }} {% if dep.delay > 0 %}(+{{ dep.delay }}m){% endif %}
          {% endfor %}
          {% else %}
          *Žádné lodní spoje*  
          *Sezona: duben - říjen*
          {% endif %}

  # Footer
  - type: divider
  - type: markdown
    content: |
      ---
      
      ## 📱 DUK Transport Integration
      
      **Supported transport:**
      🚌 Buses • 🚎 Trolleybuses • 🚋 Trams • 🚆 Trains • ⛴️ Ships • 🚠 Funicular
      
      **Cities covered:**
      Teplice • Most-Litvínov • Ústí nad Labem • Chomutov-Jirkov
      
      ---
      
      💡 **Tips:**
      - Lanovka Větruše jezdí od 9:00
      - Trolejbusy mají parciální provoz
      - CIS API pro městskou dopravu, DUK API pro regionální
      
      🔧 **Config examples:** [GitHub](https://github.com/Peta01/ha-duk-transport/blob/master/examples/)
      
      *Integration powered by GitHub Copilot 🤖*
```

## 🎨 Stylování (volitelné)

Pokud chcete přidat custom CSS, vytvořte soubor `/config/www/duk-transport.css`:

```css
/* DUK Transport Custom Styles */
.transport-card {
  transition: all 0.3s ease;
  border-radius: 15px !important;
}

.transport-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0,0,0,0.2);
}

.delay-indicator {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 5px;
}

.on-time { background: #4caf50; }
.minor-delay { background: #ff9800; }
.major-delay { background: #f44336; }

/* Lanovka special styling */
.funicular-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
  color: white !important;
}

/* Transport type colors */
.trolleybus-card { background: #2196f3; }
.tram-card { background: #4caf50; }
.bus-card { background: #ff9800; }
.train-card { background: #9c27b0; }
.ship-card { background: #00bcd4; }
```

A pak přidejte do dashboard:

```yaml
# Na začátek dashboard YAML
resources:
  - url: /local/duk-transport.css
    type: css
```

## 📋 Potřebné entity

Pro fungování tohoto dashboardu budete potřebovat tyto entity (změňte názvy podle svých potřeb):

```yaml
# Příklady entity názvů:
- sensor.duk_transport_teplice_mesto         # MD Teplice trolejbusy
- sensor.duk_transport_most_litvínov         # DPMML tramvaje  
- sensor.duk_transport_vetruse_lanovka       # DPMÚL lanovka
- sensor.duk_transport_usti_centrum          # DPMÚL trolejbusy
- sensor.duk_transport_chomutov_centrum      # DPCHJ trolejbusy
- sensor.duk_transport_krupka_katerina       # DUK regionální
- sensor.duk_transport_labska_plavebni       # Lodní doprava
```

## 🚀 Jak použít:

1. **Zkopírujte YAML** do nového dashboardu v HA
2. **Upravte názvy entit** podle vašich sensorů
3. **Přidejte obrázky** do `/config/www/images/` (volitelné) 
4. **Přidejte CSS** pro lepší styling (volitelné)
5. **Otestujte** a upravte podle potřeb

**🎯 Výsledek: Kompletní profesionální dashboard pro celý dopravní systém Ústeckého kraje!**

*Complete dashboard layout vytvořen s pomocí GitHub Copilot 🤖*