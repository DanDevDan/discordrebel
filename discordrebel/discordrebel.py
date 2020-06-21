import requests
import websocket
import sys
import json
import random
from .common import Common

token = 'NzIxNDk0MTA5MDg0NDUwODY4.Xu-riQ.KdyxbO4n_Q7P3d4BFAmHW4wGGYg'
class rebelclient():
    def __init__(self, token):
        self.token = token

    def set_game(self, game, type, status='online', twitchlink='twitch.com'):
        Common.set_game(self, self.token, game, type, status)