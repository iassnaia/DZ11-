from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import time
import polinom

value = int()
pol_1 = str()
pol_2 = str()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'Привет {update.effective_user.first_name} я бот который умеет складывать многочлены.\n/help - команды бота\n/pol - сложение многочлена')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('/start - запустить бот\n/help - команды бота\n/pol - сложение многочлена')


async def pol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global value
    await update.message.reply_text(
        'Давайте попробуем сложить два многочлена.\nДля начала введите первый многочлен в формате (3Х^3 + 2Х^2 + 1Х + 4 = 0) и отправьте мне.\nНе забывайте про пробелы.')
    value = 1


async def get_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global value, pol_1, pol_2
    if value == 1:
        await update.message.reply_text('Отлично теперь введите второй многочлен:')
        pol_2 = update.message.text
        value = 2
    elif value == 2:
        await update.message.reply_photo('1.jpg')
        time.sleep(1)
        pol_1 = update.message.text
        await update.message.reply_text(polinom.polinom(pol_1, pol_2))
        value = 0
    else:
        pass
