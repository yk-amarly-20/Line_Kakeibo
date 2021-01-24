from flask import Flask, request, abort
import os
from os.path import join, dirname
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    RichMenu, RichMenuArea, RichMenuSize, RichMenuBounds,
    MessageAction, rich_menu
)
from linebot.models.messages import Message
# import settings
# from package import config, reply, AppHandler
from package import AppHandler
# from package.rich_menu import createRichMenu

app = Flask(__name__)


CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

"""
rich_menu_list = line_bot_api.get_rich_menu_list()
if not rich_menu_list:
    result = createRichMenu(line_bot_api)
"""
"""
    if not result:
        reply.reply_message(event, message)
"""

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
    """
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )
    """
    AppHandler.TextMessage(line_bot_api, event)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
