from app import app
from flask import render_template, request, redirect, url_for, session
from utils import get_db_connection
from models.installer_sales_model import *


@app.route('/installer_sales', methods=['get'])
def sell_items():
    conn = get_db_connection()
    df_sales = get_all_sales(conn)
    df_statuses = get_all_statuses(conn)
    df_title = ['ФИО','Телефон','Машина', 'Адрес', 'Дата установки', 'Время', 'Статус']
    return render_template("installer_sale.html",
                           sales=df_sales,
                           statuses=df_statuses,
                           table_title=df_title,
                           len=len)
