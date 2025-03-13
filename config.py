import os
from dotenv import load_dotenv

load_dotenv()

# Telegram配置
TG_API_ID = os.getenv('TG_API_ID')
TG_API_HASH = os.getenv('TG_API_HASH')
TG_GROUP_USERNAME = os.getenv('TG_GROUP_USERNAME')


# 企业微信机器人配置
WECOM_BOT_KEY = os.getenv('WECOM_BOT_KEY')

# 代理配置
USE_PROXY = os.getenv('USE_PROXY', 'false').lower() == 'true'
PROXY_HOST = os.getenv('PROXY_HOST', '127.0.0.1')
PROXY_PORT = int(os.getenv('PROXY_PORT', '7890')) 

# 屏蔽关键词配置
BLOCKED_KEYWORDS = os.getenv('BLOCKED_KEYWORDS', '').split(',')
BLOCKED_KEYWORDS = [keyword.strip() for keyword in BLOCKED_KEYWORDS if keyword.strip()] 