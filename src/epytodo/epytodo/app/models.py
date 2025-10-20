#!/usr/bin/env python3

import pymysql as sql
import hashlib
import datetime
from config import *
from json_return import *
import session

db = sql.connect( host = DATABASE_HOST, port = 3306, user = DATABASE_USER, passwd = DATABASE_PASS, db = DATABASE_NAME )

def hash_passwd(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def add_user_to_sql(username, password):
    password = hash_passwd(password)
    cursor = db.cursor()
    sql = "INSERT INTO user(username, password) VALUES ('%s', '%s')" % (username, password)
    cursor.execute(sql)
    db.commit()


def user_exists(username):
    cursor = db.cursor()
    sql = "SELECT COUNT(1) FROM user WHERE username = '%s'" % (username)
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    if (result == 1):
        return True
    else:
        return False


def compare_password(username, password):
    cursor = db.cursor()
    sql = "SELECT password FROM user WHERE username = '%s'" % (username)
    cursor.execute(sql)
    db_pwd = cursor.fetchone()[0]
    new_crypted = hash_passwd(password)
    if (db_pwd == new_crypted):
        return True
    else:
        return False


def get_user_id(username):
    cursor = db.cursor()
    sql = "SELECT user_id FROM user WHERE username = '%s'" % (username)
    cursor.execute(sql)
    user_id = cursor.fetchone()[0]
    return user_id


def get_username_from_id(user_id):
    if (user_id < 0):
        return USER_ERR
    cursor = db.cursor()
    sql = "SELECT username FROM user WHERE user_id = '%d'" % (user_id)
    cursor.execute(sql)
    username = cursor.fetchone()[0]
    return username


def show_users_data():
    cursor = db.cursor()
    sql = 'SELECT * FROM user;'
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        user_id = row[0]
        name = row[1]
        password = row[2]
        print ("id = %d, name = %s, password = %s" % (user_id, name, password))


def create_task(title, begin, end, status):
    if (session.session == -1):
        return TASK_ID_ADD_ERR
    cursor = db.cursor()
    sql = "INSERT INTO task(title, begin, end, status) VALUES ('%s', '%s', '%s', '%s')" % (title, begin, end, status)
    cursor.execute(sql)
    db.commit()
    cursor.execute('SELECT * FROM task;')
    results = cursor.fetchall()
    for row in results:
        task_id = row[0]
    cursor.execute("INSERT INTO user_has_task(fk_user_id, fk_task_id) VALUES ('%d', '%d')" % (session.session, task_id))
    db.commit()
    return TASK_ID_ADD_RES

def task_exists(id):
    cursor = db.cursor()
    sql = "SELECT COUNT(1) FROM task WHERE task_id = %d" % (id)
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    if (result == 1):
        return True
    else:
        return False


def delete_task(id):
    cursor = db.cursor()
    sql = "DELETE FROM task WHERE task_id = %d" % (id)
    cursor.execute(sql)
    db.commit()


def modify_task(id, title, begin, end, status):
    cursor = db.cursor()
    if (task_exists(id) == False):
        return TASK_ID_MOD_ERR
    sql = "UPDATE task SET title = '%s', begin = '%s', end = '%s', status = '%s' WHERE task_id = %d" % (title, begin, end, status, id)
    cursor.execute(sql)
    db.commit()
    return TASK_ID_MOD_RES

def get_user_tasks():
    cursor = db.cursor()
    user = get_username_from_id(session.session)
    if (user == USER_ERR):
        return USER_ERR
    if (user_exists(user) == False):
        return USER_ERR
    cursor.execute("SELECT fk_task_id FROM user_has_task WHERE fk_user_id = '%d'" % (session.session))
    results = cursor.fetchall()
    task_list = []
    for task_id in results:
        cursor.execute("SELECT * FROM task WHERE task_id = '%d'" %(task_id[0]))
        current_task = cursor.fetchall()
        if current_task:
            title = current_task[0][1]
            begin = current_task[0][2]
            end = current_task[0][3]
            status = current_task[0][4]
            task_list.append({str(task_id[0]) : {'title': title, 'begin' : begin, 'end' : end, 'status' : status}})
    return {'result' : { 'tasks' : task_list}}

def get_one_task(task_id):
    cursor = db.cursor()
    user = get_username_from_id(session.session)
    if (user == USER_ERR):
        return USER_ERR
    if (user_exists(user) == False):
        return USER_ERR
    cursor.execute("SELECT * FROM task WHERE task_id = '%d'" % (task_id))
    current_task = cursor.fetchall()
    if not current_task:
        return TASK_ID_MOD_ERR
    current_task = current_task[0]
    title = current_task[1]
    begin = current_task[2]
    end = current_task[3]
    status = current_task[4]
    return ({str(task_id) : {'title': title, 'begin' : begin, 'end' : end, 'status' : status}})

def show_tasks():
    cursor = db.cursor()
    sql = 'SELECT * FROM task;'
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        task_id = row[0]
        title = row[1]
        begin = row[2]
        end = row[3]
        status = row[4]
        print ("id = %d, title = %s, begin = %s, end = %s, status = %s" % (task_id, title, begin, end, status))
