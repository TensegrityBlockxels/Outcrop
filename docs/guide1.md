## Simple Chat Mirror
This guide will cover how to create an app that mirrors the chat of a Minecraft world.


## Server Example

```python
import asyncio, websockets
from core import OutcropEvent, OutcropAPI, OutcropEvents
from core import OutcropEvents

def chat(data):
    print(data)

async def main():
    async with websockets.serve(OutcropAPI().event(OutcropEvents.PlayerMessage).connect(chat).handle, "", 3001):
        await asyncio.Future()
asyncio.run(main())
```
## 
- The async function ``main()``  creates a websocket server with a callback function ``chat()`` where the ``data`` gets redirected to.
- In this example, the event ``PlayerMessage`` is what will be subscribed to,
- When you subscribe to an event, minecraft will give the connected server some JSON
data, for this example, on chat messages that players do.

# How to connect ?
```
/connect localhost:PORT
```
In this example, the port is 3001