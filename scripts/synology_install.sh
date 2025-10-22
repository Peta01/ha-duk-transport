#!/bin/bash

# 🏠 Synology Installation Script for DUK Transport
# Skript pro instalaci DUK Transport na Synology NAS

echo "🏠 DUK Transport - Synology Installation"
echo "======================================="

# Funkce pro nalezení Home Assistant config složky
find_ha_config() {
    echo "🔍 Hledám Home Assistant konfiguraci..."
    
    # Možné cesty na Synology
    POSSIBLE_PATHS=(
        "/volume1/docker/homeassistant/config"
        "/volume1/@docker/containers/*/volume"
        "/volume1/vm/homeassistant/config"
        "/volume1/homes/homeassistant/config"
    )
    
    for path in "${POSSIBLE_PATHS[@]}"; do
        if [ -f "$path/configuration.yaml" ]; then
            echo "✅ Nalezena config složka: $path"
            CONFIG_DIR="$path"
            return 0
        fi
    done
    
    # Pokud nic nenalezeno, zkus find
    echo "🔍 Prohledávám všechny svazky..."
    FOUND=$(find /volume* -name "configuration.yaml" -type f 2>/dev/null | head -1)
    
    if [ -n "$FOUND" ]; then
        CONFIG_DIR=$(dirname "$FOUND")
        echo "✅ Nalezena config složka: $CONFIG_DIR"
        return 0
    fi
    
    return 1
}

# Kontrola oprávnění
check_permissions() {
    if [ "$EUID" -ne 0 ]; then
        echo "⚠️  Skript není spuštěn jako root"
        echo "💡 Zkuste: sudo $0"
        echo "💡 Nebo se přihlaste jako admin přes SSH"
    fi
}

# Hlavní instalace
install_duk() {
    echo "📦 Instaluji DUK Transport..."
    
    # Vytvořit custom_components složku
    mkdir -p "$CONFIG_DIR/custom_components"
    
    # Zkontrolovat zda existuje source složka
    if [ ! -d "./custom_components/duk_transport" ]; then
        echo "❌ Zdrojová složka ./custom_components/duk_transport nenalezena"
        echo "💡 Spusťte skript ze složky obsahující custom_components/"
        exit 1
    fi
    
    # Zkopírovat soubory
    cp -r "./custom_components/duk_transport" "$CONFIG_DIR/custom_components/"
    
    # Nastavit oprávnění
    echo "🔧 Nastavuji oprávnění..."
    chown -R 1000:1000 "$CONFIG_DIR/custom_components/duk_transport/" 2>/dev/null || {
        echo "⚠️  Nepodařilo se změnit vlastníka na 1000:1000"
        echo "💡 Zkuste ručně: chown -R 1000:1000 $CONFIG_DIR/custom_components/duk_transport/"
    }
    
    chmod -R 755 "$CONFIG_DIR/custom_components/duk_transport/"
    
    echo "✅ Soubory zkopírovány a oprávnění nastavena"
}

# Ověření instalace
verify_installation() {
    echo "🔍 Ověřuji instalaci..."
    
    REQUIRED_FILES=(
        "__init__.py"
        "manifest.json" 
        "config_flow.py"
        "const.py"
        "api.py"
        "sensor.py"
    )
    
    for file in "${REQUIRED_FILES[@]}"; do
        if [ ! -f "$CONFIG_DIR/custom_components/duk_transport/$file" ]; then
            echo "❌ Chybí soubor: $file"
            return 1
        fi
    done
    
    echo "✅ Všechny potřebné soubory jsou na místě"
    return 0
}

# Restart Home Assistant
restart_ha() {
    echo "🔄 Restartuji Home Assistant..."
    
    # Pokus o restart Docker kontejneru
    CONTAINER=$(docker ps --format "table {{.Names}}" | grep -i homeassistant | head -1)
    
    if [ -n "$CONTAINER" ]; then
        echo "🐳 Nalezen Docker kontejner: $CONTAINER"
        docker restart "$CONTAINER"
        echo "✅ Kontejner restartován"
    else
        echo "⚠️  Docker kontejner nenalezen"
        echo "💡 Restartujte Home Assistant ručně přes webové rozhraní"
        echo "💡 Nebo použijte: docker restart [název_kontejneru]"
    fi
}

# Hlavní tok
main() {
    check_permissions
    
    if find_ha_config; then
        install_duk
        
        if verify_installation; then
            restart_ha
            
            echo ""
            echo "🎉 Instalace dokončena!"
            echo "📋 Další kroky:"
            echo "1. Otevřete Home Assistant webové rozhraní"
            echo "2. Přejděte na: Nastavení → Zařízení a služby"
            echo "3. Klikněte na: + PŘIDAT INTEGRACI"
            echo "4. Vyhledejte: 'Doprava Ústeckého kraje'"
            echo "5. Zadejte ID zastávky (nebo použijte 12345 pro testování)"
            echo ""
            echo "📖 Více informací v README.md"
            
        else
            echo "❌ Instalace se nezdařila - chybí soubory"
            exit 1
        fi
    else
        echo "❌ Nelze najít Home Assistant konfiguraci"
        echo "💡 Zadejte cestu ručně:"
        read -p "Cesta ke config složce: " CONFIG_DIR
        
        if [ -f "$CONFIG_DIR/configuration.yaml" ]; then
            install_duk
            verify_installation
        else
            echo "❌ Neplatná cesta - configuration.yaml nenalezen"
            exit 1
        fi
    fi
}

# Spustit hlavní funkci
main "$@"