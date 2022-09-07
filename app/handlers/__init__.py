from typing import Type

from aiogram import Dispatcher

from .AbstractCommandHandler import AbstractCommandHandler
from .AbstractCallbackHandler import AbstractCallbackHandler

__all__ = ['AbstractCommandHandler', 'AbstractCallbackHandler']


def register_handlers(dispatcher: Dispatcher) -> None:
    from .commands.general import StartCommandHandler, SubscribeCommandHandler, UnsubscribeCommandHandler
    from .callbacks import SubscribeCallbackHandler

    # General commands
    _register_message_handler(dispatcher, StartCommandHandler, commands=['start'])
    _register_message_handler(dispatcher, SubscribeCommandHandler, commands=['subscribe'])
    _register_message_handler(dispatcher, UnsubscribeCommandHandler, commands=['unsubscribe'])

    # Callbacks
    dispatcher.register_callback_query_handler(
        SubscribeCallbackHandler.process, lambda c: c.data == 'callback_query_start'
    )


def _register_message_handler(
        dispatcher_: Dispatcher, handler_class: Type[AbstractCommandHandler],
        text: list = None, commands: list = None, state=None
):
    if text is not None:
        dispatcher_.register_message_handler(handler_class.process, text=text, state=state)

    if commands is not None:
        dispatcher_.register_message_handler(handler_class.process, commands=commands, state=state)

    if text is None and commands is None and state is not None:
        dispatcher_.register_message_handler(handler_class.process, state=state)
