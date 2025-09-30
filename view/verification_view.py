import discord
from discord.interactions import Interaction
from modal.submit_uid import SubmitUIDModal
from discord.ui import Button

class PotatoValidateView(discord.ui.View):

    def __init__(self, config):
        super().__init__(timeout=None)
        self.config = config


    @discord.ui.button(label="提交 UID | Submit UFC UID", style=discord.ButtonStyle.blurple, custom_id="update_vip")
    async def submit_uid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(SubmitUIDModal(self.config))