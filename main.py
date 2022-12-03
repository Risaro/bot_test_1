
from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher

# Токен бота для подключения к нему
TOKEN = "5646699823:AAE9SZ1NHJyJut9vlfDHzta7M9HXZj-2Xdg"
# Подкюлчаем бота к токену и
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Создание команды         название команды
#                               =
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
#Создание массива кнопок
greet_markup = ReplyKeyboardMarkup()
#создание кнопки
button_hi = KeyboardButton('/help')
#добавление кнопки
greet_markup.add(button_hi)
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, напиши что нибудь", reply_markup=greet_markup)




@dp.message_handler(commands=['help'])
async def proccess_help_command(message: types.Message):
    await message.reply("Привет\n Команды в разработке")




@dp.message_handler(commands=['img'])
async def img_send(msg: types.Message):
    # открытие изображение в переменную
    photo = open('img.jpg', 'rb')
    # id  в чат        фото
    await bot.send_photo(msg.from_user.id, photo)
    #       0           1






if __name__ == '__main__':
    executor.start_polling(dp)
    # добавляе задачу в выполнение