from telebot import types
api_key = 'token'
OWM_key = 'token'


def get_keyboard(lng):
    last_request = "Погода: зараз" if lng == 'ua' else "Weather: now"
    five_days = "Погода: 5 днiв" if lng == 'ua' else "Weather: 5 days"
    change_lng = "Зміна мови" if lng == 'ua' else "Switch language"
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    button_last_request = types.KeyboardButton(text=last_request)
    button_5day = types.KeyboardButton(text=five_days)
    button_lng = types.KeyboardButton(text=change_lng)
    keyboard.add(button_last_request)
    keyboard.add(button_5day)
    keyboard.add(button_lng)
    return keyboard

