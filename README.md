# Telegram 消息转发到企业微信机器人

将 Telegram 群组消息自动转发到企业微信机器人。

## 功能特点

- 监听指定 Telegram 群组的消息
- 自动转发到企业微信机器人
- 支持屏蔽包含特定关键词的消息
- 支持代理配置
- Docker 部署

## 环境要求

- Docker
- Docker Compose

## 快速开始

1. 克隆仓库
```bash
git clone <repository_url>
cd tg-forward
```

2. 配置环境变量
```bash
cp .env.example .env
```
然后编辑 `.env` 文件，填入你的配置：
```bash
# Telegram配置
TG_API_ID=your_api_id          # Telegram API ID
TG_API_HASH=your_api_hash      # Telegram API Hash
TG_GROUP_USERNAME=group_name   # 要监听的群组用户名

# 企业微信机器人配置
WECOM_BOT_KEY=bot_key         # 企业微信机器人 key

# 可选代理配置
USE_PROXY=false               # 是否使用代理
PROXY_HOST=127.0.0.1         # 代理主机地址
PROXY_PORT=7890              # 代理端口

# 屏蔽关键词配置
BLOCKED_KEYWORDS=关键词1,关键词2,关键词3  # 用逗号分隔的关键词列表
```

3. 首次运行（用于验证 Telegram 账号）
```bash
docker-compose run --rm tg-forward
```

4. 正常运行
```bash
docker-compose up -d
```

## 目录结构

```
.
├── main.py           # 主程序
├── config.py         # 配置文件
├── requirements.txt  # Python 依赖
├── Dockerfile        # Docker 构建文件
├── docker-compose.yml # Docker Compose 配置
├── .env.example     # 环境变量示例
└── .env             # 实际环境变量配置（不提交到git）
```

## 注意事项

1. 首次运行需要进行 Telegram 账号验证
2. 确保企业微信机器人的 webhook 地址可以正常访问
3. 如果使用代理，确保代理服务器可用
4. 不要将 `.env` 文件提交到 git 仓库

## 日志

日志会输出到 Docker 容器的标准输出，可以通过以下命令查看：
```bash
docker logs -f tg-forward
```