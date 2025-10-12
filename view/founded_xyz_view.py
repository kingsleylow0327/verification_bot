import discord
from discord.interactions import Interaction
from modal.submit_xyz import SubmitXYZModal
from discord.ui import Button

class FoundedXYZView(discord.ui.View):

    def __init__(self, config):
        super().__init__(timeout=None)
        self.config = config


    @discord.ui.button(label="提交 | Submit", style=discord.ButtonStyle.blurple, custom_id="submit")
    async def submit_uid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(SubmitXYZModal(self.config))