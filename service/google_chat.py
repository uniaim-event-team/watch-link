import json
from typing import List
import urllib.request

from mysql_dbcon import Connection
from model import GoogleChatWebhook


def send_message_list(webhook_id: int, message_list: List[str]):
    with Connection() as cn:
        print('sending to chat...')
        webhook = cn.s.query(GoogleChatWebhook).filter(GoogleChatWebhook.id == webhook_id).one()
        headers = {"Content-Type": "application/json"}
        for message in message_list:
            request = urllib.request.Request(
                webhook.url, data=json.dumps({'text': message}).encode('utf-8'),
                method='POST', headers=headers)
            with urllib.request.urlopen(request) as res:
                json_dict = json.load(res)
            print(json_dict)
