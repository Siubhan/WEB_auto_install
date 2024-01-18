from app import app
from flask import render_template, request, redirect, url_for, session
from utils import get_db_connection
from models.installer_schedule_model import *
from models.client_schedule_model import get_boxes


@app.route('/installer_schedule', methods=['get'])
def show_schedule():
    conn = get_db_connection()
    df_boxes = get_boxes(conn)

    init_schedule(conn)
    edit_schedule(conn)


    # df_statuses = get_all_statuses(conn)
    # df_title = ['Машина', 'Адрес', 'Дата установки', 'Время', 'Статус']
    return render_template("installer_schedule.html",
                           boxes=df_boxes,
                           len=len)
