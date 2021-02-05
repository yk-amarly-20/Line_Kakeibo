from linebot.models import PostbackEvent
import json
import datetime
from .db import *

class PostbackHandler():
    def __init__(self, event):
        self.event = json.loads(event)
        self.event_type = self.event.get("type")
        self.event_data = self.event.get("data")
        if self.event_type != "process":
            return

    def handle_event(self):
        self.insert_data()

    def insert_data(self):
        # データを挿入する
        category = self.event.get("category")
        date = self.event.get("date")
        year, month, day = self.date_to_str(date)
        money = self.event.get("money")
        remarks = self.event.get("remarks")
        table_name = create_table_name(year, month)
        insert_data(category, table_name, money, day, remarks)

    def date_to_str(self, date: str):
        year, month, day = list(map(int, date.split("-")))

        return (year, month, day)
