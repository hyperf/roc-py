from time import sleep
import asyncio

from roc.channel import Channel
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


async def pop(chan: Channel):
    res = await chan.pop()
    print(f"res{res}")


async def push(chan: Channel):
    await chan.push(123)


async def main2():
    chan = Channel()
    asyncio.create_task(pop(chan))
    await asyncio.sleep(2)
    await push(chan)
    print("push")
    await asyncio.sleep(2)


asyncio.run(main2())
