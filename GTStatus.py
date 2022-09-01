import requests
from datetime import datetime
from pytz import timezone

Data = {
    "Online_User": "",
    "WOTDLink" : "",
    "WOTDName" : "",
    "GTTime" : "",
    "GTDate" : ""
}

Website = requests.get(f"https://www.growtopiagame.com/detail").json()
Data["Online_User"] = Website["online_user"]
Data["WOTDLink"] = Website["world_day_images"]["full_size"] 
Data["WOTDName"] = ((Data["WOTDLink"].replace('https://www.growtopiagame.com/worlds/','')).replace('.png','')).upper()
Data["GTTime"] = datetime.now(timezone('UTC')).astimezone(timezone('America/New_York')).strftime("%X")
Data["GTDate"] = datetime.now(timezone('UTC')).astimezone(timezone('America/New_York')).strftime("%x")

# All data will be saved to (Data)
# You have to install pytz first to use this code, "pip install pytz"
