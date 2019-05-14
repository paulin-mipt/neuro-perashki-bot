import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import secret

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
model = None


def load_model():
    """
    :returns: pretrained model
    """
    #TODO
    return None


def generate_response(request: str):
    """
    :str request: raw user text
    :returns: single response string
    """
    global model
    # TODO
    return (
        'вот вы заходите в квартиру\n'
        'и понимаете что вам\n'
        'никто не рад и вы стоите\n'
        'в прихожей молча до утра'
    )


def generate(update, context):
    update.message.reply_text(generate_response(update.message.text))


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Дайте мне тему и я вам что-нибудь напишу!')


def error(update, context):
    """Log errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(secret.TOKEN, use_context=True)
    dp = updater.dispatcher

    global model
    model = load_model()
    dp.add_handler(MessageHandler(Filters.text, generate))
    dp.add_handler(CommandHandler("start", start))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main() 
