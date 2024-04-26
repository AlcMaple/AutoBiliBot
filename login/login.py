# -*- coding: utf-8 -*-
# @Author  : 2933724627wab@gmail.com
# @Time    : 2024/4/22 20:59
# @Desc    : bilibli登录实现类

from base_crawler import AbstractLogin
from playwright.sync_api import BrowserContext, Page
from typing import Optional
import utils

class BilibiliLogin(AbstractLogin):
    def __init__(self, 
                 login_type:str,
                 browser_context:BrowserContext,
                 context_page:Page,
                 login_phone:Optional[str]="",
                 cookie_str:str = ""):
        
        # 登录方法

        self.login_type = login_type
        self.browser_context = browser_context
        self.context_page = context_page
        self.login_phone = login_phone
        self.cookie_str = cookie_str

    async def begin(self):

        utils.logger.info("开始使用二维码登录哔哩哔哩网站")

        if self.login_type == "qrcode":
            await self.login_by_qrcode()
        else:
            raise ValueError("登录类型错误，请检查login_type参数")

    # 使用二维码登录哔哩哔哩网站，并保持浏览器登录状态
    async def login_by_qrcode(self):