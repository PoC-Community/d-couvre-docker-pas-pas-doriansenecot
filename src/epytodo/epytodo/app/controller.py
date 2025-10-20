from app import *
from app.models import *
from flask import request, jsonify
from json_return import *
import pymysql as sql
import session

@app.route('/register', methods = ['POST'])
def register_user():
    if request.headers['Content-Type'] == 'application/json' :
        data = request.json
    else:
        data = request.form
    username = data['username']
    password = data['password']
    if (user_exists(username)):
        return jsonify(REGISTER_ERR)
    else:
        add_user_to_sql(username, password)
    return jsonify(REGISTER_RES)


@app.route('/signin', methods = ['GET', 'POST'])
def user_login():
    if request.headers['Content-Type'] == 'application/json' :
        data = request.json
    else:
        data = request.form
    username = data['username']
    password = data['password']
    if not user_exists(username):
        return jsonify(SIGNIN_ERR)
    elif not compare_password(username, password):
        return jsonify(SIGNIN_ERR)
    else:
        session.session = get_user_id(username)
        return jsonify(SIGNIN_RES)


@app.route('/signout', methods = ['POST', 'GET'])
def user_signout():
    session.session = -1
    return jsonify(SIGNOUT_RES)


@app.route('/user', methods = ['GET'])
def user_info():
    id = session.session
    username = get_username_from_id(id);
    if (username == USER_ERR):
        return jsonify(USER_ERR)
    return jsonify({"result" :{"Username" : username,"ID" : id}})


@app.route('/user/task', methods = ['GET'])
def user_all_task():
    return jsonify(get_user_tasks())


@app.route('/user/task/<int:task_id>', methods = ['GET'])
def user_special_task(task_id):
    return jsonify(get_one_task(task_id))


@app.route('/user/task/add', methods = ['POST'])
def user_create_task():
    if request.headers['Content-Type'] == 'application/json' :
        data = request.json
    else:
        data = request.form
    title = data['title']
    begin = data['begin']
    end = data['end']
    status = data['status']
    return jsonify(create_task(title, begin, end, status))


@app.route('/user/task/del/<int:task_id>', methods = ['POST'])
def user_delete_task(task_id):
    if (task_exists(task_id)):
        delete_task(task_id)
        return jsonify(TASK_ID_DEL_RES)
    else:
        return jsonify(TASK_ID_DEL_ERR)
