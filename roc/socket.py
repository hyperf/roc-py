import socket
import asyncio
import struct
from asyncio import StreamReader, StreamWriter

from roc.packer import Packer
from roc.packet import Packet


class Client:
    def __init__(self, host: str, port: int, packer: Packer):
        self.host = host
        self.port = port
        self.reader: StreamReader | None = None
        self.writer: StreamWriter | None = None
        self.packer = packer

    async def loop(self):
        while True:
            prefix = await self.recv_all(4)
            length = struct.unpack("I", bytes.fromhex(prefix))[0]
            body = await self.recv_all(length)

            packet = self.packer.unpack(prefix + body)

            print(packet)

    async def recv_all(self, length: int):
        result = ""
        while True:
            res = await self.reader.read(length - len(result))
            result += res.decode()
            if len(result) >= length:
                return result

    async def send(self, packet: Packet):
        self.writer.write(self.packer.pack(packet).encode())

    async def start(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.reader = reader
        self.writer = writer

        asyncio.create_task(self.loop())
