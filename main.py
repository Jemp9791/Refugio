
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("¡Hola! Soy tu bot cristiano 😊")

def main():
    updater = Updater("8115619992:AAG6_BjyWcpI6fgJTwGdflVhS1GbEw851Wc", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
