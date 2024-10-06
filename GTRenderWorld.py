from datetime import datetime
import pytz, re, requests

def Render_World(world):
    result = {
        "World":None,
        "Create":{
            "DateTime":None,
            "Date":None,
            "Time":None,
            "Timezone":None
            },
        "Modify":{
            "DateTime":None,
            "Date":None,
            "Time":None,
            "Timezone":None
            },
        "Epoch":{
            "Create":None,
            "Modify":None
            },
        "Error": None
    }

    def epoch_time(matches):
        date_time = datetime.fromisoformat(matches[0])
        utc_date_time = date_time.astimezone(pytz.utc)
        return int((utc_date_time - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds())
    def worldtime(time,type):
        dt = datetime.fromisoformat(time)
        result[type]["DateTime"] = time
        result[type]["Date"] = str(dt.date())
        result[type]["Time"] = str(dt.time())
        result[type]["Timezone"] = str(dt.tzinfo)
    r = requests.get(f"https://s3.amazonaws.com/world.growtopiagame.com/{world}.png", stream=True)   
    if "Access Denied" in str(r.content):
        result["Error"] = "World Not Found or Access Denied"
    else:
        try:       
            isi = str(r.content).split('x00%tEXt')
            pattern = r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2})"
            create = re.findall(pattern, isi[1])
            modify = re.findall(pattern, isi[2])
            if create:
                worldtime(create[0], "Create")
                result["Epoch"]["Create"] = epoch_time(create)
            if modify:
                worldtime(modify[0], "Modify")
                result["Epoch"]["Modify"] = epoch_time(modify)
        except:
            result["Error"] = "Something went wrong! Please report to owner if this error still occur"
    result["World"] = world.upper()
    return result
