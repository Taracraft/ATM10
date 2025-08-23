Was macht das Startskript?

Version 1.5-Beta

1. Allgemeines

Dieses Skript ist ein Init-Skript für einen Minecraft-Server (MC_ATM10). Es ermöglicht:

Starten, Stoppen und Neustarten des Servers

Backup-Verwaltung (stündlich inkrementell, täglich Vollbackup)

Rollback auf ein vorheriges Backup

Senden von Befehlen an den Server

Echtzeit-Anzeige der Serverlogs

Logrotation für Debug- und Serverlogs

Farbig formatierte Ingame-Meldungen

Alle Dateien, Backups und Logs werden in einem einstellbaren Minecraft-Pfad ($MCPATH) abgelegt.

2. Einstellungen

Server- und Benutzerinformationen:

SERVICE: Name des Server-Startskripts oder der JAR-Datei (startserver.sh)

SCREENNAME: Name der Screen-Session (MC_ATM10)

USERNAME: Linux-User unter dem der Server läuft (mc)

SERVER_NAME: Name, der in Ingame-Meldungen angezeigt wird (Taracraft)

WORLD: Name der Minecraft-Welt (Tara)

MCPATH: Root-Pfad des Servers (/home/mc/ATM10/)

Backups:

BACKUPPATH_HOURLY: stündliche Backups

BACKUPPATH_DAILY: tägliche Backups

RAM / CPU:

MINHEAP, MAXHEAP, CPU_COUNT

Logs & Logrotation:

LOGS_DIR: $MCPATH/logs

DEBUG_LOG: debug.log im Minecraft-Log-Verzeichnis

DEBUG_LOG_RETENTION_DAYS: alte Debug-Logs nach X Tagen löschen

SERVER_LOG_RETENTION_DAYS: alte Server-Logs nach X Tagen löschen

3. Funktionen
a) Helpers

log(): schreibt sowohl in die Shell als auch optional in debug.log.

as_user(): führt Befehle als Minecraft-Benutzer aus.

mc_tell(color, msg): sendet farbige Nachrichten an alle Spieler ingame.

ensure_dir(path, label): prüft, ob ein Verzeichnis existiert, erstellbar und beschreibbar ist.

b) Serververwaltung

mc_start(): Startet den Server in einer Screen-Session. Meldet Erfolg/Fehler in Shell und ingame.

mc_stop(): Stoppt den Server sauber, inklusive Countdown (Minuten + Sekunden), speichert Welt.

mc_saveoff() / mc_saveon(): Schaltet die Welt auf Read-Only bzw. wieder Read-Write, z. B. für Backups.

c) Backups

Stündlich (inkrementell):

mc_backup_hourly()

Nutzt tar --listed-incremental mit Snapshot-Datei (*.snar), um nur Änderungen zu sichern.

Komprimiert mit gzip.

Alte Backups >24h werden gelöscht.

Meldungen werden ingame und in Shell angezeigt.

Täglich (Vollbackup):

mc_backup_daily()

Vollbackup der Welt + Serverdateien

Komprimiert mit gzip.

Alte Backups >30 Tage werden gelöscht.

Meldungen wie bei stündlichen Backups.

Backup Wrapper:

mc_backup(): führt Rotation der Logs durch (rotate_logs), dann stündliches Backup, prüft, ob tägliches Backup nötig ist.

d) Rollback

mc_rollback(): interaktive Auswahl, welche Backup-Version wiederhergestellt werden soll.

Wählt zwischen stündlich (inkrementell) und täglich (voll).

Stoppt den Server, entpackt das Backup, startet den Server wieder.

Meldungen werden ingame und in Shell angezeigt.

e) Logrotation

rotate_logs():

Komprimiert debug.log und alle .log im Minecraft-Log-Verzeichnis nach Datum (YYYY-MM-DD.log.gz).

Alte Logs werden nach konfigurierten Tagen automatisch gelöscht.

f) Server-Kommandos

mc_command("command"): sendet Befehle an die Screen-Session des Servers, z. B. /say Hello.

mc_listen(): Echtzeit-Tail der latest.log im Minecraft-Logverzeichnis.

4. Shell-Befehle / Bedienung
Shell-Befehl	Beschreibung
start	Startet den Server
stop	Stoppt den Server sauber
restart	Stoppt und startet den Server
backup	Führt stündliches + tägliches Backup aus
rollback	Interaktive Wiederherstellung eines Backups
status	Prüft, ob der Server läuft
command "..."	Sendet einen Befehl ingame
listen	Echtzeit-Tail der Serverlogs
5. Besondere Features

Farbiges Ingame-Feedback für Backups, Rollback, Shutdown, Server-Kommandos.

Automatische Logrotation inkl. Kompression.

Inkrementelle stündliche Backups sparen Speicherplatz.

Vollständige tägliche Backups gewährleisten Sicherheit.

Rollback-Funktion stellt sowohl stündliche als auch tägliche Backups wieder her.

Shell + ingame Logging parallel.
