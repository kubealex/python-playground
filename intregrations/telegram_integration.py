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


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "This is a very simple bot listing directories with the '/list <path>' command"
    )


def main():
    env = initialize_vars()
    telegram_token = env("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(telegram_token).build()

    application.add_handlers(
        [
            CommandHandler("hello", hello),
            CommandHandler("list", list),
            CommandHandler("help", help),
        ]
    )

    application.run_polling()


if __name__ == "__main__":
    main()
