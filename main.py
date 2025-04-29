
import telebot

TOKEN = '7494120179:AAEKEI-0ECjs6rcw1w7c_iokEy-_v9rKy6Q'

bot = telebot.TeleBot(TOKEN)

# Variáveis para rastrear
total_spins = 0
spins_sem_pagamento = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot de Volatilidade iniciado! Use /spin para registrar uma rodada.")

@bot.message_handler(commands=['spin'])
def spin(message):
    global total_spins, spins_sem_pagamento
    total_spins += 1
    spins_sem_pagamento += 1
    if spins_sem_pagamento >= 30:
        bot.reply_to(message, f"⚡ Atenção! {spins_sem_pagamento} spins sem pagamento. Pode estar perto de bônus!")
    else:
        bot.reply_to(message, f"Rodada registrada. {spins_sem_pagamento} spins sem grande pagamento.")

@bot.message_handler(commands=['pagou'])
def pagou(message):
    global spins_sem_pagamento
    spins_sem_pagamento = 0
    bot.reply_to(message, "Pagamento registrado! Contador zerado.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, f"Total de spins: {total_spins}\nSpins sem pagamento: {spins_sem_pagamento}")

bot.polling()
