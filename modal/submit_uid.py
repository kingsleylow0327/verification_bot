import discord
import message as ms
from view.admid_verifiy_view import AdminVerifyView
from view.go_back_view import GoBackView
from discord.interactions import Interaction

TITLE = "[提交 UID | Submit UFC UID]"
class SubmitUIDModal(discord.ui.Modal, title=TITLE):

    def __init__(self, config):
        self.config = config
        super().__init__(title=TITLE, timeout=120)

    uid = discord.ui.TextInput(label="UFC UID",placeholder="UFC UID",style=discord.TextStyle.short)

    async def on_submit(self, interaction: Interaction):
        uid = interaction.data.get("components")[0].get("components")[0].get("value")
        player_id = interaction.user.id
        
        guild = interaction.guild
        admin_channel = guild.get_channel(int(self.config.ADMIN_CHANNEL_ID))
        embed = discord.Embed(
            title=f"{interaction.user.display_name} submited UFC UID",
            description=f"UID: {uid}, Player ID: {player_id}",
            color=0xE733FF
        )
        admin_view = AdminVerifyView(self.config, user_info(player_id, uid))
        await admin_channel.send(embed=embed, view=admin_view)
        go_back_view=GoBackView(self.config)
        await interaction.response.send_message(ms.WAIT_REVIEW, ephemeral=True, view=go_back_view)


class user_info():
    def __init__(self, player_id, uid):
        self.player_id = player_id
        self.uid = uid
