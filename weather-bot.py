import telebot
import config
import requests
import json
import os
import sqlite

bot = telebot.TeleBot(config.api_key)

# check for users database existence
if 'users.db' not in os.listdir():
    sqlite.main()

print('Bot started')


def get_link(city, today=True):
    if today:
        return f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.OWM_key}'
    else:
        return f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={config.OWM_key}'


def get_weather_5d_ua(city):
    url = get_link(city, False)
    response = requests.get(url+'&lang=ua')
    if response.status_code == 404:
        return 'Задане місто не існує'
    if response.status_code != 200:
        return 'Помилка, зверніться до розробника'
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


def get_weather_5d_eng(city):
    url = get_link(city, False)
    response = requests.get(url)
    if response.status_code == 404:
        return 'The specified city does not exist'
    if response.status_code != 200:
        return 'Error, contact the developer'
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


def get_weather_today_ua(city):
    url = get_link(city)
    response = requests.get(url+'&lang=ua')
    if response.status_code == 404:
        return 'Задане місто не існує'
    if response.status_code != 200:
        return 'Помилка, зверніться до розробника'
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
    url = get_link(city)
    response = requests.get(url)
    if response.status_code == 404:
        return 'The specified city does not exist'
    if response.status_code != 200:
        return 'Error, contact the developer'
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
        text='Українська 🇺🇦', callback_data='ua'))
    markup.add(telebot.types.InlineKeyboardButton(
        text='English 🇺🇸', callback_data='eng'))
    bot.send_message(user_id, 'Вітання! Обери свою мову нижче!\n\nHello! Choose your language below!', reply_markup=markup)


def hello_message(user_id):
    lng = sqlite.get_language(user_id)
    if lng == 'ua':
        bot.send_message(user_id, 'Вітання!\nНапиши мені назву твого міста, і я відправлю інформацію про погоду в твоєму місті!\n(Ти можеш знову викликати це повідомлення командою /start або /help)\n(Також ти можеш поміняти мову командою /lang)', reply_markup=config.get_keyboard(lng))
    else:
        bot.send_message(user_id, 'Hello!\nWrite me the name of your city and I will send information about the weather in your city!\n(You can call this message again with the command /start or /help)\n(You can also change the language with the /lang command)', reply_markup=config.get_keyboard(lng))


@bot.message_handler(commands=['lang'])
def lang_message(message):
    user_id = str(message.chat.id)
    cng_lng(user_id)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    user_id = str(message.chat.id)
    users = sqlite.get_users()
    if user_id in users:
        hello_message(user_id)
    else:
        sqlite.add_user(user_id)
        cng_lng(user_id)


@bot.message_handler(content_types=["text"])
def weather_message(message):
    user_id = str(message.chat.id)
    if user_id not in sqlite.get_users():
        sqlite.add_user(user_id)
        cng_lng(user_id)
        return
    text = message.text
    req = sqlite.get_last_request(user_id)
    lng = sqlite.get_language(user_id)

    if text in ['Зміна мови', 'Switch language']:
        cng_lng(user_id)
        return
    
    if not req and text in ['Погода: зараз', 'Weather: now', 'Погода: 5 днiв', 'Weather: 5 days']:
        if lng == 'ua':
            respond = 'Зробіть хоча б один запит для використання даної функції'
        else:
            respond = 'Make at least one request to use this feature'
        bot.send_message(user_id, respond, reply_markup=config.get_keyboard(lng))
        return

    
    if text == 'Погода: зараз':
        respond = get_weather_today_ua(req)

    elif text == 'Weather: now':
        respond = get_weather_today_eng(req)

    elif text == 'Погода: 5 днiв':
        answ = get_weather_5d_ua(req)
        if isinstance(answ, str):
            respond = answ
        else:
            bot.send_message(user_id, f'Погода на наступні 5 днів по місту "{req}"', reply_markup=config.get_keyboard(lng))
            for i in answ:
                bot.send_message(user_id, i, reply_markup=config.get_keyboard(lng))
            return

    elif text == 'Weather: 5 days':
        answ = get_weather_5d_eng(req)
        if isinstance(answ, str):
            respond = answ
        else:
            bot.send_message(user_id, f'Weather for 5 days ahead in the city "{req}"', reply_markup=config.get_keyboard(lng))
            for i in answ:
                bot.send_message(user_id, i, reply_markup=config.get_keyboard(lng))
            return

    else:
        sqlite.change_last_request(user_id, text)
        if lng == 'ua':
            respond = get_weather_today_ua(text)
        else:
            respond = get_weather_today_eng(text)
    
    bot.send_message(user_id, respond, reply_markup=config.get_keyboard(lng))


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    user_id = str(call.from_user.id)
    if call.data == 'ua':
        sqlite.change_language(user_id, 'ua')
        hello_message(user_id)
    elif call.data == 'eng':
        sqlite.change_language(user_id, 'eng')
        hello_message(user_id)
    else:
        pass


bot.polling()
