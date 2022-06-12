import asyncio, websockets
from core import OutcropEvent, OutcropAPI

def chat(data):
    print(data)


playerMessagesEvent = OutcropEvent()
playerMessagesEvent.body.eventName = "PlayerMessage"

playerMessagesListener = OutcropAPI(chat)
playerMessagesListener.subscribe(playerMessagesEvent)

async def main():
    async with websockets.serve(playerMessagesListener.handle, "", 3001):
        await asyncio.Future()

asyncio.run(main())