from start.BiliAutoReply import BiliAutoReply
# 导入异步I/O、事件循环模块
import asyncio
import sys

async def main():
    pass

if __name__ == '__main__':
    # # 实例化BiliAutoReply类,并调用run方法
    # BiliAutoReply().run()
    try:
        # 运行主异步函数，使用异步可以在后期等待I/O操作的同时并发的去执行其他任务，无需等待
        asyncio.get_event_loop().run_until_complete(main())
    # Ctrl + C 退出程序
    except KeyboardInterrupt:
        sys.exit()