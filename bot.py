import telebot
import os 


bot = telebot.TeleBot("8077742390:AAGvPjKiMPTOYAiAaccET-tUxZP6toCs23I")
    
@bot.message_handler(commands=['help']) 
def send_help(message): 
    bot.reply_to(message, 'вот все команды, /start,/bye,/games,/password,/trash')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! я телеграм бот, я могу советовать игры и делать пароли,если нужна помощь. напиши /help !")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=('games')) 
def send_games(message): 
    bot.reply_to(message, "вот типы игр./shooter,/Horror,/adventures")

@bot.message_handler(commands=('shooter'))
def send_shooter(message): 
    bot.reply_to(message, "вот список: 1.Fortnite   2.Counter strike    3.Overwatch 2    4.Battlefield 2042,   5.Valorant")

@bot.message_handler(commands=("Horror"))
def send_Horror(message): 
    bot.reply_to(message, "вот список: Five nights at Freddys,Resident Evil 2,Resident Evil 4, Poppy Playtime 1-4")

@bot.message_handler(commands=("adventures"))
def send_adventures(message): 
    bot.reply_to(message,"вот список: Portal 2,Red Dead redemption 2,Cuphead,Stray,Firewatch")



@bot.message_handler(commands=['trash'])
def send_trash(message):
    bot.reply_to(message, 'вы хотите сделать так чтобы на земле было меньше мусора но не знаете как начать? я могу помочь./trashpart1')

@bot.message_handler(commands=['trashpart1'])
def send_trashpart1(message):
    bot.reply_to(message, '1.найти доброжелатилей и сделать группы которые будут собирать мусор.2.найти оборудование.3.начать работать') 

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)
    

bot.polling()