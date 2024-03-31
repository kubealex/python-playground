import os

from environs import Env
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def initialize_vars():
    env = Env()
    env.read_env()
    return env


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = " ".join(context.args)
    dirlist = os.listdir(user_input)
    await update.message.reply_text(f"{dirlist}")


def main():
    env = initialize_vars()
    telegram_token = env("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(telegram_token).build()

    start_handler = CommandHandler("hello", hello)
    list_handler = CommandHandler("list", list)

    application.add_handlers([start_handler, list_handler])

    application.run_polling()


if __name__ == "__main__":
    main()
