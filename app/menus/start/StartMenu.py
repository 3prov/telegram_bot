from aiogram import types
from aiogram.utils import markdown

import app
from app.menus.AbstractMenu import AbstractMenu
from app.keyboards.start import StartInlineKeyboard


class StartMenu(AbstractMenu):

    @staticmethod
    async def show(chat_id: int) -> None:
        await app.bot.send_message(
            chat_id,
            markdown.text(
                markdown.text('Привет!'),
                markdown.text('3проверочки — проект, который поможет тебе бесплатно подготовиться к ЕГЭ по русскому языку. Ты научишься писать сочинения на максимальный балл, используя эффективный метод обучения, основанный на взаимных проверках.'),
                markdown.text(),
                markdown.text('Более подробная информация о проекте доступна на https://3prov.ru'),
                markdown.text(),
                markdown.text('Чтобы начать, нажми кнопку ниже 👇'),
                sep='\n',
            ),
            reply_markup=await StartInlineKeyboard.show(),
        )
