import requests
import websocket
import sys
import json
import random


def setup_header(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 '
                      'Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36 '
    }
    return headers


def set_nickname(token, guildid, nickname):
    payload = {'nick':nickname}
    src = requests.patch(f'https://canary.discordapp.com/api/v6/guilds/{guildid}/members/@me/nick', headers=setup_header(token),
                        json=payload, timeout=10)


def set_game(token, game, type, status='online', twitchlink='twitch.com'):
    if status == "random":
        stat = ['online', 'dnd', 'idle']
        status = random.choice(stat)

    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=6&encoding=json")
    if type == "Playing":
        gamejson = {
            "name": game,
            "type": 0
        }
    elif type == 'Streaming':
        gamejson = {
            "name": game,
            "type": 1,
            "url": twitchlink
        }
    elif type == "Listening to":
        gamejson = {
            "name": game,
            "type": 2
        }
    elif type == "Watching":
        gamejson = {
            "name": game,
            "type": 3
        }
    auth = {
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": sys.platform,
                "$browser": "DiscordRebel.py",
                "$device": f"{sys.platform} Device"
            },
            "presence": {
                "game": gamejson,
                "status": status,
                "since": 0,
                "afk": False
            }
        },
        "s": None,
        "t": None
        }

    ws.send(json.dumps(auth))