import discord
import message as ms
from logger import Logger
from discord.ui import Button, View
from discord.interactions import Interaction
from modal.custom_message import CustomMessage

logger_mod = Logger("Admin Verify View")
logger = logger_mod.get_logger()

class AdminVerifyView(View):
    def __init__(self, config, user_info):
        super().__init__()
        self.config = config
        self.user_info = user_info


    @discord.ui.button(label="Approve", emoji="✅", style=discord.ButtonStyle.grey, custom_id="approve")
    async def approve_button(self, interaction: discord.Interaction, button: Button):
        await self.send_thread(interaction.guild, self.user_info.player_id, ms.APPROVED)
        await interaction.message.edit(view=None)
        try:
            member = interaction.guild.get_member(self.user_info.player_id)
            role = discord.utils.get(interaction.guild.roles, name="potato100")
            await member.add_roles(role)
        except Exception as e:
            logger.error(f"Member with ID {self.user_info.player_id} failed to assigned role due to:")
            logger.error(e)
            await interaction.channel.send(f"Member with ID {self.user_info.player_id} failed to assigned role, please proceed with manual assign if this have no issue")


    @discord.ui.button(label="Reject", emoji="❌", style=discord.ButtonStyle.grey, custom_id="reject")
    async def reject_button(self, interaction: discord.Interaction, button: Button):
        await self.send_thread(interaction.guild, self.user_info.player_id, ms.REJECTED)
        await interaction.message.edit(view=None)
        try:
            member = interaction.guild.get_member(self.user_info.player_id)
            role = discord.utils.get(interaction.guild.roles, name="potato100")
            await member.remove_roles(role)
        except Exception as e:
            logger.error(f"Member with ID {self.user_info.player_id} failed to remove role due to:")
            logger.error(e)
            await interaction.channel.send(f"Member with ID {self.user_info.player_id} failed to remove role, please proceed with manual remove if this have no issue")


    @discord.ui.button(label="Approve with Message", emoji="✅", style=discord.ButtonStyle.grey, custom_id="approve_message")
    async def approve_message_button(self, interaction: discord.Interaction, button: Button):
        modal = CustomMessage()
        await interaction.response.send_modal(modal)

        timeout = await modal.wait()
        if timeout:
            await interaction.channel.send("⏰ Approval message input timed out!")
            return

        custom_msg = f"[Approved ✅] {modal.result}"
        
        await self.send_thread(interaction.guild, self.user_info.player_id, custom_msg)
        await interaction.message.edit(view=None)
        try:
            member = interaction.guild.get_member(self.user_info.player_id)
            role = discord.utils.get(interaction.guild.roles, name="potato100")
            await member.remove_roles(role)
        except Exception as e:
            logger.error(f"Member with ID {self.user_info.player_id} failed to remove role due to:")
            logger.error(e)
            await interaction.channel.send(f"Member with ID {self.user_info.player_id} failed to remove role, please proceed with manual remove if this have no issue")
    
    
    @discord.ui.button(label="Reject with Message", emoji="❌", style=discord.ButtonStyle.grey, custom_id="reject_message")
    async def reject_message_button(self, interaction: discord.Interaction, button: Button):
        modal = CustomMessage()
        await interaction.response.send_modal(modal)

        timeout = await modal.wait()
        if timeout:
            await interaction.channel.send("⏰ Approval message input timed out!")
            return

        custom_msg = f"[Rejected ❌] {modal.result}"

        await self.send_thread(interaction.guild, self.user_info.player_id, custom_msg)
        await interaction.message.edit(view=None)
        try:
            member = interaction.guild.get_member(self.user_info.player_id)
            role = discord.utils.get(interaction.guild.roles, name="potato100")
            await member.remove_roles(role)
        except Exception as e:
            logger.error(f"Member with ID {self.user_info.player_id} failed to remove role due to:")
            logger.error(e)
            await interaction.channel.send(f"Member with ID {self.user_info.player_id} failed to remove role, please proceed with manual remove if this have no issue")


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

