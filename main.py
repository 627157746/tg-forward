import asyncio
import json
import requests
import logging
from telethon import TelegramClient, events
from config import *
import socks

# 设置日志
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# 初始化Telegram客户端
# 根据配置决定是否使用代理
proxy = None
if USE_PROXY:
    proxy = (socks.SOCKS5, PROXY_HOST, PROXY_PORT)

client = TelegramClient(
    'session',
    TG_API_ID,
    TG_API_HASH,
    proxy=proxy
)

def send_to_wecom(message):
    """发送消息到企业微信机器人"""
    url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={WECOM_BOT_KEY}'
    headers = {'Content-Type': 'application/json'}

    data = {
        'msgtype': 'text',
        'text': {
            'content': message
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        result = response.json()
        if result.get('errcode') != 0:
            logger.error(f"发送到企业微信失败: {result}")
        return result
    except Exception as e:
        logger.error(f"发送到企业微信异常: {str(e)}")
        return None

@client.on(events.NewMessage(chats=TG_GROUP_USERNAME))
async def handler(event):
    """处理新消息事件"""
    try:
        # 获取消息内容
        message = event.message
        sender = await event.get_sender()

        # 检查消息是否包含屏蔽关键词
        if message.text:
            for keyword in BLOCKED_KEYWORDS:
                if keyword.lower() in message.text.lower():
                    logger.info(f"消息包含屏蔽关键词 '{keyword}'，不转发")
                    return

        # 构建转发消息格式
        forward_msg = f'{message.text}\n'

        # 发送到企业微信
        send_to_wecom(forward_msg)
    except Exception as e:
        logger.error(f"处理消息异常: {str(e)}")

async def main():
    try:
        # 连接到Telegram
        await client.start()
        logger.info('Telegram client started')

        # 运行直到断开连接
        await client.run_until_disconnected()
    except Exception as e:
        logger.error(f"运行异常: {str(e)}")
        raise

async def run_with_retries():
    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        try:
            await main()
            break
        except Exception as e:
            retry_count += 1
            logger.error(f"第 {retry_count} 次重试失败: {str(e)}")
            if retry_count < max_retries:
                logger.info(f"等待 5 秒后重试...")
                await asyncio.sleep(5)
            else:
                logger.error("已达到最大重试次数，程序退出")

if __name__ == '__main__':
    asyncio.run(run_with_retries())



