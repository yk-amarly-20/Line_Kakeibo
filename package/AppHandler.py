from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import MessageEvent
from package import reply


def TextMessage(event):
    message = event.message.text

    if message == "Yes":
        reply.reply_message(event, "いいね")
    elif message == "No":
        reply.reply_message(event, "いいえ")
    else:
        reply.reply_message(event, message)
