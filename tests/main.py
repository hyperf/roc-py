from time import sleep
import asyncio

from roc.packer import Packer
from roc.socket import Client
from roc.packet import Packet


async def main():
    client = Client(host="127.0.0.1", port=9601, packer=Packer())
    await client.start()
    await client.send(Packet(1, "123"))
    await asyncio.sleep(5)
    print("End")


asyncio.run(main())
