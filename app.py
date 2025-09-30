import discord
import message as ms

from discord.ext import commands
from config import Config
from logger import Logger
from view.verification_view import PotatoValidateView
from view.admid_verifiy_view import AdminVerifyView

# Logger setup
logger_mod = Logger("Potato")
logger = logger_mod.get_logger()

# Client setup
intents = discord.Intents.all()
intents.message_content = True

# Bot setup
config = Config()

GUILD_ID = int(config.GUILD_ID)

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    view = AdminVerifyView(config, None)
    bot.add_view(view)
    await run_verification()
    logger.info("Potato is Ready")

async def run_verification():
    admin_channel = bot.get_channel(int(config.USER_APPLY_CHANNEL_ID))
    embed = discord.Embed(
        title=ms.USER_APPLY_CHANNEL_TITLE,
        color=0xE733FF  # Purple color,
    )
    file = discord.File("media/instruction.gif", filename="instruction.gif")
    embed.set_image(url="attachment://instruction.gif")
    view = PotatoValidateView(config)
    await admin_channel.send(embed=embed, view=view, file=file)

bot.run(config.TOKEN)