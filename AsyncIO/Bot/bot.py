# Add all libraries for the bot
import json
import apiai
import pyowm
import asyncio
import logging
import requests
import datetime

from bs4 import BeautifulSoup
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import TOKEN
from config import TOKEN_DIALOGFLOW
from config import PROXY_URL


# Create log string
logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s', level=logging.INFO)

# pass to bot token and proxy url
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)


# Create function which process connand /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет!\nИспользуй /help, чтобы узнать список доступных команд!')


# Create function which process connand /help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text('Я могу ответить на следующие команды:', '/weather', '/rates', '/top', '/mk', '/new_year', '/random_image', '/lambo', '/fibo10', '/gas', '/celebrations', '/goodbye', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.HTML)


# Create function which process connand /weather
@dp.message_handler(commands=['weather'])
async def process_weather_command(message: types.Message):
    town_M = 'Москва'
    town_E = 'Екатеринбург'
    town_O = 'Омск'
    town_P = 'Петухово'
    town_S = 'Шерегеш'
    owm = pyowm.OWM('70732ac514bf006244ac74c5f31de5aa', language='ru')
    obs_M = owm.weather_at_place(town_M)
    obs_E = owm.weather_at_place(town_E)
    obs_O = owm.weather_at_place(town_O)
    obs_P = owm.weather_at_place(town_P)
    obs_S = owm.weather_at_place(town_S)
    w_M = obs_M.get_weather()
    w_E = obs_E.get_weather()
    w_O = obs_O.get_weather()
    w_P = obs_P.get_weather()
    w_S = obs_S.get_weather()
    temp_M = w_M.get_temperature('celsius')['temp']
    temp_M = round(temp_M)
    temp_E = w_E.get_temperature('celsius')['temp']
    temp_E = round(temp_E)
    temp_O = w_O.get_temperature('celsius')['temp']
    temp_O = round(temp_O)
    temp_P = w_P.get_temperature('celsius')['temp']
    temp_P = round(temp_P)
    temp_S = w_S.get_temperature('celsius')['temp']
    temp_S = round(temp_S)
    wind_M = w_M.get_wind()['speed']
    wind_M = round(wind_M)
    wind_E = w_E.get_wind()['speed']
    wind_E = round(wind_E)
    wind_O = w_O.get_wind()['speed']
    wind_O = round(wind_O)
    wind_P = w_P.get_wind()['speed']
    wind_P = round(wind_P)
    wind_S = w_S.get_wind()['speed']
    wind_S = round(wind_S)
    status_M = w_M.get_detailed_status()
    status_E = w_E.get_detailed_status()
    status_O = w_O.get_detailed_status()
    status_P = w_P.get_detailed_status()
    status_S = w_S.get_detailed_status()
    msg = '<b>Москва:</b>\nt: {0}, w: {2:2} м/с, {1}.\n<b>Екатеринбург:</b>\nt: {3}, w: {5} м/с, {4}.\n<b>Омск:</b>\nt: {6}, w: {8} м/с, {7}.\n<b>Петухово:</b>\nt: {9}, w: {11} м/с, {10}.\n<b>Шерегеш:</b>\nt: {12}, w: {14:2} м/с, {13}.'.format( str(temp_M) + '°C', status_M, wind_M, str(temp_E) + '°C', status_E, wind_E, str(temp_O) + '°C', status_O, wind_O, str(temp_P) + '°C', status_P, wind_P, str(temp_S) + '°C', status_S, wind_S )
    await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /rates
@dp.message_handler(commands=['rates'])
async def process_rates_command(message: types.Message):
    URL_FOR_RATES = 'https://openexchangerates.org/api/latest.json?app_id=3314f836fa864cb39c496105697a6d7f'
    request = requests.get(URL_FOR_RATES).json()
    rub = round(request['rates']['RUB'], 2)
    eur = round(request['rates']['RUB'] / request['rates']['EUR'], 2)
    cny = round(request['rates']['RUB'] / request['rates']['CNY'], 2)
    try_ = round(request['rates']['RUB'] / request['rates']['TRY'], 2)
    thb = round(request['rates']['RUB'] / request['rates']['THB'], 2)
    kzt = round(request['rates']['RUB'] / request['rates']['KZT'], 2)
    msg = '<code>Exchange rates in RUB:\n\n1. USD     {0} ₽\n2. EUR     {1} ₽\n3. CNY     {2} ₽\n4. TRY     {3} ₽\n5. THB     {4} ₽\n6. KZT     {5} ₽</code>'.format(rub, eur, cny, try_, thb, kzt)
    await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /top
@dp.message_handler(commands=['top'])
async def process_top_command(message: types.Message):
    url = 'https://api.coinmarketcap.com/v1/ticker'
    result = requests.get(url).json()
    n_1 = result[0] ['name']
    p_1 = round(float(result[0] ['price_usd']), 2)
    n_2 = result[1] ['name']
    p_2 = round(float(result[1] ['price_usd']), 2)
    n_3 = result[2] ['name']
    p_3 = round(float(result[2] ['price_usd']), 2)
    n_4 = result[3] ['name']
    p_4 = round(float(result[3] ['price_usd']), 2)
    n_5 = result[4] ['name']
    p_5 = round(float(result[4] ['price_usd']), 2)
    n_6 = result[5] ['name']
    p_6 = round(float(result[5] ['price_usd']), 2)
    n_7 = result[6] ['name']
    p_7 = round(float(result[6] ['price_usd']), 2)
    n_8 = result[7] ['name']
    p_8 = round(float(result[7] ['price_usd']), 2)
    n_9 = result[8] ['name']
    p_9 = round(float(result[8] ['price_usd']), 2)
    n_10 = result[9] ['name']
    p_10 = round(float(result[9] ['price_usd']), 2)
    msg = '<code>#Top 10 cryptocurrency in USD\n\n1. {0:15}${1}\n2. {2:15}${3}\n3. {4:15}${5}\n4. {6:15}${7}\n5. {8:15}${9}\n6. {10:15}${11}\n7. {12:15}${13}\n8. {14:15}${15}\n9. {16:15}${17}\n10.{18:15}${19}</code>'.format(n_1, p_1, n_2, p_2, n_3, p_3, n_4, p_4, n_5, p_5, n_6, p_6, n_7, p_7, n_8, p_8, n_9, p_9, n_10, p_10)
    await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /mk
@dp.message_handler(commands=['mk'])
async def process_mk_command(message: types.Message):
    global_url = 'https://api.coinmarketcap.com/v2/global/?convert=USD'
    request = requests.get(global_url)
    results = request.json()
    active_currencies = results['data']['active_cryptocurrencies']
    active_markets = results['data']['active_markets']
    bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
    global_cap = int(results['data']['quotes']['USD']['total_market_cap'])
    global_volume = int(results['data']['quotes']['USD']['total_volume_24h'])
    active_currencies_strings = '{:,}'.format(active_currencies)
    active_markets_string = '{:,}'.format(active_markets)
    global_cap_string = '{:,}'.format(global_cap)
    global_volume_string = '{:,}'.format(global_volume)
    msg = 'There are currently ' + active_currencies_strings + ' active cryptocurrencies and ' + active_markets_string + ' active markets.\nThe global cap of all cryptos is ' + global_cap_string + ' USD' + ' and the 24h global volume is ' + global_volume_string + ' USD.\nBitcoin\'s total percentage of global cap is ' + str( bitcoin_percentage ) + '%.'
    await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /new_year
@dp.message_handler(commands=['new_year'])
async def process_new_year_command(message: types.Message):
    countdown = lambda : datetime.datetime(2020,1,1,00,00) - datetime.datetime.now().replace(microsecond=0)
    msg = '<code>New year is coming\n' + str(countdown()) + '</code>'
    await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /fibo10
@dp.message_handler(commands=['fibo10'])
async def process_fibo10_command(message: types.Message):
    a, b = 0, 1
    fibo_series = []
    x = 0
    while x < 10:
        fibo_series.append(a)
        a, b = b, a + b
        x += 1
    msg = '<code>First ten members fibonacci series\n' + str(fibo_series) + '</code>'
    await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /gas
@dp.message_handler(commands=['gas'])
async def process_gas_command(message: types.Message):
    response = requests.get('https://ethgasstation.info')
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find(class_="row tile_count")
    a_p = [row.text for row in tds.find_all(class_="count")]
    msg = 'Ethereum Gas Prices\n\nLow speed tx = {3} gwei or {2} USD\nNormal speed tx = {1} gwei or {0} USD\nWaiting time = {4} sec or {5} blocks'.format(a_p[0][1:], a_p[1], a_p[2][1:], a_p[3], a_p[4], a_p[5] )
    await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /celebrations
@dp.message_handler(commands=['celebrations'])
async def process_celebrations_command(message: types.Message):
    html = requests.get('http://kakoysegodnyaprazdnik.ru/').text
    xml = BeautifulSoup(html, 'lxml')
    celebrations = xml.find(class_="listing_wr")
    celebration = [row.text for row in celebrations.find_all(itemprop="text")]
    msg = '\n'.join(celebration)
    await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /random_image
@dp.message_handler(commands=['random_image'])
async def process_random_image_command(message: types.Message):
    msg = requests.get('https://loremflickr.com/1280/720/random', allow_redirects=True).content
    await bot.send_photo(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /lambo
@dp.message_handler(commands=['lambo'])
async def process_lambo_command(message: types.Message):
    msg = requests.get('https://loremflickr.com/1280/720/lambo', allow_redirects=True).content
    await bot.send_photo(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode=ParseMode.HTML)


# Create function which process connand /goodbye
@dp.message_handler(commands=['goodbye'])
async def process_goodbye_command(message: types.Message):
    message_text = pre(emojize('Давай покеда! :sunglasses:'))
    await bot.send_message(message.chat.id, message_text, parse_mode=ParseMode.MARKDOWN)


# Create function which process another connand
@dp.message_handler(regexp=r"/(.+)")
async def process_crypto_ticker_command(message: types.Message):
    print(message)
    url = 'https://api.coinmarketcap.com/v1/ticker{}'.format(message['text'])
    result = requests.get(url).json()
    name = result[0] ['name']
    symbol = result[0] ['symbol']
    price_btc = result[0] ['price_btc']
    price_usd = float(result[0] ['price_usd'])
    price = round(price_usd, 2)
    market_cap = int(float(result[0] ['market_cap_usd']))
    market = '{:,}'.format(market_cap)
    change_1h = result[0] ['percent_change_1h']
    change_24h = result[0] ['percent_change_24h']
    change_7d = result[0] ['percent_change_7d']
    msg = '<code>{0:20}{1}\n{2:20}#{3}\n{4:20}{5}\n{6:20}${7}\n{8:20}${9}\n{10:20}{11}%\n{12:20}{13}%\n{14:20}{15}%</code>'.format('Coin name:', name,'Market ticker:', symbol, 'Price BTC:', price_btc, 'Price USD:', price, 'Market cap:', market, 'Change 1h:', change_1h, 'Change 24h:', change_24h, 'Change 7d:', change_7d )
    await bot.send_message(message.chat.id, msg, parse_mode=ParseMode.HTML)


# Create function which process any text message from user
# and resend their to Dialogflow
@dp.message_handler()
async def dialog_flow_message(message: types.Message):
    request = apiai.ApiAI(TOKEN_DIALOGFLOW).text_request()
    request.lang = 'ru'
    request.session_id = 'Test_session_1'
    request.query = message['text']
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    msg = responseJson['result']['fulfillment']['speech']
    
    if msg:
        await bot.send_message(message.chat.id, msg, parse_mode=ParseMode.HTML)
    else:
        msg = 'Ты чо мелешь паскуда?'
        await bot.send_message(message.chat.id, msg, parse_mode=ParseMode.HTML)


# Create function which process any text message from user
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.chat.id, msg.text)


# Create function which process any message from user
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                        italic('\nЯ просто напомню,'), 'что есть',
                        code('команда'), '/help')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


# Define the function that sends weather to the chat on a schedule
@dp.message_handler()
async def sched():
    town_M = 'Москва'
    town_E = 'Екатеринбург'
    town_O = 'Омск'
    town_P = 'Петухово'
    town_S = 'Шерегеш'
    owm = pyowm.OWM('70732ac514bf006244ac74c5f31de5aa', language='ru')
    obs_M = owm.weather_at_place(town_M)
    obs_E = owm.weather_at_place(town_E)
    obs_O = owm.weather_at_place(town_O)
    obs_P = owm.weather_at_place(town_P)
    obs_S = owm.weather_at_place(town_S)
    w_M = obs_M.get_weather()
    w_E = obs_E.get_weather()
    w_O = obs_O.get_weather()
    w_P = obs_P.get_weather()
    w_S = obs_S.get_weather()
    temp_M = w_M.get_temperature('celsius')['temp']
    temp_M = round(temp_M)
    temp_E = w_E.get_temperature('celsius')['temp']
    temp_E = round(temp_E)
    temp_O = w_O.get_temperature('celsius')['temp']
    temp_O = round(temp_O)
    temp_P = w_P.get_temperature('celsius')['temp']
    temp_P = round(temp_P)
    temp_S = w_S.get_temperature('celsius')['temp']
    temp_S = round(temp_S)
    wind_M = w_M.get_wind()['speed']
    wind_M = round(wind_M)
    wind_E = w_E.get_wind()['speed']
    wind_E = round(wind_E)
    wind_O = w_O.get_wind()['speed']
    wind_O = round(wind_O)
    wind_P = w_P.get_wind()['speed']
    wind_P = round(wind_P)
    wind_S = w_S.get_wind()['speed']
    wind_S = round(wind_S)
    status_M = w_M.get_detailed_status()
    status_E = w_E.get_detailed_status()
    status_O = w_O.get_detailed_status()
    status_P = w_P.get_detailed_status()
    status_S = w_S.get_detailed_status()
    msg = '<b>Москва:</b>\nt: {0}, w: {2:2} м/с, {1}.\n<b>Екатеринбург:</b>\nt: {3}, w: {5} м/с, {4}.\n<b>Омск:</b>\nt: {6}, w: {8} м/с, {7}.\n<b>Петухово:</b>\nt: {9}, w: {11} м/с, {10}.\n<b>Шерегеш:</b>\nt: {12}, w: {14:2} м/с, {13}.'.format( str(temp_M) + '°C', status_M, wind_M, str(temp_E) + '°C', status_E, wind_E, str(temp_O) + '°C', status_O, wind_O, str(temp_P) + '°C', status_P, wind_P, str(temp_S) + '°C', status_S, wind_S )
    await bot.send_message(chat_id=-1001116481457, text=msg, parse_mode=ParseMode.HTML)


# Create scheduler with interval 1 minute
scheduler = AsyncIOScheduler()
scheduler.add_job(sched, 'cron', day_of_week='mon-sun', hour=21, minute=33)
scheduler.start()


if __name__ == '__main__':
    executor.start_polling(dp)