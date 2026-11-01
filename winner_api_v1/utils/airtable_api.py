import subprocess
from pyairtable import Api


class AirTableApi:
    def __init__(self, api_key, base_id, table_name):
        self.api_key = api_key
        self.base_id = base_id
        self.table_name = table_name
        self.api = Api(self.api_key)
        self.table = self.api.table(self.base_id, self.table_name)

    def get_hwid(self):
        cmd = "powershell (Get-CimInstance -Class Win32_ComputerSystemProduct).UUID"
        uuid = subprocess.check_output(cmd, shell=True).decode().strip()
        return uuid

    def check_license(self):
        hwid = self.get_hwid()
        formula = f"{{HWID}} = '{hwid}'"
        records = self.table.all(formula=formula)

        if records:
            fields = records[0]["fields"]
            status = fields.get("Status", "")

            print(f"מצאה רשומה. סטטוס נוכחי: {status}")

            if status == "Valid":
                return True
            else:
                return False
        else:
            print("HWID לא נמצא בטבלה. יוצר רשומה חדשה עם סטטוס Pending...")
            self.table.create({
                "HWID": hwid,
                "Status": "Pending"
            })
            return False

# דוגמה להפעלה:
# airtable_client = AirTableApi("YOUR_API_KEY", "YOUR_BASE_ID", "Licenses")
# is_valid = airtable_client.check_license()
# print("תוצאת בדיקת הרישיון:", is_valid)