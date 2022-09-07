from aiogram import types

from app.keyboards import AbstractInlineKeyboard


class SubscribeInlineKeyboard(AbstractInlineKeyboard):

    @staticmethod
    async def show() -> types.InlineKeyboardMarkup:
        inline_btn_1 = types.InlineKeyboardButton(
            'Ответы на часто задаваемые вопросы',
            url='https://3prov.ru/faq',
        )
        inline_btn_2 = types.InlineKeyboardButton(
            'Вступить в чат',
            url='https://t.me/tprov_chat',
        )
        inline_btn_3 = types.InlineKeyboardButton(
            'Техподдержка',
            url='https://t.me/tprov_feedbackbot',
        )
        inline_kb_full = types.InlineKeyboardMarkup(row_width=1).add(inline_btn_1, inline_btn_2, inline_btn_3)
        return inline_kb_full
