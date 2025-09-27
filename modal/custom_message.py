import discord
from logger import Logger

logger_mod = Logger("Custom Message")
logger = logger_mod.get_logger()

class CustomMessage(discord.ui.Modal, title="Approval Message"):
    custom_message = discord.ui.TextInput(
        label="Custom approval message",
        placeholder="Type Custom Message here",
        style=discord.TextStyle.long
    )

    async def on_submit(self, interaction: discord.Interaction):
        self.result = self.custom_message.value
        await interaction.response.defer()