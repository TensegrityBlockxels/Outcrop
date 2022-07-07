<p align="center">
  <img src="./public/outcrop256.png">
</p>

## API for Minecraft Bedrock websockets.


## Example - listening and handling custom events
```python3
import asyncio, websockets
from core import OutcropEvent, OutcropAPI // importing outcrop

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
```


# Installation
```cmd
git clone https://github.com/TensegrityBlockxels/Outcrop.git
```

- Windows 
```cmd
install.bat
``` 
- Linux 
```bash
install.sh
```



## Dependencies
- websockets == 10.3
