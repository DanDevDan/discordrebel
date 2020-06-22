import requests
import websocket
import sys
import json
import random
from .common import Common

class rebelclient():
    def __init__(self, token):
        self.token = token

    def set_game(self, game, type, status='online', twitchlink='twitch.com'):
        Common.set_game(self, self.token, game, type, status)

    def set_nickname(self, token, guildid, nickname):
        Common.set_nickname(self, self.token, guildid, nickname)