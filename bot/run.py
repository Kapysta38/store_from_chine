import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = os.path.join('../local_data/.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    load_dotenv(find_dotenv('../local_data/.env.dev'))

import asyncio
# import aioschedule
from aiogram import executor
from extra_aiogram.settings import LOG_PATH, DEBUG
from extra_aiogram.app import dp
import extra_logging as ex_log

from bot.message_handlers import LIST_HANDLERS
from bot.admin_message_handlers import LIST_ADMIN_HANDLERS
from bot.callbacks import LIST_CALLBACKS
from bot.loops import LIST_LOOPS
from bot.utils import get_reg_func

log = ex_log.Logging('run', LOG_PATH, max_bytes=ex_log.mb * 5).get_log


# async def scheduler():
#     for loop in LIST_LOOPS:
#         loop().start()
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)


async def on_startup(_):
    log.info('Start init handlers')

    LIST_HANDLERS.extend(LIST_ADMIN_HANDLERS)

    for handler in LIST_HANDLERS:
        if handler.command is not None:
            dp.register_message_handler(handler.run_handler, commands=handler.command, state=handler.state)
        if handler.state is not None:
            list_func = get_reg_func(handler)
            for func in list_func:
                if isinstance(handler.state, list):
                    state = handler.state
                else:
                    state = getattr(handler.state, func.__name__.replace("reg_", ""))
                dp.register_message_handler(func,
                                            text_startswith=handler.text_startswith,
                                            state=state,
                                            content_types=handler.content_types)
    log.info('End init handlers')

    log.info('Start init callbacks')
    for callback in LIST_CALLBACKS:
        dp.register_callback_query_handler(callback.callback, callback.custom_filters, state=callback.state)
    log.info('End init callbacks')
    #
    # log.info('Start init loops')
    # asyncio.create_task(scheduler())
    # log.info('End init loops')


if __name__ == '__main__':
    log.info('Бот запущен!')
    if DEBUG:
        log.warning("DEBUG IS ON!!!")
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
