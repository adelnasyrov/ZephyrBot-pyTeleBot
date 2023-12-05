import telebot
from telebot import types
import sqlite3
import os

bot = telebot.TeleBot('6373983672:AAFJPyO1sR_nAm0ae3A4qeR-vhWExuRk7i8')


def check_user_exists(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
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


def add_name(user_id, name):
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


def add_age(user_id, age):
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


def add_gender(user_id, gender):
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


def add_school(user_id, school):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET school = ? WHERE user_id = ?', (school, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def add_photo(user_id, photo):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET photo = ?, likes_sent = "", likes_received = "" WHERE user_id = ?', (photo, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def add_looking_for(user_id, looking_for):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET looking_for = ? WHERE user_id = ?', (looking_for, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def delete_user(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    user = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()


def create_user(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO users (user_id, looking_for) VALUES (?, 1)', (user_id,))
    user = cur.fetchall()
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


def get_looking_for(user_id):
    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('SELECT looking_for FROM users WHERE user_id = ?', (user_id,))
    looking_for = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return looking_for[0][0]


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id

    conn = sqlite3.connect('reu_zephyr.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, user_id int unique, '
                'name varchar(50), age int, gender varchar(10), school varchar(7), photo varchar(200), likes_sent '
                'varchar(30000), likes_received varchar(30000), looking_for int)')

    conn.commit()
    cur.close()
    conn.close()

    if check_user_exists(user_id):

        # global name
        # global age
        # global gender
        # global school
        # global photo
        # global likes_sent
        # global likes_received
        #
        # name = user[0][2]
        # age = user[0][3]
        # gender = user[0][4]
        # school = user[0][5]
        # photo = user[0][6]
        # likes_sent = user[0][7]
        # likes_received = user[0][8]

        bot.send_message(message.chat.id, "У тебя уже есть анкета. Используй /search чтобы начать поиск")

    else:
        delete_user(user_id)
        create_user(user_id)
        bot.send_message(message.chat.id, "Привет, для начала заполним твою анкету. Как тебя зовут?")
        bot.register_next_step_handler(message, ask_age)


def ask_age(message):
    user_id = message.chat.id
    if message.text.lower() == '/start':
        return start(message)

    if not check_name_exists(user_id):
        name = message.text.strip()
        add_name(user_id, name)
        bot.send_message(message.chat.id, f"Приятно познакомиться, {name}! Сколько тебе лет?")
    else:
        bot.send_message(message.chat.id, f"Введи целое число без букв")
    bot.register_next_step_handler(message, ask_gender)


def ask_gender(message):
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
            add_age(user_id, age)
        except ValueError:
            return ask_age(message)
        bot.send_message(message.chat.id, "Какого ты пола?", reply_markup=gender_markup)
    else:
        print("huyalh")
        bot.send_message(message.chat.id, "Используй кнопки для ответа🫣", reply_markup=gender_markup)
    bot.register_next_step_handler(message, ask_school)


def ask_school(message):
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
            add_gender(user_id, gender)
            bot.send_message(message.chat.id, "C какой ты высшей школы?", reply_markup=school_markup)
            bot.register_next_step_handler(message, ask_photo)

        else:
            print("niga")
            return ask_gender(message)
    else:
        bot.send_message(message.chat.id, "Используй кнопки для ответа🫣", reply_markup=school_markup)
        bot.register_next_step_handler(message, ask_photo)


def ask_photo(message):
    user_id = message.chat.id

    if message.text in ['ИПАМ', 'ВШКМиС', 'ВШФ', 'ВШСГН', 'ВИШ НМИТ', 'ВШЭИБ', 'ВШМ', 'ВШКИ', 'ВШП', 'Преподователь']:
        school = message.text
        add_school(user_id, school)
        bot.send_message(message.chat.id,
                         "Теперь отправь свою фотографию, но имей ввиду, другие пользователи смогут ее видеть!")
        bot.register_next_step_handler(message, finish_registration)
    else:
        return ask_school(message)


def finish_registration(message):
    if message.content_type == "text":
        if message.text.lower() == '/start':
            return start(message)
        elif message.text.lower() == '/search':
            return search(message)
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
        add_photo(user_id, photo)
        bot.send_message(message.chat.id, "Регистрация завершена! \nВведи /search для поиска знакомств.")

    else:
        bot.send_message(message.chat.id, "К чему здесь эта фотография🤡?")


@bot.message_handler(commands=['search'])
def search(message):
    user_id = message.chat.id

    if not check_user_exists(user_id):
        bot.send_message(message.chat.id, "Сначала создай профиль с помощью /start")
    else:
        search_markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Ищу друзей🫂')
        btn2 = types.KeyboardButton('Ищу напарника в проект🧠')
        btn3 = types.KeyboardButton('Ищу мероприятия🥳')
        search_markup.row(btn1)
        search_markup.row(btn2)
        search_markup.row(btn3)
        bot.send_message(message.chat.id, "Что ты хочешь найти сегодня?", reply_markup=search_markup)
        bot.register_next_step_handler(message, handle_response)
        # conn = sqlite3.connect('reu_zephyr.sql')
        # user_id = message.chat.id
        # cur = conn.cursor()
        # cur.execute('SELECT * FROM users WHERE user_id != ?', (user_id,))
        # search_list = cur.fetchall()
        # for el in search_list:
        #     message_text = f"{el[2]}, {el[3]}\n{el[5]}"
        #     response_markup = types.ReplyKeyboardMarkup()
        #     btn1 = types.KeyboardButton('❤️')
        #     btn2 = types.KeyboardButton('👎')
        #     response_markup.row(btn1, btn2)
        #     bot.send_photo(message.chat.id, photo=open(el[6], 'rb'), caption=message_text, reply_markup=response_markup)
        #     bot.register_next_step_handler(message, handle_response)
        # print(search_list)
        # cur.close()
        # conn.close()
        print()


def handle_response(message):
    user_id = message.chat.id
    if message.text == "Ищу друзей🫂":
        add_looking_for(user_id, 1)
        conn = sqlite3.connect('reu_zephyr.sql')
        user_id = message.chat.id
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE user_id != ? AND looking_for = 1', (user_id,))
        search_list = cur.fetchall()
        for el in search_list:
            message_text = f"{el[2]}, {el[3]}\n{el[5]}"
            response_markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('❤️')
            btn2 = types.KeyboardButton('👎')
            response_markup.row(btn1, btn2)
            bot.send_photo(message.chat.id, photo=open(el[6], 'rb'), caption=message_text, reply_markup=response_markup)
            bot.register_next_step_handler(message, handle_response)
        print(search_list)
        cur.close()
        conn.close()
    elif message.text == "Ищу напарника в проект🧠":
        add_looking_for(user_id, 2)
    elif message.text == "Ищу мероприятия🥳":
        add_looking_for(user_id, 3)
    else:
        search_markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Ищу друзей🫂')
        btn2 = types.KeyboardButton('Ищу напарника в проект🧠')
        btn3 = types.KeyboardButton('Ищу мероприятия🥳')
        search_markup.row(btn1)
        search_markup.row(btn2)
        search_markup.row(btn3)
        bot.send_message(message.chat.id, "Используй кнопки для ответа", reply_markup=search_markup)
        bot.register_next_step_handler(message, handle_response)


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
    if message.text == "Изменить фото":
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
        if message.text == "/start":
            return start(message)
        elif message.text == "/search":
            return search(message)
        else:
            bot.send_message("Отправь фото")
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
        add_photo(user_id, photo)
        bot.send_message(user_id, "Фото успешно изменено!")


def change_name(message):
    user_id = message.chat.id
    if message.text == "/start":
        return start(message)
    elif message.text == "/search":
        return search(message)
    else:
        add_name(user_id, message.text)
        bot.send_message(user_id, "Имя успешно изменено")


def change_age(message):
    user_id = message.chat.id
    if message.text == "/start":
        return start(message)
    elif message.text == "/search":
        return search(message)
    else:
        try:
            age = int(message.text)
            add_age(user_id, age)
            bot.send_message(user_id, "Имя успешно изменено")
            return
        except ValueError:
            bot.send_message("Введи целое число")
            bot.register_next_step_handler(message, change_age)


bot.infinity_polling()
