from package.db import *
import datetime

# 定期実行するスクリプト

def get_year_and_month():
    current_time = datetime.datetime.now()
    year = current_time.year
    month = current_time.month

    return year, month

def main():
    year, month = get_year_and_month()
    new_table_name = create_table_name(year, month)
    old_table_name = create_table_name(year - 2, month)

    drop_table(old_table_name)
    create_table(new_table_name)

if __name__ == "__main__":
    main()
