import os
from linebot.models import (
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds,
    MessageAction
)
from linebot import LineBotApi
from linebot.models.send_messages import TextSendMessage
from package import config, reply

def createRichMenu(line_bot_api: LineBotApi) -> bool:
    result = False
    try:
        rich_menu_to_create = RichMenu(
            size = RichMenuSize(width=1200, height=405),
            selected = True,
            name = "リッチメニュー",
            chat_bar_text = "TAP HERE",
            areas = [
                RichMenuArea(
                    bounds=RichMenuBounds(x=0, y=0, width=480, height=405),
                    action=MessageAction(text=config.RESISTER)
                ),
                RichMenuArea(
                    bounds=RichMenuBounds(x=480, y=0, width=480, height=405),
                    action=MessageAction(text=config.BROWSE)
                ),
                RichMenuArea(
                    bounds=RichMenuBounds(x=480, y=0, width=480, height=405),
                    action=MessageAction(text=config.MODIFY)
                )
            ]
        )

        richMenuId = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)

        path = "images/rich_menu_v1.png"

        if os.path.exists(path):
            with open(path, "rb") as f:
                line_bot_api.set_rich_menu_image(richMenuId, "image/jpeg", f)
        else:
            print("画像がありません")

        line_bot_api.set_default_rich_menu(richMenuId)

        result = True

    except Exception as e:
        result = False
        print("======error context======")
        print("type: {}", str(type(e)))
        print("args: {}", str(e.args))
        print("message: {}", e.message)
        print("e: {}", str(e))

    return result
