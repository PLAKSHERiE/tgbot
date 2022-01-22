from aiogram import executor
import logging

from loader import dp, bot, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_PORT, WEBAPP_HOST
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from aiogram.utils.executor import start_webhook
from aiogram.contrib.middlewares.logging import LoggingMiddleware

logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL)
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('close!')


if __name__ == '__main__':
    # executor.start_polling(dp, on_startup=on_startup)
    # executor.start_polling(dp, on_startup=on_startup)

    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )

