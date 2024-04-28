# 处理登录账号

# from bilibili_api import login
# from bilibili_api import settings
# from bilibili_api import user,sync
from pprint import pprint
from utils import utils
from PIL import Image

class LoginHandler:

    def __init__(self):
        # settings.proxy = "http://127.0.0.1:7890"
        # settings.timeout = 1.0
        # settings.http_client = settings.HTTPClient.AIOHTTP # default
        # settings.request_log = True
        # settings.wbi_retry_times = 10 # defaults to 3
        # self.url = "https://passport.bilibili.com/x/passport-login/web/qrcode/generate"
        # self.headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        # }
        pass

    # 使用二维码登录
    def qr_login(self):
        # 读取配置文件
        config = utils.load_json_file(path="./config/config.json")

        # 访问申请二维码
        # url_get_qrcode: 访问申请二维码，获取qrcode_key
        url_get_qrcode = config['url']['url_get_qrcode']

        # url_check_scan: 访问获取登录状态
        # url_check_scan = config['url']['url_check_scan']

        headers = config['headers']

        # 保存二维码图片，并获取对应的qrcode_key
        qrcode_key = utils.save_img(url=url_get_qrcode, headers=headers, img_location=config['qrcode_location'])
        # 打开保存的二维码图片
        img = Image.open(config['qrcode_location'])

        print("请扫描二维码登录")
        # 显示二维码图片
        img.show()