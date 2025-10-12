import gspread
from google.oauth2.service_account import Credentials


SCOPES = ["https://spreadsheets.google.com/feeds", 
         "https://www.googleapis.com/auth/drive"]

CREDENTIALS_FILE = "credentials/services_account.json"

TABLE_NUMBER = 3

class GoogleSheetService:

    def __init__(self, GBOT_GSHEET_ID: str):
        self.credentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
        self.client = gspread.authorize(self.credentials)
        self.sheet = self.client.open_by_key(GBOT_GSHEET_ID).get_worksheet(TABLE_NUMBER)
    
    def append_row(self, row_data):
        self.sheet.append_row(row_data)