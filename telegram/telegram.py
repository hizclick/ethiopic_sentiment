from telegram.ext import Updater
from telegram import Poll, Bot, PollOption



updater = Updater(token='1022567655:AAGjqp1EcNQKQlFlzMIr6MpLQLIoi_YJ4YM', use_context=True)


text = open('third round/test.txt', "r", encoding="utf-8") '''this is the file that contains all the tweets'''

lines = text.readlines()


dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    global lines
    context.bot.send_message(chat_id=update.effective_chat.id, text=lines[0])


import logging
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def instruction(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='ጽሁፉ አዎንታዊ ከሆነ "1"ን አሉታዊ "2"ን ገለልትኛ ከሆነ "3" ይጻፉ')

import logging
from telegram.ext import CommandHandler
instr = CommandHandler('instruction', instruction)
dispatcher.add_handler(instr)

dispatcher = updater.dispatcher

hi = list()
count = 1

def echo(update, context):
    global lines
    global count 
    
    if(count<len(lines) and len(lines)>0):
        if(update.message.text == '1' or update.message.text == '2' or update.message.text == '3'):
            context.bot.send_message(chat_id=update.effective_chat.id, text=lines[count])
            with open('third round/test.txt', 'w', encoding="utf-8") as fout:
                fout.writelines(lines[1:])
            text = open('third round/test.txt', "r", encoding="utf-8")
            lines = text.readlines()
            with open('third round/test2.txt', 'a', encoding="utf-8") as f: ''' the user's response will be written on a new file'''
                f.writelines(update.message.text+"\n")
        elif(update.message.text == '/end'):
            context.bot.send_message(chat_id=update.effective_chat.id, text='ስለ ትብብሮ እናመሰግናለን!')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='እባክዎን ጽሁፉ አዎንታዊ ከሆነ "1"ን አሉታዊ "2"ን ገለልትኛ ከሆነ "3" ይጻፉ')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='ስለ ትብብሮ እናመሰግናለን!')

def end(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='ስለ ትብብሮ እናመሰግናለን!')




from telegram.ext import MessageHandler, Filters
end_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(end_handler)

start_handler = CommandHandler('end', end)
dispatcher.add_handler(start_handler)
updater.start_polling()
