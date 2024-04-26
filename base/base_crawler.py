# 导入抽象基类和方法的装饰器
from abc import ABC, abstractmethod
# 导入类型提示
from typing import Dict, Optional

from playwright.async_api import BrowserContext,BrowserType

class AbstractCrawler(ABC):
    # 初始化配置
    @abstractmethod
    def init_config(self,platform:str,login_type:str,crawler_type:str,start_page:int,keyword:str):
        pass

    # 开始执行
    @abstractmethod
    async def start(self):
        pass

    # 搜索
    @abstractmethod
    async def search(self):
        pass

    # 启动浏览器
    @abstractmethod
    async def launch_browser(self,chromium:BrowserType,
                             playwright_proxy:Optional[Dict],user_agent:Optional[str],
                             headless:bool = True) -> BrowserContext:
        pass

class AbstractLogin(ABC):
    # 开始登录
    @abstractmethod
    async def begin(self):
        pass

    # 通过二维码登录
    @abstractmethod
    async def login_by_qrcode(self):
        pass

