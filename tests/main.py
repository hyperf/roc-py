from time import sleep
import asyncio

from roc.channel_manager import ChannelManager
from roc.packer import Packer
from roc.socket import Client
from roc.packet import Packet


async def main():
    client = Client(host="127.0.0.1", port=9601)
    while True:
        res = await client.request("World")
        print(res)
        await asyncio.sleep(1)


asyncio.run(main())
