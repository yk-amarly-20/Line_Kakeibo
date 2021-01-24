from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import MessageEvent
from linebot.models.send_messages import TextSendMessage
from package import reply, config, rich_menu

# とりあえずテスト用
def TextMessage(line_bot_api: LineBotApi, event: MessageEvent):
    message: str = event.message.text

    if message == config.MENU:
        # reply_message = TextSendMessage(text="いいね")
        # reply.reply_message(event, reply_message)
        rich_menu.createRichMenu(line_bot_api)
    elif message == "No":
        reply_message = TextSendMessage(text="いいえ")
        reply.reply_message(event, reply_message)
    else:
        reply_message = TextSendMessage(text=message)
        reply.reply_message(event, reply_message)
