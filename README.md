# Discordrebel.py - An API Wrapper For Selfbots
An API wrapper for interacting with the Discord api, with focus on selfbots.

## Some basic use:
```py
from discordrebel import rebelclient

client = rebelclient.YTMonsterClient('exampleuser', 'examplepassword')

print(client.get_like_video_from_exchanges())
print(client.get_channel_from_exchanges())
```

## Installation
```pip install YTMonsterClient```