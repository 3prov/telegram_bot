from aiogram import types
from aiogram.utils import markdown

import app
from app.menus.AbstractMenu import AbstractMenu


class UnsubscribeMenu(AbstractMenu):

    @staticmethod
    async def show(chat_id: int) -> None:

        await app.bot.send_message(
            chat_id,
            markdown.text(
                markdown.text('Ты отказался от участия в проекте. Теперь тебе не будут приходить уведомления.'),
                markdown.text(),
                markdown.text('Возобновить участие: /subscribe'),
                sep='\n',
            ),
            reply_markup=types.ReplyKeyboardRemove(),
        )
