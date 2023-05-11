import asyncio
from telethon import TelegramClient, events
from dotenv import dotenv_values

# Load environment variables from .env file
config = dotenv_values(".env")
api_id = config['API_ID']
api_hash = config['API_HASH']
group_name = config['GROUP_NAME']

user_name = config['USER_NAME']

async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        group_entity = await client.get_entity(group_name)

        @client.on(events.NewMessage(chats=group_entity))
        async def handler(event):
            message = event.message.message.lower()
            forbidden_words = ['no', 'report', 'blocked', 'not', 'na','fake','permission','without','Action','Register','follow','free','live','banned','chat','group','video','poll','without','link','tool','tweet','questions','group','chat','discussions','wasted_a_login','login','reschedule','travel','agent','spam','n/a','spammer','block','fresher','buying','things','?','any']

            if not any(word in message for word in forbidden_words):
                # Send the message content to another user or group
                await client.send_message(user_name, message)

        await client.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
