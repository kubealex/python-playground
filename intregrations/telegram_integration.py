from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from environs import Env


def initialize_vars():
    env = Env()
    env.read_env()
    return env


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


def main():
    env = initialize_vars()
    telegram_token = env("TELEGRAM_TOKEN")
    application = ApplicationBuilder()
    application = ApplicationBuilder().token(telegram_token).build()

    start_handler = CommandHandler("hello", hello)
    application.add_handler(start_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
