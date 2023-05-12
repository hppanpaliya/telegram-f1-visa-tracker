import asyncio
from telethon import TelegramClient, events
from dotenv import dotenv_values
import re
from keywords import forbidden_words

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
            print(message)
            with open('message.txt', 'a') as file:
                    file.write(message + '\n')

            # Ignore messages with only emojis
            if not message or message.strip().startswith(':') or re.match(r'^[\U0001F300-\U0001F6FF\s]+$', message.strip()):
                return

            # Ignore messages with forbidden words and handle cases without spaces
            if not any(word in message.split() for word in forbidden_words) and not any(re.search(r'\b{}\b'.format(re.escape(word)), message) for word in forbidden_words):
                # Save the message content to a file
                await client.send_message(user_name, message)

        await client.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
