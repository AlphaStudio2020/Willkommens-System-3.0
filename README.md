# Willkommens-System-3.0

# Discord Welcome Bot

Ein Discord-Bot, der automatisch ein personalisiertes **Willkommensbild** erstellt und es in einen bestimmten Kanal sendet, wenn ein neuer Benutzer dem Server beitritt. 🎉

## 🚀 Installation

### 1️⃣ Voraussetzungen

- **Python 3.8 oder neuer** installiert ([Download](https://www.python.org/downloads/))
- Ein **Discord-Bot-Token** (erstelle einen Bot unter [Discord Developer Portal](https://discord.com/developers/applications))

### 2️⃣ Benötigte Bibliotheken installieren

Führe diesen Befehl im Terminal oder in der Eingabeaufforderung aus:

```sh
pip install discord pillow requests
```

## 🔧 Einrichtung

### 1️⃣ Projektstruktur

```
/discord-welcome-bot
│── main.py               # Der Hauptcode des Bots
│── welcome_background.jpg # Das Hintergrundbild für das Willkommensbild
│── arial.ttf             # Schriftart (falls benötigt)
│── README.md             # Diese Datei
```

### 2️⃣ **Bot-Konfiguration** (`main.py`)

- **Setze deinen Bot-Token:** Ersetze `DEIN_BOT_TOKEN` mit deinem echten Discord-Bot-Token.
- **Setze deine Channel-ID:** Ersetze `WELCOME_CHANNEL_ID` mit der ID des Kanals, in dem das Bild gesendet werden soll.
- **Passe das Hintergrundbild & Schriftart an**, falls gewünscht.


## ▶️ Bot starten

Führe in der Konsole den folgenden Befehl aus:

```sh
python main.py
```

Falls dein Bot online geht und in Discord reagiert, ist alles korrekt eingerichtet! 🎉

## ❓ Häufige Probleme & Lösungen

**1. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*****`ModuleNotFoundError: No module named 'discord'`**\
👉 `pip install discord` ausführen.

**2. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*****`ModuleNotFoundError: No module named 'PIL'`**\
👉 `pip install pillow` ausführen.

**3. Der Bot startet, aber sendet keine Nachrichten.**\
✅ Prüfe, ob der Bot **die richtigen Berechtigungen** für den Kanal hat.
✅ Stelle sicher, dass du die **richtige Kanal-ID** in `WELCOME_CHANNEL_ID` eingetragen hast.

## 📜 Lizenz

Dieses Projekt ist unter der MIT-Lizenz veröffentlicht. Du kannst es frei nutzen und anpassen. 💡

---

🎉 **Viel Spaß mit deinem Discord-Willkommensbot!** 🚀

