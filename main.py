from logging import Handler
import dotenv
from flask import Flask, request, abort
import os
from os.path import join, dirname
from dotenv import load_dotenv
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
from linebot.models.messages import Message
import settings

app = Flask(__name__)

CHANNEL_ACSESS_TOEKEN = settings.CHANNEL_ACCESS_TOKEN
CHANNEL_SECRET = settings.CHANNEL_SECRET

line_bot_api = LineBotApi(CHANNEL_ACSESS_TOEKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

if __name__ == "__main__":
    app.run()
