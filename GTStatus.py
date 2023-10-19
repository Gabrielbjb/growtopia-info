import requests
from datetime import datetime
from pytz import timezone
def GameData():
    Result = {
        "Online_User": "",
        "WOTDLink" : "",
        "WOTDName" : "",
        "GTTime" : "",
        "GTDate" : ""
    }
    try:
        Website = requests.get(f"https://www.growtopiagame.com/detail").json()

        Result["Online_User"] = Website["online_user"]
        Result["WOTDLink"] = Website["world_day_images"]["full_size"] 
        Result["WOTDName"] = ((Result["WOTDLink"].replace('https://www.growtopiagame.com/worlds/','')).replace('.png','')).upper()
        Result["GTTime"] = datetime.now(timezone('UTC')).astimezone(timezone('America/New_York')).strftime("%X")
        Result["GTDate"] = datetime.now(timezone('UTC')).astimezone(timezone('America/New_York')).strftime("%x")
        return Result
    except: 
        return({"Error":"It looks like we can't reach growtopiagame.com! Error code 2"})
print(GameData())
