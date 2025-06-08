# telegram_bot/handlers.py

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters

from orders.models import TelegramOrder
from django.utils import timezone
import datetime

# Этапы диалога
ASK_BOUQUET, ASK_ADDRESS = range(2)

WORK_HOURS = range(9, 19)  # 09:00–18:59

def is_working_time():
    now = timezone.localtime()
    return now.weekday() != 6 and now.hour in WORK_HOURS  # Sunday = 6

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_working_time():
        await update.message.reply_text("Извините, мы принимаем заказы с 9:00 до 19:00, кроме воскресенья.")
        return ConversationHandler.END

    await update.message.reply_text("Здравствуйте! Какой букет вы хотите заказать?")
    return ASK_BOUQUET

async def ask_bouquet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['bouquet'] = update.message.text
    await update.message.reply_text("Пожалуйста, укажите адрес доставки.")
    return ASK_ADDRESS

async def ask_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    address = update.message.text
    bouquet = context.user_data.get('bouquet')

    # Сохраняем заказ
    TelegramOrder.objects.create(
        bouquet_name=bouquet,
        address=address,
        status='pending',
        created_at=timezone.now()
    )

    await update.message.reply_text("Спасибо! Ваш заказ принят. Мы свяжемся с вами для подтверждения.")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Операция отменена.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def get_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ASK_BOUQUET: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_bouquet)],
            ASK_ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_address)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
