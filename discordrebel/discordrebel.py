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
        return common.set_nickname(self.token, guildid, nickname)

    def allow_direct_messages(self, option=True):
        return discord_settings.allow_direct_messages(self.token, option)

    def allow_all_friend_requests(self, option=True):
        return discord_settings.allow_all_friend_requests(self.token, option)

    def safe_direct_messaging_filter(self, filter=0):
        return discord_settings.safe_direct_messaging_filter(self.token, filter)

    def set_avatar(self, imageurl):
        # Currently broken
        return discord_settings.set_avatar(self.token, imageurl)

    def get_account_info(self):
        return common.get_account_info(self.token)

    def set_language(self, language):
        """Locale format, Example: en-US"""
        return discord_settings.set_language(self.token, language)

    def send_message(self, message, channelid):
        return common.send_message(self.token, message, str(channelid))

    def send_dm(self, message, userid):
        return common.send_dm(self.token, message, str(userid))

    def create_server(self, name, iconurl=None, region='europe'):
        """Only accepts PNG urls as icon"""
        return common.create_server(self.token, name, iconurl, region)

    def delete_server(self, guildid):
        return common.delete_server(self.token, guildid)