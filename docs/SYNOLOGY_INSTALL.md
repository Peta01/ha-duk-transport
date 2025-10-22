# 🏠 Instalace DUK Transport na Synology NAS (VM)

## 📋 Možnosti instalace

### 🎯 Metoda 1: Přes File Station (Nejjednodušší)

1. **Otevřete File Station** na vašem Synology
2. **Přejděte do VM složky** s Home Assistant config
   - Obvykle: `/volume1/docker/homeassistant/config/`
   - Nebo: `/volume1/vm/homeassistant/config/`
3. **Vytvořte složku** `custom_components` (pokud neexistuje)
4. **Uploadujte složku** `duk_transport` z tohoto projektu do `custom_components/`
5. **Restartujte Home Assistant** přes webové rozhraní

### 🔧 Metoda 2: Přes SSH

```bash
# 1. Připojte se k Synology přes SSH
ssh admin@[IP_VASI_SYNOLOGY]

# 2. Najděte Home Assistant config složku
find /volume1 -name "configuration.yaml" -type f 2>/dev/null

# 3. Přejděte do config složky (nahraďte cestou z kroku 2)
cd /volume1/docker/homeassistant/config

# 4. Vytvořte custom_components složku
mkdir -p custom_components

# 5. Uploadujte soubory (viz další sekce)
```

### 📤 Metoda 3: Přes SCP/SFTP

```bash
# Z vašeho lokálního PC uploadujte soubory
scp -r custom_components/duk_transport admin@[SYNOLOGY_IP]:/volume1/docker/homeassistant/config/custom_components/

# Nebo použijte SFTP client jako WinSCP, FileZilla
```

### 🐳 Metoda 4: Přes Docker Volume

Pokud používáte Docker kontejner:

```bash
# Najděte Home Assistant kontejner
docker ps | grep homeassistant

# Zkopírujte soubory do kontejneru
docker cp custom_components/duk_transport [CONTAINER_ID]:/config/custom_components/

# Restartujte kontejner
docker restart [CONTAINER_ID]
```

## 📂 Typické cesty na Synology

```
/volume1/docker/homeassistant/config/           # Docker compose setup
/volume1/@docker/containers/[HASH]/volume/     # Docker GUI setup  
/volume1/vm/homeassistant/config/              # VM setup
/volume1/homes/homeassistant/config/           # Dedicated user setup
```

## 📋 Krok za krokem průvodce

### 1. Najděte vaši config složku

```bash
# SSH do Synology
ssh admin@192.168.1.100  # nahraďte vaší IP

# Najděte configuration.yaml
find /volume1 -name "configuration.yaml" -type f 2>/dev/null

# Typický výstup:
# /volume1/docker/homeassistant/config/configuration.yaml
```

### 2. Připravte soubory na PC

```powershell
# Na vašem PC vytvořte ZIP archiv
Compress-Archive -Path "custom_components\duk_transport" -DestinationPath "duk_transport.zip"
```

### 3. Upload přes File Station

1. **Otevřete DSM** ve webovém prohlížeči
2. **Spusťte File Station**
3. **Přejděte do** `/docker/homeassistant/config/` (nebo vaší cesty)
4. **Vytvořte složku** `custom_components` (pravý klik → Vytvořit složku)
5. **Uploadujte** `duk_transport.zip` (Drag & Drop nebo tlačítko Upload)
6. **Rozbalte** archiv (pravý klik → Rozbalit)
7. **Přesuňte** složku `duk_transport` do `custom_components/`

### 4. Nastavte oprávnění

```bash
# SSH do Synology
cd /volume1/docker/homeassistant/config
chown -R 1000:1000 custom_components/duk_transport/
chmod -R 755 custom_components/duk_transport/
```

### 5. Restartuj Home Assistant

- **Přes webové rozhraní**: Nastavení → Systém → Restartovat
- **Přes SSH**: `docker restart homeassistant` (nahraďte názvem kontejneru)

## 🔍 Ověření instalace

Po restartu zkontrolujte:

1. **Logy** v HA: Nastavení → Systém → Logy
2. **Integraci**: Nastavení → Zařízení a služby → + PŘIDAT
3. **Vyhledejte**: "Doprava Ústeckého kraje"

## ⚠️ Časté problémy a řešení

### Problém: Integrace se nezobrazuje
```bash
# Zkontrolujte strukturu složek
ls -la /volume1/docker/homeassistant/config/custom_components/duk_transport/

# Měli byste vidět:
# __init__.py
# manifest.json
# config_flow.py
# const.py
# api.py
# sensor.py
```

### Problém: Chyby oprávnění
```bash
# Opravte oprávnění
chown -R 1000:1000 /volume1/docker/homeassistant/config/custom_components/
chmod -R 755 /volume1/docker/homeassistant/config/custom_components/
```

### Problém: Container se nespustí
```bash
# Zkontrolujte logy kontejneru
docker logs homeassistant

# Zkontrolujte configuration.yaml syntax
docker exec homeassistant python -m homeassistant --script check_config -c /config
```

## 🎛️ Docker Compose příklad

Pokud používáte docker-compose.yml:

```yaml
version: '3'
services:
  homeassistant:
    container_name: homeassistant
    image: ghcr.io/home-assistant/home-assistant:stable
    volumes:
      - /volume1/docker/homeassistant/config:/config
      - /etc/localtime:/etc/localtime:ro
    restart: unless-stopped
    network_mode: host
```

## 📞 Podpora

- **Synology logy**: Control Panel → Log Center
- **HA logy**: Nastavení → Systém → Logy  
- **Debug**: Zapněte debug logging v configuration.yaml

```yaml
logger:
  default: info
  logs:
    custom_components.duk_transport: debug
```

---
**Úspěšnou instalaci na Synology! 🎉**