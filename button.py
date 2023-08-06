from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from sqlite_class import Baza
from main import db
# tel raqam olish uchun knopka
tel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Telefon raqamni yuborish", request_contact=True)
        ],
        
    ],resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📚 Kitoblar"),
            KeyboardButton("🔍 Qidirish"),
        ],
        [
            KeyboardButton("☎️ Aloqa"),
        ],
        
    ],resize_keyboard=True
)
ortga = ReplyKeyboardMarkup(
    keyboard=[
        
        [
            KeyboardButton("⬅️ Ortga"),
        ],
        
    ],resize_keyboard=True
)


def cat_but():
    data = db.books_select()
    # print(data)
    buttons = InlineKeyboardMarkup(row_width=2)
    for i in data:
        buttons.insert(InlineKeyboardButton(text=i[1], callback_data=f"cat_{i[0]}"))
    return buttons

def by_category_button(id):
    data = db.books_select_by_category(id)
    print(data)
    buttons = InlineKeyboardMarkup(row_width=2)
    if data != []:
        for i in data:
            buttons.insert(InlineKeyboardButton(text=i[2], callback_data=f"books_{i[0]}"))
        return buttons
    else:
        return False



def result_search_button(book_name):
    data = db.search_book(book_name)
    buttons = InlineKeyboardMarkup(row_width=2)
    if data != []:
        for i in data:
            buttons.insert(InlineKeyboardButton(text=i[2], callback_data=f"books_{i[0]}"))
        return buttons
    else:
        return False





location = ReplyKeyboardMarkup(
    keyboard=[
        
        [
            KeyboardButton("Joylashuvni yuborish!", request_location=True),
        ],
        
    ],resize_keyboard=True
)
