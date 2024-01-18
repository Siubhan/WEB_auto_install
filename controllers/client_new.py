from app import app
from flask import render_template, request, redirect, url_for, session
from models import client_index_model
from utils import get_db_connection


@app.route('/new_client', methods=['get'])
def new_client_get():
    return render_template("new_client.html")


@app.route('/new_client_post', methods=['post'])
def new_client_post():
    conn = get_db_connection()

    client_name = request.values.get("client_name")
    client_phone = request.values.get("client_phone")
    client_is_partner = request.values.get("client_partner")

    if client_is_partner is 'on':
        client_is_partner = True
    else:
        client_is_partner = False

    inserted_id = client_index_model.create_new_client(conn, client_name, client_phone, client_is_partner)

    session["client_id"] = inserted_id

    return redirect(url_for("index"))
