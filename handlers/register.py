from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext, ConversationHandler
from services.database import update_user

NAME, GENDER, LOCATION = range(3)

def request_contact(update: Update, context: CallbackContext):
    contact_btn = ReplyKeyboardMarkup(
        [[KeyboardButton("Raqamni yuborish", request_contact=True)]],
        resize_keyboard=True, one_time_keyboard=True
    )
    update.message.reply_text("Raqamingizni yuboring:", reply_markup=contact_btn)
    return NAME

def get_name(update: Update, context: CallbackContext):
    contact = update.message.contact
    chat_id = update.effective_chat.id
    update_user(chat_id, "number", contact.phone_number)
    update.message.reply_text("Ismingizni kiriting:")
    return GENDER

def get_gender(update: Update, context: CallbackContext):
    name = update.message.text
    chat_id = update.effective_chat.id
    update_user(chat_id, "name", name)

    gender_btn = ReplyKeyboardMarkup(
        [["Erkak", "Ayol"]],
        resize_keyboard=True, one_time_keyboard=True
    )
    update.message.reply_text("Jinsingizni tanlang:", reply_markup=gender_btn)
    return LOCATION

def get_location(update: Update, context: CallbackContext):
    gender = update.message.text
    chat_id = update.effective_chat.id
    update_user(chat_id, "gender", gender)

    update.message.reply_text("Iltimos, lokatsiyangizni yuboring ",
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(" Lokatsiyani yuborish", request_location=True)]],
            resize_keyboard=True, one_time_keyboard=True
        )
    )
    return ConversationHandler.END

def save_location(update: Update, context: CallbackContext):
    location = update.message.location
    chat_id = update.effective_chat.id
    loc_data = {
        "longatute": location.longitude,
        "latetute": location.latitude
    }
    update_user(chat_id, "location", loc_data)

    update.message.reply_text("Ro'yxatdan o'tganingiz uchun rahmat ")
    return ConversationHandler.END
