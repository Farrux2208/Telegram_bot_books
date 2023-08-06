import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config import *
from sqlite_class import *
from button import *

# state
from aiogram.dispatcher import FSMContext
from state import InfoState
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Baza()

db.baza_create()
db.category_create()
db.books_create()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # print(message)

    telegram_id = message.from_user.id
    data = db.user_select_telegram_id(telegram_id)
    # print(data)
    if data is None:
        
        await message.reply("Kontaktni ulashing / Поделитесь контактом🙏", reply_markup=tel )
    else:
        await message.reply('bosh_menu',reply_markup=menu)


@dp.message_handler(content_types='contact')
async def echo(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    phon_number = message.contact["phone_number"]
    db.user_insert(telegram_id, username, phon_number)
    await message.answer("siz ro'yxatdan o'tdingiz", reply_markup=menu)


@dp.message_handler(content_types='photo')
async def echo(message: types.Message):
    print(message.photo[-1]['file_id'])
    await message.answer("siz ro'yxatdan o'tdingiz")


    

@dp.message_handler(content_types='document')
async def echo(message: types.Message):
    print(message.document['file_id'])
    await message.answer("siz ro'yxatdan o'tdingiz")

 
@dp.message_handler(text='📚 Kitoblar')
async def echo(message: types.Message):
    markup = cat_but()
    await message.answer("Quyidagilardan birini tanlang", reply_markup=markup)




@dp.callback_query_handler(Text(startswith='cat_'))
async def echo(call: types.CallbackQuery):
    # print(call.data[4:])
    indx = call.data.index("_")
    id = call.data[indx+1:]
    print(id)
    markup = by_category_button(id)
    if markup:
        await call.message.answer("tanlang", reply_markup=markup)
    else:
        await call.answer("Ma'lumot topilmadi ")

@dp.callback_query_handler(Text(startswith='books_'))
async def echo(call: types.CallbackQuery):
    # print(call.data[4:])
    indx = call.data.index("_")
    id = call.data[indx+1:]
    data = db.books_select_by_id(id)
    
    await bot.send_photo(chat_id = call.from_user.id, photo = data[4], caption=f"Kitiob nomi: {data[2]}\n\n{data[5]}")
    await bot.send_document(chat_id = call.from_user.id, document=data[3])


# state boshlanishi

@dp.message_handler(text='⬅️ Ortga', state='*')
async def echo(message: types.Message, state: FSMContext):
    markup = cat_but()
    await message.answer("Quyidagilardan birini tanlang", reply_markup= menu)
    await state.finish()


@dp.message_handler(text='🔍 Qidirish', state=None)
async def echo(message: types.Message, state: FSMContext):
    await message.answer("Kitobning nomini kiriting", reply_markup= ortga)
    await InfoState.text.set()



# yozuvni ushlash uchun
@dp.message_handler(state=InfoState.text)
async def echo(message: types.Message, state: FSMContext):
    book_name = message.text
    markup = result_search_button(book_name)
    if markup:
        await message.answer("tanlang", reply_markup=markup)
    else:
        
        await message.answer("Ma'lumot topilmadi!", reply_markup=menu)
    await state.finish()


@dp.message_handler(text='☎️ Aloqa')
async def echo(message: types.Message):
    await message.answer("Admen bilan Bog'lanish:\nTelefon raqam: t.me//+998944240100\nTelegram: @Farrux2208")

    

# test location
# @dp.message_handler(text='☎️ Aloqa')
# async def echo(message: types.Message):
#     await message.answer("Joylashuvni yuboring!", reply_markup=location)


# @dp.message_handler(content_types='location')
# async def echo(message: types.Message):
#     print(message.location['latitude'])
#     print(message.location['longitude'])
    





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)