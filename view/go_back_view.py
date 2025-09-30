import discord
from discord.ui import Button

class GoBackView(discord.ui.View):

    def __init__(self, config):
        super().__init__(timeout=None)
        self.config = config
        url = f"https://discord.com/channels/{config.GUILD_ID}/{config.LANDING_CHANNEL_ID}"
        self.add_item(Button(label="⬅️ 返回 | Go Back", style=discord.ButtonStyle.link, url=url))