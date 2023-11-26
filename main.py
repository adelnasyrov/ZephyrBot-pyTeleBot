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
def start(update: Update) -> int:
    update.message.reply_text(
        "Привет, для начала заполним твою анкету. "
        "Как тебя зовут?"
    )
    return NAME


# Function to handle user's name
def get_name(update: Update, context: CallbackContext) -> int:
    name = update.message.text
    user_portfolios[update.message.chat_id] = {"name": name}
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
    print(user_portfolios)
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
    if user_id not in user_portfolios:
        update.message.reply_text(
            "Завреши регистрацию используя команду /start прежде чем знакомиться!"
        )
        return ConversationHandler.END

    # Simulate searching for other users' profiles

    search_results = context.user_data.get("search_results")

    if search_results is None:
        search_results = []

    viewed_profiles = context.user_data.get("viewed_profiles")

    if viewed_profiles is None:
        viewed_profiles = []

    for other_user_id, user_data_ in user_portfolios.items():
        if other_user_id != user_id and other_user_id not in search_results and other_user_id not in viewed_profiles:
            search_results.append(other_user_id)
    context.user_data['search_results'] = search_results
    context.user_data['viewed_profiles'] = viewed_profiles
    send_profiles(update, context)


def send_profiles(update: Update, context: CallbackContext) -> int:
    search_results = context.user_data.get('search_results', [])

    chat_id = update.message.chat_id
    bot = context.bot

    if not search_results:
        bot.send_message(chat_id, "Пока что вы просмотрели все профили, возвращайтесь через время и мы найдем вам "
                                  "кого-то еще! /search")

        return ConversationHandler.END

    try:
        other_user_id = search_results[0]
        user_data_ = user_portfolios[other_user_id]
        user_name = user_data_["name"]
        user_age = user_data_["age"]
        user_school = user_data_["school"]
        user_program = user_data_["program"]
        user_photo = user_data_["photo"]
        context.user_data['other_user_id'] = other_user_id
        message_text = f"{user_name}, {user_age}\n{user_school}: {user_program}"
        reply_markup = ReplyKeyboardMarkup([['❤️', '👎']], one_time_keyboard=True)
        bot.send_photo(chat_id=chat_id, photo=open(user_photo, 'rb'), caption=message_text,
                       reply_markup=reply_markup)
        return handle_waiting_for_answer(update, context)

    except IndexError:
        bot.send_message(chat_id, "Пока что вы просмотрели все профили, возвращайтесь через время и мы найдем вам "
                                  "кого-то еще! /search")
        return ConversationHandler.END


def send_profile_back(chat_id, profile, text, bot):
    user_name = profile["name"]
    user_age = profile["age"]
    user_school = profile["school"]
    user_program = profile["program"]

    message_text = f"{user_name}, {user_age}\n{user_school}: {user_program}"
    reply_markup = ReplyKeyboardMarkup([['❤️', '👎']], one_time_keyboard=True)
    bot.send_photo(chat_id=chat_id, photo=open(profile["photo"], 'rb'), caption=text + "\n" + message_text,
                   reply_markup=reply_markup)


def handle_waiting_for_answer(update: Update, context: CallbackContext) -> int:
    print('nigger')
    # Handle the user's answer as needed
    answer = update.message.text
    other_user_id = context.user_data.get('other_user_id')

    search_results = context.user_data.get('search_results', [])
    print(context.user_data.get('search_results', []))
    search_results.remove(other_user_id)
    context.user_data["search_results"] = search_results
    print(context.user_data.get('search_results', []))

    viewed_profiles = context.user_data.get('viewed_profiles', [])
    viewed_profiles.append(other_user_id)
    context.user_data['viewed_profiles'] = viewed_profiles
    # if answer == "❤️": chat_member = context.bot.get_chat_member(chat_id=update.message.chat_id,
    # user_id=update.message.chat_id) send_profile_back(other_user_id, user_portfolios[update.message.chat_id],
    # f"{chat_member} лайкнул ваш профиль") print(f"{update.message.chat_id} liked {other_user_id}")

    # Transition back to the SEND_PROFILES state
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
