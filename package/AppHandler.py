from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import MessageEvent
from linebot.models.send_messages import TextSendMessage
from package import reply


def TextMessage(event: MessageEvent):
    message: str = event.message.text

    if message == "Yes":
        reply_message = TextSendMessage(text="いいね")
        reply.reply_message(event, reply_message)
    elif message == "No":
        reply_message = TextSendMessage(text="いいえ")
        reply.reply_message(event, reply_message)
    else:
        reply_message = TextSendMessage(text=message)
        reply.reply_message(event, reply_message)
