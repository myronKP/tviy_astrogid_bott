import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tviyastrogid_handlers import router, daily_broadcast

# ✅ Read bot token from environment (Fly secret)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set. On Fly: fly secrets set BOT_TOKEN=<your_telegram_token>")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)

    # Kyiv timezone for scheduler
    scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")
    scheduler.add_job(daily_broadcast, "cron", hour=9, minute=0, args=[bot])
    scheduler.start()

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
