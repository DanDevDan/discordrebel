import requests
import websocket
import sys
import json
import random
from . import common


class RebelClient:
    def __init__(self, token):
        self.token = token

    def set_game(self, game, type, status='online', twitchlink='twitch.com'):
        common.set_game(self.token, game, type, status, twitchlink)

    def set_nickname(self, token, guildid, nickname):
        common.set_nickname(self.token, guildid, nickname)
