import requests
import websocket
import sys
import json
import random

class Common():

    def set_game(self, token, game, type, status='online', twitchlink='twitch.com'):
        if status == "random":
            stat = ['online', 'dnd', 'idle']
            status = random.choice(stat)
    
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=6&encoding=json")
        print('token: ' + token)
        print('game: ' + game)
        print('type: ' + type)
        print('status: ' + status)
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