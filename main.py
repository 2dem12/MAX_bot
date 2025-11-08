import asyncio
import logging
import os

from dotenv import load_dotenv
from maxapi import Bot, Dispatcher, F
from maxapi.types import MessageCreated

logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN = os.getenv("MAX_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("MAX_BOT_TOKEN не найден в .env")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message_created(F.message.body.text)
async def echo(event: MessageCreated):
    await event.message.answer(f"Повторяю за вами: {event.message.body.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())