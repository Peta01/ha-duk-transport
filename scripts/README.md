# 🔧 Instalační skripty pro DUK Transport

Tato složka obsahuje pomocné skripty pro snadnou instalaci a konfiguraci.

## install.sh (Linux/macOS)

```bash
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
```

## install.ps1 (Windows PowerShell)

```powershell
Write-Host "🚌 Instalace DUK Transport pro Home Assistant" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Green

# Najít Home Assistant config složku
$ConfigDir = ""
$PossibleDirs = @(
    "$env:APPDATA\.homeassistant",
    "C:\ProgramData\homeassistant", 
    "$env:USERPROFILE\.homeassistant"
)

foreach ($Dir in $PossibleDirs) {
    if (Test-Path $Dir) {
        $ConfigDir = $Dir
        break
    }
}

if (-not $ConfigDir) {
    Write-Host "❌ Nelze najít Home Assistant config složku" -ForegroundColor Red
    $ConfigDir = Read-Host "Zadejte cestu ručně"
}

Write-Host "📁 Používám config složku: $ConfigDir" -ForegroundColor Yellow

# Vytvořit custom_components složku
$CustomDir = Join-Path $ConfigDir "custom_components"
if (-not (Test-Path $CustomDir)) {
    New-Item -ItemType Directory -Path $CustomDir -Force
}

# Zkopírovat soubory
Write-Host "📦 Kopíruji soubory..." -ForegroundColor Yellow
$SourceDir = "custom_components\duk_transport"
$DestDir = Join-Path $CustomDir "duk_transport"

Copy-Item -Path $SourceDir -Destination $DestDir -Recurse -Force

Write-Host "✅ Instalace dokončena!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Další kroky:" -ForegroundColor Cyan
Write-Host "1. Restartujte Home Assistant"
Write-Host "2. Přidejte integraci: Nastavení → Zařízení a služby → + Přidat"
Write-Host "3. Vyhledejte 'Doprava Ústeckého kraje'"
Write-Host "4. Zkopírujte dashboard z dashboards\ složky"
Write-Host ""
Write-Host "📖 Více informací v README.md" -ForegroundColor Blue
```

## Použití skriptů

### Linux/macOS:
```bash
chmod +x install.sh
./install.sh
```

### Windows:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\install.ps1
```