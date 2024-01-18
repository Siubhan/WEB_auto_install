from app import app
from flask import render_template, request, redirect, url_for, session
from utils import get_db_connection
from models.client_schedule_model import *
from models.client_index_model import get_clients


@app.route('/schedule', methods=['get', 'post'])
def set_schedule():
    conn = get_db_connection()

    if request.method == 'POST':
        session['data'] = request.json
        print(session['data'])

    if request.values.get('fullname'):
        client_id = request.values.get('client_id')
        session['client_id'] = client_id
    elif request.values.get('address'):
        box_id = request.values.get('box_id')
        session['box_id'] = box_id
    else:
        session['box_id'] = 1

    df_clients = get_clients(conn)
    df_boxes = get_boxes(conn)
    df_schedule = get_schedule_box(conn, session['box_id'])
    df_dates = get_dates(conn)

    return render_template("client_schedule.html",
                           combo_box=df_clients,
                           boxes=df_boxes,
                           schedule=df_schedule,
                           dates=df_dates,
                           len=len)
