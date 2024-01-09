import random

import telebot
from telebot import types
import sqlite3
import os
from datetime import datetime, timedelta

bot = telebot.TeleBot('6373983672:AAFJPyO1sR_nAm0ae3A4qeR-vhWExuRk7i8')
checked_event_index = 0


def check_user_exists(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    except sqlite3.OperationalError:
        return False
    user = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if len(user) == 0:
        return False
    if user[0][6] is None:
        return False
    return True


def check_user_exists_by_uid(uid):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM users WHERE id = ?', (uid,))
    except sqlite3.OperationalError:
        return False
    user = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if len(user) == 0:
        return False
    if user[0][6] is None:
        return False
    return True


def check_name_exists(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if user[0][2] is None:
        return False
    else:
        return True


def set_name(user_id, name):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET name = ? WHERE user_id = ?', (name, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def check_age_exists(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if user[0][3] is None:
        return False
    else:
        return True


def set_age(user_id, age):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET age = ? WHERE user_id = ?', (age, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def check_gender_exists(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if user[0][4] is None:
        return False
    else:
        return True


def set_gender(user_id, gender):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET gender = ? WHERE user_id = ?', (gender, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def check_school_exists(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if user[0][5] is None:
        return False
    else:
        return True


def user_in_likes_sent(uid, found_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT likes_sent FROM users WHERE id = ?', (uid,))
    likes_sent = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    if f" {found_id}, " in likes_sent:
        return True
    return False


def set_school(user_id, school):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET school = ? WHERE user_id = ?', (school, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_photo(user_id, photo):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET photo = ?, likes_sent = " ", likes_received = " ", seen_friends = " " '
                'WHERE user_id = ?', (photo, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_looking_for(user_id, looking_for):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET looking_for = ? WHERE user_id = ?', (looking_for, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_found_id(user_id, found_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET found_id = ? WHERE user_id = ?', (found_id, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def delete_user(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def delete_first_like_received(user_id, like_received_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT likes_received FROM users WHERE user_id = ?', (user_id,))
    likes_received = cur.fetchall()[0][0]
    likes_received = likes_received.removeprefix(f" {like_received_id},")
    cur.execute('UPDATE users SET likes_received = ? WHERE user_id = ?', (likes_received, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def create_user(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO users (user_id, looking_for) VALUES (?, 1)', (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_photo(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT photo FROM users WHERE user_id = ?', (user_id,))
    photo = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return photo[0][0]


def get_name(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT name FROM users WHERE user_id = ?', (user_id,))
    name = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return name[0][0]


def get_age(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT age FROM users WHERE user_id = ?', (user_id,))
    age = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return age[0][0]


def get_school(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT school FROM users WHERE user_id = ?', (user_id,))
    school = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return school[0][0]


def get_photo_by_id(uid):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT photo FROM users WHERE id = ?', (uid,))
    photo = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return photo[0][0]


def get_name_by_id(uid):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT name FROM users WHERE id = ?', (uid,))
    name = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return name[0][0]


def get_age_by_id(uid):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT age FROM users WHERE id = ?', (uid,))
    age = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return age[0][0]


def get_school_by_id(uid):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT school FROM users WHERE id = ?', (uid,))
    school = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return school[0][0]


def get_found_id(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT found_id FROM users WHERE user_id = ?', (user_id,))
    found_id = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return found_id[0][0]


def get_amount_of_users():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) AS user_count FROM users')
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return result[0]


def get_id(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT id FROM users WHERE user_id = ?', (user_id,))
    uid = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return uid[0][0]


def get_user_ids():
    user_ids = []
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT user_id FROM users')
    ids = cur.fetchall()
    for el in ids:
        user_ids.append(el[0])
    conn.commit()
    cur.close()
    conn.close()
    return user_ids


def get_user_uids():
    user_uids = []
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT id FROM users')
    uids = cur.fetchall()
    for el in uids:
        user_uids.append(el[0])
    conn.commit()
    cur.close()
    conn.close()
    return user_uids


def get_amount_of_likes_received(user_id):
    if not check_user_exists(user_id):
        return 0
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT likes_received FROM users WHERE user_id = ?', (user_id,))
    likes_received = cur.fetchall()[0][0]
    amount_of_likes_received = likes_received.count(",")
    conn.commit()
    cur.close()
    conn.close()
    return amount_of_likes_received


def get_user_id(uid):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT user_id FROM users WHERE id = ?', (uid,))
    user_id = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    try:
        return user_id[0][0]
    except IndexError:
        return -1


def get_like_received(user_id):
    if not check_user_exists(user_id):
        return -1
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT likes_received FROM users WHERE user_id = ?', (user_id,))
    likes_received = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    try:
        index = 0
        found_uid = int(likes_received[0][0].lstrip().split(", ")[index])

        while not check_user_exists_by_uid(found_uid):
            delete_first_like_received(user_id, found_uid)
            index += 1
            found_uid = int(likes_received[0][0].lstrip().split(", ")[index])

        return int(likes_received[0][0].lstrip().split(", ")[index])
    except ValueError:
        return -1


def get_likes_received(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT likes_received FROM users WHERE user_id = ?', (user_id,))
    likes_received = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return likes_received


def like_happened(uid, found_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT likes_sent FROM users WHERE id = ?', (uid,))
    likes_sent = cur.fetchall()[0][0]
    if f" {found_id}, " not in likes_sent:
        likes_sent += f"{found_id}, "
        cur.execute('UPDATE users SET likes_sent = ? WHERE id = ?', (likes_sent, uid,))
    cur.execute('SELECT likes_received FROM users WHERE id = ?', (found_id,))
    likes_received = cur.fetchall()[0][0]
    if f" {uid}, " not in likes_received:
        likes_received += f"{uid}, "
        cur.execute('UPDATE users SET likes_received = ? WHERE id = ?', (likes_received, found_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_seen_friends(user_id, found_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT seen_friends FROM users WHERE user_id = ?', (user_id,))
    seen_friends = cur.fetchall()[0][0]
    if f" {found_id}, " not in seen_friends:
        seen_friends += f"{found_id}, "
        cur.execute('UPDATE users SET seen_friends = ? WHERE user_id = ?', (seen_friends, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def clear_seen_friends(user_id):
    likes_received = get_likes_received(user_id)
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET seen_friends = ? WHERE user_id = ?', (likes_received, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def is_in_seen_friends(user_id, found_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT seen_friends FROM users WHERE user_id = ?', (user_id,))
    seen_friends = cur.fetchall()[0][0]
    if f" {found_id}, " not in seen_friends:
        conn.commit()
        cur.close()
        conn.close()
        return False
    conn.commit()
    cur.close()
    conn.close()
    return True


def add_last_seen_event_column():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    try:
        cur.execute('ALTER TABLE users ADD last_seen_event int DEFAULT -1')
    except sqlite3.OperationalError:
        pass
    conn.commit()
    cur.close()
    conn.close()
    return


def set_last_seen_event(user_id, index):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET last_seen_event = ? WHERE user_id = ?', (index, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_last_seen_event(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT last_seen_event FROM users WHERE user_id = ?', (user_id,))
    last_seen_event = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return last_seen_event


def add_last_seen_idea_column():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    try:
        cur.execute('ALTER TABLE users ADD last_seen_idea int DEFAULT -2')
    except sqlite3.OperationalError:
        pass
    conn.commit()
    cur.close()
    conn.close()
    return


def set_last_seen_idea(user_id, index):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET last_seen_idea = ? WHERE user_id = ?', (index, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_last_seen_idea(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT last_seen_idea FROM users WHERE user_id = ?', (user_id,))
    last_seen_idea = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return last_seen_idea


def add_last_seen_question_column():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    try:
        cur.execute('ALTER TABLE users ADD last_seen_question int DEFAULT -2')
    except sqlite3.OperationalError:
        pass
    conn.commit()
    cur.close()
    conn.close()
    return


def set_last_seen_question(user_id, index):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET last_seen_question = ? WHERE user_id = ?', (index, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_last_seen_question(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT last_seen_question FROM users WHERE user_id = ?', (user_id,))
    last_seen_question = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return last_seen_question


def create_events_table():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id int unique,'
                ' event_name varchar(50), event_price int, event_time varchar(50), event_place varchar(150), '
                'event_description varchar(3000), event_photo varchar(300), views int, '
                'post_time varchar(100), is_active int, is_approved int)')
    conn.commit()
    cur.close()
    conn.close()


def create_event(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO events (user_id, views, is_active, is_approved) VALUES (?, 0, 0, 0)', (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_event_name(user_id, event_name):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET event_name = ? WHERE user_id = ?', (event_name, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_event_price(user_id, event_price):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET event_price = ? WHERE user_id = ?', (event_price, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_event_time(user_id, event_time):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET event_time = ? WHERE user_id = ?', (event_time, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_event_place(user_id, event_place):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET event_place = ? WHERE user_id = ?', (event_place, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_event_description(user_id, event_description):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET event_description = ? WHERE user_id = ?', (event_description, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_event_photo(user_id, event_photo):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET event_photo = ? WHERE user_id = ?', (event_photo, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def increment_event_views(user_id):
    views = get_event_views(user_id)

    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET views = ? WHERE user_id = ?', (views + 1, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_event_is_active(user_id, is_active):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET is_active = ? WHERE user_id = ?', (is_active, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_event_is_approved(user_id, is_approved):
    if is_approved == 2:
        bot.send_message(user_id, "Твое мероприятие не прошло модерацию, ты можешь удалить его и "
                                  "создать новое согласно описанным правилам!")
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET is_approved = ? WHERE user_id = ?', (is_approved, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_event_name(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT event_name FROM events WHERE user_id = ?', (user_id,))
    event_name = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return event_name


def get_event_price(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT event_price FROM events WHERE user_id = ?', (user_id,))
    event_price = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return event_price


def get_event_time(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT event_time FROM events WHERE user_id = ?', (user_id,))
    event_time = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return event_time


def get_event_place(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT event_place FROM events WHERE user_id = ?', (user_id,))
    event_place = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return event_place


def get_event_description(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT event_description FROM events WHERE user_id = ?', (user_id,))
    event_description = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return event_description


def get_event_photo(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT event_photo FROM events WHERE user_id = ?', (user_id,))
    event_photo = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return event_photo


def get_event_views(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT views FROM events WHERE user_id = ?', (user_id,))
    event_views = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return event_views


def get_how_long_left_event(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT post_time FROM events WHERE user_id = ?', (user_id,))
    post_time = cur.fetchall()[0][0]
    original_datetime = datetime.strptime(post_time, '%Y-%m-%d %H:%M:%S')
    new_datetime = original_datetime + timedelta(days=2)
    new_string = new_datetime.strftime('%Y-%m-%d %H:%M:%S')
    conn.commit()
    cur.close()
    conn.close()
    return new_string


def get_event_is_active(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT is_active FROM events WHERE user_id = ?', (user_id,))
    is_active = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return is_active


def get_event_is_approved(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT is_approved FROM events WHERE user_id = ?', (user_id,))
    is_approved = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return is_approved


def delete_event(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('DELETE FROM events WHERE user_id = ?', (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def check_event_exists(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    try:
        cur.execute('SELECT event_photo FROM events WHERE user_id = ?', (user_id,))
        try:
            event_photo = cur.fetchall()[0][0]
        except IndexError:
            conn.commit()
            cur.close()
            conn.close()
            return False
        conn.commit()
        cur.close()
        conn.close()
        if event_photo is None:
            return False
        return True
    except sqlite3.OperationalError:
        conn.commit()
        cur.close()
        conn.close()
        return False


def approve_event(user_id):
    current_datetime = datetime.now()
    registration_date = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET post_time = ? WHERE user_id = ?', (registration_date, user_id,))
    conn.commit()
    cur.close()
    conn.close()
    set_event_is_approved(user_id, 1)
    bot.send_message(user_id, "Поздравляем, твое мероприятие прошло модерацию, оно выложено!")
    return


def deactivate_expired_events():
    two_days_ago = datetime.now() - timedelta(days=2)
    two_days_ago_str = two_days_ago.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE events SET is_active = 0 WHERE post_time < ?', (two_days_ago_str,))
    conn.commit()
    cur.close()
    conn.close()


def get_events_not_approved():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM events WHERE is_approved = 0 AND is_active = 1')
    events = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return events


def get_events_approved():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM events WHERE is_approved = 1 AND is_active = 1')
    events = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return events


def get_event_by_name(name):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM events WHERE event_name = ?', (name,))
    event = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return event


def create_ideas_table():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ideas (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id int unique,'
                ' idea_name varchar(50), idea_description varchar(3000))')
    conn.commit()
    cur.close()
    conn.close()


def create_idea(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO ideas (user_id) VALUES (?)', (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def check_idea_exists(user_id):
    index_error = False
    exists = False
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT idea_description FROM ideas WHERE user_id = ?', (user_id,))
    try:
        idea_description = cur.fetchall()[0][0]
        if idea_description is not None:
            exists = True
    except IndexError:
        index_error = True
    conn.commit()
    cur.close()
    conn.close()
    return exists and not index_error


def set_idea_name(user_id, name):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE ideas SET idea_name = ? WHERE user_id = ?', (name, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def set_idea_description(user_id, description):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE ideas SET idea_description = ? WHERE user_id = ?', (description, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_idea_name(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT idea_name FROM ideas WHERE user_id = ?', (user_id,))
    idea_name = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return idea_name


def get_idea_description(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT idea_description FROM ideas WHERE user_id = ?', (user_id,))
    idea_description = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return idea_description


def delete_idea(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('DELETE FROM ideas WHERE user_id = ?', (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_ideas():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM ideas WHERE idea_description IS NOT NULL', )
    ideas = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return ideas


def create_questions_answers_tables():
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id int,'
                ' question varchar(100), post_time varchar(100))')
    cur.execute('CREATE TABLE IF NOT EXISTS answers (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id int,'
                ' question varchar(100), answer varchar(3000))')
    conn.commit()
    cur.close()
    conn.close()


def create_question(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO questions (user_id) VALUES (?)', (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def check_question_exists(uid, user_id):
    exists = True
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute(
        'SELECT question FROM questions WHERE id = ? AND question IS NOT NULL AND user_id != ? AND question NOT IN '
        '(SELECT question FROM answers WHERE user_id = ?)', (uid, user_id, user_id))
    questions = cur.fetchall()
    if len(questions) == 0:
        exists = False
    conn.commit()
    cur.close()
    conn.close()
    return exists


def get_question_by_uid(uid, user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute(
        'SELECT question FROM questions WHERE id = ? AND question IS NOT NULL AND user_id != ? AND question NOT IN '
        '(SELECT question FROM answers WHERE user_id = ?)', (uid, user_id, user_id))
    question = cur.fetchall()[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return question


def create_answer(user_id, question, answer):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO answers (user_id, question, answer) VALUES (?, ?, ?)', (user_id, question, answer))
    conn.commit()
    cur.close()
    conn.close()


def set_question(uid, question):
    current_datetime = datetime.now()
    registration_date = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE questions SET question = ?, post_time = ? '
                'WHERE id = ?', (question, registration_date, uid,))
    conn.commit()
    cur.close()
    conn.close()


def get_asked_questions(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM questions WHERE user_id = ? AND question IS NOT NULL', (user_id,))
    questions = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return questions


def get_questions(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM questions WHERE question IS NOT NULL AND user_id != ? AND question NOT IN '
                '(SELECT question FROM answers WHERE user_id = ?)', (user_id, user_id,))
    questions = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return questions


def get_last_added_question_uid(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM questions WHERE user_id  = ?', (user_id,))
    questions = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return questions[-1][0]


def get_answers(question):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM answers WHERE question  = ? AND answer IS NOT NULL', (question,))
    answers = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return answers


def delete_answer(answer):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('DELETE FROM answers WHERE answer = ?', (answer,))
    conn.commit()
    cur.close()
    conn.close()


def delete_expired_questions():
    one_day_ago = datetime.now() - timedelta(days=1)
    one_day_ago_str = one_day_ago.strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('DELETE FROM questions WHERE post_time < ?', (one_day_ago_str,))
    cur.execute('DELETE FROM answers WHERE question NOT IN (SELECT question FROM questions)')
    conn.commit()
    cur.close()
    conn.close()


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id

    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id int unique, '
                'name varchar(50), age int, gender varchar(10), school varchar(7), photo varchar(200), likes_sent '
                'varchar(30000), likes_received varchar(30000), looking_for int, found_id int, seen_friends '
                'varchar(30000))')

    conn.commit()
    cur.close()
    conn.close()

    if check_user_exists(user_id):
        bot.send_message(message.chat.id, "У тебя уже есть анкета. Используй /menu чтобы начать взаимодействие")
    else:
        delete_user(user_id)
        create_user(user_id)
        bot.send_message(message.chat.id, "Привет, для начала заполним твою анкету. Как тебя зовут?")
        bot.register_next_step_handler(message, ask_age)


def ask_age(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.text.lower() == '/start':
        return start(message)

    if not check_name_exists(user_id):
        name = message.text.strip()
        set_name(user_id, name)
        bot.send_message(message.chat.id, f"Приятно познакомиться, {name}! Сколько тебе лет?")
    else:
        bot.send_message(message.chat.id, f"Введи целое число без букв")
    bot.register_next_step_handler(message, ask_gender)


def ask_gender(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id

    if message.text.lower() == '/start':
        return start(message)

    gender_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Парень 👨')
    btn2 = types.KeyboardButton('Девушка 👩')
    gender_markup.row(btn1, btn2)

    if not check_age_exists(user_id):
        try:
            age = int(message.text.strip())
            set_age(user_id, age)
        except ValueError:
            return ask_age(message)
        bot.send_message(message.chat.id, "Какого ты пола?", reply_markup=gender_markup)
    else:
        bot.send_message(message.chat.id, "Используй кнопки для ответа🫣", reply_markup=gender_markup)
    bot.register_next_step_handler(message, ask_school)


def ask_school(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.text.lower() == '/start':
        return start(message)

    school_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('ИПАМ')
    btn2 = types.KeyboardButton('ВШКМиС')
    btn3 = types.KeyboardButton('ВШФ')
    btn4 = types.KeyboardButton('ВШСГН')
    btn5 = types.KeyboardButton('ВИШ НМИТ')
    btn6 = types.KeyboardButton('ВШЭИБ')
    btn7 = types.KeyboardButton('ВШМ')
    btn8 = types.KeyboardButton('ВШКИ')
    btn9 = types.KeyboardButton('ВШП')
    btn10 = types.KeyboardButton('Преподователь')
    school_markup.row(btn1, btn2)
    school_markup.row(btn3, btn4)
    school_markup.row(btn5, btn6)
    school_markup.row(btn7, btn8)
    school_markup.row(btn9, btn10)

    if not check_gender_exists(user_id):
        if message.text == "Парень 👨" or message.text == "Девушка 👩":
            gender = message.text
            set_gender(user_id, gender)
            bot.send_message(message.chat.id, "C какой ты высшей школы?", reply_markup=school_markup)
            bot.register_next_step_handler(message, ask_photo)

        else:
            return ask_gender(message)
    else:
        bot.send_message(message.chat.id, "Используй кнопки для ответа🫣", reply_markup=school_markup)
        bot.register_next_step_handler(message, ask_photo)


def ask_photo(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id

    if message.text in ['ИПАМ', 'ВШКМиС', 'ВШФ', 'ВШСГН', 'ВИШ НМИТ', 'ВШЭИБ', 'ВШМ', 'ВШКИ', 'ВШП', 'Преподователь']:
        school = message.text
        set_school(user_id, school)
        bot.send_message(message.chat.id,
                         "Теперь отправь свою фотографию, но имей ввиду, другие пользователи смогут ее видеть!")
        bot.register_next_step_handler(message, finish_registration)
    elif check_school_exists(user_id):
        bot.send_message(message.chat.id, "Отправь фотографию🫵")
        bot.register_next_step_handler(message, finish_registration)
    else:
        return ask_school(message)


def finish_registration(message):
    if message.content_type == "text":
        if message.text == '/cancel':
            return cancel(message)
        else:
            return ask_photo(message)
    user_id = message.chat.id
    # Get the photo file_id
    if check_school_exists(user_id) and not check_user_exists(user_id):
        photo_id = message.photo[-1].file_id

        # Download the photo by file_id
        photo_info = bot.get_file(photo_id)
        photo_path = photo_info.file_path
        downloaded_photo = bot.download_file(photo_path)

        # Save the photo to the "photos" folder
        photos_folder = 'photos'
        if not os.path.exists(photos_folder):
            os.makedirs(photos_folder)

        photo_filename = f'{photos_folder}/{photo_id}.jpg'
        with open(photo_filename, 'wb') as photo_file:
            photo_file.write(downloaded_photo)
        photo = photo_filename
        set_photo(user_id, photo)
        bot.send_message(message.chat.id, "Регистрация завершена! \nВведи /menu для поиска знакомств.")

    else:
        bot.send_message(message.chat.id, "К чему здесь эта фотография🤡?")


@bot.message_handler(commands=['profile'])
def profile(message):
    user_id = message.chat.id
    if not check_user_exists(user_id):
        bot.send_message(user_id, "Сначала создай профиль с помощью /start")
        return
    bot.send_message(user_id, "Вот ваш профиль:")
    profile_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Изменить фото')
    btn2 = types.KeyboardButton('Изменить имя')
    btn3 = types.KeyboardButton('Изменить возраст')
    profile_markup.row(btn1)
    profile_markup.row(btn2)
    profile_markup.row(btn3)

    message_text = f"{get_name(user_id)}, {get_age(user_id)}\n{get_school(user_id)}"
    bot.send_photo(user_id, photo=open(get_photo(user_id), 'rb'), caption=message_text, reply_markup=profile_markup)

    bot.register_next_step_handler(message, handle_profile_change)


def handle_profile_change(message):
    if message.text == '/cancel':
        return cancel(message)
    elif message.text == "Изменить фото":
        bot.send_message(message.chat.id, "Отправь новое фото, но имей ввиду, другие пользовтаели смогут его видеть!")
        bot.register_next_step_handler(message, change_photo)
    elif message.text == "Изменить имя":
        bot.send_message(message.chat.id, "Отправь новое имя")
        bot.register_next_step_handler(message, change_name)
    elif message.text == "Изменить возраст":
        bot.send_message(message.chat.id, "Отправь новый возраст")
        bot.register_next_step_handler(message, change_age)
    else:
        bot.send_message(message.chat.id, "Используй кнопки для ответа🫣")
        return profile(message)


def change_photo(message):
    user_id = message.chat.id
    if message.content_type == "text":
        if message.text == '/cancel':
            return cancel(message)
        else:
            bot.send_message(user_id, "Отправь фото")
            bot.register_next_step_handler(message, change_photo)

    elif message.content_type == "photo":
        photo_id = message.photo[-1].file_id

        # Download the photo by file_id
        photo_info = bot.get_file(photo_id)
        photo_path = photo_info.file_path
        downloaded_photo = bot.download_file(photo_path)

        # Save the photo to the "photos" folder
        photos_folder = 'photos'
        if not os.path.exists(photos_folder):
            os.makedirs(photos_folder)

        photo_filename = f'{photos_folder}/{photo_id}.jpg'
        with open(photo_filename, 'wb') as photo_file:
            photo_file.write(downloaded_photo)
        photo = photo_filename

        if not os.path.exists(photo):
            bot.send_message(user_id, "Не удалось изменить фото профиля, попробуйте позже!")
            return

        os.remove(get_photo(user_id))
        set_photo(user_id, photo)
        bot.send_message(user_id, "Фото успешно изменено!")


def change_name(message):
    user_id = message.chat.id
    if message.text == '/cancel':
        return cancel(message)
    else:
        set_name(user_id, message.text)
        bot.send_message(user_id, "Имя успешно изменено")


def change_age(message):
    user_id = message.chat.id
    if message.text == '/cancel':
        return cancel(message)
    else:
        try:
            age = int(message.text)
            set_age(user_id, age)
            bot.send_message(user_id, "Возраст успешно изменен")
            return
        except ValueError:
            bot.send_message(user_id, "Введи целое число")
            bot.register_next_step_handler(message, change_age)


@bot.message_handler(commands=['cancel'])
def cancel(message):
    reply_markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Все действия отменены. Возвращайся, используя /menu",
                     reply_markup=reply_markup)
    return


@bot.message_handler(commands=['delete'])
def delete(message):
    reply_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    reply_markup.row(btn1, btn2)
    bot.send_message(message.chat.id, "Ты уверен что хочешь удалить свой профиль?", reply_markup=reply_markup)
    bot.register_next_step_handler(message, response_to_delete)


def response_to_delete(message):
    if message.text == '/cancel':
        return cancel(message)
    if message.text == "Да":
        delete_user(message.chat.id)
        bot.send_message(message.chat.id, "Ты всегда можешь вернуться при помощи /start. Удачи🤡")
        return

    else:
        bot.send_message(message.chat.id, "Правильно, возвращайся к нам, используя /menu")
        return


@bot.message_handler(commands=['admin'])
def admin(message):
    if message.chat.id == 524931933:
        reply_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, is_persistent=True)
        btn1 = types.KeyboardButton('📈Узнать статистику по боту')
        btn2 = types.KeyboardButton('⚠️Отправить предупреждение')
        btn3 = types.KeyboardButton('👐Привлечь тех, кто не закончил регистрацию')
        btn4 = types.KeyboardButton('😪Попросить поддержку')
        btn5 = types.KeyboardButton('🥳Модерировать мероприятия')
        btn7 = types.KeyboardButton('✅Активировать мероприятия')
        btn6 = types.KeyboardButton('💬Разослать всем сообщение')

        reply_markup.row(btn1, btn2)
        reply_markup.row(btn3, btn4)
        reply_markup.row(btn5, btn7)
        reply_markup.row(btn6)

        bot.send_message(524931933, "Привет, админ! Выбери, что ты хочешь сделать", reply_markup=reply_markup)
        bot.register_next_step_handler(message, handle_admin)


def handle_admin(message):
    if message.text == '/cancel':
        return cancel(message)
    if message.text == "📈Узнать статистику по боту":
        return stats(message)
    elif message.text == "⚠️Отправить предупреждение":
        return warning()
    elif message.text == "👐Привлечь тех, кто не закончил регистрацию":
        return entertain()
    elif message.text == "😪Попросить поддержку":
        return ask_for_support()
    elif message.text == "🥳Модерировать мероприятия":
        return moderate_events(message)
    elif message.text == "✅Активировать мероприятия":
        return handle_admin_activate_event(message)
    elif message.text == "💬Разослать всем сообщение":
        return handle_send_message_to_everyone(message)


def handle_admin_activate_event(message):
    if message.text == '/cancel':
        return cancel(message)
    bot.send_message(message.chat.id, "Введи название мероприятия, которое хочешь активировать")
    bot.register_next_step_handler(message, admin_activate_event)


def admin_activate_event(message):
    if message.text == '/cancel':
        return cancel(message)
    name = message.text
    event = get_event_by_name(name)
    if len(event) == 0:
        bot.send_message(message.chat.id, "Такого мероприятия нет")
    else:
        event_creator_user_id = event[0][1]
        name = event[0][2]
        price = event[0][3]
        time = event[0][4]
        place = event[0][5]
        description = event[0][6]
        photo = event[0][7]
        set_event_is_active(event_creator_user_id, 1)
        text = (f"Это мероприятие активировано:\n{name}\n\n💵Цена: {price}₽\n📅Дата: {time}\n🏠"
                f"Место: {place}\n\n{description}\n\nДля участия пиши:"
                f"@{bot.get_chat_member(event_creator_user_id, event_creator_user_id).user.username}")

        bot.send_photo(524931933, open(photo, "rb"), caption=text, reply_markup=types.ReplyKeyboardRemove())
        return


def stats(message):
    create_ideas_table()
    create_events_table()
    create_questions_answers_tables()
    add_last_seen_question_column()
    add_last_seen_idea_column()
    add_last_seen_event_column()
    count = get_amount_of_users()
    bot.send_message(message.chat.id, f"Кол-во пользователей: {count}")
    return


def entertain():
    user_ids = get_user_ids()
    for user_id in user_ids:
        if not check_user_exists(user_id):
            try:
                bot.send_message(user_id, "Более 400 студентов РЭУ уже ждут тебя! Присоединйся используя /start")
            except telebot.apihelper.ApiTelegramException:
                pass
    return


def warning():
    user_ids = get_user_ids()
    for user_id in user_ids:
        try:
            bot.send_message(user_id, "‼️Внимание‼️\n\nЕсли в твоем профиле содержится информация не "
                                      "соответствующая действительности, в том числе фотография профиля, "
                                      "ваш профиль может быть удален в следующие 24 часа. "
                                      "Изменить профиль - /profile")
        except telebot.apihelper.ApiTelegramException:
            pass
    return


def ask_for_support():
    user_ids = get_user_ids()
    for user_id in user_ids:
        try:
            bot.send_message(user_id,
                             "Расскажи друзьям о боте, разошли его по группам, чтобы усилить наше студенческое "
                             "коммуникационное сообщество! 🌐🤝 \n\n#БотЗнакомствРЭУ")
        except telebot.apihelper.ApiTelegramException:
            pass
    return


def moderate_events(message):
    if message.text == '/cancel':
        return cancel(message)
    global checked_event_index
    events = get_events_not_approved()

    if message.text == "✅":
        approve_event(events[checked_event_index - 1][1])
    elif message.text == "❌":
        set_event_is_approved(events[checked_event_index - 1][1], 2)

    try:
        event_creator_user_id = events[checked_event_index][1]
        name = events[checked_event_index][2]
        price = events[checked_event_index][3]
        time = events[checked_event_index][4]
        place = events[checked_event_index][5]
        description = events[checked_event_index][6]
        photo = events[checked_event_index][7]

    except IndexError:
        bot.send_message(524931933, "Все мероприятия проверены", reply_markup=types.ReplyKeyboardRemove())
        checked_event_index = 0
        return

    text = (f"{name}\n\n💵Цена: {price}₽\n📅Дата: {time}\n🏠"
            f"Место: {place}\n\n{description}\n\nДля участия пиши: "
            f"@{bot.get_chat_member(event_creator_user_id, event_creator_user_id).user.username}")

    moderate_event_markup = types.ReplyKeyboardMarkup(is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("✅")
    btn2 = types.KeyboardButton("❌")

    moderate_event_markup.row(btn1, btn2)
    bot.send_photo(524931933, open(photo, "rb"), caption=text, reply_markup=moderate_event_markup)
    checked_event_index += 1
    bot.register_next_step_handler(message, moderate_events)


def handle_send_message_to_everyone(message):
    bot.send_message(524931933, "Какое сообщение вы хотите отправить?")
    bot.register_next_step_handler(message, send_message_to_everyone)


def send_message_to_everyone(message):
    if message.text == '/cancel':
        return cancel(message)
    media_group = []
    if message.photo:
        # Set the caption only for the first photo
        caption = message.text
        for photo in message.photo:
            file_id = photo.file_id

            media_group.append(types.InputMediaPhoto(media=file_id, caption=caption))
        user_ids = get_user_ids()
        for user_id in user_ids:
            try:
                bot.send_media_group(user_id, media_group)
            except telebot.apihelper.ApiTelegramException:
                pass
    else:
        user_ids = get_user_ids()
        for user_id in user_ids:
            try:
                bot.send_message(user_id, message.text)
            except telebot.apihelper.ApiTelegramException:
                pass
    return


@bot.message_handler(commands=['menu'])
def menu(message):
    user_id = message.chat.id
    if not check_user_exists(user_id):
        bot.send_message(user_id, "Сначала создай профиль, используя /start",
                         reply_markup=types.ReplyKeyboardRemove())
        return
    set_last_seen_idea(user_id, -2)
    set_last_seen_event(user_id, -1)
    set_last_seen_question(user_id, -2)
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
    btn1 = types.KeyboardButton('🤝Знакомства')
    btn2 = types.KeyboardButton('🧠Проекты')
    btn3 = types.KeyboardButton('🥳Мероприятия')
    btn4 = types.KeyboardButton('Другое')

    menu_markup.row(btn1)
    menu_markup.row(btn2)
    menu_markup.row(btn3)
    menu_markup.row(btn4)

    bot.send_message(user_id, "Что тебя интересует?", reply_markup=menu_markup)
    bot.register_next_step_handler(message, handle_menu)


def handle_menu(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id

    if message.text == "🤝Знакомства":
        bot.send_message(user_id, "Привет 👋\nЗдесь ты можешь обрести новые знакомства со студентами и "
                                  "преподователями РЭУ")
        friends_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
        btn1 = types.KeyboardButton('🔍Поиск друзей')
        btn2 = types.KeyboardButton('❤️Лайки на мой профиль')
        btn3 = types.KeyboardButton('Отмена')
        friends_markup.row(btn1)
        friends_markup.row(btn2)
        friends_markup.row(btn3)
        bot.send_message(user_id, "Выбери одну из опций", reply_markup=friends_markup)
        bot.register_next_step_handler(message, handle_menu_choice)

    elif message.text == "🧠Проекты":
        create_ideas_table()
        add_last_seen_idea_column()
        bot.send_message(user_id, "Привет 👋\nЗдесь ты можешь найти команду для своего проекта,"
                                  " а так же присоединиться к уже существующему проекту!")
        projects_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
        btn1 = types.KeyboardButton('🔍Я ищу проекты')
        btn2 = types.KeyboardButton('☄️Я ищу напарника в проект')
        btn3 = types.KeyboardButton('💡Мой проект')
        btn4 = types.KeyboardButton('Отмена')
        projects_markup.row(btn1)
        projects_markup.row(btn2)
        projects_markup.row(btn3)
        projects_markup.row(btn4)
        bot.send_message(user_id, "Выбери одну из опций", reply_markup=projects_markup)
        bot.register_next_step_handler(message, handle_menu_choice)

    elif message.text == "🥳Мероприятия":
        create_events_table()
        add_last_seen_event_column()
        bot.send_message(user_id, "Привет 👋\nВ этом разделе можно пропиарить мероприятие и найти гостей среди"
                                  " студентов и преподователей РЭУ. Более того, ты можешь сам(а) стать гостем!👑")
        events_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
        btn1 = types.KeyboardButton('🎉Я ищу мероприятия')
        btn2 = types.KeyboardButton('💵Пропиарить мероприятие')
        btn3 = types.KeyboardButton('👑Мое мероприятие')
        btn4 = types.KeyboardButton('Отмена')
        events_markup.row(btn1)
        events_markup.row(btn2)
        events_markup.row(btn3)
        events_markup.row(btn4)
        bot.send_message(user_id, "Выбери одну из опций", reply_markup=events_markup)
        bot.register_next_step_handler(message, handle_menu_choice)

    elif message.text == "Другое":
        create_questions_answers_tables()
        add_last_seen_question_column()
        bot.send_message(user_id, "Привет 👋\nВ этом разделе ты можешь задать вопросы всему сообществу РЭУ, либо "
                                  "же помочь студентам найти нужные им ответы! В единстве сила✊")
        other_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
        btn1 = types.KeyboardButton('❓Задать вопрос')
        btn2 = types.KeyboardButton('📈Ответить на вопросы других пользователей')
        btn3 = types.KeyboardButton('✉️Ответы на мои вопросы')
        btn4 = types.KeyboardButton('Отмена')
        other_markup.row(btn1)
        other_markup.row(btn2)
        other_markup.row(btn3)
        other_markup.row(btn4)
        bot.send_message(user_id, "Выбери одну из опций", reply_markup=other_markup)
        bot.register_next_step_handler(message, handle_menu_choice)
    else:
        return menu(message)


def handle_menu_choice(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id

    if message.text == "🔍Поиск друзей":
        clear_seen_friends(user_id)
        return send_profile_first(message)

    elif message.text == "❤️Лайки на мой профиль":
        like_received_id = get_like_received(user_id)
        if like_received_id == -1:
            reply_markup = types.ReplyKeyboardRemove()
            bot.send_message(user_id, "Больше лайков нет😰, возвращайся позже", reply_markup=reply_markup)
            return
        return send_like_first(message)

    elif message.text == "☄️Я ищу напарника в проект":
        return add_idea(message)
    elif message.text == "🔍Я ищу проекты":
        return send_idea(message)
    elif message.text == "💡Мой проект":
        return show_idea_to_creator(message)

    elif message.text == "💵Пропиарить мероприятие":
        if check_event_exists(user_id):
            bot.send_message(user_id, "У тебя уже есть мероприятие, используй /menu чтобы "
                                      "просмотреть", reply_markup=types.ReplyKeyboardRemove())
            return
        return add_event(message)
    elif message.text == "🎉Я ищу мероприятия":
        return send_event(message)
    elif message.text == "👑Мое мероприятие":
        if not check_event_exists(user_id):
            bot.send_message(user_id, "У тебя нет своего мероприятия, добавь его при помощи /menu",
                             reply_markup=types.ReplyKeyboardRemove())
            return
        return add_event(message)

    elif message.text == "❓Задать вопрос":
        return add_question(message)
    elif message.text == "📈Ответить на вопросы других пользователей":
        return send_question(message)
    elif message.text == "✉️Ответы на мои вопросы":
        return send_questions_list(message)
    elif message.text == "Отмена":
        return menu(message)


def send_profile_first(message):
    if message.text == "/menu":
        return menu(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/cancel':
        return cancel(message)
    if message.text == '/delete':
        return delete(message)
    user_id = message.chat.id
    found_id = get_found_id(user_id)
    uid = get_id(user_id)
    if user_id == 524931933 and message.text == 'Удалить пользователя':
        found_user_id = get_user_id(found_id)
        try:
            bot.send_message(found_user_id, "Твой профиль был удален, так как информация в нем показалась "
                                            "администрации недействительной")
        except telebot.apihelper.ApiTelegramException:
            pass
        delete_user(found_user_id)
    if message.text == "❤️":
        like_happened(uid, found_id)
        set_seen_friends(user_id, found_id)
        found_user_id = get_user_id(found_id)
        try:
            bot.send_message(found_user_id, "👀Кто-то лайкнул твой профиль. Используй /likes чтобы посмотреть")
        except telebot.apihelper.ApiTelegramException:
            pass

    elif message.text != "🔍Поиск друзей":
        set_seen_friends(user_id, found_id)

    response_markup = types.ReplyKeyboardMarkup(is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('❤️')
    btn2 = types.KeyboardButton('👎')
    response_markup.row(btn1, btn2)
    if user_id == 524931933:
        btn3 = types.KeyboardButton('Удалить пользователя')
        response_markup.row(btn3)
    found_id = uid
    found_user_id = user_id
    possible = True
    users_uids = get_user_uids()

    while is_in_seen_friends(user_id, found_id) or not check_user_exists(found_user_id):
        if len(users_uids) == 1:
            possible = False
            break
        users_uids.remove(found_id)
        index = random.randint(0, len(users_uids) - 1)
        found_id = users_uids[index]
        found_user_id = get_user_id(found_id)

    if not possible:
        reply_markup = types.ReplyKeyboardRemove()
        bot.send_message(user_id, "Просмотрены все существующие профили на данный момент. Используй /menu чтобы "
                                  "вернуться",
                         reply_markup=reply_markup)
        return

    set_found_id(user_id, found_id)
    found_user_id = get_user_id(found_id)

    bot.send_photo(user_id, photo=open(get_photo(found_user_id), 'rb'),
                   caption=f"{get_name(found_user_id)}, {get_age(found_user_id)}\n{get_school(found_user_id)}",
                   reply_markup=response_markup)
    bot.register_next_step_handler(message, send_profile_second)


def send_profile_second(message):
    if message.text == "/menu":
        return menu(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/cancel':
        return cancel(message)
    if message.text == '/delete':
        return delete(message)
    user_id = message.chat.id
    found_id = get_found_id(user_id)
    uid = get_id(user_id)

    set_seen_friends(user_id, found_id)
    if user_id == 524931933 and message.text == 'Удалить пользователя':
        found_user_id = get_user_id(found_id)
        try:
            bot.send_message(found_user_id, "Твой профиль был удален, так как информация в нем показалась "
                                            "администрации недействительной")
        except telebot.apihelper.ApiTelegramException:
            pass
        delete_user(found_user_id)
    if message.text == "❤️":
        like_happened(uid, found_id)
        found_user_id = get_user_id(found_id)
        try:
            bot.send_message(found_user_id, "👀Кто-то лайкнул твой профиль. Используй /likes чтобы посмотреть")
        except telebot.apihelper.ApiTelegramException:
            pass

    response_markup = types.ReplyKeyboardMarkup(is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('❤️')
    btn2 = types.KeyboardButton('👎')
    response_markup.row(btn1, btn2)
    if user_id == 524931933:
        btn3 = types.KeyboardButton('Удалить пользователя')
        response_markup.row(btn3)
    found_id = uid
    found_user_id = user_id
    possible = True
    users_uids = get_user_uids()

    while is_in_seen_friends(user_id, found_id) or not check_user_exists(
            found_user_id):
        if len(users_uids) == 1:
            possible = False
            break
        users_uids.remove(found_id)
        index = random.randint(0, len(users_uids) - 1)
        found_id = users_uids[index]
        found_user_id = get_user_id(found_id)

    if not possible:
        reply_markup = types.ReplyKeyboardRemove()
        bot.send_message(user_id, "Просмотрены все существующие профили на данный момент. Используй /menu чтобы "
                                  "вернуться",
                         reply_markup=reply_markup)
        return

    set_found_id(user_id, found_id)
    found_user_id = get_user_id(found_id)
    bot.send_photo(user_id, photo=open(get_photo(found_user_id), 'rb'),
                   caption=f"{get_name(found_user_id)}, {get_age(found_user_id)}\n{get_school(found_user_id)}",
                   reply_markup=response_markup)
    bot.register_next_step_handler(message, send_profile_second)


def send_like_first(message):
    if message.text == "/menu":
        return menu(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/cancel':
        return cancel(message)
    if message.text == '/delete':
        return delete(message)

    user_id = message.chat.id
    uid = get_id(user_id)

    like_received_id = get_like_received(user_id)
    if like_received_id == -1:
        reply_markup = types.ReplyKeyboardRemove()
        bot.send_message(user_id, "Больше лайков нет😰, возвращайся позже", reply_markup=reply_markup)
        return
    like_received_user_id = get_user_id(like_received_id)
    try:
        like_received_username = "@" + str(
            bot.get_chat_member(like_received_user_id, like_received_user_id).user.username)
    except TypeError:
        like_received_username = "@None"
    except telebot.apihelper.ApiTelegramException:
        like_received_username = "@None"

    if user_in_likes_sent(uid, like_received_id):
        bot.send_message(user_id, f"Вы с пользователем {like_received_username} лайкнули друг друга👇")
        bot.send_photo(user_id, photo=open(get_photo_by_id(like_received_id), "rb"),
                       caption=f"{get_name_by_id(like_received_id)}, {get_age_by_id(like_received_id)}\n"
                               f"{get_school_by_id(like_received_id)}")
        delete_first_like_received(user_id, like_received_id)
        return send_like_first(message)

    else:
        response_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
        btn1 = types.KeyboardButton('❤️')
        btn2 = types.KeyboardButton('👎')
        response_markup.row(btn1, btn2)
        bot.send_photo(user_id, photo=open(get_photo_by_id(like_received_id), "rb"),
                       caption=f"{get_name_by_id(like_received_id)}, {get_age_by_id(like_received_id)}\n"
                               f"{get_school_by_id(like_received_id)}\n\nЭтот пользователь лайкнул твой про"
                               f"филь. Лайкни в ответ чтобы познакомиться",
                       reply_markup=response_markup)
        bot.register_next_step_handler(message, send_like_second)


def send_like_second(message):
    if message.text == "/menu":
        return menu(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/cancel':
        return cancel(message)
    if message.text == '/delete':
        return delete(message)

    user_id = message.chat.id
    uid = get_id(user_id)
    like_received_id = get_like_received(user_id)
    like_received_user_id = get_user_id(like_received_id)
    try:
        like_received_username = "@" + str(
            bot.get_chat_member(like_received_user_id, like_received_user_id).user.username)
    except TypeError:
        like_received_username = "@None"
    except telebot.apihelper.ApiTelegramException:
        like_received_username = "@None"

    if message.text == '❤️':
        like_happened(uid, like_received_id)
        bot.send_message(user_id, f"👆Вы с пользователем {like_received_username} лайкнули друг друга")

        like_received_user_id = get_user_id(like_received_id)
        try:
            bot.send_message(like_received_user_id, "👀Кто-то лайкнул твой профиль. Используй /likes чтобы посмотреть")
        except telebot.apihelper.ApiTelegramException:
            pass

    delete_first_like_received(user_id, like_received_id)

    like_received_id = get_like_received(user_id)
    if like_received_id == -1:
        reply_markup = types.ReplyKeyboardRemove()
        bot.send_message(user_id, "Больше лайков нет😰, возвращайся позже", reply_markup=reply_markup)
        return
    like_received_user_id = get_user_id(like_received_id)
    try:
        like_received_username = "@" + str(
            bot.get_chat_member(like_received_user_id, like_received_user_id).user.username)
    except TypeError:
        like_received_username = "@None"
    except telebot.apihelper.ApiTelegramException:
        like_received_username = "@None"

    if user_in_likes_sent(uid, like_received_id):
        bot.send_message(user_id, f"Вы с пользователем {like_received_username} лайкнули друг друга👇")
        bot.send_photo(user_id, photo=open(get_photo_by_id(like_received_id), "rb"),
                       caption=f"{get_name_by_id(like_received_id)}, {get_age_by_id(like_received_id)}"
                               f"\n{get_school_by_id(like_received_id)}")
        delete_first_like_received(user_id, like_received_id)
        return send_like_first(message)

    else:
        response_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
        btn1 = types.KeyboardButton('❤️')
        btn2 = types.KeyboardButton('👎')
        response_markup.row(btn1, btn2)
        bot.send_photo(user_id, photo=open(get_photo_by_id(like_received_id), "rb"),
                       caption=f"{get_name_by_id(like_received_id)}, {get_age_by_id(like_received_id)}\n"
                               f"{get_school_by_id(like_received_id)}\n\nЭтот пользователь лайкнул ваш профиль. Лайкни"
                               f" в ответ чтобы познакомиться", reply_markup=response_markup)
        bot.register_next_step_handler(message, send_like_second)


def add_idea(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if check_idea_exists(user_id):
        bot.send_message(user_id, "Твой проект уже добавлен, используй /menu чтобы посмотреть",
                         reply_markup=types.ReplyKeyboardRemove())
        return
    delete_idea(user_id)
    idea_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("✅Я принимаю условия")
    btn2 = types.KeyboardButton("❌Я отказываюсь")
    idea_markup.row(btn1, btn2)
    bot.send_message(user_id, "Для начала ознакомься с правилами:\n\nВ твоем проекте запрещены:\n"
                              "🚫Упоминание наркотических веществ и алкоголя\n🚫 18+ контент\n🚫 "
                              "Мат\n🚫 Политика\n\n", reply_markup=idea_markup)
    bot.register_next_step_handler(message, ask_idea_name)


def ask_idea_name(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.text == "✅Я принимаю условия":
        create_idea(user_id)
        bot.send_message(user_id, "Введи название своего проекта")
        bot.register_next_step_handler(message, ask_idea_description)
    else:
        return menu(message)


def ask_idea_description(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_idea_name(user_id, message.text)
    bot.send_message(user_id, "Отправь описание своего проекта")
    bot.register_next_step_handler(message, show_idea)


def show_idea(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_idea_description(user_id, message.text)
    check_idea_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("✅Все верно")
    btn2 = types.KeyboardButton("✍️Изменить данные")
    btn3 = types.KeyboardButton("❌Удалить проект")
    check_idea_markup.row(btn1)
    check_idea_markup.row(btn2)
    check_idea_markup.row(btn3)
    bot.send_message(user_id,
                     f"Вот твой проект:\n\n<b>{get_idea_name(user_id)}</b>\n{get_idea_description(user_id)}\n"
                     f"Автор проекта: @{bot.get_chat_member(user_id, user_id).user.username}",
                     reply_markup=check_idea_markup, parse_mode='HTML')
    bot.register_next_step_handler(message, response_to_idea)


def show_idea_to_creator(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if not check_idea_exists(user_id):
        bot.send_message(user_id, "Ты не добавил проект, исправь это в /menu",
                         reply_markup=types.ReplyKeyboardRemove())
        return

    check_idea_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("✅Все верно")
    btn2 = types.KeyboardButton("✍️Изменить данные")
    btn3 = types.KeyboardButton("❌Удалить проект")
    check_idea_markup.row(btn1)
    check_idea_markup.row(btn2)
    check_idea_markup.row(btn3)
    bot.send_message(user_id,
                     f"Вот твой проект:\n\n<b>{get_idea_name(user_id)}</b>\n{get_idea_description(user_id)}\n"
                     f"Автор проекта: @{bot.get_chat_member(user_id, user_id).user.username}",
                     reply_markup=check_idea_markup, parse_mode='HTML')
    bot.register_next_step_handler(message, response_to_idea)


def response_to_idea(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.text == "✅Все верно":
        bot.send_message(user_id, "Твой проект выложен! Продолжай используя /menu")
        return
    elif message.text == "✍️Изменить данные":
        return change_idea(message)
    elif message.text == "❌Удалить проект":
        return handle_delete_idea(message)
    else:
        return


def change_idea(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    change_idea_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Название")
    btn2 = types.KeyboardButton("Описание")
    btn3 = types.KeyboardButton("Отмена")
    change_idea_markup.row(btn1, btn2)
    change_idea_markup.row(btn3)
    bot.send_message(user_id, "Что ты хочешь изменить?", reply_markup=change_idea_markup)
    bot.register_next_step_handler(message, handle_change_idea)


def handle_change_idea(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.text == "Название":
        bot.send_message(user_id, "Отправь новое название")
        bot.register_next_step_handler(message, change_idea_name)
    elif message.text == "Описание":
        bot.send_message(user_id, "Отправь новое описание")
        bot.register_next_step_handler(message, change_idea_description)
    elif message.text == "Отмена":
        return menu(message)


def change_idea_name(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_idea_name(user_id, message.text)
    bot.send_message(user_id, "Название проекта изменено! Продолжи, используя /menu")


def change_idea_description(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_idea_description(user_id, message.text)
    bot.send_message(user_id, "Описание проекта изменено! Продолжи, используя /menu")
    return menu(message)


def handle_delete_idea(message):
    if message.text == '/cancel':
        return cancel(message)
    reply_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('✅Да')
    btn2 = types.KeyboardButton('❌Нет')
    reply_markup.row(btn1, btn2)
    bot.send_message(message.chat.id, "Ты уверен что хочешь удалить свой проект?", reply_markup=reply_markup)
    bot.register_next_step_handler(message, response_to_delete_idea)


def response_to_delete_idea(message):
    if message.text == '/cancel':
        return cancel(message)
    if message.text == "✅Да":
        delete_idea(message.chat.id)
        bot.send_message(message.chat.id, "Твой проект успешно удален")
    return menu(message)


def send_idea(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    ideas = get_ideas()
    last_seen_idea = get_last_seen_idea(user_id)
    if user_id == 524931933 and message.text == "Удалить этот проект️":
        delete_idea(ideas[last_seen_idea][1])
    if last_seen_idea == -2:
        last_seen_idea = len(ideas)
        set_last_seen_idea(user_id, last_seen_idea)
    if last_seen_idea == 0:
        set_last_seen_idea(user_id, -2)
        bot.send_message(user_id, "Ты просмотрел все проекты, возвращайся позже, используя /menu😇",
                         reply_markup=types.ReplyKeyboardRemove())
        return

    last_seen_idea -= 1

    idea_creator_user_id = ideas[last_seen_idea][1]
    name = ideas[last_seen_idea][2]
    description = ideas[last_seen_idea][3]

    text = (f"<b>{name}</b>\n{description}\n"
            f"Автор проекта: @{bot.get_chat_member(idea_creator_user_id, idea_creator_user_id).user.username}")

    ideas_markup = types.ReplyKeyboardMarkup(is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Следующий проект➡️")
    ideas_markup.row(btn1)
    if user_id == 524931933:
        btn2 = types.KeyboardButton("Удалить этот проект️")
        ideas_markup.row(btn2)
    set_last_seen_idea(user_id, last_seen_idea)

    bot.send_message(user_id, text, reply_markup=ideas_markup, parse_mode='HTML')

    bot.register_next_step_handler(message, send_idea)


def send_event(message):
    if message.text == '/cancel':
        return cancel(message)
    deactivate_expired_events()
    user_id = message.chat.id
    events = get_events_approved()
    last_seen_event = get_last_seen_event(user_id)
    if last_seen_event == -1:
        last_seen_event = len(events)
        set_last_seen_event(user_id, last_seen_event)
    if last_seen_event == 0:
        set_last_seen_event(user_id, -1)
        bot.send_message(user_id, "Пока что мероприятий нет! Заходи позже😞",
                         reply_markup=types.ReplyKeyboardRemove())
        return

    last_seen_event -= 1
    try:
        event_creator_user_id = events[last_seen_event][1]
        name = events[last_seen_event][2]
        price = events[last_seen_event][3]
        time = events[last_seen_event][4]
        place = events[last_seen_event][5]
        description = events[last_seen_event][6]
        photo = events[last_seen_event][7]

    except IndexError:
        bot.send_message(user_id, "Пока что мероприятий нет! Заходи позже😞", reply_markup=types.ReplyKeyboardRemove())
        set_last_seen_event(user_id, -1)
        return

    text = (f"{name}\n\n💵Цена: {price}₽\n📅Дата: {time}\n🏠"
            f"Место: {place}\n\n{description}\n\nДля участия пиши: "
            f"@{bot.get_chat_member(event_creator_user_id, event_creator_user_id).user.username}")

    events_markup = types.ReplyKeyboardMarkup(is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Следующее мероприятие➡️")
    events_markup.row(btn1)

    set_last_seen_event(user_id, last_seen_event)

    bot.send_photo(user_id, open(photo, "rb"), caption=text, reply_markup=events_markup)
    increment_event_views(event_creator_user_id)

    bot.register_next_step_handler(message, send_event)


def add_event(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if check_event_exists(user_id):
        bot.send_message(user_id, "Вот твое мероприятие:", reply_markup=types.ReplyKeyboardRemove())
        return show_event_to_creator(message)
    try:
        delete_event(user_id)
    except sqlite3.OperationalError:
        pass
    event_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("✅Я принимаю условия")
    btn2 = types.KeyboardButton("❌Я отказываюсь")
    event_markup.row(btn1, btn2)
    bot.send_message(user_id, "🚀 Для успешного продвижения своего мероприятия ознакомься с нашими "
                              "правилами!\n\n📌 В рекламном посте запрещены:\n🚫 Упоминание наркотических "
                              "веществ и алкоголя\n🚫 18+ контент\n🚫 Мат\n🚫 Политика\n\n❗️ В слу"
                              "чае нарушения хотя бы одного из правил, наш администратор оставляет за со"
                              "бой право удалить твое мероприятие.\n\nПосле оплаты, мероприятие будет "
                              "размещено в течении двух дней. Пользователи смогут увидеть его в разделе "
                              "мероприятия. Если твое событие заинтересует пользователя, он(а) сможет тебе "
                              "написать, твой username будет в конце рекламного поста!\n\n👀По вопросам "
                              "обращайся к администр"
                              "атору.\n\nДавай создадим яркое событие вместе! 💫", reply_markup=event_markup)
    bot.register_next_step_handler(message, ask_event_name)


def ask_event_name(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.text == "✅Я принимаю условия":
        create_event(user_id)
        bot.send_message(user_id, "Введи название мероприятия")
        bot.register_next_step_handler(message, ask_event_price)
    else:
        bot.send_message(user_id, "Возвращайся, используя /menu", reply_markup=types.ReplyKeyboardRemove())
        return


def ask_event_price(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_event_name(user_id, message.text)
    bot.send_message(user_id, "Какова стоимость входа(напиши сумму целыми числами в рублях без букв)?")
    bot.register_next_step_handler(message, ask_event_time)


def ask_event_time(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    try:
        set_event_price(user_id, int(message.text))
        bot.send_message(user_id, "На какую дату и время запланировано твое мероприятие?")
        bot.register_next_step_handler(message, ask_event_place)

    except ValueError:
        bot.send_message(user_id, "Напиши сумму целыми числами в рублях без букв")
        bot.register_next_step_handler(message, ask_event_time)


def ask_event_place(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_event_time(user_id, message.text)
    bot.send_message(user_id, "Где будет проходить твое мероприятие?")
    bot.register_next_step_handler(message, ask_event_description)


def ask_event_description(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_event_place(user_id, message.text)
    bot.send_message(user_id, "Отправь описание своего мероприятия, но помни про правила!")
    bot.register_next_step_handler(message, ask_event_photo)


def ask_event_photo(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_event_description(user_id, message.text)
    bot.send_message(user_id, "Отправь фотографию своего мероприятия!")
    bot.register_next_step_handler(message, finish_event_registration)


def finish_event_registration(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id

    photo_id = message.photo[-1].file_id

    # Download the photo by file_id
    photo_info = bot.get_file(photo_id)
    photo_path = photo_info.file_path
    downloaded_photo = bot.download_file(photo_path)

    # Save the photo to the "photos" folder
    photos_folder = 'events_photo'
    if not os.path.exists(photos_folder):
        os.makedirs(photos_folder)

    photo_filename = f'{photos_folder}/{photo_id}.jpg'
    with open(photo_filename, 'wb') as photo_file:
        photo_file.write(downloaded_photo)
    photo = photo_filename
    set_event_photo(user_id, photo)
    bot.send_message(message.chat.id, "Твое мероприятия создано, вот так оно выглядит:")
    return show_event_to_creator(message)


def show_event_to_creator(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id

    check_event_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("✅Все верно, перейти к оплате")
    btn2 = types.KeyboardButton("✍️Изменить данные")
    btn3 = types.KeyboardButton("❌Удалить мероприятие")
    btn4 = types.KeyboardButton("📈Статистика")
    if get_event_is_active(user_id):
        check_event_markup.row(btn4)
    else:
        check_event_markup.row(btn1, btn2)
    check_event_markup.row(btn3)
    text = (f"{get_event_name(user_id)}\n\n💵Цена: {get_event_price(user_id)}₽\n📅Дата: {get_event_time(user_id)}\n🏠"
            f"Место: {get_event_place(user_id)}\n\n{get_event_description(user_id)}\n\nДля участия пиши: "
            f"@{bot.get_chat_member(user_id, user_id).user.username}")
    bot.send_photo(user_id, open(get_event_photo(user_id), "rb"), caption=text, reply_markup=check_event_markup)
    bot.register_next_step_handler(message, response_to_event)


def response_to_event(message):
    if message.text == '/cancel':
        return cancel(message)
    if message.text == "✅Все верно, перейти к оплате":
        return proceed_to_payment(message)
    elif message.text == "✍️Изменить данные":
        return change_event(message)
    elif message.text == "❌Удалить мероприятие":
        return handle_delete_event(message)
    elif message.text == "📈Статистика":
        return event_statistics(message)
    else:
        return


def proceed_to_payment(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    bot.send_message(user_id, "Для оплаты и ознакомления с тарифом, пиши администратору @zephyrs_admin",
                     reply_markup=types.ReplyKeyboardRemove())
    return


def change_event(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    change_event_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Название")
    btn2 = types.KeyboardButton("Цена")
    btn3 = types.KeyboardButton("Время")
    btn4 = types.KeyboardButton("Место")
    btn5 = types.KeyboardButton("Описание")
    btn6 = types.KeyboardButton("Фото")
    btn7 = types.KeyboardButton("Отмена")
    change_event_markup.row(btn1, btn2, btn3)
    change_event_markup.row(btn4, btn5, btn6)
    change_event_markup.row(btn7)
    bot.send_message(user_id, "Что ты хочешь изменить?", reply_markup=change_event_markup)
    bot.register_next_step_handler(message, handle_change_event)


def handle_change_event(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.text == "Название":
        bot.send_message(user_id, "Отправь новое название")
        bot.register_next_step_handler(message, change_event_name)
    elif message.text == "Цена":
        bot.send_message(user_id, "Отправь новую цену (число без букв и прочих символов)")
        bot.register_next_step_handler(message, change_event_price)
    elif message.text == "Время":
        bot.send_message(user_id, "Отправь новое время")
        bot.register_next_step_handler(message, change_event_time)
    elif message.text == "Место":
        bot.send_message(user_id, "Отправь новое место")
        bot.register_next_step_handler(message, change_event_place)
    elif message.text == "Описание":
        bot.send_message(user_id, "Отправь новое описание")
        bot.register_next_step_handler(message, change_event_description)
    elif message.text == "Фото":
        bot.send_message(user_id, "Отправь новое фото")
        bot.register_next_step_handler(message, change_event_photo)
    elif message.text == "Отмена":
        return menu(message)


def change_event_name(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_event_name(user_id, message.text)
    bot.send_message(user_id, "Название мероприятия изменено")
    return menu(message)


def change_event_price(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    try:
        price = int(message.text)
        set_event_price(user_id, price)
        bot.send_message(user_id, "Цена мероприятия изменена")
        return menu(message)
    except ValueError:
        bot.send_message(user_id, "Введи целое число без букв и прочих символов")
        bot.register_next_step_handler(message, change_event_price)


def change_event_time(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_event_time(user_id, message.text)
    bot.send_message(user_id, "Дата проведения мероприятия изменена")
    return menu(message)


def change_event_place(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_event_place(user_id, message.text)
    bot.send_message(user_id, "Место проведения мероприятия изменено")
    return menu(message)


def change_event_description(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    set_event_description(user_id, message.text)
    bot.send_message(user_id, "Описание мероприятия изменено")
    return menu(message)


def change_event_photo(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.content_type == "text":
        if message.text == "/menu":
            return menu(message)
        if message.text == '/start':
            return start(message)
        if message.text == '/profile':
            return profile(message)
        if message.text == '/cancel':
            return cancel(message)
        else:
            bot.send_message(user_id, "Отправь фото")
            bot.register_next_step_handler(message, change_event_photo)

    elif message.content_type == "photo":
        photo_id = message.photo[-1].file_id
        photo_info = bot.get_file(photo_id)
        photo_path = photo_info.file_path
        downloaded_photo = bot.download_file(photo_path)

        photos_folder = 'events_photo'
        if not os.path.exists(photos_folder):
            os.makedirs(photos_folder)

        photo_filename = f'{photos_folder}/{photo_id}.jpg'
        with open(photo_filename, 'wb') as photo_file:
            photo_file.write(downloaded_photo)
        photo = photo_filename

        if not os.path.exists(photo):
            bot.send_message(user_id, "Не удалось изменить фото мероприятия, попробуйте позже!")
            return

        os.remove(get_photo(user_id))
        set_event_photo(user_id, photo)
        bot.send_message(user_id, "Фото мероприятия успешно изменено!")


def handle_delete_event(message):
    if message.text == '/cancel':
        return cancel(message)
    reply_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('✅Да')
    btn2 = types.KeyboardButton('❌Нет')
    reply_markup.row(btn1, btn2)
    bot.send_message(message.chat.id, "Ты уверен что хочешь удалить своё мероприятие?", reply_markup=reply_markup)
    bot.register_next_step_handler(message, response_to_delete_event)


def response_to_delete_event(message):
    if message.text == '/cancel':
        return cancel(message)
    if message.text == "✅Да":
        delete_event(message.chat.id)
        bot.send_message(message.chat.id, "Твое мероприятие успешно удалено")
    return menu(message)


def event_statistics(message):
    if message.text == '/cancel':
        return cancel(message)
    bot.send_message(message.chat.id,
                     f"Просмотры: {get_event_views(message.chat.id)}\nБудет снято"
                     f": {get_how_long_left_event(message.chat.id)}")


def add_question(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    create_question(user_id)
    bot.send_message(user_id, "Задай свой вопрос", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, ask_question)


def ask_question(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    last_added_question_uid = get_last_added_question_uid(user_id)
    set_question(last_added_question_uid, message.text)
    bot.send_message(user_id, "Твой вопрос добавлен, чтобы посмотреть ответы, используй /menu")
    return


def send_question(message):
    delete_expired_questions()
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    questions = get_questions(user_id)
    last_seen_question = get_last_seen_question(user_id)

    if message.text == "Ответить на вопрос🛟":
        bot.send_message(user_id, "Введи ответ на этот вопрос, но помни, что ответы не анонимны",
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, enter_answer)
        return

    if last_seen_question == -2:
        try:
            last_seen_question = questions[-1][0] + 1
            set_last_seen_question(user_id, last_seen_question)
        except IndexError:
            set_last_seen_question(user_id, -2)
            bot.send_message(user_id, "Ты просмотрел все вопросы, возвращайся позже, используя /menu😇",
                             reply_markup=types.ReplyKeyboardRemove())
            return
    if last_seen_question == 1:
        set_last_seen_question(user_id, -2)
        bot.send_message(user_id, "Ты просмотрел все вопросы, возвращайся позже, используя /menu😇",
                         reply_markup=types.ReplyKeyboardRemove())
        return

    last_seen_question -= 1
    while not check_question_exists(last_seen_question, user_id):
        last_seen_question -= 1
        if last_seen_question == 0:
            set_last_seen_question(user_id, -2)
            bot.send_message(user_id, "Ты просмотрел все вопросы, возвращайся позже, используя /menu😇",
                             reply_markup=types.ReplyKeyboardRemove())
            return

    question = get_question_by_uid(last_seen_question, user_id)
    question_markup = types.ReplyKeyboardMarkup(is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Ответить на вопрос🛟")
    btn2 = types.KeyboardButton("Следующий вопрос➡️")

    question_markup.row(btn1)
    question_markup.row(btn2)
    set_last_seen_question(user_id, last_seen_question)
    bot.send_message(user_id, question, reply_markup=question_markup)
    bot.register_next_step_handler(message, send_question)


def enter_answer(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    question = get_question_by_uid(get_last_seen_question(user_id), user_id)
    answer = message.text
    create_answer(user_id, question, answer)
    bot.send_message(user_id, "Ответ отправлен, ты можешь продолжать!")
    return send_question(message)


def send_questions_list(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    questions_asked = get_asked_questions(user_id)
    if len(questions_asked) == 0:
        bot.send_message(user_id, "Упс😅, кажется ты не задавал(а) вопросов, либо же прошло более двух дней с"
                                  " момента размещения вопроса. Но ты всегда можешь задать новый в /menu")
        return
    text = "Введи номер вопроса, который тебя интересует: \n"
    for i in range(1, len(questions_asked) + 1):
        if len(questions_asked[i - 1][2]) > 22:
            text += f"{i}. {questions_asked[i - 1][2][:22]}..?\n"
        else:
            text += f"{i}. {questions_asked[i - 1][2]}\n"

    bot.send_message(user_id, text, reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, handle_question_number)


def handle_question_number(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    try:
        question_number = int(message.text)
        questions_asked = get_asked_questions(user_id)
        set_last_seen_question(user_id, questions_asked[question_number - 1][0])
        return send_answers(message)
    except ValueError:
        return send_questions_list(message)


def send_answers(message):
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.text == "Выбрать другой вопрос🫥":
        return send_questions_list(message)
    question = get_question_by_uid(get_last_seen_question(user_id), 1)
    answers = get_answers(question)
    try:
        text = (f"<b>Вопрос: {question}\n\n</b>Ответ от @"
                f"{bot.get_chat_member(answers[0][1], answers[0][1]).user.username}:\n{answers[0][3]}")
        delete_answer(answers[0][3])
    except IndexError:
        bot.send_message(user_id, "Новых ответов нет, возвращайся позже, используя /menu")
        return
    except telebot.apihelper.ApiTelegramException:
        text = f"Ответ от @None:\n{answers[0][3]}"
        delete_answer(answers[0][3])
    answer_markup = types.ReplyKeyboardMarkup(is_persistent=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Следующий ответ➡️")
    btn2 = types.KeyboardButton("Выбрать другой вопрос🫥")
    answer_markup.row(btn1)
    answer_markup.row(btn2)
    bot.send_message(user_id, text, reply_markup=answer_markup, parse_mode='HTML')
    bot.register_next_step_handler(message, send_answers)


bot.infinity_polling()
