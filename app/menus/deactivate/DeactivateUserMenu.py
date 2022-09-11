from aiogram import types
from aiogram.utils import markdown

import app
from app.menus.AbstractMenu import AbstractMenu


class DeactivateMenu(AbstractMenu):

    @staticmethod
    async def show(message: types.Message) -> None:

        await app.bot.send_message(
            message.chat.id,
            markdown.text(
                markdown.text('Ты отказался от участия в проекте. Теперь тебе не будут приходить уведомления.'),
                markdown.text(),
                markdown.text('Возобновить участие: /activate'),
                sep='\n',
            ),
            reply_markup=types.ReplyKeyboardRemove(),
        )
