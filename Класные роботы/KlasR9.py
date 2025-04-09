import telebot
from PIL.DdsImagePlugin import item3
from telebot import types
import random

bot = telebot.TeleBot("7391508590:AAGGB5gf5Wq90OHxNP8rFn04GqbrgRYnlYs")

@bot.message_handler(commands=["start"])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Яку оцінку сьогодні отримаєш?")
    item2 = types.KeyboardButton("😊 Як справи?")
    item3 = types.KeyboardButton("🛍 купи что нибуть в магазине")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Привет дорогой что ты хотел?".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def processing_text(message):

    if message.text == "🎲 Яку оцінку сьогодні отримаєш?":
        bot.send_message(message.chat.id, random.randint(2,12))
    elif message.text  == "😊 Як справи?":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Так", callback_data='good')
        item2 = types.InlineKeyboardButton("Ні", callback_data='bad')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Чудово! Убрался дома?".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)
    elif message.text == "🛍 купи что нибуть в магазине":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Шоколадку", callback_data='choco')
        item2 = types.InlineKeyboardButton("Фруктов или Овошей", callback_data='fruit')
        item3 = types.InlineKeyboardButton("Ничего", callback_data='noth')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "🛍 Что купить в магазине?".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

    elif message.text  == "Привіт":
        bot.send_message(message.chat.id, "Здоров")
    elif message.text == "У тебя спина белая😁":
        bot.send_message(message.chat.id, "А у тебя кривая😘")
    else:
        bot.send_message(message.chat.id, "Я не зрозумів тебе")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, '😁')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                    text="Молодец жди вкусняшек 😊")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="😊 Як справи?", reply_markup=None)
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Волар бебе прийдет по попе надает👿')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                    text="👿👿👿")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="😊 Як справи?", reply_markup=None)
            elif call.data == 'choco':
                bot.send_message(call.message.chat.id, 'Ты на деете😠')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                    text="A a a")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="🛍 Что купить в магазине?", reply_markup=None)
            elif call.data == 'fruit':
                bot.send_message(call.message.chat.id, '😁😁😁')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                    text="Окей здоровое питания всегда хорошо😘")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="🛍 Что купить в магазине?", reply_markup=None)
            elif call.data == 'noth':
                bot.send_message(call.message.chat.id, '🤨')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                    text="Ну ладно😑")

            # remove inline buttons


            # show alert
    except Exception as e:
        print(repr(e))

# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'choco':
#                 bot.send_message(call.message.chat.id, 'А а а')
#                 bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
#                     text="Ты на деете😠")
#             elif call.data == 'fruit':
#                 bot.send_message(call.message.chat.id, '😁😁😁')
#                 bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
#                     text="Окей здоровое питания всегда хорошо😘")
#             elif call.data == 'noth':
#                 bot.send_message(call.message.chat.id, '🤨')
#                 bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
#                     text="Ну ладно😑")
#
#             # remove inline buttons
#
#
#             # show alert
#     except Exception as e:
#         print(repr(e))

bot.polling()