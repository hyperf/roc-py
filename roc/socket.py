import socket
import asyncio
import struct
from asyncio import StreamReader, StreamWriter

from roc.packer import Packer
from roc.packet import Packet


class SocketException(Exception):
    def __init__(self, message, error_code: int = 0):
        super().__init__(message)
        self.error_code = error_code


class Client:
    def __init__(self, host: str, port: int, packer: Packer):
        self.host = host
        self.port = port
        self.reader: StreamReader | None = None
        self.writer: StreamWriter | None = None
        self.packer = packer

    async def loop(self):
        while True:
            try:
                prefix = await self.recv(4)
                length = struct.unpack(">I", prefix.encode())[0]
                body = await self.recv(length)

                packet = self.packer.unpack(prefix + body)

                print(packet.body)

            except SocketException:
                self.writer = None
                self.reader = None
                break

    async def recv(self, length: int):
        result = ""
        while True:
            res = await self.reader.read(length - len(result))
            if res.decode() == "":
                raise SocketException("read failed")
            result += res.decode()
            if len(result) >= length:
                return result

    async def send(self, packet: Packet):
        try:
            if self.writer is None:
                await self.start()

            self.writer.write(self.packer.pack(packet).encode())
        except Exception as exception:
            print(f"发生了异常: {exception}")

    async def start(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.reader = reader
        self.writer = writer

        asyncio.create_task(self.loop())
