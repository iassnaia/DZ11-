from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from commands import *

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("pol", pol))
app.add_handler(MessageHandler(filters.TEXT, get_message))

app.run_polling()
