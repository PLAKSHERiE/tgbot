from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    # link = await bot.create_chat_invite_link(chat_id='-1001724246403', member_limit=1)
    # await message.answer(link.invite_link)
    # await bot.ban_chat_member(-1001724246403, 2076789459)
    # await bot.unban_chat_member(-1001724246403, 2076789459)
    pass
