from datetime import datetime, timezone, timedelta
import json
import urllib.request

from mysql_dbcon import Connection
from model import SlackChannel, SlackUser, SlackMessage


# TODO set timezone at config
jst = timezone(timedelta(hours=+9), 'JST')


def get_new_message_list(channel_id: int):
    with Connection() as cn:
        token, channel = cn.s.query(SlackChannel.token, SlackChannel.channel).filter(
            SlackChannel.id == channel_id).one()
        user_dict = {user.user: user.other_name for user in cn.s.query(SlackUser).all()}
        with urllib.request.urlopen(
                f'https://slack.com/api/channels.history?token={token}&channel={channel}') as res:
            json_dict = json.load(res)
            print(json_dict)
        messages = sorted(json_dict['messages'], key=lambda x: x.get('ts', ''))
        client_msg_id_list = [
            id_ for id_, in cn.s.query(SlackMessage.client_msg_id).filter(
                SlackMessage.client_msg_id.in_([message.get('client_msg_id') for message in messages])
            ).all()]
        message_list = []
        insert_msg_id_list = []
        for message in messages:
            if not (message.get('user') and message.get('text') and message.get('client_msg_id')):
                continue
            if message.get('client_msg_id') in client_msg_id_list:
                continue
            time_stamp = message.get('ts', '')
            if time_stamp:
                time_stamp = datetime.fromtimestamp(float(time_stamp), jst).strftime('%m/%d %H:%M:%S')
            text = message['text']
            for user, name in user_dict.items():
                text = text.replace(user, name)
            message_list.append(user_dict[message['user']] + ':[' + time_stamp + '] ' + text)
            insert_msg_id_list.append({'client_msg_id': message['client_msg_id']})
        cn.s.bulk_insert_mappings(SlackMessage, insert_msg_id_list)
        cn.s.commit()

    return message_list
