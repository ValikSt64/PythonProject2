import telebot

bot = telebot.TeleBot("7391508590:AAGGB5gf5Wq90OHxNP8rFn04GqbrgRYnlYs")

@bot.message_handler(commands=["lol"])
def welcome(message):
    bot.send_message(message.chat.id, "Болезнь Альцгеймера и диарея. Ты бежишь, но не можешь вспомнить куда")

@bot.message_handler(commands=["silvia"])
def sticker(message):
    sti = open('silva.png','rb')
    sti1 = open('silva1.png', 'rb')
    sti2 = open('silva2.png', 'rb')
    sti3 = open('silva3.png', 'rb')
    sti4 = open('silva4.png', 'rb')
    sti5 = open('silva5.png', 'rb')
    bot.send_sticker(message.chat.id,sti)
    bot.send_sticker(message.chat.id, sti1)
    bot.send_sticker(message.chat.id, sti2)
    bot.send_sticker(message.chat.id, sti3)
    bot.send_sticker(message.chat.id, sti4)
    bot.send_sticker(message.chat.id, sti5)

@bot.message_handler(commands=["clash"])
def sticker(message):
    mus = open('clash1.mp4','rb')
    bot.send_video(message.chat.id, mus)

@bot.message_handler(commands=["film"])
def info(message):
    bot.send_message(message.chat.id, "Вся линия фильмов трансформеры")

@bot.message_handler(commands=["game"])
def info(message):
    bot.send_message(message.chat.id, "Dota 2, Terraria, Project Zomboid x64, REPO")

@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(message.chat.id, "Имя: Валентин")
    bot.send_message(message.chat.id,"Фамилия: Ступак")
    bot.send_message(message.chat.id,"Страна: Украина")
    bot.send_message(message.chat.id,"Город: Краматорск")

@bot.message_handler(commands=["friends"])
def info(message):
    bot.send_message(message.chat.id, "Все из Зубастого рта а точнее")
    bot.send_message(message.chat.id,"Максимка(Капибариш)")
    bot.send_message(message.chat.id,"Самирка(Кингпро-сильвия)")
    bot.send_message(message.chat.id,"Ромчик")
    bot.send_message(message.chat.id,"Костя(Нерпа)")
    bot.send_message(message.chat.id,"Ваня(Гова)")
    bot.send_message(message.chat.id,"Арсениый(Артем(Арсениый(никто не знает как его на самом деле зовут)))")

@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(message.chat.id, "1.Основная информация  ")
    bot.send_message(message.chat.id,"/film Мой любимый фильм  ")
    bot.send_message(message.chat.id,"/film Мой любимый фильм  ")
    bot.send_message(message.chat.id,"/game Моя любимая игра  ")
    bot.send_message(message.chat.id,"/info Больше информации про меня  ")
    bot.send_message(message.chat.id,"/friends Мои друзя  ")
    bot.send_message(message.chat.id,"2.Смешные команды бота  ")
    bot.send_message(message.chat.id,"/clash СКАЧАТЬ ОБОЯ КЛЕЩЬ РАЯЛЬ ):<  ")
    bot.send_message(message.chat.id,"/silvia Смешные картинки кошки моего друга  ")
    bot.send_message(message.chat.id,"/lol Андекдот  ")


@bot.message_handler(commands=["start"])
def info(message):
    bot.send_message(message.chat.id,"Привет это телеграм бот про мою жизнь(Ступака Валентина)")
    bot.send_message(message.chat.id, "1.Основная информация  ")
    bot.send_message(message.chat.id,"/film Мой любимый фильм  ")
    bot.send_message(message.chat.id,"/game Моя любимая игра  ")
    bot.send_message(message.chat.id,"/info Больше информации про меня  ")
    bot.send_message(message.chat.id,"/friends Мои друзя  ")
    bot.send_message(message.chat.id,"2.Смешные команды бота  ")
    bot.send_message(message.chat.id,"/clash СКАЧАТЬ ОБОЯ КЛЕЩЬ РАЯЛЬ ):<  ")
    bot.send_message(message.chat.id,"/silvia Смешные картинки кошки моего друга  ")
    bot.send_message(message.chat.id,"/lol Андекдот  ")

bot.polling()