from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8653792322:AAFMsQCfGePWnj1FCUlsGJrqf26ihF18bM0"
CHANNEL_USERNAME = "Telugu Movies"

movies = {
    "pushpa": {
        "title": "Pushpa Movie",
        "file": "https://example.com/pushpa.mp4"
    }
}

async def is_user_joined(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot

    if not await is_user_joined(bot, user_id):
        await update.message.reply_text(f"Join channel first: {CHANNEL_USERNAME}")
        return

    args = context.args

    if args:
        movie_id = args[0]
        if movie_id in movies:
            movie = movies[movie_id]
            await update.message.reply_video(
                video=movie["file"],
                caption=movie["title"]
            )
        else:
            await update.message.reply_text("Movie not found ❌")
    else:
        await update.message.reply_text("Welcome 👋")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
