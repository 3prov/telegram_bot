from aiogram import types
from aiogram.utils import markdown

import app
from app.keyboards.activate import ActivateInlineKeyboard
from app.menus.AbstractMenu import AbstractMenu


class ActivateMenu(AbstractMenu):

    @staticmethod
    async def show(message: types.Message) -> None:
        await app.bot.send_message(
            message.chat.id,
            markdown.text(
                markdown.text('Отлично! Ты зарегистрировался на участие. Напоминаю, тут мы пишем сочинения ЕГЭ по русскому языку и сами их проверяем.'),
                markdown.text('Ты сможешь получить 3 проверки своей работы только после того, как проверишь 3 чужие работы.'),
                markdown.text(),
                markdown.text('Понедельник — начало приёма сочинений. Четверг — начало проверки сочинений.'),
                markdown.text('Сроки этапов могут быть изменены, следи за изменениями в https://t.me/tprov'),
                markdown.text('До {название-следующего-этапа} осталось {времени}.'),
                markdown.text(),
                markdown.text('Отказаться от участия: /deactivate'),
                sep='\n',
            ),
            reply_markup=await ActivateInlineKeyboard.show(),
        )
