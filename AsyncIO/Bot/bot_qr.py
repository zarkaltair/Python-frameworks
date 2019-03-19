import asyncio
import logging
import pyqrcode
import io

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from config import TOKEN
from config import PROXY_URL


# Create log string
logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s', level=logging.INFO)

# pass to bot token and proxy url
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)


# Create function which process connand /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('''Привет!\nЭтот бот поможет тебе превратить твою ссылку в QR-код,
 для этого тебе нужно всего лишь отправить свою ссылку боту.''')


# Create function which process convertation url to QR-code
@dp.message_handler(regexp=r'(.+)')
async def process_url_to_qrcode(message: types.Message):
    buffer = io.BytesIO()
    msg = pyqrcode.create(message.text)
    msg.png(buffer)
    print(list(buffer.getvalue()))
    await bot.send_photo(message.chat.id, msg, reply_to_message_id=message.message_id)


# Create function which process any message from user
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                        '\nЕсли хочешь получить QR-код просто отправь ссылку.')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)


'''
{"message_id": 1029, 
 "from": {"id": 252027450, 
          "is_bot": false, 
          "first_name": "Zark", 
          "last_name": "Alt", 
          "username": "Zark_Alt", 
          "language_code": "ru"}, 
 "chat": {"id": 252027450, 
          "first_name": "Zark", 
          "last_name": "Alt", 
          "username": "Zark_Alt", 
          "type": "private"}, 
 "date": 1552814245, 
 "text": "www.google.com", 
 "entities": [{"offset": 0, 
               "length": 14, 
               "type": "url"}]}
'''