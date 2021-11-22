from telebot import types
api_key = 'type here your token'
OWM_key = 'type here your token'


def get_keyboard_rus():
    keyboard_rus = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    button_last_request = types.KeyboardButton(text="Погода: сейчас")
    button_5day = types.KeyboardButton(text="Погода: 5 дней")
    button_lng = types.KeyboardButton(text="Смена языка")
    keyboard_rus.add(button_last_request)
    keyboard_rus.add(button_5day)
    keyboard_rus.add(button_lng)
    return keyboard_rus


def get_keyboard_ua():
    keyboard_ua = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    button_last_request = types.KeyboardButton(text="Погода: зараз")
    button_5day = types.KeyboardButton(text="Погода: 5 днiв")
    button_lng = types.KeyboardButton(text="Зміна мови")
    keyboard_ua.add(button_last_request)
    keyboard_ua.add(button_5day)
    keyboard_ua.add(button_lng)
    return keyboard_ua


def get_keyboard_en():
    keyboard_en = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    button_last_request = types.KeyboardButton(text="Weather: now")
    button_5day = types.KeyboardButton(text="Weather: 5 days")
    button_lng = types.KeyboardButton(text="Switch language")
    keyboard_en.add(button_last_request)
    keyboard_en.add(button_5day)
    keyboard_en.add(button_lng)
    return keyboard_en
