import requests
import websocket
import sys
import json
import random
import base64


def setup_header(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 '
                      'Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36 '
    }
    return headers


def allow_direct_messages(token, option=True):
    if option:
        payload = dict(restricted_guilds=[], default_guilds_restricted=False)
        r = requests.patch('https://discord.com/api/v6/users/@me/settings', data=json.dumps(payload),
                           headers=setup_header(token))
    else:
        payload = {'default_guilds_restricted': True, 'restricted_guilds': []}
        r = requests.patch('https://discord.com/api/v6/users/@me/settings', data=json.dumps(payload),
                           headers=setup_header(token))


def allow_all_friend_requests(token, option=True):
    payload = dict(friend_source_flags={"all": True, "mutual_friends": True, "mutual_guilds": True})
    r = requests.patch('https://discord.com/api/v6/users/@me/settings', data=json.dumps(payload),
                       headers=setup_header(token))


def safe_direct_messaging_filter(token, filter=0):
    payload = dict(explicit_content_filter=filter)
    r = requests.patch('https://discord.com/api/v6/users/@me/settings', data=json.dumps(payload),
                       headers=setup_header(token))


def set_avatar(token, imageurl):

    encoded = base64.b64encode(requests.get(imageurl).content).decode('utf-8')

    payload = {'avatar': 'data:image/png;base64,' + encoded}
    r = requests.patch('https://discord.com/api/v6/users/@me', json=payload, headers=setup_header(token))

