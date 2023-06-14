import asyncio
import telegram
import os
from dotenv import load_dotenv
load_dotenv()

token = os.environ.get('token')
if not token:
    xit("No token found")

async def main():
    bot = telegram.Bot(token)
    async with bot:
        about_me = await bot.get_me()
        # User(can_join_groups=True, can_read_all_group_messages=False, first_name='Kantoniko', id=5972296076, is_bot=True, supports_inline_queries=False, username='kantoniko_bot')
        updates = await bot.get_updates()
        #print(updates)
        #for update in updates:
        #    print(update)
        #    print()
        echar_lashon_id = -810127428
        #first_name = updates[0].message.from_user.first_name
        #user_id = updates[0].message.from_user.id
        #await bot.send_message(text=f'Hi {first_name}', chat_id=user_id)
        #await bot.send_message(text=f'Yo so Kantoniko', chat_id=echar_lashon_id)


if __name__ == '__main__':
    asyncio.run(main())
