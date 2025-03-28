from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import discord
from discord.ext import commands

# Bot-Setup
intents = discord.Intents.default()
intents.members = True  # Erforderlich für on_member_join
bot = commands.Bot(command_prefix="!", intents=intents)

# Einstellungen
WELCOME_CHANNEL_ID = ID_HIER  # Hier die ID deines Welcome-Channels einfügen
BACKGROUND_IMAGE = "welcome_background.jpg"  # Dein Hintergrundbild
FONT_PATH = "arial.ttf"  # Pfad zur Schriftart (z. B. in den Bot-Ordner legen)
FONT_SIZE = 200  # Schriftgröße für den Text
TEXT_COLOR = "white"  # Textfarbe
IMAGE_SIZE = (6912, 3456)  # Bildgröße


@bot.event
async def on_member_join(member):
    try:
        # Hintergrundbild laden
        background = Image.open(BACKGROUND_IMAGE)
        draw = ImageDraw.Draw(background)

        # Schriftart laden
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

        # Begrüßungstext
        text = f"Willkommen, {member.name}!"

        # Textgröße berechnen
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]  # Breite
        text_height = bbox[3] - bbox[1]  # Höhe

        # Avatar von Discord abrufen
        response = requests.get(member.avatar.url)
        avatar = Image.open(BytesIO(response.content))

        # Avatargröße berechnen (40% der Bildhöhe)
        avatar_size = int(IMAGE_SIZE[1] * 0.2)
        avatar = avatar.resize((avatar_size, avatar_size))  # Quadratische Skalierung

        # Positionen berechnen
        spacing = 50  # Abstand zwischen Avatar und Text
        total_width = avatar_size + spacing + text_width  # Gesamtbreite von Avatar + Text

        # Startposition für zentrierte Darstellung
        x_start = (IMAGE_SIZE[0] - total_width) // 2
        y_center = (IMAGE_SIZE[1] - avatar_size) // 2

        # Avatar platzieren (links vom Text)
        background.paste(avatar, (x_start, y_center))

        # Text zeichnen (rechts neben dem Avatar)
        text_x = x_start + avatar_size + spacing
        text_y = (IMAGE_SIZE[1] - text_height) // 2
        draw.text((text_x, text_y), text, font=font, fill=TEXT_COLOR)

        # Bild in einen Bytes-Stream speichern (ohne Datei zu erstellen)
        img_byte_array = BytesIO()
        background.save(img_byte_array, format="PNG")
        img_byte_array.seek(0)  # Stream zum Anfang setzen

        # Bild an Discord senden
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f"Willkommen {member.mention}!", file=discord.File(fp=img_byte_array, filename="welcome.png"))

    except Exception as e:
        print(f"Fehler beim Erstellen des Willkommensbildes: {e}")


bot.run("Token-Hier")
