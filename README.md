# Minecraft Server Startskript 🚀

**Version:** 1.5-Beta

## Inhaltsverzeichnis
- [Allgemeines](#allgemeines)
- [Einstellungen](#einstellungen)
- [Funktionen](#funktionen)
- [Shell-Befehle](#shell-befehle)
- [Besondere Features](#besondere-features)

---

## Allgemeines 📝
Dieses Skript ist ein Init-Skript für einen Minecraft-Server (MC_ATM10). Es ermöglicht:

- Starten, Stoppen und Neustarten des Servers  
- Backup-Verwaltung (stündlich inkrementell, täglich Vollbackup)  
- Rollback auf ein vorheriges Backup  
- Senden von Befehlen an den Server  
- Echtzeit-Anzeige der Serverlogs  
- Logrotation für Debug- und Serverlogs  
- Farbig formatierte Ingame-Meldungen  
- Du brauchst Screen um das Skript auszuführen. mit apt install screen kannst du dies z.b. auf Debian/Ubunto installieren
Alle Dateien, Backups und Logs werden in einem einstellbaren Minecraft-Pfad (`$MCPATH`) abgelegt.

> 💡 Das Startskript befindet sich im Unterordner [`Linux/MC_ATM10`](Linux/MC_ATM10)

---

## Einstellungen ⚙️
<details>
<summary>Server- und Benutzerinformationen</summary>

| Variable        | Beschreibung |
|-----------------|--------------|
| `SERVICE`       | Name des Server-Startskripts oder der JAR-Datei (`MC_ATM10`) |
| `SCREENNAME`    | Name der Screen-Session (`MC_ATM10`) |
| `USERNAME`      | Linux-User unter dem der Server läuft (`mc`) |
| `SERVER_NAME`   | Name, der in Ingame-Meldungen angezeigt wird (`Taracraft`) |
| `WORLD`         | Name der Minecraft-Welt (`Tara`) |
| `MCPATH`        | Root-Pfad des Servers (`/home/mc/ATM10/`) |

</details>

<details>
<summary>Backups 💾</summary>

| Variable               | Beschreibung |
|------------------------|--------------|
| `BACKUPPATH_HOURLY`    | Pfad für stündliche Backups |
| `BACKUPPATH_DAILY`     | Pfad für tägliche Backups |

</details>

<details>
<summary>RAM / CPU 🖥️</summary>

- `MINHEAP`, `MAXHEAP`, `CPU_COUNT`

</details>

<details>
<summary>Logs & Logrotation 📂</summary>

| Variable                     | Beschreibung |
|-------------------------------|--------------|
| `LOGS_DIR`                    | `$MCPATH/logs` |
| `DEBUG_LOG`                   | `debug.log` im Minecraft-Log-Verzeichnis |
| `DEBUG_LOG_RETENTION_DAYS`    | Alte Debug-Logs nach X Tagen löschen |
| `SERVER_LOG_RETENTION_DAYS`   | Alte Server-Logs nach X Tagen löschen |

</details>

---

## Funktionen ⚡
<details>
<summary>Alle Funktionen anzeigen</summary>

### a) Helpers 🛠️
- `log()`: schreibt sowohl in die Shell als auch optional in `debug.log`  
- `as_user()`: führt Befehle als Minecraft-Benutzer aus  
- `mc_tell(color, msg)`: sendet farbige Nachrichten an alle Spieler ingame  
- `ensure_dir(path, label)`: prüft, ob ein Verzeichnis existiert, erstellbar und beschreibbar ist  

### b) Serververwaltung 🖥️
- `mc_start()`: Startet den Server in einer Screen-Session  
- `mc_stop()`: Stoppt den Server sauber, inkl. Countdown, speichert die Welt  
- `mc_saveoff() / mc_saveon()`: Schaltet die Welt auf Read-Only bzw. wieder Read-Write  

### c) Backups 💾
<details>
<summary>Stündlich (inkrementell) ⏰</summary>

- `mc_backup_hourly()`  
  - Nutzt `tar --listed-incremental` mit Snapshot-Datei (`*.snar`)  
  - Komprimiert mit `gzip`  
  - Alte Backups >24h werden gelöscht  
  - Meldungen ingame und in Shell

</details>

<details>
<summary>Täglich (Vollbackup) 📅</summary>

- `mc_backup_daily()`  
  - Vollbackup der Welt + Serverdateien  
  - Komprimiert mit `gzip`  
  - Alte Backups >30 Tage werden gelöscht  
  - Meldungen ingame und in Shell

</details>

<details>
<summary>Backup Wrapper 🔄</summary>

- `mc_backup()`: führt Logrotation durch (`rotate_logs`), stündliches Backup, prüft tägliches Backup

</details>

### d) Rollback ↩️
<details>
<summary>Rollback-Funktion</summary>

- `mc_rollback()`: interaktive Auswahl des Backups  
  - Stoppt Server, entpackt Backup, startet Server wieder  
  - Meldungen ingame und in Shell

</details>

### e) Logrotation 📂
<details>
<summary>Logs rotieren</summary>

- `rotate_logs()`: komprimiert `debug.log` und alle `.log` im Minecraft-Log-Verzeichnis nach Datum (`YYYY-MM-DD.log.gz`)  
- Alte Logs werden automatisch nach konfigurierten Tagen gelöscht

</details>

### f) Server-Kommandos 💬
<details>
<summary>Server-Kommandos</summary>

- `mc_command("command")`: sendet Befehle an die Screen-Session (`/say Hello`)  
- `mc_listen()`: Echtzeit-Tail der `latest.log`

</details>

</details>

---

## Shell-Befehle 🖱️
> Alle Befehle müssen vom Unterordner [`linux/MC_ATM10`](linux/MC_ATM10) ausgeführt werden

<details>
<summary>Server starten / stoppen 🚀</summary>

| Befehl  | Beschreibung |
|---------|--------------|
| `./MC_ATM10 start` | Startet den Server |
| `./MC_ATM10 stop`  | Stoppt den Server sauber |
| `./MC_ATM10 restart` | Stoppt und startet den Server |
| `./MC_ATM10 status` | Prüft, ob der Server läuft |

</details>

<details>
<summary>Backups 💾</summary>

| Befehl  | Beschreibung |
|---------|--------------|
| `./MC_ATM10 backup` | Führt stündliches + tägliches Backup aus |
| `./MC_ATM10 rollback` | Interaktive Wiederherstellung eines Backups |

</details>

<details>
<summary>Server-Kommandos 💬</summary>

| Befehl                | Beschreibung |
|-----------------------|--------------|
| `./MC_ATM10 command "..."` | Sendet einen Befehl ingame |
| `./MC_ATM10 listen`        | Echtzeit-Tail der Serverlogs |

</details>

---

## Besondere Features 🌟
- Farbiges Ingame-Feedback für Backups, Rollback, Shutdown, Server-Kommandos  
- Automatische Logrotation inkl. Kompression  
- Inkrementelle stündliche Backups sparen Speicherplatz  
- Vollständige tägliche Backups gewährleisten Sicherheit  
- Rollback-Funktion stellt sowohl stündliche als auch tägliche Backups wieder her  
- Shell + ingame Logging parallel
