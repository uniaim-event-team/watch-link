import codecs

from service.watch_link import get_watch_link_list
from service import slack, google_chat


codecs.register(
    lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


if __name__ == '__main__':
    watch_link_list = get_watch_link_list()
    message_list = []
    for watch_link in watch_link_list:
        # watch
        if watch_link.watch_table == 'slack_channels':
            message_list = slack.get_new_message_list(watch_link.watch_id)
        # link
        if watch_link.link_table == 'google_chat_webhook':
            google_chat.send_message_list(watch_link.link_id, message_list)
