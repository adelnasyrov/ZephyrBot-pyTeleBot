import os

from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import ConversationHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define states for conversation
NAME, AGE, GENDER, LOOKING_FOR, SCHOOL, PROGRAM, PHOTO, SEARCH, WAITING_FOR_ANSWER = range(9)

user_portfolios = {}
PHOTOS_FOLDER = 'photos'


# Start command
def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Привет, для начала заполним твою анкету. "
        "Как тебя зовут?"
    )
    return NAME


# Function to handle user's name
def get_name(update: Update, context: CallbackContext) -> int:
    name = update.message.text
    user_portfolios[update.message.chat_id] = {"name": name, "likes_received": {}, "likes_sent": {}}
    context.user_data["name"] = name
    update.message.reply_text(
        f"Приятно познакомиться, {user_portfolios[update.message.chat_id]['name']}! Сколько тебе лет?"
    )
    return AGE


# Function to handle user's age
def get_age(update: Update, context: CallbackContext) -> int:
    try:
        age = int(update.message.text)
    except ValueError:
        return AGE
    user_portfolios[update.message.chat_id]["age"] = age
    context.user_data["age"] = age
    keyboard = [['Парень 👨', 'Девушка 👩']]
    update.message.reply_text(
        "Какого ты пола?",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True),
    )
    return GENDER


# Function to handle user's gender
def get_gender(update: Update, context: CallbackContext) -> int:
    gender = update.message.text
    user_portfolios[update.message.chat_id]["gender"] = gender
    context.user_data["gender"] = gender
    keyboard = [['Парень 👨', 'Девушка 👩'], ['Неважно']]
    update.message.reply_text(
        "С кем ты хочешь познакомиться?",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True),
    )
    return LOOKING_FOR


# Function to handle who the user is looking for
def get_looking_for(update: Update, context: CallbackContext) -> int:
    looking_for = update.message.text
    user_portfolios[update.message.chat_id]["looking_for"] = looking_for
    context.user_data["looking_for"] = looking_for
    keyboard = [['ИПАМ', 'ВШКМиС'], ['ВШФ', 'ВШСГН'], ['ВИШ НМИТ', 'ВШЭИБ'], ['ВШМ', 'ВШКИ'], ['ВШП', 'Преподователь']]
    update.message.reply_text(
        "С какой ты высшей школы?",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True),
    )
    return SCHOOL


def get_school(update: Update, context: CallbackContext) -> int:
    school = update.message.text
    user_portfolios[update.message.chat_id]["school"] = school
    context.user_data["school"] = school
    if user_portfolios[update.message.chat_id]["school"] != "Преподователь":
        update.message.reply_text(
            "На каком направлении ты учишься?",
        )
        return PROGRAM
    user_portfolios[update.message.chat_id]["program"] = ""
    context.user_data["program"] = ""
    update.message.reply_text(
        "Теперь отправь свою фотографию, но имей ввиду, другие пользователи смогут ее видеть!"
    )
    return PHOTO


def get_program(update: Update, context: CallbackContext) -> int:
    program = update.message.text
    user_portfolios[update.message.chat_id]["program"] = program
    context.user_data["program"] = program
    update.message.reply_text(
        "Теперь отправь свою фотографию, но имей ввиду, другие пользователи смогут ее видеть!"
    )
    return PHOTO


# Function to handle user's photo
def get_photo(update: Update, context: CallbackContext) -> int:
    # Get the file ID of the photo
    file_id = update.message.photo[-1].file_id
    file = context.bot.get_file(file_id)

    # Create the photos folder if it doesn't exist
    os.makedirs(PHOTOS_FOLDER, exist_ok=True)

    # Save the photo with a unique name
    photo_path = os.path.join(PHOTOS_FOLDER, f'{file_id}.jpg')
    file.download(photo_path)

    # Store the file path in user_data
    user_portfolios[update.message.chat_id]["photo"] = photo_path
    context.user_data["photo"] = photo_path
    update.message.reply_text(
        "Регистрация завершена! \nВведи /search для поиска знакомств."
    )

    return SEARCH


# Function to cancel the conversation
def cancel(update: Update) -> int:
    update.message.reply_text(
        "Диалог был завершен. \nВведи /start чтобы начать."
    )
    return ConversationHandler.END


def search(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    bot = context.bot
    if user_id not in user_portfolios:
        update.message.reply_text(
            "Завреши регистрацию используя команду /start прежде чем знакомиться!"
        )
        return ConversationHandler.END

    answer = update.message.text
    other_user_id = context.user_data.get('other_user_id')
    if other_user_id is not None:
        my_user_username = context.bot.get_chat_member(chat_id=update.message.chat_id,
                                                       user_id=update.message.chat_id)["user"]["username"]
        other_user_username = context.bot.get_chat_member(chat_id=other_user_id,
                                                          user_id=other_user_id)["user"]["username"]

        if other_user_id in user_portfolios[user_id]['likes_received']:
            if answer == "❤️":
                bot.send_message(user_id,
                                 f"Вы с @{other_user_username} лайкнули профили друг друга. Приятного знакоства!")
                del user_portfolios[user_id]['likes_received'][other_user_id]
                user_portfolios[other_user_id]['likes_received'][user_id] = my_user_username
            elif answer == "👎":
                del user_portfolios[user_id]['likes_received'][other_user_id]
                del user_portfolios[other_user_id]['likes_sent'][user_id]

        else:
            if answer == "❤️":
                user_portfolios[user_id]["likes_sent"][other_user_id] = other_user_username
                print(my_user_username, user_portfolios[user_id]["likes_sent"])

                user_portfolios[other_user_id]["likes_received"][user_id] = my_user_username

    search_results = context.user_data.get("search_results")

    if search_results is None:
        search_results = []

    viewed_profiles = context.user_data.get("viewed_profiles")

    if viewed_profiles is None:
        viewed_profiles = []

    likes_sent_and_received = []
    likes_received = []

    for other_user_id, user_data_ in user_portfolios.items():

        if other_user_id in user_portfolios[user_id]['likes_received'] and other_user_id in \
                user_portfolios[user_id]['likes_sent']:
            if other_user_id in search_results:
                search_results.remove(other_user_id)
            likes_sent_and_received.append(other_user_id)

        elif other_user_id in user_portfolios[user_id]['likes_received']:
            if other_user_id in search_results:
                search_results.remove(other_user_id)
            likes_received.append(other_user_id)

        elif other_user_id != user_id and other_user_id not in search_results and other_user_id not in viewed_profiles:
            search_results.append(other_user_id)

    context.user_data['search_results'] = likes_sent_and_received + likes_received + search_results
    context.user_data['viewed_profiles'] = viewed_profiles

    send_profiles(update, context)


def send_profiles(update: Update, context: CallbackContext) -> int:
    search_results = context.user_data.get('search_results', [])

    chat_id = update.message.chat_id
    bot = context.bot

    if not search_results:
        bot.send_message(chat_id, "Пока что вы просмотрели все профили, возвращайтесь через время и мы найдем тебе "
                                  "кого-то еще! А возможно тебя кто-то лайкнул, используй /search чтобы вернуться!")

        return ConversationHandler.END

    other_user_id = search_results[0]
    user_data_ = user_portfolios[other_user_id]
    user_name = user_data_["name"]
    user_age = user_data_["age"]
    user_school = user_data_["school"]
    user_program = user_data_["program"]
    user_photo = user_data_["photo"]
    context.user_data['other_user_id'] = other_user_id

    if other_user_id in user_portfolios[chat_id]["likes_received"] and other_user_id in user_portfolios[chat_id][
        "likes_sent"]:
        print("hueta")
        message_text = f"{user_name}, {user_age}\n{user_school}: {user_program}\n\n@{user_portfolios[chat_id]['likes_sent'][other_user_id]} лайкнул ваш профиль в ответ!"
        bot.send_photo(chat_id=chat_id, photo=open(user_photo, 'rb'), caption=message_text)

        del user_portfolios[chat_id]["likes_received"][other_user_id]
        del user_portfolios[chat_id]["likes_sent"][other_user_id]

        return search(update, context)

    message_text = f"{user_name}, {user_age}\n{user_school}: {user_program}"

    if other_user_id in user_portfolios[chat_id]["likes_received"]:
        message_text = f"Этому пользователю понравилась ваша анкета. Лайкни в ответ чтобы познакомиться!\n\n{user_name}, {user_age}\n{user_school}: {user_program}"

    reply_markup = ReplyKeyboardMarkup([['❤️', '👎']], one_time_keyboard=True)
    bot.send_photo(chat_id=chat_id, photo=open(user_photo, 'rb'), caption=message_text,
                   reply_markup=reply_markup)

    return handle_waiting_for_answer(update, context)


def handle_waiting_for_answer(update: Update, context: CallbackContext) -> int:
    other_user_id = context.user_data.get('other_user_id')

    search_results = context.user_data.get('search_results', [])
    search_results.remove(other_user_id)

    context.user_data["search_results"] = search_results

    viewed_profiles = context.user_data.get('viewed_profiles', [])
    viewed_profiles.append(other_user_id)
    context.user_data['viewed_profiles'] = viewed_profiles

    return SEARCH


# Set up the ConversationHandler
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        NAME: [MessageHandler(Filters.text & ~Filters.command, get_name)],
        AGE: [MessageHandler(Filters.regex('^\d+$'), get_age)],
        GENDER: [MessageHandler(Filters.regex('^(Парень 👨|Девушка 👩)$'), get_gender)],
        LOOKING_FOR: [MessageHandler(Filters.regex('^(Парень 👨|Девушка 👩|Неважно)$'), get_looking_for)],
        SCHOOL: [MessageHandler(Filters.regex('^(ИПАМ|ВШКМиС|ВШФ|ВШСГН|ВИШ НМИТ|ВШЭИБ|ВШМ|ВШКИ|ВШП|Преподователь|)$'),
                                get_school)],
        PROGRAM: [MessageHandler(Filters.text & ~Filters.command, get_program)],
        PHOTO: [MessageHandler(Filters.photo, get_photo)],
        SEARCH: [MessageHandler(Filters.text & ~Filters.command, search)],
        WAITING_FOR_ANSWER: [MessageHandler(Filters.text & ~Filters.command, handle_waiting_for_answer)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

# Run the bot
if __name__ == '__main__':
    updater = Updater('6373983672:AAFJPyO1sR_nAm0ae3A4qeR-vhWExuRk7i8', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("search", search))
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()
