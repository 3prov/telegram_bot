from aiogram import types
from aiogram.utils import markdown

import app
from app.keyboards.subscribe import SubscribeInlineKeyboard
from app.menus.AbstractMenu import AbstractMenu


class SubscribeMenu(AbstractMenu):

    @staticmethod
    async def show(chat_id: int) -> None:
        await app.bot.send_message(
            chat_id,
            markdown.text(
                markdown.text('Отлично! Ты зарегистрировался на участие. Напоминаю, тут мы пишем сочинения ЕГЭ по русскому языку и сами их проверяем.'),
                markdown.text('Ты сможешь получить 3 проверки своей работы только после того, как проверишь 3 чужие работы.'),
                markdown.text(),
                markdown.text('Понедельник — начало приёма сочинений. Четверг — начало проверки сочинений.'),
                markdown.text('Сроки этапов могут быть изменены, следи за изменениями в https://t.me/tprov'),
                markdown.text('До {название-следующего-этапа} осталось {времени}.'),
                markdown.text(),
                markdown.text('Отказаться от участия: /unsubscribe'),
                sep='\n',
            ),
            reply_markup=await SubscribeInlineKeyboard.show(),
        )
