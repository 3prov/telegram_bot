from typing import Type

from aiogram import Dispatcher

from .AbstractCommandHandler import AbstractCommandHandler
from .AbstractCallbackHandler import AbstractCallbackHandler

__all__ = ['AbstractCommandHandler', 'AbstractCallbackHandler']


def register_handlers(dispatcher: Dispatcher) -> None:
    from .commands.general import StartCommandHandler, ActivateUserCommandHandler, DeactivateUserCommandHandler
    from .callbacks import ActivateUserCallbackHandler

    # General commands
    _register_message_handler(dispatcher, StartCommandHandler, commands=['start'])
    _register_message_handler(dispatcher, ActivateUserCommandHandler, commands=['activate'])
    _register_message_handler(dispatcher, DeactivateUserCommandHandler, commands=['deactivate'])

    # Callbacks
    dispatcher.register_callback_query_handler(
        ActivateUserCallbackHandler.process, lambda c: c.data == 'callback_query_activate'
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
