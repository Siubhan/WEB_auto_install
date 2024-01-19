import flask

from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection
from models.client_index_model import *


def normalize_sql(filtred_prod, filtred_type):
    if not len(filtred_prod):
        filtred_prod = ''
    elif len(filtred_prod) == 1:
        filtred_prod = f"= '{filtred_prod[0]}'"
    else:
        filtred_prod = ', '.join([f"'{data}'" for data in filtred_prod])
        filtred_prod = f'in ({filtred_prod})'

    if not len(filtred_type):
        filtred_type = ''
    elif len(filtred_type) == 1:
        filtred_type = f"= '{filtred_type[0]}'"
    else:
        filtred_type = ', '.join([f"'{data}'" for data in filtred_type])
        filtred_type = f'in ({filtred_type})'

    return filtred_prod, filtred_type


@app.route('/', methods=['get', 'post'])
def index():
    conn = get_db_connection()
    df_catalog = get_catalog(conn)
    df_clients = get_clients(conn)

    if request.method == 'POST':
        print(request.json)
        session['data'] = request.json
        # ! Не работает редирект
        return redirect(url_for('set_schedule', _method='POST'), code=302)

    # нажата кнопка Найти
    if request.values.get('client'):
        client_id = request.values.get('client_id')
        session['client_id'] = client_id

    elif request.values.get('itemName'):
        searched_item = request.args.get('itemName')
        df_catalog = get_products(conn, searched_item)

    elif request.values.get('filter'):
        filtred_prod = tuple(request.args.getlist('producer'))
        filtred_type = tuple(request.args.getlist('name'))

        filtred_prod, filtred_type = normalize_sql(filtred_prod, filtred_type)

        df_catalog = get_filtred(conn, filtred_prod, filtred_type)

    elif request.values.get('reset'):
        df_catalog = get_catalog(conn)

    elif request.values.get('new_client'):

        client_name = request.values.get("client_name")
        client_phone = request.values.get("client_phone")
        client_is_partner = request.values.get("client_partner")

        session['client_id'] = create_new_client(conn, client_name, client_phone, client_is_partner)
    elif request.values.get('noselect'):
        a = 1
    else:
        session['client_id'] = 1

    catalog_h = ['Артикул', 'Тип устройства', 'Название',
                 'Цена', 'В наличии', 'Производитель', 'Цена установки']
    df_filters_producer = get_filters_producer(conn)
    df_filters_type = get_filters_type(conn)

    html = render_template(
        'client_index.html',
        client_id=session['client_id'],
        combo_box=df_clients,
        catalog=df_catalog,
        catalog_header=catalog_h,
        producers=df_filters_producer,
        device_types=df_filters_type,
        len=len
    )

    return html


@app.route('/buy', methods=['post'])
def buy_systems():
    conn = get_db_connection()
    client_id = session['client_id']
    data = request.json
    df_catalog = get_catalog(conn)
    df_clients = get_clients(conn)
    catalog_h = ['Артикул', 'Тип устройства', 'Название',
                 'Цена', 'В наличии', 'Производитель', 'Цена установки']
    df_filters_producer = get_filters_producer(conn)
    df_filters_type = get_filters_type(conn)

    insert_systems(conn, client_id, data)

    html = render_template(
        'client_index.html',
        client_id=session['client_id'],
        combo_box=df_clients,
        catalog=df_catalog,
        catalog_header=catalog_h,
        producers=df_filters_producer,
        device_types=df_filters_type,
        len=len
    )

    return html
