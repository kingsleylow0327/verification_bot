import os

from dotenv import load_dotenv

class Config():
    
    def __init__(self) -> None:
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD_ID = os.getenv('GUILD_ID')
        self.LANDING_CHANNEL_ID=os.getenv('LANDING_CHANNEL_ID')
        self.USER_APPLY_CHANNEL_ID = os.getenv('USER_APPLY_CHANNEL_ID')
        self.ADMIN_CHANNEL_ID = os.getenv('ADMIN_CHANNEL_ID')
        self.PUBLIC_THREAD_CHANNEL_ID = os.getenv('PUBLIC_THREAD_CHANNEL_ID')