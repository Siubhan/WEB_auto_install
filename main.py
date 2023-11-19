import sqlite3
from scripts import *
from fill_db import *
from init_db import *

if __name__ == '__main__':
    connect = sqlite3.connect('supplies.db')
    cursor = connect.cursor()
    # init db
    # cursor.executescript(init_db)

    # fill db
    cursor.executescript(fill_script)

    # scripts execution
    # cursor.execute(script_3)
    # cursor.executescript(script_4)
    # cursor.execute(script_5)
    # print(cursor.fetchall())

    connect.commit()
    connect.close()


    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    # pd.set_option('max_colwidth', None)
    # df = pd.read_sql(script_4, connect)
    # print(df)
