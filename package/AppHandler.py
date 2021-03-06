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
        result = rich_menu.createRichMenu(line_bot_api)
        if not result:
            reply_message = TextSendMessage(text="リッチメニューを表示できません")
            reply.reply_message(event, reply_message)
    elif message == config.RESISTER:
        pass
    else:
        reply_message = TextSendMessage(text=message)
        reply.reply_message(event, reply_message)
