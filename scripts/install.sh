#!/bin/bash

echo "🚌 Instalace DUK Transport pro Home Assistant"
echo "============================================="

# Najít Home Assistant config složku
CONFIG_DIR=""
if [ -d "/config" ]; then
    CONFIG_DIR="/config"
elif [ -d "$HOME/.homeassistant" ]; then
    CONFIG_DIR="$HOME/.homeassistant"
elif [ -d "/usr/share/hassio/homeassistant" ]; then
    CONFIG_DIR="/usr/share/hassio/homeassistant"
else
    echo "❌ Nelze najít Home Assistant config složku"
    echo "Zadejte cestu ručně:"
    read -p "Cesta: " CONFIG_DIR
fi

echo "📁 Používám config složku: $CONFIG_DIR"

# Vytvořit custom_components složku
mkdir -p "$CONFIG_DIR/custom_components"

# Zkopírovat files
echo "📦 Kopíruji soubory..."
cp -r custom_components/duk_transport "$CONFIG_DIR/custom_components/"

echo "✅ Instalace dokončena!"
echo ""
echo "📋 Další kroky:"
echo "1. Restartujte Home Assistant"
echo "2. Přidejte integraci: Nastavení → Zařízení a služby → + Přidat"
echo "3. Vyhledejte 'Doprava Ústeckého kraje'"
echo "4. Zkopírujte dashboard z dashboards/ složky"
echo ""
echo "📖 Více informací v README.md"