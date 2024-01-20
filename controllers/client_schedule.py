from app import app
from flask import render_template, request, redirect, url_for, session
from utils import get_db_connection
from models.client_schedule_model import *
from models.client_index_model import get_clients


@app.route('/schedule', methods=['get', 'post'])
def set_schedule():
    conn = get_db_connection()
    if request.method == 'POST':
        date_dict = request.json
        print(date_dict, session['client_id'], session['data'])
        enroll_install(conn, date_dict, session['client_id'], session['data'])

        return redirect(url_for('index'))

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
                           client_id=session['client_id'],
                           box_id=session['box_id'],
                           combo_box=df_clients,
                           boxes=df_boxes,
                           schedule=df_schedule,
                           dates=df_dates,
                           len=len)