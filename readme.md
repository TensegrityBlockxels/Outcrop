<p align="center">
  <img src="./public/outcrop256.png">
</p>

# Outcrop


## API for Minecraft Bedrock websockets.


## Example - listening and handling custom events
```python3
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
