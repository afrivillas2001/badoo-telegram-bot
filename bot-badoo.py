import os
import badoo_macht
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton


INPUT_TEXT = 0

def star_comand(update, context):
    update.message.reply_text(
        text= 'Hola, bienvenido seas ¿Que deseas hacer?',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Matches en badoo', callback_data='numbers')],
        ])
    )

def  url_comand_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text= 'Envia el numero de maches que quieres dar'
    )
    return INPUT_TEXT

def input_url(update, context):
    url = update.message.text
    update.message.reply_text('procesando...')
    chat = update.message.chat
    short = badoo_macht.ejecutar_baboo_mach(url)
    chat.send_action(
        action = ChatAction.TYPING,
        timeout = None
    )
    chat.send_message(
        text=short
    )
    return ConversationHandler.END 

#Ejecucion
if __name__ == '__main__':
    #Coneccion a la API Telegram
    uptader = Updater(token='5519027480:AAH5eagNVPDohtYyWGtNUHHSoTud1UJ0xPM', use_context=True)
    dp = uptader.dispatcher

    #Comandos
    dp.add_handler(CommandHandler('start', star_comand))
    dp.add_handler(ConversationHandler(
        entry_points = [
            CallbackQueryHandler(pattern='numbers', callback=url_comand_handler)
        ],
        states = {
            INPUT_TEXT: [MessageHandler(Filters.text, input_url)]
        },
        fallbacks = []
    ))

    #Inicializacion de la escucha de eventos
    uptader.start_polling()
    uptader.idle()
