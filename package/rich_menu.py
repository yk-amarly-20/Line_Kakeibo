from linebot.models import (
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds,
    MessageAction
)
from linebot import LineBotApi
from package import config

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
                )
            ]
        )

        richMenuId = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)

        path = "../images/test.jpg"

        with open(path, "rb") as f:
            line_bot_api.set_rich_menu_image(richMenuId, "image/jpg", f)

        line_bot_api.set_default_rich_menu(richMenuId)

        result = True

    except Exception:
        result = False

    return result
