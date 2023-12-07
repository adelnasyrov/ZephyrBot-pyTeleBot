import random

import telebot
from telebot import types
import sqlite3
import os

bot = telebot.TeleBot('6373983672:AAFJPyO1sR_nAm0ae3A4qeR-vhWExuRk7i8')


def check_user_exists(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    except sqlite3.OperationalError:
        return False
    user = cur.fetchall()
    print(user)
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


def get_user_id(uid):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT user_id FROM users WHERE id = ?', (uid,))
    user_id = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return user_id[0][0]


def get_like_received(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT likes_received FROM users WHERE user_id = ?', (user_id,))
    likes_received = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    try:
        return int(likes_received[0][0].lstrip().split(", ")[0])
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


def looking_for_fits(uid, found_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT looking_for FROM users WHERE id = ? OR id = ?', (uid, found_id,))
    looking_for = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if uid == found_id:
        return False
    return looking_for[0][0] == looking_for[1][0]


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
        bot.send_message(message.chat.id, "У тебя уже есть анкета. Используй /search чтобы начать поиск")
    else:
        delete_user(user_id)
        create_user(user_id)
        bot.send_message(message.chat.id, "Привет, для начала заполним твою анкету. Как тебя зовут?")
        bot.register_next_step_handler(message, ask_age)


def ask_age(message):
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
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
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id

    if message.text.lower() == '/start':
        return start(message)

    gender_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
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
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    if message.text.lower() == '/start':
        return start(message)

    school_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
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
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id

    if message.text in ['ИПАМ', 'ВШКМиС', 'ВШФ', 'ВШСГН', 'ВИШ НМИТ', 'ВШЭИБ', 'ВШМ', 'ВШКИ', 'ВШП', 'Преподователь']:
        school = message.text
        set_school(user_id, school)
        bot.send_message(message.chat.id,
                         "Теперь отправь свою фотографию, но имей ввиду, другие пользователи смогут ее видеть!")
        bot.register_next_step_handler(message, finish_registration)
    else:
        return ask_school(message)


def finish_registration(message):
    if message.content_type == "text":
        if message.text == "/search":
            return search(message)
        if message.text == '/start':
            return start(message)
        if message.text == '/profile':
            return profile(message)
        if message.text == '/likes':
            return likes(message)
        if message.text == '/cancel':
            return cancel(message)
        else:
            bot.send_message(message.chat.id, "Отправь фотографию🫵")
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
        print(photo)
        set_photo(user_id, photo)
        bot.send_message(message.chat.id, "Регистрация завершена! \nВведи /search для поиска знакомств.")

    else:
        bot.send_message(message.chat.id, "К чему здесь эта фотография🤡?")


@bot.message_handler(commands=['search'])
def search(message):
    user_id = message.chat.id

    if not check_user_exists(user_id):
        bot.send_message(message.chat.id, "Сначала создай профиль с помощью /start")
    else:
        search_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Ищу друзей🫂')
        btn2 = types.KeyboardButton('Ищу напарника в проект🧠')
        btn3 = types.KeyboardButton('Ищу мероприятия🥳')
        search_markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Что ты хочешь найти сегодня?", reply_markup=search_markup)
        bot.register_next_step_handler(message, handle_search_options)


def handle_search_options(message):
    user_id = message.chat.id

    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
    if message.text == '/cancel':
        return cancel(message)

    if message.text == "Ищу друзей🫂":
        clear_seen_friends(user_id)
        looking_for = 1
    elif message.text == "Ищу напарника в проект🧠":
        looking_for = 2
    elif message.text == "Ищу мероприятия🥳":
        looking_for = 3
    else:
        return search(message)
    set_looking_for(user_id, looking_for)
    return send_profile_first(message)


def send_profile_first(message):
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    found_id = get_found_id(user_id)
    uid = get_id(user_id)

    if message.text == "❤️":
        like_happened(uid, found_id)

    response_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('❤️')
    btn2 = types.KeyboardButton('👎')
    response_markup.row(btn1, btn2)
    number_of_users = get_amount_of_users()
    found_id = uid
    possible = True
    users_uids = list(range(1, number_of_users + 1))

    while (not looking_for_fits(uid, found_id)) or is_in_seen_friends(user_id, found_id):
        if len(users_uids) == 1:
            possible = False
            break
        users_uids.remove(found_id)
        index = random.randint(0, len(users_uids) - 1)
        found_id = users_uids[index]

    if not possible:
        bot.send_message(user_id, "Просмотрены все существующие профили на данный момент. Используй /search чтобы "
                                  "посмотреть новые профили или /likes чтобы посмотреть кто тебя лайкнул!")
        return

    set_seen_friends(user_id, found_id)
    set_found_id(user_id, found_id)
    found_user_id = get_user_id(found_id)
    bot.send_photo(user_id, photo=open(get_photo(found_user_id), 'rb'),
                   caption=f"{get_name(found_user_id)}, {get_age(found_user_id)}\n{get_school(found_user_id)}",
                   reply_markup=response_markup)
    bot.register_next_step_handler(message, send_profile_second)


def send_profile_second(message):
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
    if message.text == '/cancel':
        return cancel(message)
    user_id = message.chat.id
    found_id = get_found_id(user_id)
    uid = get_id(user_id)

    if message.text == "❤️":
        like_happened(uid, found_id)

    response_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('❤️')
    btn2 = types.KeyboardButton('👎')
    response_markup.row(btn1, btn2)
    number_of_users = get_amount_of_users()
    found_id = uid
    possible = True
    users_uids = list(range(1, number_of_users))

    while (not looking_for_fits(uid, found_id)) or is_in_seen_friends(user_id, found_id):
        if len(users_uids) == 1:
            possible = False
            break
        users_uids.remove(found_id)
        index = random.randint(0, len(users_uids) - 1)
        found_id = users_uids[index]

    if not possible:
        bot.send_message(user_id, "Просмотрены все существующие профили на данный момент. Используй /search чтобы "
                                  "посмотреть новые профили или /likes чтобы посмотреть кто тебя лайкнул!")
        return

    set_seen_friends(user_id, found_id)
    set_found_id(user_id, found_id)
    found_user_id = get_user_id(found_id)
    bot.send_photo(user_id, photo=open(get_photo(found_user_id), 'rb'),
                   caption=f"{get_name(found_user_id)}, {get_age(found_user_id)}\n{get_school(found_user_id)}",
                   reply_markup=response_markup)
    bot.register_next_step_handler(message, send_profile_second)


@bot.message_handler(commands=['profile'])
def profile(message):
    user_id = message.chat.id
    if not check_user_exists(user_id):
        bot.send_message(user_id, "Сначала создай профиль с помощью /start")
        return
    bot.send_message(user_id, "Вот ваш профиль:")
    profile_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
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
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
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
        if message.text == "/search":
            return search(message)
        if message.text == '/start':
            return start(message)
        if message.text == '/profile':
            return profile(message)
        if message.text == '/likes':
            return likes(message)
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

        os.remove(get_photo(user_id))
        set_photo(user_id, photo)
        bot.send_message(user_id, "Фото успешно изменено!")


def change_name(message):
    user_id = message.chat.id
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
    if message.text == '/cancel':
        return cancel(message)
    else:
        set_name(user_id, message.text)
        bot.send_message(user_id, "Имя успешно изменено")


def change_age(message):
    user_id = message.chat.id
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/likes':
        return likes(message)
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


@bot.message_handler(commands=['likes'])
def likes(message):
    user_id = message.chat.id
    like_received_id = get_like_received(user_id)
    if like_received_id == -1:
        bot.send_message(user_id, "Пока что лайков нету😰, возвращайтесь позже")
        return
    return send_like_first(message)


def send_like_first(message):
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/cancel':
        return cancel(message)

    user_id = message.chat.id
    uid = get_id(user_id)

    like_received_id = get_like_received(user_id)
    if like_received_id == -1:
        bot.send_message(user_id, "Пока что лайков нету😰, возвращайтесь позже")
        return
    like_received_user_id = get_user_id(like_received_id)
    like_received_username = "@" + bot.get_chat_member(like_received_user_id, like_received_user_id).user.username

    if user_in_likes_sent(uid, like_received_id):
        bot.send_message(user_id, f"Вы с пользователем {like_received_username} лайкнули друг друга👇")
        bot.send_photo(user_id, photo=open(get_photo_by_id(like_received_id), "rb"),
                       caption=f"{get_name_by_id(like_received_id)}, {get_age_by_id(like_received_id)}\n"
                               f"{get_school_by_id(like_received_id)}")
        delete_first_like_received(user_id, like_received_id)
        return send_like_first(message)

    else:
        response_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('❤️')
        btn2 = types.KeyboardButton('👎')
        response_markup.row(btn1, btn2)
        bot.send_photo(user_id, photo=open(get_photo_by_id(like_received_id), "rb"),
                       caption=f"{get_name_by_id(like_received_id)}, {get_age_by_id(like_received_id)}\n"
                               f"{get_school_by_id(like_received_id)}\n\nЭтот пользователь лайкнул ваш про"
                               f"филь. Лайкни в ответ чтобы познакомиться",
                       reply_markup=response_markup)
        bot.register_next_step_handler(message, send_like_second)


def send_like_second(message):
    if message.text == "/search":
        return search(message)
    if message.text == '/start':
        return start(message)
    if message.text == '/profile':
        return profile(message)
    if message.text == '/cancel':
        return cancel(message)

    user_id = message.chat.id
    uid = get_id(user_id)
    like_received_id = get_like_received(user_id)
    like_received_user_id = get_user_id(like_received_id)
    like_received_username = "@" + bot.get_chat_member(like_received_user_id, like_received_user_id).user.username

    if message.text == '❤️':
        like_happened(uid, like_received_id)
        bot.send_message(user_id, f"👆Вы с пользователем {like_received_username} лайкнули друг друга")

    delete_first_like_received(user_id, like_received_id)

    like_received_id = get_like_received(user_id)
    if like_received_id == -1:
        bot.send_message(user_id, "Пока что лайков нету😰, возвращайтесь позже")
        return
    like_received_user_id = get_user_id(like_received_id)
    like_received_username = "@" + bot.get_chat_member(like_received_user_id, like_received_user_id).user.username

    print(like_received_username)
    print(like_received_username)

    if user_in_likes_sent(uid, like_received_id):
        bot.send_message(user_id, f"Вы с пользователем {like_received_username} лайкнули друг друга👇")
        bot.send_photo(user_id, photo=open(get_photo_by_id(like_received_id), "rb"),
                       caption=f"{get_name_by_id(like_received_id)}, {get_age_by_id(like_received_id)}"
                               f"\n{get_school_by_id(like_received_id)}")
        delete_first_like_received(user_id, like_received_id)
        return send_like_first(message)

    else:
        response_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('❤️')
        btn2 = types.KeyboardButton('👎')
        response_markup.row(btn1, btn2)
        bot.send_photo(user_id, photo=open(get_photo_by_id(like_received_id), "rb"),
                       caption=f"{get_name_by_id(like_received_id)}, {get_age_by_id(like_received_id)}\n"
                               f"{get_school_by_id(like_received_id)}\n\nЭтот пользователь лайкнул ваш профиль. Лайкни"
                               f" в ответ чтобы познакомиться", reply_markup=response_markup)
        bot.register_next_step_handler(message, send_like_second)


@bot.message_handler(commands=['cancel'])
def cancel(message):
    bot.send_message(message.chat.id, "Все действия отменены. Возвращайся, используя /search")
    return


bot.infinity_polling()
