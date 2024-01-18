import flask

from app import app
from flask import render_template, request, redirect, url_for, session
from utils import get_db_connection
from models.client_installs_model import *
from models.client_index_model import get_clients


@app.route('/install', methods=['GET'])
def set_install():
    conn = get_db_connection()
    df_clients = get_clients(conn)

    df_title = ['Машина', 'Устройства', 'Адрес', 'Дата', 'Время', 'Статус']
    title_purc = ['Устройства', 'Статус']

    if request.values.get('fullname'):
        client_id = request.values.get('client_id')
        session['client_id'] = client_id

    df_installs = get_client_installs(conn, session['client_id'])

    df_purcases = get_client_purcases(conn, session['client_id'])

    return render_template("client_installs.html",
                           combo_box=df_clients,
                           title_purcases=title_purc,
                           purcases=df_purcases,
                           len=len)
