import asyncio
from telethon import TelegramClient, events

api_id = 'API_ID'
api_hash = 'API_HASH'
group_name = 'F1_Visa_Slots_Only'

async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        group_entity = await client.get_entity(group_name)

        @client.on(events.NewMessage(chats=group_entity))
        async def handler(event):
            message = event.message.message.lower()
            forbidden_words = ['no', 'report', 'blocked', 'not', 'na']

            if not any(word in message for word in forbidden_words):
                # Forward the message to another user or group
                await client.forward_messages('USER_NAME', event.message)

        await client.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
