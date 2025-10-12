import discord
import message as ms

from config import Config
from discord.interactions import Interaction
from dto.user_info import UserInfo
from service.gsheet_service import GoogleSheetService
from view.admid_verifiy_view import AdminVerifyView
from view.go_back_view import GoBackView

TITLE = "提交资讯 | Submit Detail"
class SubmitXYZModal(discord.ui.Modal, title=TITLE):

    def __init__(self, config: Config):
        self.config = config
        super().__init__(title=TITLE, timeout=120)

    name = discord.ui.TextInput(label="⁠全名 Full Name",placeholder="全名 |  Full Name",style=discord.TextStyle.short)
    email = discord.ui.TextInput(label="⁠注册所用的邮箱 Registered Email",placeholder="⁠注册所用的邮箱 | Registered Email",style=discord.TextStyle.short)
    uid = discord.ui.TextInput(label="⁠UID",placeholder="⁠UID（FundedXYZ 个人后台查看 | Visible in FundedXYZ dashboard)",style=discord.TextStyle.short)

    async def on_submit(self, interaction: Interaction):
        name = self.name.value
        email = self.email.value
        uid = self.uid.value
        player_id = str(interaction.user.id)

        guild = interaction.guild
        admin_channel = guild.get_channel(int(self.config.ADMIN_CHANNEL_ID))
        embed = discord.Embed(
            title=f"[XYZ] {interaction.user.display_name} submited XYZ Detail",
            description=f"UID: {uid}, Player ID: {player_id}",
            color=0xE733FF
        )
        gsheet_service = GoogleSheetService(self.config.GBOT_GSHEET_ID)
        gsheet_service.append_row([player_id, uid, name, email])

        admin_view = AdminVerifyView(self.config, UserInfo(player_id, uid))
        await admin_channel.send(embed=embed, view=admin_view)
        go_back_view=GoBackView(self.config)
        await interaction.response.send_message(ms.XYZ_WAIT, ephemeral=True, view=go_back_view)
