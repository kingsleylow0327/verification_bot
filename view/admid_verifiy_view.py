import discord
import message as ms
from discord.ui import Button, View
from discord.interactions import Interaction

class AdminVerifyView(View):
    def __init__(self, config, user_info):
        super().__init__()
        self.config = config
        self.user_info = user_info


    @discord.ui.button(label="Approve", emoji="✅", style=discord.ButtonStyle.grey, custom_id="approve")
    async def approve_button(self, interaction: discord.Interaction, button: Button):
        await self.send_thread(interaction.guild, self.user_info.player_id, ms.APPROVED)
        await interaction.message.edit(view=None)

    @discord.ui.button(label="Reject", emoji="❌", style=discord.ButtonStyle.grey, custom_id="reject")
    async def reject_button(self, interaction: discord.Interaction, button: Button):
        await self.send_thread(interaction.guild, self.user_info.player_id, ms.REJECTED)
        await interaction.message.edit(view=None)
    
    async def send_thread(self, guild, member_id, message):
        channel = guild.get_channel(int(self.config.PUBLIC_THREAD_CHANNEL_ID))
        user = guild.get_member(member_id) 
        thread = await channel.create_thread(
            name=f"Private with {user.display_name}",
            type=discord.ChannelType.private_thread,
            invitable=False
        )
        await thread.add_user(user)
        await thread.send(message)

