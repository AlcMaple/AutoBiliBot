# import sys,xlrd3,asyncio
# # from bilibili_api import Credential, sync, user
# # from bilibili_api.session import Session, Event, send_msg
# # from bilibili_api.user import User, RelationType
# # from bilibili_api.utils.picture import Picture

# class AutoBiliBot:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         # self.session = Session()
#         self.banner = r"""
#             \\         //
#             \\       //
#         #####################     ________   ___   ___        ___   ________   ___   ___        ___
#         ##                 ##    |\   __  \ |\  \ |\  \      |\  \ |\   __  \ |\  \ |\  \      |\  \
#         ##    //     \\    ##    \ \  \|\ /_\ \  \\ \  \     \ \  \\ \  \|\ /_\ \  \\ \  \     \ \  \
#         ##   //       \\   ##     \ \   __  \\ \  \\ \  \     \ \  \\ \   __  \\ \  \\ \  \     \ \  \
#         ##                 ##      \ \  \|\  \\ \  \\ \  \____ \ \  \\ \  \|\  \\ \  \\ \  \____ \ \  \
#         ##       www       ##       \ \_______\\ \__\\ \_______\\ \__\\ \_______\\ \__\\ \_______\\ \__\
#         ##                 ##        \|_______| \|__| \|_______| \|__| \|_______| \|__| \|_______| \|__|
#         #####################
#             \/         \/                               哔哩哔哩 (゜-゜)つロ 干杯~
# """

#     # 登录B站账号
#     def login(self):
#         # credential = Credential(self.username, self.password)
#         # self.session.login(credential)
#         pass
    
#     # 检查是否登录成功
#     def check_login(self):
#         if self.session.is_login:
#             print(self.banner)
#         else:
#             print("登录失败")

from ..base.base_crawler import AbstractCrawler

class BiliAutoReply:

    @staticmethod
    def create_bili_auto_reply() -> AbstractCrawler:
        # 实例化B站自动回复消息类
        return