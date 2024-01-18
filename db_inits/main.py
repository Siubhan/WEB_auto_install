import sqlite3
import pandas as pd
from scripts import *
from fill_db import *
from init_db import *

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('max_colwidth', None)

    connect = sqlite3.connect('supplies.db')
    cursor = connect.cursor()
    # # * init db
    # cursor.executescript(init_db)
    #
    # # * fill db
    # cursor.executescript(fill_script)
    # cursor.executescript(fill_cars)
    # cursor.executescript(fill_client_cars)
    #
    # # * edit scripts
    # cursor.executescript(edit_1)
    # cursor.execute(edit_3)

    # * select scripts
    df = pd.read_sql(select_1, connect)
    print(df)

    print('\n--------\n')
    df = pd.read_sql(select_2, connect)
    print(df)

    # * group scripts
    print('\n--------\n')
    df = pd.read_sql(group_1, connect)
    print(df)

    print('\n--------\n')
    df = pd.read_sql(group_2, connect)
    print(df)

    # * table scripts
    print('\n--------\n')
    df = pd.read_sql(complex_1, connect)
    print(df)

    print('\n--------\n')
    df = pd.read_sql(complex_2, connect)
    print(df)

    connect.commit()
    connect.close()




