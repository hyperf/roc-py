from roc.packet import Packet
import struct


class Packer:
    def pack(self, packet: Packet) -> bytes:
        return struct.pack(">I", packet.len()) + struct.pack(">I", packet.id) + packet.body.encode()

    def unpack(self, raw: bytes) -> Packet:
        id = struct.unpack(">I", raw[4:8])[0]
        body = raw[8:]
        return Packet(int(id), body.decode())
