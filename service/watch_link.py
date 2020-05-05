from typing import List

from mysql_dbcon import Connection
from model import WatchLink


def get_watch_link_list() -> List[WatchLink]:
    with Connection() as cn:
        return cn.s.query(WatchLink).all()
