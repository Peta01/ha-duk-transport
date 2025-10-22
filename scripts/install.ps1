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