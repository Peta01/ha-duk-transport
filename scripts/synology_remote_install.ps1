# 🏠 Synology PowerShell Installation Script
# Pro vzdálené spuštění z Windows PC na Synology

param(
    [Parameter(Mandatory=$false)]
    [string]$SynologyIP,
    
    [Parameter(Mandatory=$false)]
    [string]$Username = "admin",
    
    [Parameter(Mandatory=$false)]
    [string]$ConfigPath
)

Write-Host "🏠 DUK Transport - Synology Remote Installation" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Green

# Získat IP adresu Synology
if (-not $SynologyIP) {
    $SynologyIP = Read-Host "Zadejte IP adresu vašeho Synology NAS"
}

Write-Host "🔍 Připojuji se k Synology: $SynologyIP" -ForegroundColor Yellow

# Funkce pro SCP upload
function Upload-ToSynology {
    param($LocalPath, $RemotePath)
    
    try {
        # Použití SCP (vyžaduje nainstalovaný OpenSSH nebo PuTTY)
        $scpCommand = "scp -r `"$LocalPath`" ${Username}@${SynologyIP}:`"$RemotePath`""
        Write-Host "📤 Uploaduji: $LocalPath -> $RemotePath" -ForegroundColor Yellow
        
        Invoke-Expression $scpCommand
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Upload úspěšný" -ForegroundColor Green
            return $true
        } else {
            Write-Host "❌ Upload se nezdařil" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Write-Host "❌ Chyba při uploadu: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Funkce pro SSH příkaz
function Invoke-SSHCommand {
    param($Command)
    
    try {
        $sshCommand = "ssh ${Username}@${SynologyIP} `"$Command`""
        Write-Host "🔧 Spouštím: $Command" -ForegroundColor Cyan
        
        $result = Invoke-Expression $sshCommand
        
        if ($LASTEXITCODE -eq 0) {
            return $result
        } else {
            Write-Host "❌ SSH příkaz selhal: $Command" -ForegroundColor Red
            return $null
        }
    }
    catch {
        Write-Host "❌ SSH chyba: $($_.Exception.Message)" -ForegroundColor Red
        return $null
    }
}

# Hlavní instalace
function Install-DUKTransport {
    Write-Host "📋 Zahajuji instalaci..." -ForegroundColor Green
    
    # 1. Najít Home Assistant config
    if (-not $ConfigPath) {
        Write-Host "🔍 Hledám Home Assistant konfiguraci..." -ForegroundColor Yellow
        
        $findCommand = "find /volume1 -name 'configuration.yaml' -type f 2>/dev/null | head -1"
        $configFile = Invoke-SSHCommand $findCommand
        
        if ($configFile) {
            $ConfigPath = Split-Path $configFile -Parent
            Write-Host "✅ Nalezena config složka: $ConfigPath" -ForegroundColor Green
        } else {
            Write-Host "❌ Nelze najít Home Assistant konfiguraci" -ForegroundColor Red
            $ConfigPath = Read-Host "Zadejte cestu ke config složce ručně"
        }
    }
    
    # 2. Vytvořit custom_components složku
    Write-Host "📁 Vytvářím custom_components složku..." -ForegroundColor Yellow
    $mkdirResult = Invoke-SSHCommand "mkdir -p `"$ConfigPath/custom_components`""
    
    # 3. Upload souborů
    if (Test-Path "custom_components\duk_transport") {
        Write-Host "📤 Uploaduji DUK Transport soubory..." -ForegroundColor Yellow
        
        $uploadSuccess = Upload-ToSynology "custom_components\duk_transport" "$ConfigPath/custom_components/"
        
        if (-not $uploadSuccess) {
            Write-Host "❌ Upload se nezdařil. Zkuste ruční metodu." -ForegroundColor Red
            Show-ManualInstructions
            return
        }
    } else {
        Write-Host "❌ Složka custom_components\duk_transport nenalezena" -ForegroundColor Red
        Write-Host "💡 Spusťte skript ze složky obsahující custom_components/" -ForegroundColor Blue
        return
    }
    
    # 4. Nastavit oprávnění
    Write-Host "🔧 Nastavuji oprávnění..." -ForegroundColor Yellow
    Invoke-SSHCommand "chown -R 1000:1000 `"$ConfigPath/custom_components/duk_transport/`""
    Invoke-SSHCommand "chmod -R 755 `"$ConfigPath/custom_components/duk_transport/`""
    
    # 5. Restart Home Assistant
    Write-Host "🔄 Restartuji Home Assistant..." -ForegroundColor Yellow
    $container = Invoke-SSHCommand "docker ps --format 'table {{.Names}}' | grep -i homeassistant | head -1"
    
    if ($container) {
        Write-Host "🐳 Restartuji Docker kontejner: $container" -ForegroundColor Cyan
        Invoke-SSHCommand "docker restart $container"
    } else {
        Write-Host "⚠️  Docker kontejner nenalezen - restartujte ručně" -ForegroundColor Yellow
    }
    
    # 6. Úspěch!
    Write-Host ""
    Write-Host "🎉 Instalace dokončena!" -ForegroundColor Green
    Write-Host "📋 Další kroky:" -ForegroundColor Cyan
    Write-Host "1. Otevřete Home Assistant na http://$SynologyIP:8123"
    Write-Host "2. Přejděte na: Nastavení → Zařízení a služby"
    Write-Host "3. Klikněte na: + PŘIDAT INTEGRACI"
    Write-Host "4. Vyhledejte: 'Doprava Ústeckého kraje'"
    Write-Host "5. Zadejte ID zastávky DUK"
    Write-Host ""
}

# Manuální instrukce jako fallback
function Show-ManualInstructions {
    Write-Host ""
    Write-Host "📖 Manuální instalace:" -ForegroundColor Blue
    Write-Host "1. Otevřete DSM webové rozhraní: http://$SynologyIP:5000"
    Write-Host "2. Spusťte File Station"
    Write-Host "3. Přejděte do složky s Home Assistant config"
    Write-Host "4. Vytvořte složku 'custom_components' (pokud neexistuje)"
    Write-Host "5. Uploadujte složku 'duk_transport' do 'custom_components/'"
    Write-Host "6. Restartujte Home Assistant"
    Write-Host ""
    Write-Host "📞 Nebo použijte WinSCP/FileZilla pro upload přes SFTP" -ForegroundColor Blue
}

# Kontrola předpokladů
function Test-Prerequisites {
    Write-Host "🔍 Kontroluji předpoklady..." -ForegroundColor Yellow
    
    # Test SSH spojení
    try {
        $sshTest = Invoke-SSHCommand "echo 'SSH OK'"
        if ($sshTest -eq "SSH OK") {
            Write-Host "✅ SSH spojení funguje" -ForegroundColor Green
            return $true
        }
    }
    catch {
        Write-Host "❌ SSH spojení selhalo" -ForegroundColor Red
        Write-Host "💡 Ujistěte se, že:" -ForegroundColor Blue
        Write-Host "   - SSH je povoleno na Synology (Control Panel → Terminal & SNMP)"
        Write-Host "   - Máte správné přihlašovací údaje"
        Write-Host "   - IP adresa je správná"
        Write-Host "   - OpenSSH je nainstalováno na tomto PC"
        return $false
    }
}

# Hlavní bod vstupu
if (Test-Prerequisites) {
    Install-DUKTransport
} else {
    Show-ManualInstructions
}

Write-Host ""
Write-Host "Více informací v SYNOLOGY_INSTALL.md" -ForegroundColor Blue