import asyncio
import discord
import logging.handlers

# Intents
intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.presences = True
client = discord.Client(intents=intents)

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    filename='BT-Rollen.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate durch 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

#Config
Botlog = "1327954289670361109"
Token = ""

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('https://www.bad-timing.eu'),
                                     status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('Rollen...'), status=discord.Status.online)
        await asyncio.sleep(5)

@client.event
async def on_member_join(member: discord.Member):
    role = discord.utils.get(member.guild.roles, name="Mitglied")
    if role:
        await member.add_roles(role)
        channel = client.get_channel(Botlog)
        if channel:
            await channel.send(
                f"{member.mention} hat die {role.name} Role zugewiesen bekommen und wurde per DM begrüßt")

        embed = discord.Embed(
            title="Willkommen auf dem Discord von Bad-Timing.",
            description="Wichtige Infos für die Benutzung des Discord.",
            color=0x8b6f6f
        )
        embed.add_field(
            name="Bitte die Regeln lesen!",
            value="Bei Nicht-Einhaltung behalten wir uns das Recht vor, zu kicken oder zu bannen. Bei Fragen stehen wir jederzeit zur Verfügung.",
            inline=False
        )
        embed.add_field(
            name="",
            value="Server-IP findet ihr unter dem Info-Channel",
            inline=False
        )
        embed.add_field(
            name="",
            value="Viel Spaß wünscht Bad-Timing",
            inline=False
        )
        embed.set_footer(text="by Thomas(Taracraft)")
        await member.send(embed=embed)
    else:
        logger.warning(f"Role 'Mitglieder' not found in guild {member.guild.name}")


@client.event
async def on_ready():
    print("Bot is ready!")
    print(f"Logged in as: {client.user.name}")
    print(f"Bot ID: {client.user.id}")
    for guild in client.guilds:
        print(f"Connected to server: {guild}")
    print("------")
    client.loop.create_task(status_task())


# Replace with your actual bot token

client.run(Token)