import requests
import websocket
import sys
import json
import random
from . import common
from . import discord_settings


class RebelClient:
    def __init__(self, token):
        self.token = token

    def set_game(self, game, type, status='online', twitchlink='twitch.com'):
        common.set_game(self.token, game, type, status, twitchlink)

    def set_nickname(self, guildid, nickname):
        common.set_nickname(self.token, guildid, nickname)

    def allow_direct_messages(self, option=True):
        discord_settings.allow_direct_messages(self.token, option)

    def allow_all_friend_requests(self, option=True):
        discord_settings.allow_all_friend_requests(self.token, option)

    def safe_direct_messaging_filter(self, filter=0):
        discord_settings.safe_direct_messaging_filter(self.token, filter)

    def set_avatar(self, imageurl):
        # Currently broken
        discord_settings.set_avatar(self.token, imageurl)