import telebot
import config
import requests
import json
import os

bot = telebot.TeleBot(config.api_key)

# check for folder users existence
if 'users' not in os.listdir():
    os.mkdir("users")

print('Bot started')


def get_weather_5d_ru(city, usr_id):
    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    querystring = {"lang": "ru", "q": f"{city}"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "type here your api key"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if str(response) == '<Response [404]>':
        return 'Заданный город не существует'
    data = json.loads(response.text)
    s = ''
    result = []
    for i in data['list']:
        date = str(i['dt_txt']).split(' ')
        day = date[0].split('-')
        day = f'{day[2]}/{day[1]}/{day[0]}'
        time_ = date[1].split(':')
        time_ = f'{time_[0]}:00'
        tempa = '{0:+3.0f}'.format(int(i['main']['temp'])-273.15)
        weath = i['weather'][0]['description']
        if time_ == '12:00':
            s = f'''{day} {time_} :
Температура:{tempa}°C
Погодные условия: {weath}\n\n'''
            result.append(s)
    return result


def get_weather_5d_ua(city, usr_id):
    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    querystring = {"lang": "ua", "q": f"{city}"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "type here your api key"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if str(response) == '<Response [404]>':
        return 'Задане місто не існує'
    data = json.loads(response.text)
    s = ''
    result = []
    for i in data['list']:
        date = str(i['dt_txt']).split(' ')
        day = date[0].split('-')
        day = f'{day[2]}/{day[1]}/{day[0]}'
        time_ = date[1].split(':')
        time_ = f'{time_[0]}:00'
        tempa = '{0:+3.0f}'.format(int(i['main']['temp'])-273.15)
        weath = i['weather'][0]['description']
        if time_ == '12:00':
            s = f'''{day} {time_} :
Температура:{tempa}°C
Погодні умови: {weath}\n\n'''
            result.append(s)
    return result


def get_weather_5d_eng(city, usr_id):
    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    querystring = {"lang": "eng", "q": f"{city}"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "type here your api key"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if str(response) == '<Response [404]>':
        return 'The specified city does not exist'
    data = json.loads(response.text)
    s = ''
    result = []
    for i in data['list']:
        date = str(i['dt_txt']).split(' ')
        day = date[0].split('-')
        day = f'{day[2]}/{day[1]}/{day[0]}'
        time_ = date[1].split(':')
        time_ = f'{time_[0]}:00'
        tempa = '{0:+3.0f}'.format(int(i['main']['temp'])-273.15)
        weath = i['weather'][0]['description']
        if time_ == '12:00':
            s = f'''{day} {time_} :
Temperature:{tempa}°C
Weather: {weath}\n\n'''
            result.append(s)
    return result


def get_weather_today_rus(city):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"lang": "ru", "q": f"{city}"}
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "type here your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if str(response) == '<Response [404]>':
        return 'Заданный город не существует'
    weather = json.loads(response.text)
    weather_now = weather['weather'][0]['description']
    weather_temp_now = weather['main']['temp'] - 273.15
    weather_temp_feels_like = weather['main']['feels_like'] - 273.15
    weather_temp_min = weather['main']['temp_min'] - 273.15
    weather_temp_max = weather['main']['temp_max'] - 273.15
    weather_pressure = round((int(weather['main']['pressure'])/1.333), 2)
    weather_humidity = weather['main']['humidity']
    weather_wind_speed = weather['wind']['speed']
    weather_info = f'''Погодные условия: {weather_now}

Температура:
    Сейчас: {int(weather_temp_now)}°C, ощущается как {int(weather_temp_feels_like)}°C
    Минимальная температура за сегодня: {int(weather_temp_min)}°C
    Максимальная температура за сегодня: {int(weather_temp_max)}°C

Давление: {weather_pressure} мм рт.ст.

Влажность: {weather_humidity}%

Скорость ветра: {weather_wind_speed} м/с'''

    return weather_info


def get_weather_today_ua(city):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"lang": "ua", "q": f"{city}"}
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "type here your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if str(response) == '<Response [404]>':
        return 'Задане місто не існує'
    weather = json.loads(response.text)
    weather_now = weather['weather'][0]['description']
    weather_temp_now = weather['main']['temp'] - 273.15
    weather_temp_feels_like = weather['main']['feels_like'] - 273.15
    weather_temp_min = weather['main']['temp_min'] - 273.15
    weather_temp_max = weather['main']['temp_max'] - 273.15
    weather_pressure = round((int(weather['main']['pressure'])/1.333), 2)
    weather_humidity = weather['main']['humidity']
    weather_wind_speed = weather['wind']['speed']
    weather_info = f'''Погодні умови: {weather_now}

Температура:
    Зараз: {int(weather_temp_now)}°C, відчувається як {int(weather_temp_feels_like)}°C
    Мінімальна температура за сьогодні: {int(weather_temp_min)}°C
    Максимальна температура за сьогодні: {int(weather_temp_max)}°C

Тиск: {weather_pressure} мм рт.ст.

Вологість: {weather_humidity}%

Швидкість вітру: {weather_wind_speed} м/с'''

    return weather_info


def get_weather_today_eng(city):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"lang": "eng", "q": f"{city}"}
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "type here your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if str(response) == '<Response [404]>':
        return 'The specified city does not exist'
    weather = json.loads(response.text)
    weather_now = weather['weather'][0]['description']
    weather_temp_now = weather['main']['temp'] - 273.15
    weather_temp_feels_like = weather['main']['feels_like'] - 273.15
    weather_temp_min = weather['main']['temp_min'] - 273.15
    weather_temp_max = weather['main']['temp_max'] - 273.15
    weather_pressure = round((int(weather['main']['pressure'])/1.333), 2)
    weather_humidity = weather['main']['humidity']
    weather_wind_speed = weather['wind']['speed']
    weather_info = f'''Weather: {weather_now}

Temperature:
    Now: {int(weather_temp_now)}°C, feels like {int(weather_temp_feels_like)}°C
    Minimum temperature today: {int(weather_temp_min)}°C
    Maximum temperature for today: {int(weather_temp_max)}°C

Pressure: {weather_pressure} mmHg

Humidity: {weather_humidity}%

Wind speed: {weather_wind_speed} m/s'''

    return weather_info


def cng_lng(user_id):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text='Русский 🇷🇺', callback_data='rus'))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Українська 🇺🇦', callback_data='ua'))
    markup.add(telebot.types.InlineKeyboardButton(
        text='English 🇺🇸', callback_data='eng'))
    bot.send_message(user_id, 'Привет! Выбери свой язык ниже!\n\nВітання! Обери свою мову нижче!\n\nHello! Choose your language below!', reply_markup=markup)


def reg(user_id):
    if 'last_request' not in os.listdir(f'users/{user_id}'):
        f = open(f'users/{user_id}/last_request', 'w')
        f.write('')
        f.close()
        hello_message(user_id)
    else:
        hello_message(user_id)


def hello_message(user_id):
    f = open(f'users/{user_id}/lang', 'r')
    lng = f.read()
    if lng == 'rus':
        bot.send_message(user_id, 'Привет!\nНапиши мне название твоего города, и я отправлю информацию о погоде в твоём городе!\n(Ты можешь снова вызвать это сообщение командой /start или /help)\n(Также ты можешь поменять язык командой /lang)', reply_markup=config.get_keyboard_rus())
    elif lng == 'ua':
        bot.send_message(user_id, 'Вітання!\nНапиши мені назву твого міста, і я відправлю інформацію про погоду в твоєму місті!\n(Ти можеш знову викликати це повідомлення командою /start або /help)\n(Також ти можеш поміняти мову командою /lang)', reply_markup=config.get_keyboard_ua())
    else:
        bot.send_message(user_id, 'Hello!\nWrite me the name of your city and I will send information about the weather in your city!\n(You can call this message again with the command /start or /help)\n(You can also change the language with the /lang command)', reply_markup=config.get_keyboard_en())


@bot.message_handler(commands=['lang'])
def lang_message(message):
    user_id = message.chat.id
    cng_lng(user_id)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    user_id = message.chat.id
    if str(user_id) in os.listdir('users'):
        hello_message(user_id)
    else:
        os.system(f'mkdir users/{user_id}')
        cng_lng(user_id)


@bot.message_handler(content_types=["text"])
def weather_message(message):
    user_id = message.chat.id
    text = message.text
    if text == 'Погода: сейчас':
        f = open(f'users/{user_id}/last_request', 'r')
        req = f.read()
        if req == '':
            bot.send_message(user_id, 'Сделайте хотя бы один запрос для использования данной функции', reply_markup=config.get_keyboard_rus)
        else:
            s = get_weather_today_rus(req)
            bot.send_message(user_id, s, reply_markup=config.get_keyboard_rus())

    elif text == 'Погода: зараз':
        f = open(f'users/{user_id}/last_request', 'r')
        req = f.read()
        if req == '':
            bot.send_message(user_id, 'Зробіть хоча б один запит для використання даної функції', reply_markup=config.get_keyboard_ua())
        else:
            s = get_weather_today_ua(req)
            bot.send_message(user_id, s, reply_markup=config.get_keyboard_ua())

    elif text == 'Weather: now':
        f = open(f'users/{user_id}/last_request', 'r')
        req = f.read()
        if req == '':
            bot.send_message(user_id, 'Make at least one request to use this feature', reply_markup=config.get_keyboard_en())
        else:
            s = get_weather_today_eng(req)
            bot.send_message(user_id, s, reply_markup=config.get_keyboard_en())

    elif text == 'Погода: 5 дней':
        f = open(f'users/{user_id}/last_request', 'r')
        req = f.read()
        if req == '':
            bot.send_message(user_id, 'Сделайте хотя бы один запрос для использования данной функции', reply_markup=config.get_keyboard_rus())
            return
        answ = get_weather_5d_ru(req, user_id)
        if 'str' in str(type(answ)):
            bot.send_message(user_id, answ, reply_markup=config.get_keyboard_rus())
        else:
            bot.send_message(user_id, f'Погода на 5 дней вперёд по городу "{req}"', reply_markup=config.get_keyboard_rus())
            for i in answ:
                bot.send_message(user_id, i, reply_markup=config.get_keyboard_rus())

    elif text == 'Погода: 5 днiв':
        f = open(f'users/{user_id}/last_request', 'r')
        req = f.read()
        if req == '':
            bot.send_message(user_id, 'Зробіть хоча б один запит для використання даної функції', reply_markup=config.get_keyboard_ua())
            return
        answ = get_weather_5d_ua(req, user_id)
        if 'str' in str(type(answ)):
            bot.send_message(user_id, answ, reply_markup=config.get_keyboard_ua())
        else:
            bot.send_message(user_id, f'Погода на наступні 5 днів по місту "{req}"', reply_markup=config.get_keyboard_ua())
            for i in answ:
                bot.send_message(user_id, i, reply_markup=config.get_keyboard_ua())

    elif text == 'Weather: 5 days':
        f = open(f'users/{user_id}/last_request', 'r')
        req = f.read()
        if req == '':
            bot.send_message(user_id, 'Make at least one request to use this feature', reply_markup=config.get_keyboard_en())
            return
        answ = get_weather_5d_eng(req, user_id)
        if 'str' in str(type(answ)):
            bot.send_message(user_id, answ, reply_markup=config.get_keyboard_en())
        else:
            bot.send_message(user_id, f'Weather for 5 days ahead in the city "{req}"', reply_markup=config.get_keyboard_en())
            for i in answ:
                bot.send_message(user_id, i, reply_markup=config.get_keyboard_en())

    elif text == 'Смена языка' or text == 'Зміна мови' or text == 'Switch language':
        cng_lng(user_id)

    else:
        f = open(f'users/{user_id}/last_request', 'w')
        f.write(text)
        f.close()
        f = open(f'users/{user_id}/lang', 'r')
        lng = f.read()
        f.close()
        if lng == 'rus':
            s = get_weather_today_rus(text)
            bot.send_message(user_id, s, reply_markup=config.get_keyboard_rus())
        elif lng == 'ua':
            s = get_weather_today_ua(text)
            bot.send_message(user_id, s, reply_markup=config.get_keyboard_ua())
        else:
            s = get_weather_today_eng(text)
            bot.send_message(user_id, s, reply_markup=config.get_keyboard_en())


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    user_id = call.from_user.id
    if call.data == 'rus':
        f = open(f'users/{user_id}/lang', 'w')
        f.write('rus')
        f.close()
        reg(user_id)
    elif call.data == 'ua':
        f = open(f'users/{user_id}/lang', 'w')
        f.write('ua')
        f.close()
        reg(user_id)
    elif call.data == 'eng':
        f = open(f'users/{user_id}/lang', 'w')
        f.write('eng')
        f.close()
        reg(user_id)
    else:
        pass


bot.polling()
