from time import sleep
import asyncio

from roc.packer import Packer
from roc.socket import Client
from roc.packet import Packet


async def main():
    client = Client(host="127.0.0.1", port=9601, packer=Packer())
    while True:
        await client.send(Packet(1, "123"))
        await asyncio.sleep(1)
        
    await client.send(Packet(1, "1234"))
    await asyncio.sleep(1)
    await client.send(Packet(1, "1235"))
    await asyncio.sleep(1)
    print("End")


asyncio.run(main())
