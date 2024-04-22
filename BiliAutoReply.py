import sys,xlrd3,asyncio
from bilibili_api import Credential, sync, user
from bilibili_api.session import Session, Event, send_msg
from bilibili_api.user import User, RelationType
from bilibili_api.utils.picture import Picture