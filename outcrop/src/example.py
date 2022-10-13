import asyncio, websockets
from core import OutcropEvent, OutcropAPI, OutcropEvents
from core import OutcropEvents

def chat(data):
    print(data)


async def main():
    async with websockets.serve(OutcropAPI().event(OutcropEvents.PlayerMessage).connect(chat).handle, "", 3001):
        await asyncio.Future()

asyncio.run(main())