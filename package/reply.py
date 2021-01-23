from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
import os

CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

def reply_message(event, message):
    line_bot_api.reply_message(
        event.reply_token,
        message
    )
