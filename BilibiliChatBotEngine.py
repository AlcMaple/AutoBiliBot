# Bilibili 聊天机器人的主要执行文件。它包含了整个机器人的逻辑和控制流程.

from LoginHandlers import bilibili_login
from utils import utils

def main():
    # 实例化登录类
    login = bilibili_login.LoginHandler()

    utils.save_json_file(path="./cookie.json", data=login.qr_login())

if __name__ == '__main__':
    main()