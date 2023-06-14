import logging
import asyncio
import telegram
from telegram.ext import filters, Application, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"START")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Yo so un bot. Avle kon me, por favor!")

async def help(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"help")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Yo so un bot. Avle kon me, por favor! https://kantoniko.com/")


async def echo(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    logging.info(f"received: '{text}'")
    response = f"Resivi: '{text}'"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def translate(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) > 2:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No puedo tradusir ekspresiones kon mas de una palavra!")
        return
    text = context.args[0]
    if text == 'kaza':
        translation = 'house'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=translation)
        return

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"No konosko la palavar '{text}'")


#        echar_lashon_id = -810127428

async def post_init(application: Application) -> None:
    logging.info(f"post_init")
    #await application.bot.set_my_commands([('start', 'Starts the bot'), ('traduse', 'Tradusir una palavara')])
    await application.bot.set_my_commands([('ayuda', 'Ayudame!'), ('traduse', 'Tradusir una palavara')])


if __name__ == '__main__':
    token = os.environ.get('token')
    if not token:
        exit("No token found")

    application = ApplicationBuilder().token(token).post_init(post_init).build()
    #echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    #start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('ayuda', help)
    translate_handler = CommandHandler('traduse', translate)

    #application.add_handler(start_handler)
    #application.add_handler(echo_handler)
    application.add_handler(help_handler)
    application.add_handler(translate_handler)
    #print(dir(application))
    #print(dir(application.bot))

    application.run_polling()

