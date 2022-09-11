from aiogram import types

from app.keyboards import AbstractReplyKeyboard


class StartInlineKeyboard(AbstractReplyKeyboard):

    @staticmethod
    async def show() -> types.InlineKeyboardMarkup:
        inline_btn_1 = types.InlineKeyboardButton(
            'Начать',
            callback_data='callback_query_activate',
        )

        inline_kb_full = types.InlineKeyboardMarkup(row_width=1).add(inline_btn_1)
        return inline_kb_full
