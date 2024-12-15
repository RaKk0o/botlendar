import discord
import requests

# Raid helper API URL
SERVER_ID = os.get
CHANNEL_ID = os.get
url = "https://api.raid-helper.dev/api/v2/servers/{SERVER_ID}/channels/{CHANNEL_ID}/event"

# Header with authentification
headers = {
    "Authorization": "Bearer {RH_API_TOKEN}",
    "Content-Type": "application/json;charset=utf-8"
}

# Get event's data
LEADER_DISCORD_ID = os.get
event_date =
event_time =
event_title =
event_description = 
event_schedule =

# Event's data
data = {
    "leaderId": "{LEADER_DISCORD_ID}"
    "templateId": 10,
    "date": "{event_date}",
    "time": "{event_time}",
    "title": "{event_title}",
    "description": "{event_description}",
    "schedule": "{event_schedule}",
    "duration": 120,
    "classLimits": {
        "tank": 2,
        "healer": 2,
        "melee_dps": 2,
        "magic_dps": 1,
        "physic_dps": 1
    }
}

# POST request
response = requests.post(url,json=data, headers=headers)

# Results
if response.status_code == 201:
    print("Success: Event created! ", response.json())
else:
    print("Error: ", response.text)