# 处理登录账号

from AutoBiliBot.bilibili_api import login

class LoginHandler:
    # 使用二维码登录
    def qr_login(self):
        login.login_with_qrcode_term()